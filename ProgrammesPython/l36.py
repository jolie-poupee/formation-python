def register():
    data = []
    while True :
        day = input ("entrez le jour (ou 'q' pour quitter):")
        if day == 'q' :
              break
        eat1 = input("entrez le premier repas :")
        eat2 = input("entrez le deuxieme repas :")
        eat3 = input("entrez le troisieme repas :")
        diseases = input(" entrez le malaise :")
        ligne = f" {day} , {eat1} ,{eat2} ,{eat3} ,{diseases}"
        data.append(ligne)
    with open ("donees.txt",'a')as fichier:
        for ligne in data:
            fichier.write(ligne +"\n")
register()            
             

              

