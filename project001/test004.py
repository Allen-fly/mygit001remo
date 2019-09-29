#!/usr/bin/python
# -*- coding: UTF-8 -*-

#!/usr/bin/env python
#coding:utf-8
import requests,json
url="http://xxx.xxx.com/xxx/login"
headers={'Content-Type':'application/json;charset=UTF-8'}
request_param={
    "phone":"18200000000",
    "password":"111111"
}
response = requests.post(url,data = json.dumps(request_param), headers=headers)
print response.text
print response.status_code
print response.content