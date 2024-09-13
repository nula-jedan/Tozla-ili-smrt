ime = input("bok, utipkaj svoje ime:")
print("bok " + ime + " dobrodosao u moju igru")

hocemo_li_igrati = input("zelis li igrati? ").lower()

if hocemo_li_igrati == "d" or hocemo_li_igrati == "da":
    print("nego sto, nego ocemo!")

    put = input("zelis li ici livo ili desno? (livo/desno)").lower()
    if put == "livo":
        print("isao si livo i pao sa litice, kraj igre, pokusaj ponovno")
    elif put == "desno":
        odabir = input("odlicno, sad vidis most, zelis li plivati od ispod ili ga prijeci? (plivati/prijeci)")
        if odabir == "plivati":
            print("poila te masu velika riba, umra si, kraj igre")
        else:
            print("nasa si zlato i dobia si")
    else:
        print("alo, eli ti znas pisati, umra si")

else:
    print("ne igramo, vise...")        
