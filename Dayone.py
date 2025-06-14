word="coding section"

print(word.upper()) #DODING SECTION

print(word.lower()) #doding section

print(word.capitalize()) #Doding section

print(word.title()) #Doding Section

print(word.index('g')) #5

print(word.rindex("g")) #5

print(word.replace("c","b",1)) #boding section

print(word.find("o")) #1

print(word.rfind("o",0,7)) #12      ->print(word.rfind("o",0,7))=> #1

a="he is a supperman"
print(a.split())    #['he', 'is', 'a', 'supperman']

print(a.split(' ',2)) # ['he', 'is', 'a supperman'] 

print(a.rsplit(' ',2)) #['he is', 'a', 'supperman']

j="stone"
print('*'.join(j)) # s*t*o*n*e

""" a="he is a supperman" """
print(a.count("p")) #2

print(j.istitle()) #False

print(j.startswith('s'))#True

print(j.endswith('t'))#False

print(j.isupper()) #False

print(j.islower()) #True

s="**###this is #*section%####**"
print(s.strip('*#')) #this is #*section%

print(s.rstrip('#*'))  # """  **###this is #*section% """

print(s.lstrip("*"))   # """ ###this is #*section%####** """