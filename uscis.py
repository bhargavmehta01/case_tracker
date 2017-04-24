#!/bin/bash
#PATH=/usr/local/bin:/usr/local/sbin:~/bin:/usr/bin:/bin:/usr/sbin:/sbin

import requests
#from lxml import html
from bs4 import BeautifulSoup
import boto3
import os.path

#uscis_url="https://egov.uscis.gov/casestatus/landing.do"

#st_cod = page.status_code
#print("status code: {}".format(st_cod))

payload = {'appReceiptNum':''}
result = requests.post("https://egov.uscis.gov/casestatus/mycasestatus.do",data=payload)

#tree = html.fromstring(result.text)
#p_tag =
soup = BeautifulSoup(result.content, 'html.parser')
txtf = soup.find('p').get_text()

if(os.path.isfile("/Users/BhargavMehta/Desktop")):
    f1 = open('otpt.txt','r')
    prev_status = f1.read()
else:
    prev_status = "empty"

checker = True
if(prev_status == txtf):
    checker = False

#if(checker):



print("fist p tag: {}".format(checker))

f = open('otpt.txt','w')
f.write(txtf)
f.close()

sns_client = boto3.client('sns')

response = sns_client.publish(
    PhoneNumber='+',
    Message=txtf,
)
