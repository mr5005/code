msg=input("Scrivere messaggio (senza spazi).")
mn=dict()
letver=dict()
alfa={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"l":9,"m":10,"n":11,"o":12,"p":13,"q":14,"r":15,"s":16,"t":17,"u":18,"v":19,"z":20,"0":21,
    "1":22,"2":23,"3":24,"4":25,"5":26,"6":27,"7":28,"8":29,"9":30}
ver=["0","c","5","t","9","r","2","f"]
msgf=""
n=0

for i in range(0,len(msg)):
    mn[i]=msg[i]
for i in mn:
    if n==len(ver):
        n=0
    letver[i]=ver[n]
    n+=1

for i in letver:
    alfam=alfa[mn[i]]
    alfav=alfa[letver[i]]
    if (alfam+alfav)<31:
        for i in alfa:
            if alfa[i]==(alfam+alfav):
                msgf+=str(i)
    else:
        for i in alfa:
            if alfa[i]==((alfam+alfav)-31):
                msgf+=str(i)

print(msgf)
input("Enter per chiudere")
