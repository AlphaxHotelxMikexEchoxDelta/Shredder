# coding:utf-8
from random import *

print("""
████████╗██╗  ██╗███████╗    ███████╗██╗  ██╗██████╗ ███████╗██████╗ ██████╗ ███████╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██║  ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
   ██║   ███████║█████╗      ███████╗███████║██████╔╝█████╗  ██║  ██║██║  ██║█████╗  ██████╔╝
   ██║   ██╔══██║██╔══╝      ╚════██║██╔══██║██╔══██╗██╔══╝  ██║  ██║██║  ██║██╔══╝  ██╔══██╗
   ██║   ██║  ██║███████╗    ███████║██║  ██║██║  ██║███████╗██████╔╝██████╔╝███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ 
""")

ChangementFinal = []
Changement = []
Changement_1 = []
Changement_2 = []

Liste_NumLettre_Values = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
Liste_NumLettre_Keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
Dictionnaire_NumLettre = {}
Liste_CharacteresSpeciaux = ["℠","℡","™","℣","ℤ","℥","Ω","℧","ℨ","℩","K","Å","ℬ","ℭ","℮","ℯ","ℰ","ℱ","Ⅎ","ℳ","ℴ","ℵ","ℶ","ℷ","ℸ","ℹ","℺","℻","ℼ",
"ℽ","ℾ","ℿ","℀","℁","ℂ","℃","℄","℅","℆","ℇ","℈","℉","ℊ","ℋ","ℌ","ℍ","ℎ","ℐ","ℑ","ℒ","ℓ","℔","ℕ","№","℗","℘","ℙ","ℚ","ℛ","ℜ",
"ℝ","℞","℟","▂","▃","▄","▅","▆","▇","█","▉","▊","▋","▌","▍","▎","▐","░","▒","▓","▔","▕","▖","▗","▘","▙","▚","▛","▜","▝",
"▞","▟","🍌","🍏","🍍","🍐","🍊","🍋","🍉","🍇","🍓","🥝"]



def Aide_Dechiffrage():
    Changement.append(Changement_1)
    Changement.append(Changement_2)
    for i in reversed(list(Changement[0][0])):
        ChangementFinal.append(i)
        


def ChangeCharacteres(CodeSecret_1):
    Changement1 = []

    for i in Liste_NumLettre_Keys:  
        X = choice(Liste_NumLettre_Values)
        Dictionnaire_NumLettre[i] = X
        Liste_NumLettre_Values.remove(X)
    Dictionnaire_NumLettre[" "]="#"

    for Y in CodeSecret_1:
        for i in Dictionnaire_NumLettre:
            if Y == i:
                Changement1.append(Y)
                Changement1.append(Dictionnaire_NumLettre[Y])
                CodeSecret_2.append(Dictionnaire_NumLettre[Y])

    Changement_1.append("".join(Changement1))


def Change_Position():
    CodeSecret_X =  list("".join(CodeSecret_2))

    X = randint(0,len(CodeSecret_2))
    Y = randint(0,len(CodeSecret_2))
    
    if Y > X :
        for g in reversed(CodeSecret_X[X:Y]):
            CodeSecret_3.append(g)

        Changement_2.append(X)
        Changement_2.append(Y)

        CodeSecret_3[:0] = CodeSecret_2[:X+1]
        CodeSecret_3[-1:] = CodeSecret_2[Y:]

    elif Y < X:
        for g in reversed(CodeSecret_X[Y:X]):
            CodeSecret_3.append(g)

        Changement_2.append(Y)
        Changement_2.append(X)

        CodeSecret_3[:0] = CodeSecret_2[:Y+1]
        CodeSecret_3[-1:] = CodeSecret_2[X:]

    else:
        CodeSecret_3[:] = CodeSecret_2
        Changement_2.append("NONE")


def CharacteresTrompeur_Normaux():
    
    CodeSecret_X = list("$".join(CodeSecret_3))

    for i in range(0,len(CodeSecret_X)):

        X = choice(Liste_NumLettre_Keys)
        if CodeSecret_X[i] == "$":
            CodeSecret_X[i] = X

    CodeSecret_4.append("".join(CodeSecret_X))


def CharacteresTrompeur_Ilisible():

    CodeSecret_X = list("&".join(CodeSecret_4[0]))

    for i in range(0,len(CodeSecret_X)):

        X = choice(Liste_CharacteresSpeciaux)
        if CodeSecret_X[i] == "&":
            CodeSecret_X[i] = X

    CodeSecret_5.append("".join(CodeSecret_X))


def Chiffre_Moi():
    ChangeCharacteres(CodeSecret_1)
    Change_Position()
    CharacteresTrompeur_Normaux()
    CharacteresTrompeur_Ilisible()
    Aide_Dechiffrage()
    Code_TXT = open("Code_Chiffrer","w")
    Code_TXT.write(str(CodeSecret_0))
    Code_TXT.write("    <= chaines de Characteres")
    Code_TXT.write("\n\n")
    Code_TXT.write(str("".join(CodeSecret_5)))
    Code_TXT.write("    <= Chiffrement de la chaines de characteres")
    Code_TXT.write("\n\n")
    Code_TXT.write(str("".join(ChangementFinal)))
    Code_TXT.write(str(Changement[1]))
    Code_TXT.write("    <= Balise de Dechiffrage")
    Code_TXT.write("\n\n")
    print("\nchiffrage de la chaines de caracteres:\t{0}\n\nBalise de Dechiffrage:\t{1}{2}".format("".join(CodeSecret_5),"".join(ChangementFinal),Changement[1] ))
    print("\n\n\n( vous trouverez toutes ces informations dans le fichier 'Code_Chiffrer' )")


CodeSecret_0 = input("entrer les characteres a chiffrer :\t")

CodeSecret_1 = list(CodeSecret_0)
CodeSecret_2 = []
CodeSecret_3 = []
CodeSecret_4 = []
CodeSecret_5 = []

Chiffre_Moi()