def divmod(a,b):
    qt=a//b#(//permet de donner la valeur entiere de a divise par b or / donne la partie decimale)
    reste=a%b
    return qt,reste
print("entrez deux nombres a et b (a>b)")   
a=input(" ") 
b=input(" ")
A=int(a)
B=int(b)
q,r=divmod(A,B)    
print("le quotion est q= ",q)
print("le reste est r= ",r)