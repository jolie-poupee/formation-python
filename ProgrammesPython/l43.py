fruits=["tomate","pommme"]
print(fruits[0])
print(fruits[-1])
fruits[1]="avocat"
print(fruits)
size=len(fruits)
print(fruits[size-1])
fruits.append("orange")
fruits.insert(2,"raisin")
print(fruits)
fruits.remove("raisin")
print(fruits)
del fruits[1]
print(fruits)