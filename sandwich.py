from random import choice
from time import sleep

sandwiches = ["#1 Pepe", "#2 Big John", "#3 Totally Tuna", "#4 Turkey Tom", "#5 Vito", "#6 Veggie Sub", "JJ BLT",
"#7 Smoked Ham Club", "#8 Billy Club", "#9 Italian Night Club", "#10 Hunters Club", "#11 Country Club", "#12 Beach Club",
"#13 Veggie Club", "#14 Bootlegger Club", "#15 Club Tuna", "#16 Club Lulu", "#17 Ultimate Porker", "JJ Gargantuan",
 "Slim 1", "Slim 2", "Slim 3", "Slim 4", "Slim 5", "Slim 6", "Slim Bacon"
]

breads = ["French bread", "wheat bread", "Unwich"]

condiments = ["mayo", "dijon mustard", "avocado spread", "oil vinaigrette", "Jimmy mustard"]

veggies = ["lettuce", "tomatoes", "onions", "cherry peppers", "oregano", "cucumbers"]

meats = ["ham", "turkey", "cheese", "vito meat", "salami", "capicola", "roast beef", "bacon", "tuna"]

modifiers = ["add", "no", "extra"]
styles = ["LBI", "TBO", "cut in half"]

selsandwich = ""
selbread = ""
selcondiment = ""
selveggie = ""
sel2veggie = ""
sel3veggie = ""
selmeat = ""
selmodifier = ""
sel2modifier = ""
selstyle = ""

def new_order():
    global selsandwich
    global selbread
    global selcondiment
    global selveggie
    global selmeat
    global selmodifier
    global selstyle
    selsandwich = choice(sandwiches[:6])
    selbread = choice(breads)
    selcondiment = choice(condiments)
    selveggie = choice(veggies)
    selmeat = choice(meats)
    selmodifier = choice(modifiers)
    selstyle = choice(styles)

def validate_pepe():
    valid = False
    global selsandwich
    global selbread
    global selcondiment
    global selveggie
    global selmeat
    global selmodifier
    global selstyle
    print "Found a %s." % selsandwich
    sleep(1)
    while not valid:
        if selbread == "French bread" and selstyle == "TBO":
            selstyle = choice(styles)
            valid = False
        else:
            valid = True
        if selbread != "French bread" and selstyle != "cut in half":
            selstyle = choice(styles)
            valid = False
        else:
            valid = True
        if selmodifier == "add":
            print "Add %s?" % selcondiment
            sleep(1)
            if selcondiment == "mayo":
                print "Changing condiment..."
                sleep(1)
                selcondiment = choice(condiments)
                valid = False
        elif selmodifier == "no":
            print "No %s?" % selcondiment
            sleep(1)
            if selcondiment != "mayo":
                print "Changing condiment.."
                sleep(1)
                selcondiment = choice(condiments)
                valid = False
        else:
            valid = True
        if selmodifier == "add":
            print "Add %s?" % selveggie
            sleep(1)
            if selveggie in ["lettuce", "tomatoes"]:
                print "Changing veggies..."
                sleep(1)
                selveggie = choice(veggies)
                valid = False
        elif selmodifier == "no":
            print "No %s?" % selveggie
            sleep(1)
            if selveggie not in ["lettuce", "tomatoes"]:
                print "Changing veggie..."
                sleep(1)
                selveggie = choice(veggies)
                valid = False
        else:
            valid = True

def validate_vito():
    valid = False
    global selsandwich
    global selbread
    global selcondiment
    global selveggie
    global selmeat
    global selmodifier
    global selstyle
    print "Found a %s." % selsandwich
    sleep(1)
    while not valid:
        if selbread == "French bread" and selstyle == "TBO":
            selstyle = choice(styles)
            valid = False
        else:
            valid = True
        if selbread != "French bread" and selstyle != "cut in half":
            selstyle = choice(styles)
            valid = False
        else:
            valid = True
        if selmodifier == "add":
            print "Add %s?" % selcondiment
            sleep(1)
            if selcondiment == "oil vinaigrette":
                print "Changing condiment..."
                sleep(1)
                selcondiment = choice(condiments)
                valid = False
        elif selmodifier == "no":
            print "No %s?" % selcondiment
            sleep(1)
            if selcondiment != "oil vinaigrette":
                print "Changing condiment.."
                sleep(1)
                selcondiment = choice(condiments)
                valid = False
        else:
            valid = True
        if selmodifier == "add":
            print "Add %s?" % selveggie
            sleep(1)
            if selveggie not in ["cherry peppers", "cucumbers"]:
                print "Changing veggies..."
                sleep(1)
                selveggie = choice(veggies)
                valid = False
        elif selmodifier == "no":
            print "No %s?" % selveggie
            sleep(1)
            if selveggie  in ["cherry peppers", "cucumbers"]:
                print "Changing veggie..."
                sleep(1)
                selveggie = choice(veggies)
                valid = False
        else:
            valid = True

def validate_veggiesub():
    valid = False
    global selsandwich
    global selbread
    global selcondiment
    global selveggie
    global selmeat
    global selmodifier
    global selstyle
    print "Found a %s." % selsandwich
    sleep(1)
    while not valid:
        if selbread == "French bread" and selstyle == "TBO":
            selstyle = choice(styles)
            valid = False
        else:
            valid = True
        if selbread != "French bread" and selstyle != "cut in half":
            selstyle = choice(styles)
            valid = False
        else:
            valid = True
        if selmodifier == "add":
            print "Add %s?" % selcondiment
            sleep(1)
            if selcondiment in ["mayo", "avocado spread"]:
                print "Changing condiment..."
                sleep(1)
                selcondiment = choice(condiments)
                valid = False
        elif selmodifier == "no":
            print "No %s?" % selcondiment
            sleep(1)
            if selcondiment not in ["mayo", "avocado spread"]:
                print "Changing condiment.."
                sleep(1)
                selcondiment = choice(condiments)
                valid = False
        else:
            valid = True
        if selmodifier == "add":
            print "Add %s?" % selveggie
            sleep(1)
            if selveggie in ["lettuce", "tomatoes", "cucumbers"]:
                print "Changing veggies..."
                sleep(1)
                selveggie = choice(veggies)
                valid = False
        elif selmodifier == "no":
            print "No %s?" % selveggie
            sleep(1)
            if selveggie not in ["lettuce", "tomatoes", "cucumbers"]:
                print "Changing veggie..."
                sleep(1)
                selveggie = choice(veggies)
                valid = False
        else:
            valid = True

def validate_tuna():
    valid = False
    global selsandwich
    global selbread
    global selcondiment
    global selveggie
    global selmeat
    global selmodifier
    global selstyle
    print "Found a %s." % selsandwich
    sleep(1)
    while not valid:
        if selbread == "French bread" and selstyle == "TBO":
            selstyle = choice(styles)
            valid = False
        else:
            valid = True
        if selbread != "French bread" and selstyle != "cut in half":
            selstyle = choice(styles)
            valid = False
        else:
            valid = True
        if selmodifier == "add":
            print "Add %s?" % selcondiment
            sleep(1)
        elif selmodifier == "no":
            print "No %s?" % selcondiment
            sleep(1)
            if selcondiment:
                print "Switching to 'add' %s..." % selcondiment
                sleep(1)
                selmodifier = "add"
                valid = False
        else:
            valid = True
        if selmodifier == "add":
            print "Add %s?" % selveggie
            sleep(1)
            if selveggie in ["lettuce", "tomatoes", "cucumbers"]:
                print "Changing veggies..."
                sleep(1)
                selveggie = choice(veggies)
                valid = False
        elif selmodifier == "no":
            print "No %s?" % selveggie
            sleep(1)
            if selveggie not in ["lettuce", "tomatoes", "cucumbers"]:
                print "Changing veggie..."
                sleep(1)
                selveggie = choice(veggies)
                valid = False
        else:
            valid = True


i = 0
while i < 5:
    new_order()
    if selsandwich in ["#1 Pepe", "#2 Big John", "#4 Turkey Tom"]:
        validate_pepe()
    if selsandwich == "#3 Totally Tuna":
        validate_tuna()
    if selsandwich == "#5 Vito":
        validate_vito()
    if selsandwich == "#6 Veggie Sub":
        validate_veggiesub()
    offer1 = "Try a %s %s %s %s." % (selsandwich, selmodifier, selveggie, selstyle)
    print offer1
    # validity_checker()
    # offer1 = "Try a %s %s %s %s." % (selsandwich, selmodifier, selveggie, selstyle)
    # print offer1
    # offer2 = "Order a %s %s %s and %s on %s." % (selsandwich, selmodifier, selveggie, sel2veggie, selbread)
    # print offer2
    # offer3 = "How about a %s %s %s %s %s?" % (selsandwich, selmodifier, selveggie, sel2modifier, selcondiment)
    # print offer3
    i += 1