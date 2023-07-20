# cấu hình
import os,sys,time,random
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'

def banner():
  os.system("clear")
  ban = f'''{red}
  ___ ___                              
 /   |   \  _________    ____    ____  
/    ~    \/  _ \__  \  /    \  / ___\ 
\    Y    (  <_> ) __ \|   |  \/ /_/  >
 \___|_  / \____(____  /___|  /\___  / 
       \/            \/     \//_____/  
  '''
  for i in ban:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.0012)
  print("-------------------------")

def dem():
  mang = [vang,do,hong,xnhac]
  for i in range(10):
    mau = random.choice(mang)
    print(f"{mau}Đã spam xong vui lòng chờ",end="")
    print("\r",end="")
    time.sleep(1)

# nhận dữ liệu
banner()
sdt = input(f"=>{hong}Nhập số điện thoại:")
count = int(input(f"{vang}Nhập số lần spam:"))


# web





# chạy 
def runner(sdt, count):
  banner()
  dem()
runner(sdt, count)

