#Dec/Codifica in esadecimale

txt=""
msg=""

def cod(fn,txt,msg):
    f=open(f"{fn}.txt","r")
    for i in f:
        txt+=i
    f.close()
    for i in txt:
        msg+=hex(ord(i))[2:]+" "
    f1=open("text.txt","w")
    f1.write(msg)
    f1.close()
    print("File creato: text.txt")

def dec(fn,txt,msg):
    f=open(f"{fn}.txt","r")
    for i in f:
        txt+=i
    f.close()
    t=txt.split()
    for i in t:
        msg+=chr(int(i,16))
    f1=open("message.txt","w")
    f1.write(str(msg))
    f1.close()
    print("File creato: message.txt")

def showr():
    cd=input("Codifica/Decodifica: ")
    fn=input("Indirizzo e nome del file: ")

    if cd=="codifica":
        cod(fn,txt,msg)
    elif cd=="decodifica":
        dec(fn,txt,msg)
    else:
        showr()

showr()
