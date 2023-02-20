from random import*
import string


def registreerimine(nimi:list,parool:list):
    nimi=input("sisesta oma nimi:")
    print("1-ese koostan parooli,2-arvuti genireerib")
    print()

    if 1:
         int(input("ese koostan parooli"))
         pass 
    else:
        int(input("arvuti genireerib"))
        salasona=salasona(5)
        nimi.append(nimi)
        parool.append(salasona)
        return nimi,parool

def autoriseerimine(u:list,p:list):
    nimi=input("sisesta oma nimi:")
    salasona=input("sisesta oma salasõna:")
    if nimi in u:
        ind=u.index(nimi)
        if salasona==p[ind]:
            print("tere tulemast!")
        else:
            print("vale salasõna!")
    else:
        print("nimi ei ole nimekirjas!")
       
def salasona(k: int):
    sala="" 
    for i in range(k):
        t=choice(string.ascii_letters) 
        num=choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        saladus+=choice(t_num)
        return saladus 
def salasona(k: int):
  sala=""
  for i in range(k):
   t=choice(string.ascii_letters) #Aa...Zz
   num=choice([1,2,3,4,5,6,7,8,9,0])
   t_num=[t,str(num)]
   sala+=choice(t_num)
  return sala