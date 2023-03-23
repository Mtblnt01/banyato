melysegek=[]
with open("melyseg.txt","r",encoding="utf-8") as fin:
    fin.readline()
    fin.readline()
    for sor in fin:
        seged_lista=list(map(int,sor.strip().split()))
        melysegek.append(seged_lista)
#print(melysegek)
from colorama import Fore, Back
for melyseg_sor in melysegek: #Így szépen írja ki minden lista 1-1sor.
    for melyseg in melyseg_sor:
        if melyseg>0:
            print(f"{Back.BLUE}{Fore.WHITE}{melyseg:2d}", end=" ")
        else:
            print(f"{Back.RESET}{Fore.RESET}{melyseg:2d}", end=" ")
    print() #ezis hogy szépen írja ki

# 2. feladat
# A mérés sorának azonosítója=12
# A mérés oszlopának azonosítója=6
# A mért mélység az adott helyen 33 dm
print("2.Feladat")

be_sor=int(input("A mérés sorának azonosítója=") or "12")
be_oszlop=int(input("A mérés oszoplának azonosítója=") or "6")
print(f"A mért mélység az adott helyen {melysegek[be_sor-1][be_oszlop-1]}dm")
# 3. feladat
# A tó felszíne: 646 m2, átlagos mélysége: 4,28 m

print("3.Feladat")
def megszamolas(m):
    darab=0
    for seged_lista in m:
        for elem in seged_lista:
            if elem>0:
                darab+=1
    return darab

def atlagolas(m):
    osszeg=0
    db=0
    for seged_lista in m:
        for elem in seged_lista:
            if elem>0:
                db+=1
                osszeg+=elem
    return osszeg/db



felszin=megszamolas(melysegek)
atlagos_melyseg=atlagolas(melysegek)
print(f"A tó felszíne:{felszin}m2, átlagos mélysége: {atlagolas(melysegek)/10:0.2f}")
"""
4. feladat
Mekkora a tó legnagyobb mélysége, és hol a legmélyebb a tó? Jelenítse meg a választ
a képernyőn! A legmélyebb pont koordinátáit a mintának megfelelően (sor; oszlop)
formában írassa ki! Ha több ilyen mérési eredmény is van, mindegyik koordinátapárja
jelenjen meg!
"""



def maximum_kivalasztas(m):
    max_sor_i=0
    max_oszlop_i=0
    for i in range(1,len(m)):
        for j in range(len(m[i])):
            if m[max_sor_i][max_oszlop_i]<m[i][j]:
                max_sor_i=i
                max_oszlop_i=j
    return max_sor_i, max_oszlop_i

max_s, max_o=maximum_kivalasztas(melysegek)


"""
def maximum_kivalasztas(lista):
    max_index=0
    for index in range(1,len(lista)):
        if lista[max_index]<lista[index]:
            max_index=index
    return max_index
"""
print("4. feladat")
print(f"A tó legnagyobb mélysége: {melysegek[max_s][max_o]} dm")
#print("A legmélyebb helyek sor-oszlop koordinátái: (14; 20) (26; 11) (32; 16)")
def legmelyebb_pontok_koordinatai(m, max_ertek):
    for sor_index,sor in enumerate(m):
        for oszlop_index,elem in enumerate(sor):
            if elem==max_ertek:
                print(f"{sor_index+1}; {oszlop_index}", end=" ")
    print()

legmelyebb_pontok_koordinatai(melysegek, melysegek[max_s][max_o])




"""
5. feladat
Milyen hosszú a tó partvonala, vagyis az ábrán a szürkével jelölt részt határoló vastag fekete
vonal hossza? A partvonalhoz vegye hozzá a tóban lévő szigetek kerületét is! Írassa ki
az eredményt a mintának megfelelően a képernyőre! (A megoldás során felhasználhatja,
hogy a táblázat első és utolsó sorában és oszlopában minden adat 0.) 
"""

print("5. Feladat")
def partvonal_hossza(m):
    hossz=0
    for i in range(1, len(m)-1):
        for j in range(1, len(m[i])-1):
            if m[i][j]>0:
                if m[i-1][j]==0:
                    hossz+=1
                if m[i+1][j]==0:
                    hossz+=1
                if m[i][j-1]==0:
                    hossz+=1
                if m[i][j+1]==0:
                    hossz+=1
    return hossz

print(f"A tó partvonala {partvonal_hossza(melysegek)} m hosszú")