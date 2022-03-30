import Compte
#import main

souscpte = []


def Add_souscompte(snum):
    for i in Compte.sommep.keys():
        if snum == i:
            num = input("Entrer le numero du sous-compte: ")
            prct = int(input("Entrer le pourcentage: "))
            soldesc = int(Compte.sommep[snum]) # recuperation du solde principale
            print(soldesc)
            solde2 = (soldesc * prct) / 100
            print(solde2)
            souscpte.append(solde2)
            Compte.sommep[num] = souscpte
            print(Compte.sommep)
            break
        else:
            print("Numéro incorrect")



def Add_sous_sous(num1):
    print(Compte.sommep)
    addsc = Compte.sommep
    i = 0
    for i in addsc.keys():
        i1 = 0
        if num1 == i:
            ssnum = input("Entrer le numéro du sous compte: ")  # numero du sous-compte
            prct1 = int(input("Entrer le pourcentage de solde sous compte: "))  # solde du sous-compte
            ssolde = (int(addsc[num1][0]) * prct1) / 100
            addsc[num1].append([ssnum, ssolde])
            print(addsc)
            break
        else:
            i1 += 1

def credit_souscompte(snum):
    for i in Compte.sommep.keys():
        if snum == i:
            num = input("Entrer le numero du sous-compte: ")
            prct = int(input("Entrer la somme à : "))
            soldesc = Compte.sommep[snum] # recuperation du solde principale
            print(soldesc)
            solde2 = (soldesc * prct) / 100
            print(solde2)
            souscpte.append(solde2)
            Compte.sommep[num] = souscpte
            print(Compte.sommep)
            break
        else:
            print("Numéro incorrect")


def debit_souscompte(snum):
    for i in Compte.sommep.keys():
        if snum == i:
            num = input("Entrer le numero du sous-compte: ")
            prct = int(input("Entrer le pourcentage: "))
            soldesc = Compte.sommep[snum] # recuperation du solde principale
            print(soldesc)
            solde2 = (soldesc * prct) / 100
            print(solde2)
            souscpte.append(solde2)
            Compte.sommep[num] = souscpte
            print(Compte.sommep)
            break
        else:
            print("Numéro incorrect")

