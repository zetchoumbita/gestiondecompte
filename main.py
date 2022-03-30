import Compte
import Souscompte

#liste1 = [[1,2],[1,4]]
#liste1.append([5,7])
#print(liste1)
#liste1.append([8,3])
#print(liste1)
#print(liste1.count([1,4]))


#liste = [1,2,3,4]
#print(len(liste))

#Compte.creation_compte()
#Souscompte.Add_souscompte()
#Souscompte.Add_sous_sous()
#Souscompte.add()

#m ={}
#p = {}
#p["jour"] = 100
#m["key"] = [1000,["sc",100],["sp",5000]]
#m["key"].append(["si",700])
#m["key"][0] = 500
#print(m["key"])
#test = {}
#test["nom"] = "landry"
#test["prenom"] = "kokou"
#for i in test.keys():
#  print(i)
#print(m.keys().mapping)
#print(p["jour"])
#print(m["key"][0])


def Menu():
    print(
        "*************************************** COMPTE DE BANCAIRE **************************************************\n"
        "1- Enregister un compte\n"
        "2- Enregistrer un sous-compte\n"
        "3- Enregister un élément d'un sous-compte\n"
        "4- crediter compte\n"
        "5- debiter compte\n"
        "6- sortir")
    val = int(input("Entrez une valeur : "))
    while (val != 6):
        if val == 1:
            n1 = input("Entrer un numéro de compte principal: ")
            solde1 = int(input("Entrer le solde initial: "))
            Compte.creation_compte(n1, solde1)
        elif val == 2:
            print("*********** Enregistrement du sous-compte ************")
            snum1 = input("Entrer numéro principal: ")
            Souscompte.Add_souscompte(snum1)
        elif val == 3:
            num12 = input("Entrer le numero du compte de vérification sous-compte: ")
            Souscompte.Add_sous_sous(num12)
        elif val == 4:
            n1 = input("Entrer un numéro de compte principal: ")
            solde1 = int(input("Entrer montant: "))
            try:
                Compte.credit_compte(n1, solde1)
            except:
                print(" *** Erreur compte inexistant ***")
                Menu()
        val = int(input("Entrez une valeur: "))




#valeur = int(input("Entrez une valeur : "))
Menu()


