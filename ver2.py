# -*- coding: utf-8 -*-

listek = []
odg = "0"
shrani = "0"

while odg != "ne":
    odg = raw_input("Želiš dodati izdelek? (da/ne) ")
    if odg == "da":
        item = raw_input("Dodaj izdelek: ")
        listek.append(item)

    elif odg == "ne":
        print("Hvala za nakup!")
        for x in listek:
            print(x)

    else:
        print("Poskusite z 'da' ali 'ne' ")

while shrani != "ne":
    shrani = raw_input("Želiš shraniti nakup v arhiv? (da/ne) ")
    if shrani == "da":
        a = raw_input("Vpišite ime za arhiv (brez presledka): ")
        with open(a + ".txt", "wb") as f:
            for x in listek:
                f.write(x + "\n")
        print("Vaš arhiv je shranjen kot " + a + ".txt")
        break

    elif shrani == "ne":
        print("Niste shranili vašega nakupa")

    else:
        print("Poskusite z 'da' ali 'ne' ")

print("Lep dan še naprej!")
