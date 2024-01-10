
import subprocess
from sys import *
import sys

print("""
████████╗██╗  ██╗███████╗    ███████╗██╗  ██╗██████╗ ███████╗██████╗ ██████╗ ███████╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██║  ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
   ██║   ███████║█████╗      ███████╗███████║██████╔╝█████╗  ██║  ██║██║  ██║█████╗  ██████╔╝
   ██║   ██╔══██║██╔══╝      ╚════██║██╔══██║██╔══██╗██╔══╝  ██║  ██║██║  ██║██╔══╝  ██╔══██╗
   ██║   ██║  ██║███████╗    ███████║██║  ██║██║  ██║███████╗██████╔╝██████╔╝███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ 
""")

print("""
      ################By Captain A################
      #                                          #
      #  Option ↴                                #
      #  1 / Chiffrement                         #
      #  2 / Dechiffrement                       #
      #  3 / Comment cela marche?                #
      #                                          #
      ############################################
""")

X = False
while X == False:
   Saisi = input("Selectionnez l'option qui vous convient:  ")
   
   if Saisi == "1":
      subprocess.call("clear ; python3 Chiffrement.py | lolcat", shell=True)
      X = True
   
   elif Saisi == "2":
      subprocess.call("clear ; python3 Dechiffrement.py | lolcat", shell=True)
      X = True

   elif Saisi == "3":
      subprocess.call("clear ; python3 Fonctionnement.py | lolcat", shell=True)
      X = True
   
   elif Saisi.upper() == "TURTLE NINJA":
      print("\t-->  https://www.youtube.com/watch?v=AxuvUAjHYWQ  ")

   elif Saisi.upper() == "EXIT":
      print("\n\tAurevoir !")
      sys.exit()

   else:
      print("Saisi inconnu !")


print("\n\tAurevoir !")
subprocess.call("sleep 8s ; clear", shell=True)