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

selsandwich = "#1 Pepe"
selbread = choice(breads)
selcondiment = choice(condiments)
selveggie = choice(veggies)
sel2veggie = choice(veggies)
selmeat = choice(meats)
selmodifier = choice(modifiers)
selstyle = choice(styles)

def new_order():
    global selsandwich
    global selbread
    global selcondiment
    global selveggie
    global sel2veggie
    global selmeat
    global selmodifier
    global selstyle
    selsandwich = choice(sandwiches)
    selbread = choice(breads)
    selcondiment = choice(condiments)
    selveggie = choice(veggies)
    sel2veggie = choice(veggies)
    selmeat = choice(meats)
    selmodifier = choice(modifiers)
    selstyle = choice(styles)

def validity_checker():
    valid = False
    global selsandwich
    global selbread
    global selcondiment
    global selveggie
    global sel2veggie
    global selmeat
    global selmodifier
    global selstyle
    while not valid:
        valid_sandwich = False
        while not valid_sandwich:  
            if selsandwich in ["#1 Pepe", "#2 Big John", "#4 Turkey Tom"]:
                if selbread in ["Unwich", "wheat bread"]:
                    if selstyle != "cut in half":
                        selstyle = choice(styles)
                        valid = False
                    else:
                        valid = True
                if selstyle == "TBO":
                    selstyle = choice(styles)
                    valid = False
                else:
                    valid = True
                if selveggie == sel2veggie:
                    selveggie = choice(veggies)
                    sel2veggie = choice(veggies)
                    valid = False
                else:
                    valid = True
                if selmodifier == "add":
                    if selcondiment == "mayo":
                        selcondiment = choice(condiments)
                        valid = False
                    elif selveggie in ["lettuce", "tomatoes"]:
                        selveggie = choice(veggies)
                        valid = False
                    elif sel2veggie in ["lettuce", "tomatoes"]:
                        sel2veggie = choice(veggies)
                        valid = False
                    elif selmeat not in ["salami", "capicola", "tuna"]:
                        selmeat = choice(meats)
                        valid = False
                    else:
                        valid = True
                if selmodifier == "no":
                    if selcondiment != "mayo":
                        selcondiment = choice(condiments)
                        valid = False
                    elif selveggie not in ["lettuce", "tomatoes"]:
                        selveggie = choice(veggies)
                        valid = False
                    elif sel2veggie not in ["lettuce", "tomatoes"]:
                        sel2veggie = choice(veggies)
                        valid = False
                    else:
                        valid = True
                if selmodifier == "extra":
                    if selmeat not in ["cheese", "salami", "capicola", "tuna"]:
                        selmeat = choice(meats)
                        valid = False
                    else:
                        valid = True
                if valid:
                    break
            elif selsandwich == "#3 Totally Tuna":
                if selbread in ["Unwich", "wheat bread"]:
                    if selstyle != "cut in half":
                        selstyle = choice(styles)
                        valid = False
                    else:
                        valid = True
                if selstyle == "TBO":
                    selstyle = choice(styles)
                    valid = False
                else:
                    valid = True
                if selveggie == sel2veggie:
                    selveggie = choice(veggies)
                    sel2veggie = choice(veggies)
                    valid = False
                else:
                    valid = True
                if selmodifier == "add":
                    if selveggie in ["lettuce", "tomatoes", "cucumbers"]:
                        selveggie = choice(veggies)
                        valid = False
                    elif sel2veggie in ["lettuce", "tomatoes", "cucumbers"]:
                        sel2veggie = choice(veggies)
                        valid = False    
                    elif selmeat == "cheese":
                        selmeat = choice(meats)
                        valid = False
                    else:
                        valid = True
                if selmodifier == "no":
                    if selveggie not in ["lettuce", "tomatoes", "cucumbers"]:
                        selveggie = choice(veggies)
                        valid = False
                    elif sel2veggie not in ["lettuce", "tomatoes", "cucumbers"]:
                        sel2veggie = choice(veggies)
                        valid = False
                    else:
                        valid = True
                if selmodifier == "extra":
                    if selmeat != "tuna":
                        selmeat = choice(meats)
                        valid = False
                    else:
                        valid = True
                if valid:
                    break
            else:
                selsandwich = choice(sandwiches)
i = 0
while i < 5:
    new_order()
    validity_checker()
    offer1 = "Try a %s %s %s %s." % (selsandwich, selmodifier, selveggie, selstyle)
    print offer1
    new_order()
    validity_checker()
    offer2 = "Order a %s %s %s and %s on %s." % (selsandwich, selmodifier, selveggie, sel2veggie, selbread)
    print offer2
    i += 1