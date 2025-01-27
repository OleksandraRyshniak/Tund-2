#1
from datetime import *
from calendar import *
from base64 import b16decode
from math import*
from xml.dom import minicompat

tana=date.today()
print(f"Tere! Täna on {tana}")
# 27/12/2022
tana_=tana.strftime("%d/%m/%Y")
print(f"Tere! Täna on {tana}")
paevadekogus=monthrange(2025,1)[1]
print(f"Jaanuaris on {paevadekogus}")
päevad=tana.day
onjäänud=paevadekogus-päevad
print(f"Jaanuaris on jäänud {onjäänud} päevad")
# 1
aastalõpuni=365-monthrange(2025,1)[1]
print(f"Aastal on jäänud {aastalõpuni} päevad")
#2
aastalõpuni=onjäänud+monthrange(2025,2)[1]+monthrange(2025,3)[1]+monthrange(2025,4)[1]+monthrange(2025,5)[1]+monthrange(2025,6)[1]+monthrange(2025,7)[1]++monthrange(2025,8)[1]+monthrange(2025,9)[1]+monthrange(2025,10)[1]+monthrange(2025,11)[1]+monthrange(2025,12)[1]

### December 27, 2022
##tana = tana.strftime("%B %d, %Y")
##print(f"Tere! Täna on {tana}")
## 12/27/22
#tana = tana.strftime("%m/%d/%y")
#print(f"Tere! Täna on {tana}")
### Dec-27-2022
#tana = tana.strftime("%b-%d-%Y")
#print(f"Tere! Täna on {tana}")

#2
a=3+8/(4-2)*4
print(f"Vastus: {a}") # ничего не менялось
b=3+8/4-2*4
print(f"Vastus: {b}") # убрала скобки
c=(3+8)/(4-2)*4
print(f"Vastus: {c}") #добавила скобки
d=(3+8)/4+2*4
print(f"Vastus: {d}") # добавила и убрала скобки

# 3
try:
    R=float(input("R: "))
    Sruudu=round((2*R)**2,2)
    Sringi=round(pi*R**2,2)
    Pruudu=round(8*R,2)
    Pringi=round(2*pi*R,2)
    print(f"Vastus:\n Ruudu pindala on {Sruudu}\n Ruudu ümbermõõt on {Pruudu}\n Ringi pindala on {Sringi}\n Ringi ümbermõõt on {Pringi}")
except:
    print("Sisesta ujukomaarvud!")

#4 
d=2.575 # mündi d sm
maaR=6378 #maa radius km
maaR*=100000 #maa radius sm
Pmaa=2*pi*maaR #ümbermõõt maa
kogus=Pmaa/d
print(f"Meil on vaja {int(kogus):,d} mündi.")
print(f"Meil on vaja {int(kogus*2):,d} euro.")

#5
a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(a*2,b,a*2,b,a*4)

#6
tekst="Rong see sõitis tsuhh tsuhh tsuhh,\n piilupart oli rongijuht.\n Rattad tegid rat tat taa,\n rat tat taa ja tat tat taa.\n Aga seal rongi peal,\n kas sa tead, kes olid seal?\n Rong see sõitis tuut tuut tuut,\n piilupart oli rongijuht.\n Rattad tegid kill koll koll,\n kill koll koll ja kill koll kill.\n"
Suur=tekst.upper()
print(Suur)


#7
try:
    a=float(input("A: "))
    b=float(input("B: "))
    if a>0 and b>0:
        print("Pindala ja ümbermõõdu arvutamine: ")
        S=a*b
        P=(a+b)*2
        print(f"S={S}, P={P}")
    else:
        print("Arvud peaval suurem kui 0 olla!")
except:
    print("Viga!")

# 8
try:
    liitrid=float(input("Mitu liitrit kütust on paagis: "))
    km=float(input("Mitu kilomeetrit on sõidetud: "))
    if liitrid>0 and km>0:
         tarbimine=liitrid/km*100
         print(f"Keskmine kütusekulu 100 km kohta: {tarbimine}")
    else: 
        print("Liitrid ja kilomeetrid peavad olema suuremad kui 0!")
except:
    print("Sisesta ujukomaarvud!")

#9
try:
   rullustaja=29.9#km/h
   kiirus=29.9*1/3.6 #m/c
   m=int(input("Mitu minutit peab rulluisutaja sõitma: "))
   if m>0:
     meetrit=kiirus*m*60
     print(f"Nii kaugele ei saa rulaja minna: {meetrit} meetrit {m} minutiga")
   else: 
       print("Minutid peavad olema suuremad kui 0!")
except:
   print("Sisestage minutid täisarvudes!")

#10
try:
    minut=int(input("Minutid: "))
    if minut>0:
      tunnid=minut//60 
      minut_=minut%60
      print(tunnid,":",minut_)
    else:
        print("Sisestage väärtus, mis on suurem kui 0!")
except:
    print("Sisestage minutid täisarvudes!")
        

  

