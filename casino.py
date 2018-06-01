# -*- coding: utf-8 -*-
import random
#argent depart
Banque = 1000
#
volonte = "oui"
while Banque > 0 and volonte == "oui" :
	print("Bienvenu dans ce jeu de roulette virtuel \n")
	print ("votre disposez de "+str(Banque)+" euros")
	print("\n\nvoulez-vous jouez un nombre unique (1) ? \n\nPariez sur un nombre pair ou impair (2) ? \n \nMisez sur plusieurs nombre (3)\n")
	mode_jeu = input("selectionner votre mode de jeu : 1,2 ou 3 : ")
	mode_jeu = int(mode_jeu)
	if mode_jeu == 1 :
		lance = random.randint(1,36)
		mise = input("Combiens d'argent voulez-vous misez ?")
		paris = input("Quel nombre voulez-vous jouez : ")
		if paris == lance :
			Banque +=36

		else :
			print("perdu vous êtes tombé sur le mauvais nombre")
			Banque = Banque - int(mise)
			print("il vous reste " + str(Banque) +" euros" )

	if mode_jeu == 2 :
		lance =random.randint(1,2)
		result = str
		if lance == 1 :
			result = "impair" 
		elif lance == 2 :
			result = "pair"

		mise = input("Combiens d'argent voulez-vous misez ?")
		paris = input("voulez-vous jouer un nombre pair ou impair ? saisir 'impair(1)/pair(2)' ")
		paris = int(paris)
		if paris == lance:
			print("Bravo vous remportez 2 fois votre mise ! le chiffre {0} est bien {1}".format(lance,result))
			Banque = Banque + int(mise)*2


		else :
			print("Perdu ! le chiffre {0} n'est pas {1}".format(lance,result))
			Banque = Banque - int(mise)
			print("il vous reste " + str(Banque) +" euros" )

	if mode_jeu == 3 :
		mise = []







	volonte = input("voulez-vous continuez à jouer, saisir 'oui' ou 'non'")
	if volonte == "oui":
		volonte = "oui"
	elif volonte == "non":
		volonte = "non"



