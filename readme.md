PROJET 5 OpenClassrooms - Utilisez les données publiques d'OpenFoodFacts
Gaspard Fouché


Concept

Le programme permet de récupérer les aliments via l'API d'OpenFoodFacts et de les comparer avec ceux choisis par l'utilisateur, et d'en proposer un substitut plus sain.


Installation

Remplacez les éléments d'identifiant MYSQL dans le fichier Constants.py par les vôtres. Le programme se lance à partir de main.py


Description

Sur le terminal, au premier écran, trois choix :

1- Nouvel utilisateur : Créer la base de données.
2- Utilisateur existant : Poursuivre.
3- Quitter le programme.

Si l'utilisateur sélectionne 1, le programme crée la base de données et amène l'utilisateur à l'écran deux.

Si l'utilisateur sélectionne 2, le programme se connecte à la base de données et amène l'utilisateur à l'écran deux.

Si l'utilisateur sélectionne 3, le programme se ferme.


Sur le deuxième écran, un nouveau choix :

1- Mettre à jour les catégories et produits ? 1 == Oui / 2 == Non

Si l'utilisateur sélectionne 1, le programme télécharge les catégories alimentaires de la base de données et les produits associés, puis l'amène à l'écran trois.

Si l'utilisateur sélectionn 2, le programme passe la mise à jour et amène l'utilisateur à l'écran trois.


Le troisième écran présente le coeur des fonctionnalités du programme :

1- Substituer un aliment.
2- Accéder aux aliments substitués.
3- Quitter le programme.

Si l'utilisateur sélectionne 1, le programme propose une liste de catégories. L'utilisateur devra choisir la catégorie en écrivant son ID. Le programme
affichera une liste d'aliments appartenant à la catégorie choisie. L'utilisateur choisira l'aliment à substituer en entrant son ID.

Si l'utilisateur sélectionne 2, Le programme affichera la liste des aliments substitués et leur produit de substitution associé.

Si l'utilisateur sélectionn 3, le programme se ferme.

