# - Az elmúlt időszak nyertes 5-ös lottószámai vannak a lotto.txt fájlban.
# - Hány hét sorsolásai találhatóak benne?  = 1
# - Írd ki a képernyőre a nyerőszámokat!  = 2
# - Mely szám a leggyakoribb a húzások alkalmával?  = 3
# - Kérj be a user-től 5 számot, majd nézd meg, hogy hányasa lett volna?  = 4
# - Egy tipp.txt-be gyűjtsd ki a tuti tippet!  = 5

fajl = open("lotto.txt","r",encoding="utf-8")

#sorsolasi hetek szama
hetek = fajl.read().splitlines()
sor = len(hetek)
print("Hetek száma:", sor) 


for i in hetek:
    print("Nyerő számok:", i.strip())

#leggyakoribb szamok 
szamok = []

for sor in hetek:
    dbszamok = sor.split()
    for szam in dbszamok:
        szamok.append(int(szam))

legyak_szam = max(set(szamok), key=szamok.count)

print('Legyakorabb szám:', legyak_szam)

#User alatal bekert szamok es 
user_szamok = []
print("Adj meg 5 számot 1 és 90 között:")

while len(user_szamok) < 5:
    szam_input = input(f"{len(user_szamok)+1}. szám: ")
    if szam_input.isdigit():
        szam = int(szam_input)
        if szam >= 1 and szam <= 90 and szam not in user_szamok:
            user_szamok.append(szam)
        else:
            print("Érvénytelen szám (1-90 között)")
    else:
        print("csak szamokat adhatsz meg.")

tuti_tippek = []

for het in hetek:
    nyeroszamok = list(map(int, het.split()))
    talalatok = 0
    for szam in user_szamok:
        if szam in nyeroszamok:
            talalatok += 1
    print("Nyero szamok:", nyeroszamok, "talaltok szama:", talalatok)   
    
    if talalatok == 5:
        tuti_tippek.append(user_szamok[:])  


if tuti_tippek:
    fajl = open("tipp.txt", "w")
    for tipp in tuti_tippek:
        for szam in tipp:
            fajl.write(str(szam) + " ")
        fajl.write("\n")
    fajl.close()
    print("Tuti tipp mentve a tipp.txt-be!")
else:
    print("Nem volt teljes találat egyik héten sem.")

fajl.close()
