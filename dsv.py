# Author: suegdu
# I demand my credits to the code wherever it's used.
# Open issues at: https://github.com/suegdu/DSV/issues/new
# NOTE : Spamming Discord's API is against TOS, You may get your account suspended and I am not responsible. For a further caution, use an alt's token and a higher delay.




import random
import string 
import requests
import os
import time
from colorama import Fore,init
from configparser import ConfigParser
import sys
init(autoreset=True)
__version__ = "Author: suegdu DSV 1.9"
__versions__ = "Traductor: a5x for DSV 1.9"
__github__= "https://github.com/suegdu"
__githubs__= "https://github.com/a5x"
dir_path = os.path.dirname(os.path.realpath(__file__))
configur = ConfigParser()
configur.read(os.path.join(dir_path, f"config.ini"))
tokens_list = os.path.join(dir_path, f"tokens.txt")
integ_0 = 0
sys_url = "https://discord.com/api/v9/users/@me"
URL = "https://discord.com/api/v9/users/@me/pomelo-attempt"
def s_sys_h():
   if configur.getboolean("sys","MULTI_TOKEN") == True:
      return {
    "Content-Type": "Application/json",
    "Orgin": "https://discord.com/",

    "Authorization":avail_tokens(tokens_list)[0]
    }
   elif configur.getboolean("sys","MULTI_TOKEN") == False:
      return{
    "Content-Type": "Application/json",
    "Orgin": "https://discord.com/",

    "Authorization":configur.get("sys","TOKEN")
    }
   else:
      return {
    "Content-Type": "Application/json",
    "Orgin": "https://discord.com/",

    "Authorization":configur.get("sys","TOKEN")
    }
def sys_c_t():
   if configur.get("sys","TOKEN") != "":
      pass
   elif configur.get("sys","TOKEN") == "" and configur.getboolean("sys","MULTI_TOKEN") == False:
        print(f"{Lb}[!]{Fore.RED} Aucun TOKEN. MET TON TOKEN DANS LE FICHIER 'config.ini', JUSTE APRÈS 'TOKEN'.")
        exit()
   elif configur.getboolean("sys","MULTI_TOKEN") == True and not avail_tokens(tokens_list)[0]:
       print(f"{Lb}[!]{Fore.RED} Aucun TOKENS. VOUS DEVEZ METTRE TOUT VOS TOKENS DANS LE DOSSIER : 'tokens.txt'.")
       exit()
   elif configur.getboolean("sys","MULTI_TOKEN") is not True and configur.getboolean("sys","MULTI_TOKEN") is not False and configur.get("sys","TOKEN") == "":
       print(f"{Lb}[!]{Fore.RED} configuration invalide détecter. SVP Merci de revérifier, `config.ini` et de sauvegarder\n. TIPS: pour les multi tokens ouvrir config.ini retire ton token de 'token' et remplace MULTI_TOKEN = false par MULTI_TOKEN = true et pour un seul token mettre MULTI_TOKEN = false et mettre votre token dans 'token'. ")
       exit()
available_usernames = []
def vali_():
   return {
    "Content-Type": "Application/json",
    "Orgin": "https://discord.com/",
    "Authorization":avail_tokens(tokens_list)[integ_0]
    }
av_list = os.path.join(dir_path, f"available_usernames.txt")
sample_0 = r"_."
Lb = Fore.LIGHTBLACK_EX
Ly = Fore.LIGHTYELLOW_EX
Delay = configur.getfloat("other","default_delay")
def setconf():
   global string_0
   global digits_0
   global punctuation_0
   #global multi_token_0
   global sat_string
   global sat_digits
   global sat_multi_token
   global sat_punct
   sat_string = configur.getboolean("config","string")
   sat_digits = configur.getboolean("config","digits")
   sat_punct = configur.getboolean("config","punctuation")
   sat_multi_token = configur.getboolean("sys","MULTI_TOKEN")
   if sat_string == True:
      string_0 = string.ascii_lowercase
   elif sat_string == False:
      string_0 = ""
   else:
      string_0 = string.ascii_lowercase
      sat_string = True
   if sat_digits == True:
      digits_0 = string.digits
   elif sat_digits == False:
      digits_0 = ""
   else:
      digits_0 = string.digits
      sat_digits = True
   if sat_punct == True:
      punctuation_0 = sample_0
   elif sat_punct == False:
      punctuation_0 = ""
   else:
      punctuation_0 = sample_0
      sat_punct = True
   if sat_punct == False and sat_digits == False and sat_string == False:
      punctuation_0 = sample_0
      digits_0 = string.digits
      string_0 = string.ascii_lowercase

def main():
    sys_c_t()
    os.system(f"title {__version__} - Connectée a {requests.get(sys_url,headers=s_sys_h()).json()['username']}")
    s_sys_h()
    setconf()    
    print(f"""{Fore.LIGHTYELLOW_EX}
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
  {__version__} 
  {__github__}                     {Fore.LIGHTCYAN_EX}Connectée a {requests.get(sys_url,headers=s_sys_h()).json()['username']}{Ly}#{Fore.LIGHTCYAN_EX}{requests.get(sys_url,headers=s_sys_h()).json()['discriminator']}{Ly}
                            
  ██████╗ ███████╗██╗   ██╗                     {Fore.LIGHTCYAN_EX}1-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Générer des noms et les vérifier{Fore.LIGHTBLACK_EX}]{Ly}             
  ██╔══██╗██╔════╝██║   ██║                     {Fore.LIGHTCYAN_EX}2-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Vérifier une liste spécifique{Fore.LIGHTBLACK_EX}]{Ly}             
  ██║  ██║███████╗██║   ██║                     
  ██║  ██║╚════██║╚██╗ ██╔╝                     Config.ini:
  ██████╔╝███████║ ╚████╔╝                             {Fore.LIGHTCYAN_EX}Digits: {Fore.YELLOW}{sat_digits}{Ly}                {Fore.BLUE}████{Fore.WHITE}████{Fore.RED}████{Fore.LIGHTYELLOW_EX}
  ╚═════╝ ╚══════╝  ╚═══╝                              {Fore.LIGHTCYAN_EX}String: {Fore.YELLOW}{sat_string}{Ly}                {Fore.BLUE}████{Fore.WHITE}████{Fore.RED}████{Fore.LIGHTYELLOW_EX}
                                                       {Fore.LIGHTCYAN_EX}Punctuation: {Fore.YELLOW}{sat_punct}{Ly}           {Fore.BLUE}████{Fore.WHITE}████{Fore.RED}████{Fore.LIGHTYELLOW_EX}
  {__githubs__}                               {Fore.LIGHTCYAN_EX}Multi-Token: {Fore.YELLOW}{sat_multi_token}{Ly}
  {__versions__}                           {Fore.LIGHTCYAN_EX}Delay: {Fore.YELLOW}{Delay}{Ly}
                                                         
  Discord Username's checker French version.   / Owner of this original tool : https://github.com/suegdu
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
""")
    proc0()
    
def setdelay():
   global Delay
   print(f"{Lb}[!]{Ly} Délai par défaut est : {Delay}s (config.ini){Lb}")
   d_input = input(f"{Lb}[{Ly}Modifier le délai ou (Appuie sur ENTRER pour skip){Lb}]:> ")
   if d_input=="" or d_input.isspace():
      return
   else:   
    try:
      int(d_input)
      Delay = int(d_input)
    except ValueError:
      print(f"{Lb}[!]{Fore.RED}Erreur: Merci de rentrer quelque chose de valide. strings.")
      setdelay()

def proc0():
    m_input = input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}DSV{Fore.LIGHTBLACK_EX}]:> {Fore.LIGHTYELLOW_EX}").lower()
    if m_input=="exit":
        sys.exit(0)
    if m_input=="":
        proc0()
    elif m_input=="2":
        setdelay()
        opt2load()
    elif m_input=="1":
       setdelay()
       opt1load()
    else:
        proc0()
def validate_names(opt,usernames):
   global available_usernames
   global integ_0
   if opt == 2:
    for username in usernames:
       body = {
           "username": username
       }
       time.sleep(Delay)
       endpoint = requests.post(URL, headers=vali_(), json=body)
       json_endpoint = endpoint.json()
       if endpoint.status_code == 429 and sat_multi_token == True and len(avail_tokens(tokens_list)) != integ_0:
           integ_0 = (integ_0 +1) % len(avail_tokens(tokens_list))
           print(f"{Lb}[!]{Ly} Token {integ_0} TOKEN EST A LA LIMITE. Utilisation du TOKEN index : {integ_0} connectée a : {requests.get(sys_url,headers=vali_()).json()['username']}#{requests.get(sys_url,headers=vali_()).json()['discriminator']}")
       elif endpoint.status_code == 429 and sat_multi_token == False:
         sleep_time = endpoint.json()["retry_after"]
         print(f"{Lb}[!]{Fore.RED} RateLimite atteinte. Pause de {sleep_time}s (Discord ratelimite) ceci ne provient pas de ce tool")
         time.sleep(sleep_time)
       if json_endpoint.get("taken") is not None:
           if json_endpoint["taken"] is False:
            print(f"{Lb}[+]{Fore.LIGHTGREEN_EX} '{username}' disponible.")
            save(username)
            available_usernames.append(username)
           elif json_endpoint["taken"] is True:
              print(f"{Lb}[-]{Fore.RED} '{username}' pas disponible.")
       else:
           print(f"{Lb}[?]{Fore.RED} Erreur validation '{username}': {endpoint.json()['message']} |DSV: Merci de vérifier que votre token est valide.")
   elif opt == 1:
       body = {
           "username": usernames
       }
       endpoint = requests.post(URL, headers=vali_(), json=body)
       json_endpoint = endpoint.json()
       if endpoint.status_code == 429 and len(avail_tokens(tokens_list)) != integ_0:
           integ_0 = (integ_0 +1) % len(avail_tokens(tokens_list))
           print(f"{Lb}[!]{Ly} Token {integ_0} TOKEN EST A LA LIMITE. Utilisation du TOKEN index  {integ_0} connectée a : {requests.get(sys_url,headers=vali_()).json()['username']}#{requests.get(sys_url,headers=vali_()).json()['discriminator']}")
       elif endpoint.status_code == 429 and sat_multi_token == False:
         sleep_time = endpoint.json()["retry_after"]
         print(f"{Lb}[!]{Fore.RED} RateLimite atteinte. Pause de {sleep_time}s (Discord ratelimite) ceci ne provient pas de ce tool")
         time.sleep(sleep_time)
       if json_endpoint.get("taken") is not None:
           if json_endpoint["taken"] is False:
            print(f"{Lb}[+]{Fore.LIGHTGREEN_EX} '{usernames}' disponible.")
            save(usernames)
            available_usernames.append(usernames)
           elif json_endpoint["taken"] is True:
              print(f"{Lb}[-]{Fore.RED} '{usernames}' pas disponible.")
       else:
           print(f"{Lb}[?]{Fore.RED} Erreur validation '{usernames}': {endpoint.json()['message']} |DSV: Merci de vérifier que votre token est valide.")
def avail_tokens(path):
   with open(path, 'r') as at:
        tokens = at.read().splitlines()
   return tokens
def exit():
   input(f"{Fore.YELLOW}Appuie sur ENTRER pour quitter.")
   sys.exit(0)
def checkavail(): 
   if len(available_usernames) < 1:
      print(f"{Lb}[!]{Fore.RED}Erreur: Aucun nom d'utilisateur disponible trouvé.")
      exit()
   else:
      return
def opt2load():
    global av_list
    global dir_path
    list_path = os.path.join(dir_path, f"usernames.txt")
    print(f"{Lb}[!]{Ly}Verification de 'usernames.txt' Pour une potentielle liste valide...")
    try:
     with open(list_path) as file:
      usernames = [line.strip() for line in file]
      validate_names(2,usernames)
     checkavail()
     print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Fini. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Nom d'utilisateur valide, sauvegarde effectué ! se situe dans ce fichier : '{av_list}' .")
     exit()
    except FileNotFoundError:
       print(f"{Lb}[!]{Fore.RED}Erreur: impossible de trouver (usernames.txt). Merci de créer le même nom de fichier dans le même répertoire : \n({dir_path}\\)")
       exit()
def opt1load():
   opt1_input:int = input(f"{Lb}[{Ly}Combien de lettre(s) dans le nom d'utilisateur?{Lb}]:> ")
   try:
    int(opt1_input)
    if int(opt1_input) >32 or int(opt1_input) <2:
       print(f"{Lb}[!]{Fore.RED}Erreur: LES NOMS D'UTILISATEUR PEUVENT CONTENIR UNIQUEMENT 2 à 32 CARACTERES PAS PLUS / PAS MOINS.")
       opt1load()
    opt2_input:int = input(f"{Lb}[{Ly}Combien de nom d'utilisateur veux-tu générer?{Lb}]:> ")
    opt1func(int(opt2_input),int(opt1_input))
   except ValueError:
      print(f"{Lb}[!]{Fore.RED}Erreur: Merci de rentrer quelque chose de valide. strings.")
      opt1load()
def save(content:string):
   with open(av_list, "a") as file:
        file.write(f"\n{content}")
def opt1func(v1,v2):
   for i in range(v1):
    name = get_names(int(v2))
    validate_names(1,name)
    time.sleep(Delay)
   checkavail()
   print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Fini. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Nom d'utilisateur valide, sauvegarde effectué ! se situe dans ce fichier : '{av_list}' .")
   exit()
def get_names(length: int) ->str:
   return ''.join(random.sample(string_0 + digits_0 + punctuation_0, length))
    
if __name__ == "__main__":
    main()
