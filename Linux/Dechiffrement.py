import subprocess

print("""
████████╗██╗  ██╗███████╗      ███████╗██╗  ██╗██████╗ ███████╗██████╗ ██████╗ ███████╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝      ██╔════╝██║  ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
   ██║   ███████║█████╗        ███████╗███████║██████╔╝█████╗  ██║  ██║██║  ██║█████╗  ██████╔╝
   ██║   ██╔══██║██╔══╝        ╚════██║██╔══██║██╔══██╗██╔══╝  ██║  ██║██║  ██║██╔══╝  ██╔══██╗
   ██║   ██║  ██║███████╗  No  ███████║██║  ██║██║  ██║███████╗██████╔╝██████╔╝███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝      ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ 
""")

CodeSecret_0 = list(input("Entrez la chaines de characteres à dechiffer:\t"))
CodeSecret_1 = []
CodeSecret_2 = []
Balisage_0 = list(input("Entrez la balise de la chaines de characteres chiffrer:\t"))
Balisage_1 = []
Balisage_1X = []
Balisage_2 = []


def Del_CharacteresTrompeurs():
    Y = 0
    for I in range(0,len(CodeSecret_0)):
        if I == Y:
            CodeSecret_1.append(CodeSecret_0[I])
            Y += 2
    U = 0
    for R in range(0,len(CodeSecret_1)):
        if R == U:
            CodeSecret_2.append(CodeSecret_1[R])
            U += 2

def Balisage():
    Y = 0
    for I in range(0,len(Balisage_0)):
        if I != Y:
            Balisage_1.append(Balisage_0[I])
            Y += 2
        if I == Y:
            Balisage_1X.append(Balisage_0[I])

    for R in reversed(Balisage_1):
        Balisage_2.append(R)



Del_CharacteresTrompeurs()
Balisage()
print("".join(CodeSecret_2))
print("".join(Balisage_2))
print("".join(Balisage_1X))






"""
# Y🍉b℀2ℍ8🍌6ℊp▕kℤG℀2ℚ5ℵkℸX🍌#ℾzℸ1ℱl🍌2▙a▂uℴKℴ2
Y26k2k#12u2
apap namtab

Y26u21k2k2
2k2k12u62Y
Y26 k2k12u  2  [2, 10]
"""
