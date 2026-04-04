import sys
import random

#lectura y limpieza de datos
db=str()
a=1
while sys.argv[a] != "":
    db=db+open(sys.argv[a]+".spl1", "r").read()
    if a == len(sys.argv)-1:
        break
    a+=1
db=db.replace("\n","")
db=db.replace("\t","")
db=db.replace(" ","")
pr=db.split("$").copy()
while '' in pr:
    pr.remove('')
for a in range(len(pr)):
    pr[a]=pr[a].replace("_"," ")
    pr[a]=pr[a].split("&").copy()

# hellow &t& hola $ pink &m& rosa&pony&purpura

cf=([0]*len(pr)).copy()

c=[0]*len(pr)
d=0
f=0
while True:
    if d == len(pr):
        for e in range(len(cf)):
            if cf[e]>1:
                print(f"Debes repasar {pr[e][0].capitalize()} -> {pr[e][2].capitalize()}, as fallado {cf[e]-1}.")
        print("\nNo quedan mas preguntas.")
        exit()
    a=int((random.random()*1000)%len(pr))
    while c[a] == 1:
        a=int((random.random()*1000)%len(pr))
        if f == 9999:
            a=c.index(0)
        f+=1
    b=pr[a]
    if b[1] == 't':
        print(f"Traduce {b[0].capitalize()}:")
        cf[a]=cf[a]+1
        ind=""
        while ind == "":
            ind=input(">")
            if ind == "<TOTAL>":
                print(f"Total de traduciones : ({d}/{len(pr)}).")        
                ind=""
        if ind.lower() == b[2].lower():
            print("Correcto!")
            c[a]=1
            d+=1
        else:
            print(f"Mal!\nRespuesta correcta:\n\t{b[0].capitalize()} -> {b[2].capitalize()}")
    elif b[1] == 'm':
        #por disenyar!
        c[a]=1
        d+=1
