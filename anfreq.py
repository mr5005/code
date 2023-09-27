import re

testo=input("scrivi un testo \n")

testo=re.sub(" ","",testo)

abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

lent=len(testo)
for i in abc:
    let=re.findall(i,testo)
    perc=(len(let)*100)/lent
    perc=str("{:.2f}".format(perc))
    print(i+" --> "+perc+"%")

input("enter per chiudere")