import random
# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

def useSuperTonic():
    hero.health = 10
    print("Your health has been restored.")
    hero.items.remove("SuperTonic")
    
def useArmor():
    hero.armor += 2
    print("Your armor is now " + str(hero.armor))
    hero.items.remove("Armor")

def useEvade():
    hero.evade += 2
    print("Your evade is now " + str(hero.evade))
    hero.items.remove("WD-40")

def usePoison():
    zombie.power -= 1
    shadow.power -= 1
    goblin.power -= 1
    paladin.power -= 1
    warlock.power -= 1
    print("Enemies' power decreased")

def useProteinBar():
    print("You eat protein bar.")
    hero.power += 1
    print("Your power is now " + str(hero.power))

def printShop():
    print("")
    print("------------------------------------|")
    print("You have {} coins.                                                            (  (                  /\\".format(hero.coins))
    print("What would you like to buy?                                                    (_)                 /  \  /\\")
    print("1. SuperTonic - restores health                                        ________[_]________      /\/    \/  \\")
    print("   [Cost: 10 coins]                                           /\      /\        ______    \    /   /\/\  /\/\\")
    print("2. Armor - reduces damage taken                              /  \    //_\       \    /\    \  /\/\/    \/    \\")
    print("   [Cost: 7 coins]                                    /\    / /\/\  //___\       \__/  \    \/")
    print("3. WD-40 - makes you harder to hit                   /  \  /\/    \//_____\       \ |[]|     \\")
    print("   [Cost: 5 coins]                                  /\/\/\/       //_______\       \|__|      \\")
    print("4. Poison - weakens enemy's power                  /      \      /XXXXXXXXXX\                  \\")
    print("   [Cost: 20 coins]                                        \    /_I_II  I__I_\__________________\\")
    print("5. Protein Bar - strengthens your power                           I_I|  I__I_____[]_|_[]_____I")
    print("   [Coins: 15 coins]                                              I_II  I__I_____[]_|_[]_____I ")
    print("6. Leave - choose this if you'd like to enter the next battle.    I II__I  I     XXXXXXX     I")
    print("                                                               ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~")
    print("> ", end=' ')

def theShop():
    printShop()
    itemChoice = input()
    if itemChoice == "1" and hero.coins > 9:
        print("Thank you for your purchase!")
        hero.coins -= 10
        use1 = input("Would you like to this now(Y or N)? ")
        if use1 == "Y":
            hero.health = 10
            print("Your health has been restored.")
        #adds supertonic to bag
        elif use1 == "N":
            hero.items.append("SuperTonic")
            print("You put the SuperTonic in your inventory.")
        else:
            print("Invalid input.")
    #buys armor
    elif itemChoice == "2" and hero.coins > 6:
        print("Thank you for your purchase!")
        hero.coins -= 7
        use2 = input("Would you like to this now(Y or N)? ")
        if use2 == "Y":
            hero.armor += 2
            print("You now have " + str(hero.armor) + " armor.")
        #adds armor to bag
        elif use2 == "N":
            hero.items.append("Armor")
            print("You put the Armor in your inventory.")
        else:
            print("Invalid input.")
    #buys evade
    elif itemChoice == "3" and hero.coins > 4:
        print("Thank you for your purchase!")
        hero.coins -= 5
        use3 = input("Would you like to this now(Y or N)? ")
        if use3 == "Y":
            hero.evade += 2
            print("You now have " + str(hero.evade) + " evade.")
        else:
            hero.items.append("WD-40")
            print("You put the WD-40 in your inventory.")
    #buys poison
    elif itemChoice == "4":
        print("Thank you for your purchase!")
        hero.coins -= 20
        use4 = input("Would you like to this now(Y or N)? ")
        if use4 == "Y":
            usePoison()
        else:
            hero.items.append("Poison")
            print("You put the poison in your inventory.")

    #buys protein bar
    elif itemChoice == "5":
        print("Thank you for your purchase!")
        hero.coins -= 15
        use5 = input("Would you like to this now(Y or N)? ")
        if use5 == "Y":
            useProteinBar()

        else:
            hero.items.append("Protein Bar")
            print("You put the Protein Bar in your inventory.")
    else:
        print("You don't have enough coins!")
        itemChoice == input()

class Characture:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0:
            return True
        else:
            False

class Hero(Characture):
    def __init__(self, health, power, coins, armor, items, evade):
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = armor
        self.items = items
        self.evade = evade
        items = []
        coins = 0
        evade = 0

    def attack(self, enemy):
        attack = [1, 2, 3, 4, 5, 6]
        attacks = attack[(random.randint(0, 6) - 1)]
        criticalAttack = attack[4]
        chanceOfAttack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        finishingBlow = chanceOfAttack[5]
        chanceOfReflect = [1, 2, 3, 4, 5]
        reflect = chanceOfReflect[2]
        #includes chance of critical strike
        if attacks == criticalAttack and enemy.name != "Shadow" and enemy.name != "Paladin":
            print("Critical Strike!")
            enemy.health -= (hero.power * 2)
            print("You do {} damage to the {}.".format(hero.power, enemy.name))
        elif attacks != criticalAttack and enemy.name != "Shadow" and enemy.name != "Paladin":
            enemy.health -= hero.power
            print("You do {} damage to the {}.".format(hero.power, enemy.name))
        #handles the paladin's counter attack
        elif enemy.name == "Paladin":
            if chanceOfReflect[random.randint(0, 4)] == reflect:
                print("Paladin reflects your attack!")
                hero.health -= hero.power
                print("You do {} damage to the yourself.".format(hero.power))
            else:
                enemy.health -= hero.power
                print("You do {} damage to the {}.".format(hero.power, enemy.name))
        #handles Shadow's evade
        elif enemy.name == "Shadow":
            if chanceOfAttack[random.randint(0, 10)] == finishingBlow:
                enemy.health -= hero.power
                print("You do {} damage to the {}.".format(hero.power, enemy.name))
            else:
                print("Shadow dodges your attack!")
        #handles enemies death and the zombie's lack of death
        if enemy.health <= 0 and enemy.name != "Zombie" and enemy.name != "Paladin":
            print("The " + enemy.name + " is dead.")
            print("You receive {} coins!".format(enemy.coins))
            hero.coins += enemy.coins
            print("You have {} coins, ".format(hero.coins))
            visitStore = input("would you like to go to the store(Y or N)? ")
            if visitStore == "Y":
                theShop()
            elif visitStore == "N":
                print("You approch the next enemy.")
        elif enemy.health <= 0 and enemy.name == "Paladin":
            print("The paladin dies!")
            print("")
            print("-----------------------------")
            print("----------YOU WIN------------")
            print("-----------------------------")
        elif enemy.health <= 0 and enemy.name == "Zombie":
            print("The " + enemy.name + " appears dead.")
            print("The zombie gets back up!")
    def print_status(self):
        print("You have {} health and {} power.".format(hero.health, hero.power))

class Zombie(Characture):
    def __init__(self, name, health, power, coins):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins
    def attack(self, you):
        evadeChance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        theEvade = evadeChance[2]
        if hero.evade == 0:
            hero.health -= (zombie.power - hero.armor)
            print("The zombie does {} damage to you.".format(zombie.power))
        elif hero.evade == 2:
            if evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade:
                print("The zombie misses!")
            else:
                hero.health -= (zombie.power - hero.armor)
                print("The zombie does {} damage to you.".format(zombie.power))
        elif hero.evade == 4:
            if evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade:
                print("The zombie misses!")
            else:
                hero.health -= (zombie.power - hero.armor)
                print("The zombie does {} damage to you.".format(zombie.power))
        if hero.health <= 0:
            print("You are dead.")
    def print_status(self):
        print("The zombie has {} health and {} power.|".format(zombie.health, zombie.power))

class Shadow(Characture):
    def __init__(self, name, health, power, coins):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins
    def attack(self, you):
        evadeChance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        theEvade = evadeChance[5]
        if hero.evade == 0:
            hero.health -= (shadow.power - hero.armor)
            print("Shadow does {} damage to you.".format(shadow.power))
        elif hero.evade == 2:
            if evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade:
                print("Shadow misses!")
            else:
                hero.health -= (shadow.power - hero.armor)
                print("Shadow does {} damage to you.".format(shadow.power))
        if hero.evade == 4:
            if evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade:
                print("Shadow misses!")
            else:
                hero.health -= (shadow.power - hero.armor)
                print("Shadow does {} damage to you.".format(shadow.power))
        if hero.health <= 0:
            print("You are dead.")
    def print_status(self):
        print("Shadow has {} health and {} power.".format(shadow.health, shadow.power))

class Medic(Characture):
    def __init__(self, name, health, power, coins):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins
    def attack(self, you):
        chance_of_heal = [1, 2, 3, 4, 5, 6]
        heal = chance_of_heal[4]
        evadeChance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        theEvade = evadeChance[3]
        if hero.evade == 0:
            if chance_of_heal[random.randint(0, 5)] == heal:
                print("Medic recuperates 2 health!")
                medic.health += 2
                print("Medic now has " + str(medic.health) + " health")
                hero.health -= (medic.power - hero.armor)
                print("The medic does {} damage to you.".format(medic.power))
            else:
                hero.health -= (medic.power - hero.armor)
                print("The medic does {} damage to you.".format(medic.power))
        elif hero.evade == 2:
            if evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade:
                print("The medic misses!")
                print("Medic recuperates 2 health!")
                medic.health += 2
                print("Medic now has " + str(medic.health) + " health")
            else:
                if chance_of_heal[random.randint(0, 5)] == heal:
                    print("Medic recuperates 2 health!")
                    medic.health += 2
                    print("Medic now has " + str(medic.health) + " health")
                    hero.health -= (medic.power - hero.armor)
                    print("The medic does {} damage to you.".format(medic.power))
                else:
                    hero.health -= (medic.power - hero.armor)
                    print("The medic does {} damage to you.".format(medic.power))
        if hero.evade == 4:
            if evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade:
                print("The medic misses!")
                print("Medic recuperates 2 health!")
                medic.health += 2
                print("Medic now has " + str(medic.health) + " health")
            else:
                if chance_of_heal[random.randint(0, 5)] == heal:
                    print("Medic recuperates 2 health!")
                    medic.health += 2
                    print("Medic now has " + str(medic.health) + " health")
                    hero.health -= (medic.power - hero.armor)
                    print("The medic does {} damage to you.".format(medic.power))
                else:
                    hero.health -= (medic.power - hero.armor)
                    print("The medic does {} damage to you.".format(medic.power))
        if hero.health <= 0:
            print("You are dead.")
    def print_status(self):
        print("Medic has {} health and {} power.".format(medic.health, medic.power))

class Paladin(Characture):
    def __init__(self, name, health, power, coins):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins
    def attack(self, you):
        evadeChance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        theEvade = evadeChance[6]
        if hero.evade == 0:
            hero.health -= (paladin.power - hero.armor)
            print("The paladin does {} damage to you.".format(paladin.power))
        elif hero.evade == 2:
            if evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade:
                print("The paladin misses!")
            else:
                hero.health -= (paladin.power - hero.armor)
                print("The paladin does {} damage to you.".format(paladin.power))
        if hero.evade == 4:
            if evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade:
                print("The paladin misses!")
            else:
                hero.health -= (paladin.power - hero.armor)
                print("The paladin does {} damage to you.".format(paladin.power))
        if hero.health <= 0:
            print("You are dead.")
    def print_status(self):
        print("The paladin has {} health and {} power|".format(paladin.health, paladin.power))

class Goblin(Characture):
    def __init__(self, name, health, power, coins):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins
    def attack(self, you):
        evadeChance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        theEvade = evadeChance[1]
        if hero.evade == 0:
            hero.health -= (goblin.power - hero.armor)
            print("The goblin does {} damage to you.".format(goblin.power))
        elif hero.evade == 2:
            if evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade:
                print("The goblin misses!")
            else:
                hero.health -= (goblin.power - hero.armor)
                print("The goblin does {} damage to you.".format(goblin.power))
            if hero.evade == 4:
                if evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade or evadeChance[random.randint(0, 10)] == theEvade:
                    print("The goblin misses!")
                else:
                    hero.health -= (goblin.power - hero.armor)
                    print("The goblin does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
            print("You are dead.")
    def print_status(self):
        print("The goblin has {} health and {} power.|".format(goblin.health, goblin.power))

class Warlock(Characture):
    def __init__(self, name, health, power, coins):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins
    def attack(self, you):
        evadeChance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        randomEvade = random.randint(0, 10)
        if hero.evade == 0:
            hero.health -= (warlock.power - hero.armor)
            warlock.health += (warlock.power - hero.armor)
            print("The warlock steals {} life from you.".format(warlock.power))
        elif hero.evade == 2:
            if evadeChance[random.randint(0, 10)] == randomEvade or evadeChance[random.randint(0, 10) == randomEvade]:
                print("The warlock misses!")
            else:
                hero.health -= (warlock.power - hero.armor)
                warlock.health += (warlock.power - hero.armor)
                print("The warlock steals {} life from you.".format(warlock.power))
            if hero.evade == 4:
                if evadeChance[random.randint(0, 10)] == randomEvade or evadeChance[random.randint(0, 10) == randomEvade] or evadeChance[random.randint(0, 10)] == randomEvade or evadeChance[random.randint(0, 10) == randomEvade]:
                    print("The warlock misses!")
                else:
                    hero.health -= (warlock.power - hero.armor)
                    warlock.health += (warlock.power - hero.armor)
                    print("The warlock steals {} life from you.".format(warlock.power))
        
        if hero.health <= 0:
            print("You are dead.")
    def print_status(self):
        print("The warlock has {} health and {} power|".format(warlock.health, warlock.power))

hero = Hero(10, 5, 0, 0, [], 0)
goblin = Goblin("Goblin", 6, 2, 6)
medic = Medic("Medic", 7, 3, 9)
shadow = Shadow("Shadow", 1, 1, 13)
zombie = Zombie("Zombie", 10, 4, 53)
paladin = Paladin("Paladin", 8, 3, 15)
warlock = Warlock("Warlock", 6, 3, 11)


def warlockFight():
    while warlock.alive() and hero.alive():
        hero.print_status()
        warlock.print_status()
        print("------------------------------------|")
        print("What do you want to do?             |              _,._    ")
        print("                                    |  .||,       /_ _\\  ")
        print("1. fight warlock                    | \.`',/      |'L'| |  ")
        print("2. do nothing                       | = ,. =      | -,| L   ")
        print("3. use item                         | / || \    ,-'\"/,'`.  ")
        print("4. flee                             |   ||     ,'   `,,. `.  ")
        print("                                    |")
        print("> ", end=' ')
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(warlock)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            useItem = input("Would you like to use an item?(Y or N)")
            if useItem == "Y":
                if len(hero.items) == 0:
                    print("You don't have any items!")
                elif len(hero.items) == 1:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                elif len(hero.items) == 2:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                elif len(hero.items) == 3:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    print("3. " + hero.items[2])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
            else:
                pass
            
        elif raw_input == "4":
            print("You flee the battle.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if warlock.alive():
            warlock.attack(hero)

def goblin_fight():
    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print("------------------------------------|")
        print("What do you want to do?             |      \\\_____//")
        print("                                    |     /===   ===\\")
        print("1. fight goblin                     |  /\/¦  0 ¦ 0 ¦\\/\\")
        print("2. do nothing                       |  \  \  <x x>  / /")
        print("3. use item                         |    \/  <--->  \/")
        print("4. flee                             |       \__,__/")
        print("                                    |")
        print("> ", end=' ')
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            useItem = input("Would you like to use an item?(Y or N)")
            if useItem == "Y":
                if len(hero.items) == 0:
                    print("You don't have any items!")
                elif len(hero.items) == 1:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                        hero.items.remove("Poison")
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                        hero.items.remove("Protein Bar")
                elif len(hero.items) == 2:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                elif len(hero.items) == 3:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    print("3. " + hero.items[2])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
            else:
                pass
            
        elif raw_input == "4":
            print("You flee the battle.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            goblin.attack(hero)

def medicFight():
    while medic.alive() and hero.alive():
        hero.print_status()
        medic.print_status()
        print("------------------------------------|")
        print("What do you want to do?             |        .----. ")
        print("                                    |       ===(_)== ")
        print("1. fight medic                      |      // 6  6 \\\\")
        print("2. do nothing                       |      (    7   )")
        print("3. use item                         |       \  --  /")
        print("4. flee                             |        \_ ._/")
        print("                                    |")
        print("> ", end=' ')
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(medic)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            useItem = input("Would you like to use an item?(Y or N)")
            if useItem == "Y":
                if len(hero.items) == 0:
                    print("You don't have any items!")
                elif len(hero.items) == 1:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                elif len(hero.items) == 2:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                elif len(hero.items) == 3:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    print("3. " + hero.items[2])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
            else:
                pass
            
        elif raw_input == "4":
            print("You flee the battle.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if medic.alive():
            medic.attack(hero)

def shadowFight():
    while shadow.alive() and hero.alive():
        hero.print_status()
        shadow.print_status()
        print("------------------------------------|")
        print("What do you want to do?             |           .--._")
        print("                                    |     __   '---._)")
        print("1. fight shadow                     |      )\   Q Q )")
        print("2. do nothing                       |     =_/   c  /")
        print("3. use item                         |     | \_.-;-'-,._")
        print("4. flee                             |     |  '  o---o   )")
        print("                                    |")
        print("> ", end=' ')
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(shadow)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            useItem = input("Would you like to use an item?(Y or N)")
            if useItem == "Y":
                if len(hero.items) == 0:
                    print("You don't have any items!")
                elif len(hero.items) == 1:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                elif len(hero.items) == 2:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                elif len(hero.items) == 3:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    print("3. " + hero.items[2])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
            else:
                pass
            
        elif raw_input == "4":
            print("You flee the battle.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if shadow.alive():
            shadow.attack(hero)

def zombieFight():
    while hero.alive():
        hero.print_status()
        zombie.print_status()
        print("------------------------------------|")
        print("What do you want to do?             |                  ..... ")
        print("                                    |                 C C  /  ")
        print("1. fight zombie                     |                /<   /  ")
        print("2. do nothing                       | ___ __________/_#__=o  ")
        print("3. use item                         |/(- /(\_\________   \    ")
        print("4. flee                             |\ ) \ )_      \o     \    ")
        print("                                    |")
        print("> ", end=' ')
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(zombie)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            useItem = input("Would you like to use an item?(Y or N)")
            if useItem == "Y":
                if len(hero.items) == 0:
                    print("You don't have any items!")
                elif len(hero.items) == 1:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                elif len(hero.items) == 2:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                elif len(hero.items) == 3:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    print("3. " + hero.items[2])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
            else:
                pass
            
        elif raw_input == "4":
            print("You flee the battle.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        zombie.attack(hero)

def paladinFight():
    while paladin.alive() and hero.alive():
        hero.print_status()
        paladin.print_status()
        print("------------------------------------|")
        print("What do you want to do?             | |\\           _!_")
        print("                                    |  \\\         /___\\")
        print("1. fight paladin                    |   \\\        [+++]")
        print("2. do nothing                       |    \\\    _ _\^^^/_ _")
        print("3. use item                         |     \\\/ (    '-'  ( )")
        print("4. flee                             |     /( \/ | {&}   /\ \\")
        print("> ", end=' ')
        print("                                    |")
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(paladin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            useItem = input("Would you like to use an item?(Y or N)")
            if useItem == "Y":
                if len(hero.items) == 0:
                    print("You don't have any items!")
                elif len(hero.items) == 1:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                elif len(hero.items) == 2:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
                elif len(hero.items) == 3:
                    print("What would you like to use?")
                    print("1. " + hero.items[0])
                    print("2. " + hero.items[1])
                    print("3. " + hero.items[2])
                    whichItem = input()
                    theAnswer = int(whichItem) - 1
                    if hero.items[theAnswer] == "SuperTonic":
                        useSuperTonic()
                    elif hero.items[theAnswer] == "Armor":
                        useArmor()
                    elif hero.items[theAnswer] == "WD-40":
                        useEvade()
                    elif hero.items[theAnswer] == "Poison":
                        usePoison()
                    elif hero.items[theAnswer] == "Protein Bar":
                        useProteinBar()
            else:
                pass
            
        elif raw_input == "4":
            print("You flee the battle.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if paladin.alive():
            paladin.attack(hero)


goblin_fight()
medicFight()
shadowFight()
goblin_fight()
zombieFight()
warlockFight()
paladinFight()
