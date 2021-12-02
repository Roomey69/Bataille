import random

jeu = []
p1 = []
p2 = []
hit = 50  #Nombre de coup maximum

def distribution(jeu,p1,p2):
    '''La fonction retourne deux listes qui sont enfaite un jeu de cartes mélanger en deux'''
    for i in range(8):   #Crée un jeu de carte (32 cartes - De 7 à l'As)
        for k in range(4):
            jeu.append(i+7)

    random.shuffle(jeu)   #Mélanger le jeu
    
    for i in range(16):   #Distribuer les cartes
        p1.append(jeu[i])   #On donne la 1ere moitié du jeu au joueur 1
        del jeu[i]   #On supprime la 1ere moitié du jeu
    p2=jeu   #On donne la 2e partie du jeu (le reste de la liste) au joueur 2
    return p1, p2


def tour_de_jeu(p1,p2):
    cartep1 = p1[0]
    cartep2 = p2[0]
    if cartep1>cartep2:  #Le joueur 1 a une meilleur carte
        p2.pop(0)
        p1.append(cartep2)
        p1.pop(0)
        p1.append(cartep1)
        affichage(p1, p2, cartep1, cartep2)
        print("Le joueur 1 l'emporte !")
    elif cartep2>cartep1:  #Le joueur 2 a une meilleur carte
        p1.pop(0)
        p2.append(cartep1)
        p2.pop(0)
        p2.append(cartep2)
        affichage(p1, p2, cartep1, cartep2)
        print("Le joueur 2 l'emporte !")
    elif cartep1==cartep2:  #Bataille
        affichage(p1, p2, cartep1, cartep2)
        print("Bataille !")
        bataille_p1 = []
        bataille_p2 = []
        bataille_p1.append(cartep1)
        bataille_p2.append(cartep2)
        p1.pop(0)
        p2.pop(0)
        print("Cliquez sur entrée pour jouer !")
        continuer=input()
        while cartep1==cartep2:   
            bataille_p1.append(p1[0])  #Les cartes égalités sont ajoutées à la liste temporaire
            bataille_p2.append(p2[0])  
            p1.pop(0)
            p2.pop(0)
            bataille_p1.append(p1[0])  #Les cartes façe caché sont ajoutées à la liste temporaire
            bataille_p2.append(p2[0]) 
            cartep1=p1[0]
            cartep2=p2[0]
            p1.pop(0)
            p2.pop(0)
            if not cartep1>cartep2 or cartep2>cartep1:
                affichage(p1, p2, cartep1, cartep2)
                print("Double bataille !")
                print("Cliquez sur entrée pour jouer !")
                continuer=input() 
        if cartep1>cartep2:
            p1.extend(bataille_p2)
            p1.extend(bataille_p1)
            bataille_p2.clear()
            bataille_p1.clear()
            affichage(p1, p2, cartep1, cartep2)
            print("Le joueur 1 remporte la bataille !")
        elif cartep2>cartep1:
            p2.extend(bataille_p1)
            p2.extend(bataille_p2)
            bataille_p2.clear()
            bataille_p1.clear()            
            affichage(p1, p2, cartep1, cartep2)
            print("Le joueur 2 remporte la bataille !")


def affichage(p1,p2,cartep1,cartep2):
    '''Cette fonction permet d'avoir une ergonomie visuelle du jeu plus claire'''
    if cartep1==14:
        cartep1 ="A"
    if cartep2==14:
        cartep2 ="A"
    if cartep1==13:
        cartep1 ="R"
    if cartep2==13:
        cartep2 ="R"
    if cartep1==12:
        cartep1 ="D"
    if cartep2==12:
        cartep2 ="D"
    if cartep1==11:
        cartep1 ="V"
    if cartep2==11:
        cartep2 ="V"
    print("============================")
    print(" ")
    print("Nombre de coup restant :",hit)
    print("  ",len(p1),"            ",len(p2))            
    print("Joueur 1        Joueur 2")
    print(" |", cartep1, "|           |", cartep2,"|")
    print(" ")
    


p1, p2 = distribution(jeu, p1, p2)

while p1 or p2:
    if len(p1)==0:  #Le joueur 1 n'as plus de cartes 
        print("Le joueur 2 a gagné !")
        break
    if len(p2)==0:  #Le joueur 2 n'as plus de cartes 
        print("Le joueur 1 a gagné !")
        break
    elif hit == 0:   #Après 100 coups, le joueurs ayant le plus cartes gagne la partie
        if len(p1)>len(p2):
            print("Le nombre de coups maximum a été dépassé, le joueur 1 a le plus de cartes il est donc gagnant !")
        elif len(p1) == len(p2): #Partie nulle si les deux joueurs ont le même nombre de cartes
            print("La partie est nulle, les deux joueurs ont le même nombre de cartes après que le nombre de coups maximum soit atteint !")
            break
        else:
            print("Le nombre de coups maximum a été dépassé, le joueur 2 a le plus de cartes il est donc gagnant !")
        break
    else:  
        tour_de_jeu(p1, p2)
        hit-=1
        print("Cliquez sur entrée pour jouer !")
        continuer=input()
