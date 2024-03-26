#les dictionnaires
etudiant={
    "nom":"patrice",
    "age":"15 ans",
    "niveau":"master6"
}
etudiant["age"]="2 ans"
print(etudiant)
etudiant["ville"]="yaounde"
print(etudiant)
for cle in etudiant.keys():
    print(cle)
print("\n")    
for valeur in etudiant.values():
    print(valeur)    
print("\n")
for cle,valeur in etudiant.items():
    print(cle,":",valeur)    