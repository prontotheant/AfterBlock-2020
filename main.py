#  Alex Patterson
#  AfterBlock - Create a world for your novel (Like pick your own adventure for idea inspiration)


# import os (Unused for now)

# from PIL import Image, ImageDraw, ImageFont (Unused for now)

print("Thank you for using AfterBlock for your novel needs!")

#  Repeated phrases "dictionary" to reduce line length

scale1 = "On a scale of 1-10, 1 being"  # On a scale - phrase to reduce line length
percentage1 = "What percentage of the"  # Percentage - phrase to reduce line length
percentage2 = "[Please enter in decimal format]"  # Decimal - phrase to reduce line length
between1 = "[Please enter a number between 1-"
greater1 = "[Please do not enter a number greater than "

# Text Repository

# Repository for culture text

# CULTURE 1 stoic
C11 = "people are of average height with beautiful tan skin, the most common hair colors\n"
C12 = "are dark chocolate brown and black. They value control and perceive emotional outbursts as shameful.\n"
C13 = "They are godless but honor their elders, and have some spirituality with their ancestors.\n"
C14 = "Their clothes are simple but very good quality and are often dyed deep jewel tones when they are not dyed black."
C15 = "\nThey do not discriminate between genders but women are often seen as more respectable due to their control\n"
C16 = "of their emotions, they also acknowledge those outside of the binary and offer them great respect.\n"
C17 = "Family oriented, the country is an excellent producer of delicate workmanship and machinery.\n"
C18 = "Their countryside is rocky and densely forested.\n"
C1 = C11 + C12 + C13 + C14 + C15 + C16 + C17 + C18
# The + operator when used with strings combines them with no spaces a + b = ab

# CULTURE 2 sparta
C21 = "people are above average height, the most common hair colors are golden and dark brown.\n"
C22 = "They value athleticism and have strong bonds between friends. They have many gods, but the\n"
C23 = "most called upon is the god of revelry. Their clothes are revealing, and they often wear gaudy\n"
C24 = "and elaborate jewelry. Everyone is taught to fight, however men are expected to belong to a\n"
C25 = "mercenary military group, and women are to handle negotiations and money. A matriarchy, these\n"
C26 = "people have wealth from shrewd planning and domination of other countries, they are also highly\n"
C27 = "relied upon for trade. Their countryside is flat and hot, but also hosts the most precious flowers.\n"
C2 = C21 + C22 + C23 + C24 + C25 + C26 + C27

# CULTURE 3 artistic masters
C31 = "not written quite yet\n"
C32 = "not written quite yet\n"
C33 = "not written quite yet\n"
C34 = "not written quite yet\n"
C35 = "not written quite yet\n"
C36 = "not written quite yet\n"
C37 = "not written quite yet\n"
C3 = C31 + C31 + C33 + C34 + C35 + C36 + C37

# CULTURE 4 forest based
C41 = "not written quite yet\n"
C42 = "not written quite yet\n"
C43 = "not written quite yet\n"
C44 = "not written quite yet\n"
C45 = "not written quite yet\n"
C46 = "not written quite yet\n"
C47 = "not written quite yet\n"
C4 = C41 + C42 + C43 + C44 + C45 + C46 + C47

# CULTURE 5 water based
C51 = "not written quite yet\n"
C52 = "not written quite yet\n"
C53 = "not written quite yet\n"
C54 = "not written quite yet\n"
C55 = "not written quite yet\n"
C56 = "not written quite yet\n"
C57 = "not written quite yet\n"
C5 = C51 + C52 + C53 + C54 + C55 + C56 + C57

# CULTURE 6 weird white people
C61 = "not written quite yet\n"
C62 = "not written quite yet\n"
C63 = "not written quite yet\n"
C64 = "not written quite yet\n"
C65 = "not written quite yet\n"
C66 = "not written quite yet\n"
C67 = "not written quite yet\n"
C6 = C61 + C62 + C63 + C64 + C65 + C66 + C67

# CULTURE 7 giants
C71 = "not written quite yet\n"
C72 = "not written quite yet\n"
C73 = "not written quite yet\n"
C74 = "not written quite yet\n"
C75 = "not written quite yet\n"
C76 = "not written quite yet\n"
C77 = "not written quite yet\n"
C7 = C71 + C72 + C73 + C74 + C75 + C76 + C77

# CULTURE 8 pygmies
C81 = "not written quite yet\n"
C82 = "not written quite yet\n"
C83 = "not written quite yet\n"
C84 = "not written quite yet\n"
C85 = "not written quite yet\n"
C86 = "not written quite yet\n"
C87 = "not written quite yet\n"
C8 = C81 + C82 + C83 + C84 + C85 + C86 + C87

# Repository for god text

G11 = "GOD OF A SAFE HOME"
G1 = G11

G21 = "GOD OF LAUGHTER AND DELIGHT (REVELRY)"
G2 = G21

G31 = "GOD OF WINE AND THE HARVEST"
G3 = G31

G41 = "GOD OF CHARM AND WICKEDNESS"
G4 = G41

G51 = "GOD OF JUSTICE"
G5 = G51

G61 = "PROTECTOR OF THE SOFT"
G6 = G61

G71 = "GOD OF THE PLANETS AND THE SKY"
G7 = G71

G81 = "ONE GOD"
G8 = G81

# User input section

title = input("What would you like the name of your main civilization to be? ")
age = int(input("Please enter the approx. age of civilization of main plot" + between1 + "3000]"))
amt_cult = int(input("How many cultures can you see yourself keeping track of?" + greater1 + "6]"))
agression = int(input(scale1 + " pacifists, how likely is the main culture to praise fighting arts?"))
agriculture = float(input(percentage1 + "population would NOT be rural/agriculturally focused?" + percentage2))
theology = int(input("Enter the number of gods for the main culture: " + greater1 + "7]"))
scholars = int(input(scale1 + " trump supporters, how likely is the main culture to value education?"))
water = int(input(scale1 + " landlocked, about how much of your main civilization's borders are coastline?"))

# Sprint 2
# Colors Repository
#  Used https://www.rapidtables.com/ to find colors decimal code
red = (200, 0, 0)
darkBlue = (0, 0, 139)
lightBlue = (176, 224, 230)
peach = (255, 127, 80)
lime = (0, 255, 0)
sangria = (220, 15, 55)
orange = (255, 140, 0)
mahogany = (160, 82, 45)
darkGreen = (0, 100, 0)
paleGreen = (152, 251, 152)
palePurple = (200, 112, 147)
darkBrown = (120, 49, 15)
yellow = (255, 215, 0)
ultramarine = (30, 144, 255)
silver = (192, 192, 192)
black = (0, 0, 0)

#  Value creation to establish what text is selected (System not fully designed yet)
colors = (65 - water) / 3  # - is subtraction, / is division
ares_v_athena_effect = agression // scholars  # Floor division to get lower(when rounding) whole number answer
sails_v_plows = water // agriculture  # Floor division to get lower(when rounding) whole number answer
pirates_v_navy = agression * theology // 1  # Multiplication, I used floor divison with 1 to get a whole number
size = amt_cult // (water * agriculture)
ego = age ** size  # The ** is x to the y power x**y
monsters = (666 + theology) % 7  # + is addition, % is called the modulus it returns the remainder from division
familiar = 4 + agression
size += 1  # Will take variable add 1 and then return the new value under the same variable
holy = "mol" + "e" * 2

# Conditional Statements Value Creation for attribute picking
#  Basic Color Pick and Culture Selection
# if-elif-else, once one becomes true the others will not be executed but if none are true else will execute
if colors >= 21 or ares_v_athena_effect == 150:
    finalColor = darkGreen
elif 20 >= colors > 19.75 and sails_v_plows < 2:
    finalColor = red
elif 19.75 >= colors > 19.5:
    finalColor = peach
elif 19.5 >= colors > 19.25:
    finalColor = paleGreen
elif 19.25 >= colors > 19:
    finalColor = sangria
elif 19 >= colors > 18.75:
    finalColor = ultramarine
else:
    finalColor = yellow

# God Selection
# if, if true then code will execute
if pirates_v_navy >= 100:
    x = 2
if size >= 100:
    x = 3
# Miscellaeneous
# if-elif, once a statement works it does not execute following statements
if monsters >= 100:
    terrible = 'Arachnids'
elif monsters >= 2:
    terrible = 'Cannibals'
elif monsters >= 1:
    terrible = 'Sentient Plants'
# if-else, if is true then if executes otherwise else is executed
if familiar >= 100:
    witchFriend = 'Dragon'
else:
    witchFriend = 'Feline'

#  Not And Or
# Both must be true
if witchFriend == 'Dragon' and finalColor == yellow:
    model = 'emperordragon'
# One must be true and one must not
if witchFriend == 'Feline' and not finalColor == sangria:
    model = 'notboozycats'
# Either being true will make it true
if witchFriend == 'Dragon' or finalColor == darkGreen:
    thisis = 'AlexFavorite'


#  While For Range In
#  While loops work while the statement within remains true
whilecounter = 0
while whilecounter < 2:
    whilecounter += 2
    print('Come and stay awhile by the fire good sir')
#  For loops work as many times as specified in range
#  Range starts at 0 and will not include the last value example Range(7)=(0 thru 6)
for booty in range(7):
    booty += 4
    print(booty)


# Playing with functions and files
# Function with Parameters
# a and b are parameters, ego and size are arguments, c would be the output
def tired(a, b):
    c = (a + b) ** 2
    print(c)


tired(ego, size)


# Function without parameters will just execute when called
def fileboi():
    outcometext = open("Scripture.txt", 'a')
    outcometext.write("Holy Moly")
    outcometext.close()
    print("Your world is complete! Open Scripture and take a look ...")


fileboi()
# Playing with images
# filename = "MapDisplay.png"
# fnt = ImageFont.truetype('advanced_pixel-7.ttf', 12)
# image = Image.new('RGB', size=(500, 500), color=(0, 100, 0))
# draw = ImageDraw.Draw(image)
# draw.text((10, 10), "I DID IT!", font=fnt, fill=(255, 255, 0))
# image.save(filename)
# os.system(filename)
# # a.save('MapDisplay')
# a = Image.open("dragon.jpg")
# a.show()
