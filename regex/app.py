import re

file = open('exploit.txt',encoding="utf8") 
texto= file.read()

resultado=[]
for item in re.findall("(\w+\s\w+)(:\sA+)",texto):
    resultado.append(item[0])
print(resultado)