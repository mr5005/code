import re

dict={
    "a6":"8","b6":"e","c6":"6","d6":"4","e6":"r","f6":"g",
    "a5":"o","b5":"k","c5":"5","d5":"f","e5":"s","f5":"q",
    "a4":"w","b4":"d","c4":"7","d4":"l","e4":"0","f4":"m",
    "a3":"9","b3":"z","c3":"v","d3":"b","e3":"3","f3":"1",
    "a2":"x","b2":"c","c2":"u","d2":"t","e2":"2","f2":"p",
    "a1":"n","b1":"j","c1":"y","d1":"i","e1":"h","f1":"a"
    }

codice=""
messd=[]
mess=""

f=open("cyphtext.txt","r")
for i in f:
    codice=i
messd=re.findall(".{1,2}",codice)

for i in messd:
    mess=mess+dict[i]

f1=open("message.txt","w")
f1.write(mess)
f1.close()

input("messaggio decifrato in message.txt\nEnter per chiudere")