from Mymodule import *
p=[]
l=[]
while True:
    loe_pas_ja_log("data.txt", l, p)
    print(l)
    print(p)
    v=int(input("1-Registreerimine\n2-Aurotiseerimine\n3-Muuta_salasõna\n4-Taastamine\n5-Välja"))
    if v==1:
        l,p=Registreerimine(l,p)
        kirjuta_pas_ja_log("data.txt", l, p)
    elif v==2:
        Autoriseerimine(l,p)
    elif v==3:
        muuda_parool(l,p)
    elif v==4:
        taasta_parool(l,p)
    elif v==5:
        kirjuta_pas_ja_log("data.txt", l, p)
        break
    else:
        print("Tee õige valik")
