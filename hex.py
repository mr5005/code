import math

def codif(n):
    cod={"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
    t=""
    msg=""
    n=int(n)
    while True:
        if n<16:
            t+=str(n)
            break
        n/=16
        r=int(16*(n-math.floor(n)))
        t+=str(r)+" "
        n=math.floor(n)

    t=t.split()
    for i in t:
        for j in cod:
            if i==j:
                msg+=cod[i]
    msg=msg[::-1]

    print(msg)

def decodif(n):
    
    cod={"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","A":"10","B":"11","C":"12","D":"13","E":"14","F":"15",
        "a":"10","b":"11","c":"12","d":"13","e":"14","f":"15"}
    msg=[]
    t=0
    r=0
    n=n[::-1]
    for i in n:
        for j in cod:
            if i==j:
                msg.append(int(cod[i]))
    
    for i in range(0,len(msg)):
        t=msg[i]*pow(16,i)
        r+=t
    r=str(r)

    print(r)

####################################################################################################

def showr():
    istr=input("istruzione (cod/dec) : ")

    if istr=="cod":
        n=input("numero dec: ")
        codif(n)
    elif istr=="dec":
        n=input("numero hex: ")
        decodif(n)
    else:
        showr()

showr()
