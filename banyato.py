

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

    
