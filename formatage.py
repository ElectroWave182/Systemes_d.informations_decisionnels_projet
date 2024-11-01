def requetage (nomTable):

	fichier = open (nomTable + ".csv", "r")
	donnees = fichier.read ().split ("\n")
	colonnes = donnees [0]

	for ligne in donnees:
		sortie = "INSERT INTO " + nomTable + " (" + colonnes + ")\n"
		sortie += "VALUES (" + ligne + ");"
		print (sortie)
		
        
requetage ("Patient")
