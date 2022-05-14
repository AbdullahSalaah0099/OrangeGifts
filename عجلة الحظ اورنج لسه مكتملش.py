import requests,json
from bs4 import BeautifulSoup as BS
from time import sleep
import sys,os, time, json,termcolor 
print ('\033[1;95mWelcome')
sleep (1)
print ()
print ('\033[1;92mclick on this link to get password👇')
#sleep (0.1)
print ()
link="\033[1;93m https://pastelink.net/vsngvbe8"
print (link)
#sleep (1)
print ()
password=input ('\033[1;92m》Enter Password Script :  \033[1;96m')
sleep (1)

rrr=requests.get('https://pastelink.net/vsngvbe8').text
soup=BS(rrr,'html.parser')
lxc=(soup.find('div',{'class':'body-display'})).text

if password in lxc:
    print ()
    print ('\033[1;96m》True Password《')
    sleep (1)
else:
    print ()
    print ('\033[1;91mError Password')
    exit()
import time, sys 
print ()



from termcolor import colored
from pyfiglet import Figlet

'''f=Figlet(font='banner3-D')
print (colored(f.renderText('Orange\nGifts'), 'red'))'''
import os, time, pyfiglet,sys
c=('\033[1;092m××××××××××××××××××××××××××××××××××××')
for I in c+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.040)
print ()
d =('\033[1;092m#####Welcome To Abdullah Script#####')
for I in d +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.050)
print ()
p=('\033[1;092m##### Script Orange 200:1000 MG ####')
for I in p+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.050)
print ()
u=('\033[1;092m### Projected By Abdullah Salah###')
for I in u+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.050)

print ('\033[1;092m')

vg=pyfiglet.figlet_format ('Abdullah')

for I in vg+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.010)

print ()
i='\033[;092m Telegram channel : \n\n◇ http://t.me/Techno0099\n\n\nYouttube channel  :\n \n◇ https://youtube.com/channel/UCAbtkFAe9yyX0HJNFXyKJUg '
for I in i +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)
print ('\033[;091m')


logo='''\033[1;095m
░█████╗░██████╗░░█████╗░███╗░░██╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔════╝░
██║░░██║██████╔╝███████║██╔██╗██║██║░░██╗░
██║░░██║██╔══██╗██╔══██║██║╚████║██║░░╚██╗
╚█████╔╝██║░░██║██║░░██║██║░╚███║╚██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░

░██████╗░██╗███████╗████████╗░██████╗
██╔════╝░██║██╔════╝╚══██╔══╝██╔════╝
██║░░██╗░██║█████╗░░░░░██║░░░╚█████╗░
██║░░╚██╗██║██╔══╝░░░░░██║░░░░╚═══██╗
╚██████╔╝██║██║░░░░░░░░██║░░░██████╔╝
░╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═════╝░
'''
print (logo)
print ()
print ('\033[;091m='*50)
#print ('\033[1;092m='*40)
print ()

e=('\033[1;93mSTEP 1 : Know If You Have Megabytes Or Not')
for I in e+"\n":
    sys.stdout.write (I)
    sys.stdout.flush ()
    time.sleep(0.08)
print ()
req=requests.Session ()

num=input ('\033[1;092m》Enter your Number: \033[1;096m')
print ()
pas=input ('\033[1;092m》Enter your password : \033[1;096m')
print ()


url1='https://services.orange.eg/SignIn.svc/SignInUser'

headers1={

#'_ctv': ctv,

#'_htv': htv,
'Content-Type': 'application/json; charset=UTF-8',

'Content-Length': '163',

'Host': 'services.orange.eg',

'Connection': 'Keep-Alive',

'Accept-Encoding': 'gzip',

'User-Agent': 'okhttp/3.12.0'


}

data1='{"appVersion":"5.5.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":%s,"isAndroid":true,"password":%s}'%(num,pas)

r1=req.post (url1,headers=headers1,data=data1).json()


if (r1["SignInUserResult"]["ErrorCode"])==0:
    print ('Done login')
elif (r1["SignInUserResult"]["ErrorCode"])==9:
    print ('\033[1;091mError Number Or Password')
    sleep(0.5)

#####################################


import hashlib,requests,json

headers = {
    'Content-Type': 'application/json; charset=UTF-8',
     'Content-Length': '78',
    'Host': 'services.orange.eg',
    'Connection': 'Keep-Alive',
     'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.0',
}

data = {"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}

re = requests.post('https://services.orange.eg/GetToken.svc/GenerateToken', headers=headers, json=data).json()

x=re.get("GenerateTokenResult")
#c=(x.get("Token"))
print()
a_string =x.get("Token")

hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
z=(hashed_string.upper())




print ()
ctv=input ('\033[1;92m》Enter ctv : \033[1;096m')
print ()
htv=input ('\033[1;92m》Enter htv : \033[1;096m')
print ()
url2="https://backend.orange.eg/api/WheelOfFortune/CheckEligibility"

headers2={
"_ctv":ctv,
"_htv":htv,

"isEasyLogin": "false",

"Content-Type": "application/json; charset=UTF-8",

"Content-Length": "190",

"Host": "backend.orange.eg",

"Connection": "Keep-Alive",

"Accept-Encoding": "gzip",

"User-Agent": "okhttp/3.12.0"
}

data2={"ServiceClassID":"1045","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"Dial":f"{num}","IsEasyLogin":False,"Lang":"ar","Password":f"{pas}"}
r2=requests.post (url2,headers=headers2,json=data2).json()
c=(r2["OfferId"])

#print (c)
#if c==:
#    print ('None')
if (r2["ErrorCode"]==9):
    print ('\033[1;91mError Number Or Password')
    exit()
elif (r2["ErrorCode"]==16):
    print ('\033[1;91mError ctv Or htv')
    exit()
elif (r2["OfferId"])=="" and (r2["ErrorCode"])==218:
    print ('\033[1;91mAttempts are Over , Try Tomorrow')
    exit()
elif(r2["ErrorCode"])==219:
    print ('\033[1;91mYou take before, Try after some days')
    exit()
if (r2["OfferId"])=="2":
    print ('\033[1;96mCongratulation, You have 500 mg')
elif (r2["OfferId"])=="4":    
    print ('\033[1;96mCongratulation, You have 1000 mg')
elif (r2["OfferId"])=="3":
    print ('\033[1;96mCongratulation, You have 200 mg')
elif (r2["OfferId"]) =="5":
    print ('\033[1;93mTry your luck again')
    exit()
elif (r2["OfferId"]) =="1":
    print ('\033[1;93mTry your luck again')
    exit()

print ()

print ('='*60)
sleep (7)
os.system ('clear')


######################################


s=('\033[1;93mSTEP 2 : Adding Megabytes ')
for I in s+"\n":
    sys.stdout.write (I)
    sys.stdout.flush ()
    time.sleep(0.08)
#c=str(input ('choose'))
print ()

ctv1=input ('\033[1;92m》Enter ctv : \033[1;96m')
print ()
htv1=input ('\033[1;92m》Enter htv : \033[1;96m')

url3="https://backend.orange.eg/api/WheelOfFortune/Offerfulfillment"

data3={"OfferID":f"{c}","ServiceClassID":"1044","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"Dial":f"{num}","IsEasyLogin":"false","Lang":"ar","Password":f"{pas}"}


headers3={
"_ctv": ctv1,

"_htv": htv1,

"isEasyLogin": "false",

"Content-Type": "application/json; charset=UTF-8",

"Content-Length": "190",

"Host": "backend.orange.eg",

"Connection": "Keep-Alive",

"Accept-Encoding": "gzip",

"User-Agent": "okhttp/3.12.0"
}

if True :
    r=requests.post(url3,headers=headers3,json=data3)
#    print (r.text)
    print ()
    
    if (r.json()["ErrorCode"])==0:
        print ('\033[1;96mDone Add Megabytes')
    elif(r.json()["ErrorCode"])==13:
        print ('\033[1;91mctv & htv unexpired')
        print ('be fast')
        exit()
    elif (r.json()["ErrorCode"])==16:
        print ('\033[1;91mError ctv or htv')
        exit()
    elif (r.json()["ErrorCode"])==9:
        print ('\033[1;91mError Number Or Password')
        exit()
    elif (r.json()["ErrorCode"])==219:
        print ('\033[1;91mYou take before')
        exit()
    elif (r.json()["ErrorCode"])==197:
        print ('\033[1;91mYou take before')
    elif (r.json()["ErrorCode"])==228:
        print ('\033[1;91mYou take before')
        exit()
    elif(r.json()["ErrorCode"])==10:
        print ("\033[1;91mSomething Wrong, Try again")
        exit()
    else :
        print ('\033[1;91mSomthing Wrong Try again later')
        exit()
        print ()