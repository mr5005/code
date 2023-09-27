dict={
    "a":"a5","b":"b5","c":"c5","d":"d5","e":"e5",
    "f":"a4","g":"b4","h":"c4","i":"d4","l":"e4",
    "m":"a3","n":"b3","o":"c3","p":"d3","q":"e3",
    "r":"a2","s":"b2","t":"c2","u":"d2","v":"e2",
    "z":"a1","x":"b1","y":"c1","j":"d1","k":"e1",
    " ":""
    }
txt=input("Scrivi messaggio\n")
cyp=""
for le in txt:
    cyp=cyp+dict[le]
f=open("cyphtext.txt","w")
f.write(cyp)
f.close()
input("file creato\nEnter per chiudere")