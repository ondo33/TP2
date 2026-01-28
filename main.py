def calcul_moyenne(notes):
    if not notes:
        return 0
    return sum(notes) / len(notes)

def afficher_moyenne(notes):
    if moyenne < 10:
        return "faible"
    elif moyenne < 12:
        return "assez bien"
    elif moyenne < 14:
        return "bien"
    else :
        return "tres bien"

list1=[8,9,10]
list2=[10,11,12]
list3=[12,13,14]
list4=[15,16,17]

listes=[list1,list2,list3,list4]
for notes in listes:
    moyenne= calcul_moyenne(notes)
    mention=afficher_moyenne(moyenne)
    print("Notes :", notes)
    print("Moyenne :", moyenne)
    print("Mention :", mention)
    print("-------------------")
 

