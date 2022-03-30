import  Souscompte

sommep = {} # dico pour le compte principal et sous-compte
numcompte = []
numMnt = []
listecompte = []

def creation_compte(n1, solde1):
    numcompte.append(n1)
    sommep[n1] = solde1
    print(sommep)
    return sommep

def credit_compte(n1,somme):
    try:
        for i in sommep.keys():
            if n1 == i:
                numcompte.append(n1)
                sol = int(sommep[n1]) + somme
                sommep[n1] = sol
                print(sommep)
                Souscompte.Add_souscompte()
                break
            else:
                print("Numéro de compte invalide")

    except:
        print("Erreur")

