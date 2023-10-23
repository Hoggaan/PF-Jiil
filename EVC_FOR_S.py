pn = 1234
haraaga = 100
pin = int(input("Fadlan gali biinkaaga: "))
if pin == pn:
    print("1. Itus Haragayga.")
    print("2. Kaarka ku hadalka.")
    print("3. Bixi biilka")
    # print("4. U wareeji EVC-PLUS")
    # print("5. Warbixin kooban")
    print("0. Ka bax!")
else:
    print("Lambarka sirta ah waa qalad. Fadlan soo gali markale.")

next_step = int(input())
if next_step == 1:
    print("Haraagaagu waa ", haraaga)

elif next_step == 2:
    print("1. Ku shubo airtime.")
    print("2. Ugu shub airtime.")
    print("3. MIFI backages.")
    airtime = int(input())
    if airtime == 1:
        print("Fadlan gali lacagta:")
        lacagta = int(input())
        print("Ma hubtaa inaad lacaga ugu shubto: ")
        print("1. HAA")
        print("2. MAYA")
        haamaya = int(input())
        if haamaya == 1:
            print("Waa lagu shubay")
        else:
            if haamaya == 2:
                print("Waa laga noqday")
            else:
                print("Macasalaama!")

elif next_step == 3:
    print("1. postpaid")
    print("2. ku iibso")

else: 
    print("Macasalaama!")

