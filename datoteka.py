# -*- coding: utf-8 -*-

listek = []
odg = "fgs"


while odg != "ne":
    odg = raw_input("Želiš dodati izdelek? (da/ne)")
    if odg == "da":
        item = raw_input("Dodaj izdelek: ")
        listek.append(item)

    elif odg == "ne":
        print("Hvala za nakup!")
        for x in listek:
            print(x)

    else:
        print("Poskusi z da ali ne")
