print("Zdravím tě,uživateli")

print("Pro převod z decimální soustavy do binární,zadejte dec: ")
print("Pro převod z binární do decimální soustavy,zadejte bin: ")

volba = input("Tak co to bude?: ")

dec = int(dec)
bin = int(bin)

if volba == dec:
    print("Vybral jste převod z decimální IP adresy: ")
    a = int(input("Zadejte první část IP adresy: "))
    b = int(input("Zadejte druhou část IP adresy: "))
    c = int(input("Zadejte třetí část IP adresy: "))
    d = int(input("Zadejte čtvrtou část IP adresy: "))
    if a>0 and b>0 and c>0 and d>0:
       if a<256 and b <256 and c<256 and d<256:
            prevod_a = ((((((((a/128)/64)/32)/16)/8)/4)/2)/1)
            prevod_b = ((((((((b/128)/64)/32)/16)/8)/4)/2)/1)
            prevod_c = ((((((((c/128)/64)/32)/16)/8)/4)/2)/1)
            prevod_d = ((((((((d/128)/64)/32)/16)/8)/4)/2)/1)

            print("Výsledek je: ", prevod_a, prevod_b, prevod_c, prevod_d)

elif volba == bin:
    print("Vybral jste si převod z binární IP adresy: ")
    a = int(input("Zadejte první část IP adresy"))
    b = int(input("Zadejte druhou část IP adresy: "))
    c = int(input("Zadejte třetí část IP adresy: "))
    d = int(input("Zadejte čtvrtou část IP adresy: "))
    if a>0 and b>0 and c>0 and d>0:
        if a<11111111 and b<11111111 and c<11111111 and d<11111111:
