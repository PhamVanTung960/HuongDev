
try :
    import requests
    import time
    import os 
    from art import *
    from colorama import Fore
    from time import sleep
    import json
    import random
    from tabulate import tabulate
    import sys
    import requests
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem
except ImportError:
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
    os.system('pip install random_user_agent')
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        colors = [
            "\033[1;37mT\033[1;36mu\033[1;35mn\033[1;34mg\033[1;36m🍉 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
            "\033[1;34mT\033[1;31mu\033[1;37mn\033[1;35mg\033[1;32m🍉 - Tool\033[1;34m Vip \033[1;31m\033[1;32m",
            "\033[1;31mT\033[1;37mu\033[1;36mn\033[1;32mg\033[1;37m🍉 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
            "\033[1;32mT\033[1;33mu\033[1;34mn\033[1;37mg\033[1;34m🍉 - Tool\033[1;31m Vip \033[1;31m\033[1;32m",
            "\033[1;37mT\033[1;34mu\033[1;35mn\033[1;33mg\033[1;34m🍉 - Tool\033[1;37m Vip \033[1;31m\033[1;32m",
            "\033[1;34mT\033[1;33mu\033[1;37mn\033[1;36mg\033[1;37m🍉 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
            "\033[1;36mT\033[1;35mu\033[1;31mn\033[1;35mg\033[1;33m🍉 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
        ]
        for color in colors:
            print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
            time.sleep(0.12)
                                  
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ",end = "\r")
def TIKTOKINFO():
    url1_2 = 'https://gateway.golike.net/api/tiktok-account'
    checkurl1_2 = ses.get(url1_2,headers=headers).json()
    user_tiktok1 = []
    account_id1 = []
    STT = []
    STATUS =[]
    tong = 0
    dem = 0
    i = 1

    for data in checkurl1_2['data']:
        usernametk = data['nickname']
        account_id = data['id']
        user_tiktok1.append(usernametk)
        account_id1.append(account_id)
        STT.append(i)
        STATUS.append(Fore.GREEN + "Hoạt Động" + Fore.RESET)  # Sử dụng Fore.RESET để trả lại màu gốc
        
        print(f'\033[1;36m[{i}] \033[1;36m✈ \033[1;97mTài Khoản┊\033[1;32m㊪ :\033[1;93m {usernametk} \033[1;97m|\033[1;32m㊪ :\033[1;93m {STATUS[-1]}')
        
        i += 1
    print('\033[97m════════════════════════════════════════════════')
    choose = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Tài Khoản : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_tiktok1) :
        user_tiktok1 = user_tiktok1[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_tiktok1[0] 
        account_id = account_id1[0]
        banner()
        choose = int(input(Fore.RED+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Số Lượng Job : '))
        DELAY = int(input(Fore.RED+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập delay : '))
        print('\033[97m════════════════════════════════════════════════')
        print(f'\033[1;36m|STT\033[1;97m| \033[1;33mThời gian ┊ \033[1;32mStatus | \033[1;31mType Job | \033[1;32mID Acc | \033[1;32mXu |\033[1;33m Tổng')

        for i in range(choose):
            url2 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id='+str(account_id)+'&data=null'
            checkurl2 = ses.get(url2,headers=headers).json()
            if checkurl2['status'] ==200:
                linkjob = []
                linkjob = str(checkurl2['data']['link'])
                lenjob = len(checkurl2['data']['link'])
                ads_id = checkurl2['data']['id']
                object_id = checkurl2['data']['object_id']
                type = checkurl2['data']['type']
                # os.system("start "+linkjob+"")
                os.system("termux-open-url "+str(linkjob[0:lenjob])+"")
                PARAMS = {
                        'ads_id' : ads_id,
                        'account_id' : account_id,
                        'object_id' : object_id ,
                        'async': 'true',
                        'data': 'null',
                        'type': type,
                        }
                countdown(DELAY)
                url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                time.sleep(1)
                checkurl3 = ses.post(url3,params=PARAMS).json()
                if checkurl3['status'] == 400 :

                        time.sleep(2)

                        url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                        checkurl3 = ses.post(url3,params=PARAMS).json()
                        if checkurl3['status'] == 200:
                            dem += 1
                            local_time = time.localtime()
                            hour = local_time.tm_hour
                            minute = local_time.tm_min
                            second = local_time.tm_sec

                            # Định dạng giờ, phút, giây
                            h = f"{hour:02d}"
                            m = f"{minute:02d}"
                            s = f"{second:02d}"
                            prices = checkurl3['data']['prices']

                            # Cộng dồn giá trị prices vào tổng tiền
                            tong += prices
                            chuoi = (
                                f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                f"\033[1;31m{type}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                f"\033[1;33m{tong} vnđ"
                            )
                            print(chuoi) 
                                # prices = checkurl3['data']['prices']
                                # print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                        else:

                                    time.sleep(2)

                                    url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                                    checkurl3 = ses.post(url3,params=PARAMS).json()
                                    if checkurl3['status'] == 200:
                                        dem += 1
                                        local_time = time.localtime()
                                        hour = local_time.tm_hour
                                        minute = local_time.tm_min
                                        second = local_time.tm_sec

                                        # Định dạng giờ, phút, giây
                                        h = f"{hour:02d}"
                                        m = f"{minute:02d}"
                                        s = f"{second:02d}"
                                        prices = checkurl3['data']['prices']

                                        # Cộng dồn giá trị prices vào tổng tiền
                                        tong += prices
                                        chuoi = (
                                            f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                            f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                            f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                            f"\033[1;31m{type}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                            f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                            f"\033[1;33m{tong} vnđ"
                                        )
                                        print(chuoi) 
                                            # prices = checkurl3['data']['prices']
                                            # print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                    else:
                                        time.sleep(2)

                                        url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                                        checkurl3 = ses.post(url3,params=PARAMS).json()
                                        if checkurl3['status'] == 200:
                                            dem += 1
                                            local_time = time.localtime()
                                            hour = local_time.tm_hour
                                            minute = local_time.tm_min
                                            second = local_time.tm_sec

                                            # Định dạng giờ, phút, giây
                                            h = f"{hour:02d}"
                                            m = f"{minute:02d}"
                                            s = f"{second:02d}"
                                            prices = checkurl3['data']['prices']

                                            # Cộng dồn giá trị prices vào tổng tiền
                                            tong += prices

                                            chuoi = (
                                                f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                                f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                                f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                                f"\033[1;31m{type}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                                f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                                f"\033[1;33m{tong} vnđ"
                                            )
                                            print(chuoi) 
                                                # prices = checkurl3['data']['prices']
                                                # print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                        else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    'async': 'true',
                                                    'data': 'null',
                                                    'type': type,
                                                    }
                elif checkurl3['status'] == 200:
                        dem += 1
                        local_time = time.localtime()
                        hour = local_time.tm_hour
                        minute = local_time.tm_min
                        second = local_time.tm_sec

                        # Định dạng giờ, phút, giây
                        h = f"{hour:02d}"
                        m = f"{minute:02d}"
                        s = f"{second:02d}"
                        prices = checkurl3['data']['prices']

                        # Cộng dồn giá trị prices vào tổng tiền
                        tong += prices

                        chuoi = (
                            f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                            f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                            f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                            f"\033[1;31m{type}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                            f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                            f"\033[1;33m{tong} vnđ"
                        )
                        print(chuoi) 
                    
                    # print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                else :
                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                    if checkskipjob['status'] == 200:
                        message = checkskipjob['message']
                        print(Fore.RED+str(message))
                        PARAMSr = {
                        'ads_id' : ads_id,
                        'account_id' : account_id,
                        'object_id' : object_id ,
                        'async': 'true',
                        'data': 'null',
                        'type': type,
                        }
            else : 
                countdown(15)
                print(checkurl2['message'])
                skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                if checkskipjob['status'] == 200:
                    message = checkskipjob['message']
                    print(Fore.RED+str(message))
                    PARAMSr = {
                    'ads_id' : ads_id,
                    'account_id' : account_id,
                    'object_id' : object_id ,
                    'async': 'true',
                    'data': 'null',
                    'type': type,
                    }
def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f"""
© Tool Gộp Vip  By phamvantung
        Zalo: 0988196974
        Telegram: @toolgolike0
         admin cod: @Dark121918
         ngân hàng: MBBank 
         STK: 3555020409  
\033[1;97mTool By: \033[1;32mVan Tung            \033[1;97mPhiên Bản: \033[1;32m2.2    
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)        
def LIST():
    banner()
os.system('cls' if os.name== 'nt' else 'clear')
banner()
checkfile = os.path.isfile('user.txt')
if checkfile == False:
    AUTHUR = input(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNHẬP Authorization Golike : ')
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()

ses = requests.Session()
User_Agent=random.choice([
"android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9100 Build/KTU84P) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/50.0.3755.367 Mobile Safari/600.8",
"android|Mozilla/5.0 (Linux; Android 5.0; SM-N910V Build/LRX22C) AppleWebKit/601.33 (KHTML, like Gecko) Chrome/54.0.1548.302 Mobile Safari/537.0",
"android|Mozilla/5.0 (Linux; U; Android 7.1; Pixel C Build/NRD90M) AppleWebKit/600.2 (KHTML, like Gecko) Chrome/53.0.2480.357 Mobile Safari/600.7",
"android|Mozilla/5.0 (Linux; U; Android 7.0; Nexus 7 Build/NME91E) AppleWebKit/537.24 (KHTML, like Gecko) Chrome/55.0.1165.180 Mobile Safari/535.4",
"android|Mozilla/5.0 (Android; Android 4.4.4; IQ4502 Quad Build/KOT49H) AppleWebKit/603.22 (KHTML, like Gecko) Chrome/55.0.3246.371 Mobile Safari/535.0",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG SM-G925FQ Build/KOT49H) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/49.0.2349.273 Mobile Safari/533.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; SM-G935S Build/LMY47X) AppleWebKit/601.8 (KHTML, like Gecko) Chrome/51.0.1541.177 Mobile Safari/603.6",
"android|Mozilla/5.0 (Android; Android 7.1; Nexus 6 Build/NME91E) AppleWebKit/533.39 (KHTML, like Gecko) Chrome/52.0.3581.331 Mobile Safari/602.0",
"android|Mozilla/5.0 (Android; Android 7.1; Pixel C Build/NME91E) AppleWebKit/536.42 (KHTML, like Gecko) Chrome/47.0.2862.396 Mobile Safari/534.0",
"android|Mozilla/5.0 (Linux; Android 5.0.1; LG-D725 Build/LRX22G) AppleWebKit/603.18 (KHTML, like Gecko) Chrome/54.0.3919.385 Mobile Safari/601.9",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; Lenovo A7000-a Build/LRX21M;) AppleWebKit/600.8 (KHTML, like Gecko) Chrome/47.0.1683.316 Mobile Safari/534.4",
"android|Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925M Build/LRX22G) AppleWebKit/533.12 (KHTML, like Gecko) Chrome/48.0.3195.222 Mobile Safari/534.1",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; MOTOROLA XT1021 Build/LXB22) AppleWebKit/602.21 (KHTML, like Gecko) Chrome/51.0.3324.323 Mobile Safari/536.2",
"android|Mozilla/5.0 (Linux; Android 4.4; LG-D350 Build/KOT49I) AppleWebKit/601.4 (KHTML, like Gecko) Chrome/50.0.1490.201 Mobile Safari/602.6",
"android|Mozilla/5.0 (Linux; Android 7.0; Xperia Build/NDE63X) AppleWebKit/600.18 (KHTML, like Gecko) Chrome/48.0.3885.393 Mobile Safari/602.7",
"android|Mozilla/5.0 (Android; Android 7.1; Nexus 9X Build/NPD90G) AppleWebKit/536.38 (KHTML, like Gecko) Chrome/52.0.2441.242 Mobile Safari/601.0",
"android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9600 Build/KTU84P) AppleWebKit/602.14 (KHTML, like Gecko) Chrome/53.0.2318.108 Mobile Safari/534.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; MOTO XT1570 MOTO X STYLE Build/LMY47Z) AppleWebKit/534.48 (KHTML, like Gecko) Chrome/55.0.1855.292 Mobile Safari/602.5",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; HTC Butterfly S 919d Build/LRX22G) AppleWebKit/534.18 (K
