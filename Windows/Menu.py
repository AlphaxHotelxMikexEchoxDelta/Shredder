import os, sys

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
      os.system('cmd /k "cls & python3 Windows/Chiffrement.py"')
      X = True
   
   elif Saisi == "2":
      os.system('cmd /k "cls & python3 Windows/Dechiffrement.py"')
      X = True

   elif Saisi == "3":
      os.system('cmd /k "cls & python3 Windows/Fonctionnement.py"')
      X = True
   
   elif Saisi.upper() == "TURTLE NINJA":
      print("\t-->  https://www.youtube.com/watch?v=AxuvUAjHYWQ  ")

   elif Saisi.upper() == "EXIT":
      print("\n\tAurevoir !")
      sys.exit()

   else:
      print("Saisi inconnu !")


print("\n\tAurevoir !")
os.system('cmd /k "timeout /T 8 & cls"')