import re

"""__author__ Alex Patterson"""
""" AfterBlock - Create a world for your novel (Like pick your own adventure for idea inspiration) """
print("Thank you for using AfterBlock for your novel needs!")

# Reduce Line Length
scale1 = "On a scale of 1 - 5, please rate "
scale2 = " with 1 being "
scale3 = " and 5 being "
#
title = ""

print("Please enter a name with no spaces.")
titleverify = 0
while titleverify == 0:
    title = input("What is the name of your civilization: ")
    if re.findall('[!@#%&*?>< ]', title):
        print("There was an issue with your name, Please try again.")
    else:
        titleverify = 2

finalFile = open(str(title) + ".txt", 'a')


def repository():
    """ Retrieve text from file"""
    textrepository = open("IntegrationProjectTextRepository.txt", "r")
    # Culture Text Variables
    cult11 = ""
    cult21 = ""
    cult31 = ""
    cult41 = ""
    cult51 = ""
    for x in range(40):
        read = textrepository.readline()
        if 0 < x < 9:
            cult11 += read
        elif 9 < x < 17:
            cult21 += read
        elif 17 < x < 22:
            cult31 += read
        elif 22 < x < 33:
            cult41 += read
        elif 33 < x < 40:
            cult51 += read
    x = cult11, cult21, cult31, cult41, cult51
    return x


cult1 = repository()[0]
cult2 = repository()[1]
cult3 = repository()[2]
cult4 = repository()[3]
cult5 = repository()[4]


def afterblockinput():
    """ Ask user for input """
    amtverify = 0
    amt_cult1 = ""
    agressionverify = 0
    agression1 = ""
    agricultverify = 0
    agriculture1 = ""
    theologyverify = 0
    theology1 = ""
    scholarsverify = 0
    scholars1 = ""
    waterverify = 0
    water1 = ""
    while amtverify == 0:
        amt_cult1 = input("With a number between 0 and 3, "
                          "please indicate the number of neighboring countries: ")
        if amt_cult1.isdigit() and -1 < int(amt_cult1) < 4:
            amtverify = 1
            amt_cult1 = int(amt_cult1)
        else:
            print("Your input was not in the correct format. Please try again"
                  " :)")

    while agressionverify == 0:
        agression1 = input(scale1 + "the violence of your civilization"
                           + scale2 + "pacifists" + scale3 + "war hungry: ")
        if agression1.isdigit() and 0 < int(agression1) < 6:
            agressionverify = 1
            agression1 = int(agression1)
        else:
            print("Your input was not in the correct format. Please try again"
                  " :)")

    while agricultverify == 0:
        agriculture1 = input(
            scale1 + "the ruralness of your country"
            + scale2 + "mostly urban areas" + scale3 + "mostly farms: ")
        if agriculture1.isdigit() and 0 < int(agriculture1) < 6:
            agricultverify = 1
            agriculture1 = int(agriculture1)
        else:
            print("Your input was not in the correct format. Please try again"
                  " :)")

    while theologyverify == 0:
        theology1 = input("With a number between 0 and 3, Please indicate "
                          "the "
                          "number of gods for your civilization: ")
        if theology1.isdigit() and -1 < int(theology1) < 4:
            theologyverify = 1
            theology1 = int(theology1)
        else:
            print("Your input was not in the correct format. Please try again"
                  " :)")

    while scholarsverify == 0:
        stext1 = "the value of education in your civilization"
        scholars1 = input(scale1 + stext1 + scale2 + "trump-supporters" + scale3
                          + "scientists: ")
        if scholars1.isdigit() and 0 < int(scholars1) < 6:
            scholarsverify = 1
            scholars1 = int(scholars1)
        else:
            print("Your input was not in the correct format. Please try again"
                  " :)")

    while waterverify == 0:
        water1 = input(scale1 + "how much of the country's borders "
                                "are coastline"
                       + scale2 + "landlocked" + scale3 + "island: ")
        if water1.isdigit() and 0 < int(water1) < 6:
            waterverify = 1
            water1 = int(water1)
        else:
            print("Your input was not in the correct format. Please try again"
                  " :)")
    x = amt_cult1, agression1, agriculture1, theology1, scholars1, water1
    return x


a = afterblockinput()[:]
amt_cult = a[0]
agression = a[1]
agriculture = a[2]
theology = a[3]
scholars = a[4]
water = a[5]


def afterblockvcreation(agression2, agriculture2, scholars2, water2,
                        theology2):
    """Work with input numbers"""
    #  Value creation to establish what text is selected for main
    weapon01 = (agression2 ** 2) / 3 // 1
    # Used **, /, and //. **2 will raise the variable to the second power
    # /3 will divide the resulting value by three
    # //1 is a floor dividor meaning it will round the answer down
    monster01 = (agriculture2 * 3)
    # *3 will multiply by 3
    culture01 = scholars2
    # 2789 % ((9 * scholars) - 2)
    # -2 will subtract 2 and % will return the remainder
    # from the division of the 2 numbers it is between
    country01 = water2
    familiar01 = theology2 + 3
    # +3 is addition
    # text selection based off of values for main
    x = weapon01, monster01, culture01, country01, familiar01
    return x


c = afterblockvcreation(agression, agriculture, scholars, water, theology)[:]
weapon0 = c[0]
monster0 = c[1]
culture0 = c[2]
country0 = c[3]
familiar0 = c[4]


def valuechoice(weapon02, monster02, culture02, familiar02, country02,
                cult12, cult22, cult32, cult42, cult52, theology3):
    """Choose text bites"""
    weapontext1 = ""
    monstertext1 = ""
    culturetext1 = ""
    familiartext1 = ""
    countrytext1 = ""
    if weapon02 == 0:
        weapontext1 = " is the bow."
    elif weapon02 == 1:
        weapontext1 = " are spears."
    elif weapon02 == 3:
        weapontext1 = " is the sword."
    elif weapon02 == 5:
        weapontext1 = " is the axe."
    elif weapon02 == 8:
        weapontext1 = " are knives."

    if monster02 == 3:
        monstertext1 = "cannibals."
    elif monster02 == 6:
        monstertext1 = "sentient animals."
    elif monster02 == 9:
        monstertext1 = "arachnids."
    elif monster02 == 12:
        monstertext1 = "flesh-eating insects."
    elif monster02 == 15:
        monstertext1 = "carnivorous plants."

    if culture02 == 3 and theology3 == 0:
        culturetext1 = " " + cult12
    elif culture02 == 2 and theology3 > 0:
        culturetext1 = " " + cult22
    elif culture02 == 4 or culture02 == 3:
        culturetext1 = " " + cult32
    elif culture02 == 5:
        culturetext1 = " " + cult42
    elif culture02 == 1 or culture02 == 2:
        culturetext1 = " " + cult52

    if familiar02 == 3:
        familiartext1 = "reptiles."
    elif familiar02 == 4:
        familiartext1 = "felines."
    elif familiar02 == 5:
        familiartext1 = "dragons."
    elif familiar02 == 6:
        familiartext1 = "canines."
    elif familiar02 == 6 and weapon0 <= 4:
        familiartext1 = "birds."

    if country02 == 1:
        countrytext1 = "Switzerland"
    elif country02 == 2:
        countrytext1 = "Romania"
    elif country02 == 3:
        countrytext1 = "Portugal"
    elif country02 == 4:
        countrytext1 = "Chile"
    elif country02 == 5:
        countrytext1 = "Madagascar"

    x = weapontext1, monstertext1, culturetext1, familiartext1, countrytext1
    return x


b = valuechoice(weapon0, monster0, culture0, familiar0, country0, cult1, cult2, cult3,
                cult4, cult5, theology)[:]

weapontext = b[0]
monstertext = b[1]
culturetext = b[2]
familiartext = b[3]
countrytext = b[4]


def godtext(culturetext2, cult14, cult24, cult34, cult44, cult54):
    """Structure god text"""
    god1 = "God of Laughter and Delight"
    god2 = "God of Wine and the Harvest"
    god3 = "God of Charm and Wickedness"
    god4 = "God of Justice"
    god5 = "God of the Planets and the Sky"
    finalgod1 = ""
    finalgod2 = ""
    finalgod3 = ""
    reducegod1 = "They honor the "
    gtext1 = ""
    if culturetext2 == " " + cult24:
        finalgod1 = god2
        finalgod2 = god3
        finalgod3 = god1
    if culturetext2 == " " + cult34:
        finalgod1 = god4
        finalgod2 = god3
        finalgod3 = god5
    if culturetext2 == " " + cult44:
        finalgod1 = god3
        finalgod2 = god5
        finalgod3 = god2
    if culturetext2 == " " + cult54:
        finalgod1 = god2
        finalgod2 = god4
        finalgod3 = god1
    if culturetext2 == " " + cult14:
        gtext1 = ""
    else:
        if culturetext == " " + cult24:
            reducegod1 = "They also honor the "
        if theology == 0:
            gtext1 = "They honor no god.\n"
        if theology == 1:
            gtext1 = reducegod1 + finalgod1 + ". \n"
        if theology == 2:
            gtext1 = reducegod1 + finalgod1 + " and the " + finalgod2 + ". \n"
        if theology == 3:
            gtext1 = reducegod1 + finalgod1 + ", the" + finalgod2 \
                     + ", and the" + finalgod3 + ". \n"

    x = gtext1, finalgod1, finalgod2, finalgod3
    return x


gtext = godtext(culturetext, cult1, cult2, cult3, cult4, cult5)[0]


def neighbortext(culturetext3, amt_cult3, cult15, cult25, cult35,
                 cult45, cult55):
    """Structure the neighbor text"""
    neighbor1 = ""
    neighbor2 = ""
    neighbor3 = ""
    n1 = "Their closest neighbor is "
    n2 = "Their second neighbor is "
    n3 = "Their third neighbor is "
    ntext1 = ""

    if culturetext3 == " " + cult15:
        neighbor1 = n1 + "Darar. The " + cult35
        neighbor2 = n2 + "Kalen. The " + cult45
        neighbor3 = n3 + "Diniel. The " + cult55

    if culturetext3 == " " + cult25:
        neighbor1 = n1 + "Daren. The " + cult35
        neighbor2 = n2 + "Kaliel. The " + cult15
        neighbor3 = n3 + "Dinar. The " + cult45

    if culturetext3 == " " + cult35:
        neighbor1 = n1 + "Dariel. The " + cult4
        neighbor2 = n2 + "Kalar. The " + cult2
        neighbor3 = n3 + "Dinen. The " + cult5

    if culturetext3 == " " + cult45:
        neighbor1 = n1 + "Ardan. The " + cult2
        neighbor2 = n2 + "Enkal. The " + cult5
        neighbor3 = n3 + "Latar. The " + cult1

    if culturetext3 == " " + cult55:
        neighbor1 = n1 + "Endar. The " + cult1
        neighbor2 = n2 + "Arkal. The " + cult4
        neighbor3 = n3 + "Entiel. The " + cult5

    if amt_cult3 == 0:
        ntext1 = ""
    elif amt_cult3 == 1:
        ntext1 = neighbor1
    elif amt_cult3 == 2:
        ntext1 = neighbor1 + neighbor2
    elif amt_cult3 == 3:
        ntext1 = neighbor1 + neighbor2 + neighbor3
    x = ntext1
    return x


ntext = neighbortext(culturetext, amt_cult, cult1, cult2, cult3, cult4, cult5)
# Write information to Final File

finalw = "The favored weapon of this people" + weapontext + "\n"
finalf = "Their companions are most often " + familiartext + "\n"
finalm = "The local battles are with " + monstertext + "\n"
finalc = "The country's borders loosely resemble " + countrytext + "'s.\n"
finaltotaltext = title + culturetext + gtext + finalw + finalf \
                 + finalm + finalc + ntext

finalFile.write(finaltotaltext)

# Close Final File
finalFile.close()
print("The file for your civilization bears its name. Enjoy!")
