from moduleprojet2 import*
from tkinter import*
from csv import*

def read(nom_du_fichier):
    assert type(nom_du_fichier)!='str'
    fichier=open("listefichier.csv", encoding='utf8')
    tableau = list(DictReader(fichier))
    fichier.close()
    liste_fichier =[elt['liste_des_fichier'] for elt in tableau if elt['liste_des_fichier'] == nom_du_fichier]
    if len(liste_fichier) == 0:
        return
    else :
        fichier=open(nom_du_fichier, encoding='utf8')
        tableau = list(DictReader(fichier,delimiter=";"))
        fichier.close()
        return tableau

print(read('1nsi.csv'))
