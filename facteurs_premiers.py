def facteurs_premiers():
  valeur = int(input("Saisir une valeur")) # Saisi de la valeur
  facteur = []
  diviseur = 2
  while diviseur <= valeur: # Tant que 'diviseur' est inférieur ou égal à 'valeur'
    if valeur % diviseur == 0: # Si le reste dans la division euclidienne est égal à 0
      facteur.append(diviseur) # Ajouter 'diviseur'
      valeur = valeur // diviseur # Quotien dans la division euclidienne
    else:
      diviseur += 1 # J'attribue au diviseur le chiffre 1
  print(facteur)

facteurs_premiers()