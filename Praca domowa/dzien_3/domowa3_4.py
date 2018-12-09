# 4) Kalkulator do wyliczania wieku psa.
#    Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#    Np: 15 ludzkich lat to 73 psie lata

wiek = int(input('Podaj wiek psa w latach'))

if wiek <= 2:
    lata = wiek * 10.5
    print(f"Pies ma {lata} ludzkich lat")
else:
    lata = (wiek-2) * 4 + 2*10.5
    print(f"Pies ma {lata} ludzkich lat")
