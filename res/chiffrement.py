from random import randint

class Chiffrement:
    
    message = [None,None,None,None]

    def isEmpty(list):
        cpt = 0
        for something in list:
            if something == None:
                cpt+1
        if cpt == len(list):
            return True
        else:
            return False
    
    def add_letters(letters):
        for i in range(97,123):
            letters.append(chr(i))

    def key_changer(key,key_split):
        for i in range(len(key_split)):
            key[i] = key[i]+str(i)

    def dup_tableau(list,word_split,key_split):
        list.append(word_split[:len(key_split)])
        for i in word_split[:len(key_split)]:
            word_split.remove(i)

    def adds_chars(list,key_split,adds):
        for y in range(len(list)):
            if len(list[y]) != len(key_split):
                adds = len(key_split) - len(list[y])
                for _ in range(0,adds):
                    list[y].append(chr(randint(97,123)))
    
    def pos_to_pos(y,list1,list2):
        for o in range(len(list1)):
            list2[o].append(list1[o][y])


# Part 1 - Take the key and the Word(s), change them with DUPLICE
    def DUPLICE(key,key_split,word_split,adds,letters,message=message):
        add_letters(letters)
        key_changer(key,key_split)
        while isEmpty(word_split) != True:
            dup_tableau()
        adds_chars()
        dup_order()
        message[3] = sorted(key_split)
        message[1] = str(adds)


# Part 2 - Take the key to change it with ROTN
    def ROTN(word,letters,message=message):
        add_letters(letters)
        liste_rotn = []
        rotn = randint(0,26)
        word_split = list(str(word))
        word_final = []

        for i in range(97,123):
            letters.append(chr(i))

        for b in range(rotn-1, len(letters)):
            liste_rotn.append(letters[b])
        for o in range(0, rotn-1):
            liste_rotn.append(letters[o])
            
        for b in word_split:
            for y in range(0,len(letters)):
                if b == letters[y]:
                    word_final.append(liste_rotn[y])
            
        message[0] = str(rotn)
        message[2] = "".join(word_final)    


# Part 3 - Take the key to change it with PROLYBE 
    def POLYBE(message=message):
        letters = [ ['a','b','c','d','e'],
                    ['f','g','h','i','k'],
                    ['l','m','n','o','p'],
                    ['q','r','s','t','u'],
                    ['v','w','x','y','z'] ]
        key_split = list(message[2])
        key_final = []

        for letter in key_split:
            for y in range(len(letters)):
                for x in range(len(letters[y])):
                    if letter == letters[y][x]:
                        key_final.append(str(y+1)+str(x+1))
            if letter == "j":
                key_final.append("24")

        message[2] = "".join(key_final)