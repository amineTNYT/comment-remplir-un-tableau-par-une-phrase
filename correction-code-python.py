from numpy import array

def Calcule(ch):
    c = 1  # Commence à 1 car même sans espaces, il y a au moins 1 mot
    for i in range(len(ch)):
        if ch[i] == " ":  # Si on trouve un espace
            c = c + 1     
    return c  # Retourne le nombre total de mots


#methode repeter jusqu'à
def Remplir(ch, T):
    pos = ch.find(" ")                  # Trouve la position du premier espace
    N = 0                               # Indice pour remplir le tableau T
    while pos != -1:                    # Tant qu'on trouve des espaces
        element = ch[:pos]              # Extrait le mot depuis le début jusqu'à l'espace
        T[N] = element                  # Stocke le mot dans le tableau
        N = N + 1                       # Passe à la case suivante du tableau
        ch = ch[pos + 1:]               # Supprime le mot traité de la chaîne
        pos = ch.find(" ")              # Cherche le prochain espace
    T[N] = ch  # Ajoute le dernier mot restant (sans espace après)

def Affichage(T, n):
    for i in range(n):  # Parcours toutes les cases utilisées du tableau
        print("T[", i, "] =", T[i])  # Affiche l'indice et le mot

# Programme Principal
ch = input("Donner une phrase : ")  # Saisie de la phrase
n = Calcule(ch)  # Calcule le nombre de mots
T = array([str] * n)  # Crée un tableau numpy de taille n
Remplir(ch, T)  # Remplit le tableau avec les mots
Affichage(T, n)  # Affiche le contenu du tableau
