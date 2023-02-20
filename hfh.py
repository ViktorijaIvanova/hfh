from random import*
from Omamoodul import*
nimi=["vika;alisa"]
parool=["12345;21212"]
while True:
     print("1-registreerimine,2-autoriseerimine,3-välja")
     v1=input("1-registreerimine:") 
     v2=input("2-autoriseerimine")
     v3=input("3-välja:")
     v4=input("nime või parooli muutmine:")
     v5=input("unustanud parooli taastamine:")
     if v1:
        nimi,parool=registreerimine(nimi,parool) 
     elif v2:
         autoriseerimine()
     elif v3:
         break
     else:print("tee õige valik")
     print()
     if v5:
      str0=".,:;!_*-+()/#¤%&"
      str1 = '0123456789'
      str2 = 'qwertyuiopasdfghjklzxcvbnm'
      str3 = str2.upper()
      print(str3) 
      str4 = str0+str1+str2+str3
      print(str4)
      ls = list(str4)
      print(ls)
      random.shuffle(ls)
      print(ls)

      psword = ''.join([random.choice(ls) for x in range(12)])
      print(psword)