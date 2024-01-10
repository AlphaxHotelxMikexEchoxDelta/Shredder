from res.run import *
import os, sys

run.banner()
run.menu()

while True:
   saisie = str(input("Selectionnez le numero de l'option qui vous convient:  "))
   
   if saisie == "1":
      os.system("clear")
      run.chiffrement()
      sys.exit()

   elif saisie == "2":
      os.system("clear")
      run.dechiffrement()
      sys.exit()
