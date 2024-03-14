import rarfile
import sys

karsilama = """
███╗   ███╗██╗   ██╗     ██████╗  █████╗ ██████╗ ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
████╗ ████║╚██╗ ██╔╝     ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██╔████╔██║ ╚████╔╝█████╗██████╔╝███████║██████╔╝██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██║╚██╔╝██║  ╚██╔╝ ╚════╝██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
██║ ╚═╝ ██║   ██║        ██║  ██║██║  ██║██║  ██║██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
╚═╝     ╚═╝   ╚═╝        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝

"""
print(karsilama)
rarfile_adres = input("lütfen rar dosyanızın yolunu giriniz:")
password_list = input("lütfen wordlist dosyanızın yolunu giriniz:")

rarfile.UNRAR_TOOL = r"C:\Users\aksar\PycharmProjects\UnRAR.exe"
rar_file = rarfile.RarFile(rarfile_adres)
passwordlist = open(password_list)
print("******************************")
parola_bulundu_mu = False
sayici = 0
islenen_password = ""
for password in passwordlist:
    sayici = sayici + 1
    islenen_password = password.strip("\n")
    print("{} TANE ŞİFRE DENENDİ".format(sayici))
    try:
        rar_file.setpassword(islenen_password)
        rar_file.testrar()
        print("*******************************")
        print("Parola bulundu :) . {} TANE DENEMEDE BULUNDU".format(sayici))
        parola_bulundu_mu = True
        break
    except:
        continue
if parola_bulundu_mu:
    print("ŞİFRE ->> {}", format(islenen_password))
    sys.exit()
else:
    print("***********************************")
    print("Aradım taradım her taşın altına baktım ama bulamadım")    