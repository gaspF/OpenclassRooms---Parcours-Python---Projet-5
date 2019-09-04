PROJET 5 OpenClassrooms - Utilisez les donn�es publiques d'OpenFoodFacts
Gaspard Fouch�


Concept

Le programme permet de r�cup�rer les aliments via l'API d'OpenFoodFacts et de les comparer avec ceux choisis par l'utilisateur, et d'en proposer un substitut plus sain.


Installation

Remplacez les éléments d'identifiant MYSQL dans le fichier Constants.py par les v�tres. Le programme se lance � partir de main.py


Description

Sur le terminal, au premier �cran, trois choix :

1- Nouvel utilisateur : Cr�er la base de donn�es.
2- Utilisateur existant : Poursuivre.
3- Quitter le programme.

Si l'utilisateur s�lectionne 1, le programme cr�e la base de donn�es et am�ne l'utilisateur � l'�cran deux.

Si l'utilisateur s�lectionne 2, le programme se connecte � la base de donn�es et am�ne l'utilisateur � l'�cran deux.

Si l'utilisateur s�lectionne 3, le programme se ferme.


Sur le deuxi�me �cran, un nouveau choix :

1- Mettre � jour les cat�gories et produits ? 1 == Oui / 2 == Non

Si l'utilisateur s�lectionne 1, le programme t�l�charge les cat�gories alimentaires de la base de donn�es et les produits associ�s, puis l'am�ne � l'�cran trois.

Si l'utilisateur s�lectionn 2, le programme passe la mise � jour et am�ne l'utilisateur � l'�cran trois.


Le troisi�me �cran pr�sente le coeur des fonctionnalit�s du programme :

1- Substituer un aliment.
2- Acc�der aux aliments substitu�s.
3- Quitter le programme.

Si l'utilisateur s�lectionne 1, le programme propose une liste de cat�gories. L'utilisateur devra choisir la cat�gorie en �crivant son ID. Le programme
affichera une liste d'aliments appartenant � la cat�gorie choisie. L'utilisateur choisira l'aliment � substituer en entrant son ID.

Si l'utilisateur s�lectionne 2, Le programme affichera la liste des aliments substitu�s et leur produit de substitution associ�.

Si l'utilisateur s�lectionn 3, le programme se ferme.

