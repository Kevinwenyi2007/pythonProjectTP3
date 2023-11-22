# cree par Kevin Wen
# cree en 2023
# ce projet montre le code de TP3

# ce jeu montre un game d'un utilisateur contre un monstre

import random

print('bienvenue dans le jeu de monstres')
Jeu = str(input('est-ce que vous voulez jouer au jeu. yes or no.'))

# le status du jeu
victoiresConsecutive = 0
numeroAdversaire = 0
numero_combat = 0
nombre_victoire = 0
nombre_defaites = 0

startingScore = 20
print('ton niveau de vie au debut est',startingScore)


while Jeu == 'yes':
    scoreMonstre1 = random.randint(1, 6)
    scoreMonstre2 = random.randint(1, 6)

    scoreMonstre = scoreMonstre1 + scoreMonstre2

    print('le score de votre adversaire est de', scoreMonstre)
    print('Que voulez-vous faire: combattre cet adversaire(choix 1), Contourner cet adversaire et aller ouvrir une autre porte(choix 2), Afficher les règles du jeu(choix 3), Quitter la partie(choix 4)')

    choix = int(input('cest quoi votre choix'))

    if startingScore <= 0:
        break


    if choix == 1:
        score_de = random.randint(1, 30)
        if scoreMonstre >= score_de:
            nombre_defaites += 1
            victoiresConsecutive = 0
            startingScore -= scoreMonstre  # l'utilisateur perd

            print('votre nombre de defaites est de', nombre_defaites)
            print('votre nombre de victoire consecutive est de', victoiresConsecutive)
        elif scoreMonstre < score_de:
            nombre_victoire += 1
            victoiresConsecutive += 1
            startingScore += scoreMonstre  # l'utilisateur gagne

            print('votre nombre de victoire est de', nombre_victoire)
            print('votre nombre de victoire consecutive est de', victoiresConsecutive)
    numero_combat += 1
    print('cest le',numero_combat,'combat')

    # si L'utilisatuer gagne plus trois fois cosecutivement, il va combattre avec un plus grand monstre #question
    if victoiresConsecutive >= 3:
        scoreMonstre3 = random.randint(7, 12)
        scoreMonstre4 = random.randint(7, 12)
        score2 = scoreMonstre3 + scoreMonstre4
        print(score2)

    if choix == 2:
        startingScore -= 1
        print(startingScore,'est votre nombre de vie maintenant')
    if choix == 3:
        print(
            'Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de usager est augmenté de la force de adversaire.Une défaite a lieu lorsque la valeur du dé lancé par usager est inférieure ou égale à la force de adversaire.  Dans ce cas, le niveau de vie de usager est diminué de la force de adversaire.La partie se termine lorsque les points de vie de usager tombent sous 0.Usager peut combattre ou éviter chaque adversaire, dans le cas de évitement, il y a une pénalité de 1 point de vie. ')

    if choix == 4:
        print('merci et au revoir')
        break
else:
    print('merci et au revoir')
# pour la question theorique, la reponse est que on peut creer plusieurs variables qui representent les forces
# des monstres en utilisant la fonction random randint sur un interval de valeur.