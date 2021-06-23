# coding=utf-8
#!/usr/bin/env python3

""" 
Before changing the program and publishing it somewhere, please
Please note that this program is under GPLv3 license.
More information:
https://tr.wikipedia.org/wiki/gnu_genel_kamu_lisans%c4%b1
https://www.gnu.org/licenses/quick-guide-gplv3.html
"""

__author__ = "Ladroa : @ladroa__"
__license__ = "GPLv3"
__version__ = "0.1"
__status__ = "being developed"



from time import time, sleep
from random import choice
from multiprocessing import Process

from libs.utils import CheckPublicIP, IsProxyWorking
from libs.utils import PrintStatus, PrintSuccess, PrintError
from libs.utils import PrintBanner, GetInput, PrintFatalError
from libs.utils import LoadUsers, LoadProxies, PrintChoices

from libs.instaclient import InstaClient

USERS = []
PROXIES = []

def MultiThread(username, userid, loginuser, loginpass, proxy, reasonid):
    client = None
    if (proxy != None):
        PrintStatus("[" + loginuser + "]", "Logging into the Account!")
        client = InstaClient(
            loginuser,
            loginpass,
            proxy["ip"],
            proxy["port"]
        )
    else:
        PrintStatus("[" + loginuser + "]", "Logging into the Account!")
        client = InstaClient(
            loginuser,
            loginpass,
            None,
            None
        )
        
    client.Connect()
    client.Login()
    client.Spam(userid, username, reasonid)
    print("")

def NoMultiThread():
    for user in USERS:
        client = None
        if (useproxy):
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Logging into the Account!")
            client = InstaClient(
                user["user"],
                user["password"],
                proxy["ip"],
                proxy["port"]
            )
        else:
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Logging into the Account!")
            client = InstaClient(
                user["user"],
                user["password"],
                None,
                None
            )
        
        client.Connect()
        client.Login()
        client.Spam(userid, username, reasonid)
        print("")


if __name__ == "__main__":
    PrintBanner()
    PrintStatus("Loading users!")
    USERS = LoadUsers("./users.txt")
    PrintStatus("Loading Proxes!")
    PROXIES = LoadProxies("./proxy.txt")
    print("")

    username = GetInput("Şikayet etmek istediğiniz hesap kullanıcı adı:")
    userid = GetInput("Şikayet etmek istediğiniz hesap numarası:")
    useproxy = GetInput("Proxy kullanmak istiyor musunuz? [Evet Hayır]:")
    if (useproxy == "Evet"):
        useproxy = True
    elif (useproxy == "Hayır"):
        useproxy = False
    else:
        PrintFatalError("Lütfen sadece 'Evet' veya 'Hayır' girin!")
        exit(0)
    usemultithread = GetInput("Çoklu iş parçacığı kullanmak istiyor musunuz? [Evet / Hayır] (Çok fazla kullanıcınız varsa veya bilgisayarınız yavaşsa bu özelliği kullanmayın!):")
    
    if (usemultithread == "Evet"):
        usemultithread = True
    elif (usemultithread == "Hayır"):
        usemultithread = False
    else:
        PrintFatalError("Lütfen sadece 'Evet' veya 'Hayır' girin!")
        exit(0)
    
    PrintChoices()
    reasonid = GetInput("Lütfen yukarıdaki şikayetin nedenlerinden birini seçin (ör. spam için 1):")

    
    
    
    print("")
    PrintStatus("Ladroa spam bot başlatılıyor")
    print("")

    if (usemultithread == False):
        NoMultiThread()
    else:
        for user in USERS:
            p = Process(target=MultiThread,
                args=(username,
                    userid,
                    user["user"],
                    user["password"],
                    None if useproxy == False else choice(PROXIES),
                    reasonid
                )
            )
            p.start() 
    

    
