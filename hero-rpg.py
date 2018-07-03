import random
# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

def theShop():
    print("")
    print("------------------------------------|")
    print("You have {} coins.".format(hero.coins))
    print("What would you like to buy?")
    print("1. SuperTonic - restores health")
    print("   Cost: 10 coins")
    print("2. Armor - reduces damage taken")
    print("   Cost: 7 coins")
    print("3. WD-40 - makes you harder to hit")
    print("   Cost: 5 coins")
    print("4. ~~~~~~~~")
    print("   Cost:")
    print("5. ~~~~~~")
    print("   Coins: ")
    print("6. Leave - choose this if you'd like to enter the next battle")
    print("> ", end=' ')
    itemChoice = input()
    if itemChoice == "1":
        print("Thank you for your purchase!")
        hero.coins -= 10
        use1 = input("Would you like to this now(Y or N)?")
        if use1 == "Y":
            hero.health = 10
            print("Your health has been restored.")
            ifDone = input("Would you like to purchase anything else(Y or N)?")
            if ifDone == "Y":
                print("")
                print("------------------------------------|")
                print("What would you like to buy?")
                print("1. SuperTonic - restores health")
                print("   Cost: 10 coins")
                print("2. Armor - reduces damage taken")
                print("   Cost: 7 coins")
                print("3. WD-40 - makes you harder to hit")
                print("   Cost: 5 coins")
                print("> ", end=' ')
                itemChoice = input()
            elif ifDone == "N":
                print("Thank you, come again!")
            else:
                print("Invalid input")
                ifDone = input("Would you like to purchase anything else(Y or N)?")
        elif use1 == "N":
            print("Thank you, come again!")
        else:
            print("Invalid input.")
    elif itemChoice == "2":
        print("Thank you for your purchase!")
        hero.coins -= 7
        use2 = input("Would you like to this now(Y or N)?")
    elif itemChoice == "3":
        print("Thank you for your purchase!")
        hero.coins -= 5
        use3 = input("Would you like to this now(Y or N)?")
    elif itemChoice == "4":
        print("Thank you for your purchase!")
        hero.coins -= 10
        use4 = input("Would you like to this now(Y or N)?")
    elif itemChoice == "5":
        print("Thank you for your purchase!")
        hero.coins -= 10
        use5 = input("Would you like to this now(Y or N)?")
    else:
        print("Invalid input")
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
    def __init__(self, health, power, coins, armor):
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = armor
        coins = 0
    def attack(self, enemy):
        attacks = [1, 2, 3, 4, 5, 6]
        criticalAttack = attacks[4]
        chanceOfAttack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        finishingBlow = chanceOfAttack[5]
        chanceOfReflect = [1, 2, 3, 4, 5]
        reflect = chanceOfReflect[2]
        useItem = input("Would you like to use an item?")
        #includes chance of critical strike
        if attacks[random.randint(0,5)] == criticalAttack and enemy.name != "Shadow" and enemy.name != "Paladin":
            print("Critical Strike!")
            enemy.health -= (hero.power * 2)
            print("You do {} damage to the {}.".format(hero.power, enemy.name))
        elif attacks[random.randint(0,5)] != criticalAttack and enemy.name != "Shadow" and enemy.name != "Paladin":
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
        if enemy.health <= 0 and enemy.name != "Zombie":
            print("The " + enemy.name + " is dead.")
            print("You receive {} coins!".format(enemy.coins))
            hero.coins += enemy.coins
            print("You have {} coins, ".format(hero.coins))
            visitStore = input("would you like to go to the store(Y or N)?")
            if visitStore == "Y":
                theShop()
            elif visitStore == "N":
                print("You approch the next enemy.")
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
        hero.health -= zombie.power
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
        hero.health -= shadow.power
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
        if chance_of_heal[random.randint(0, 5)] == heal:
            print("Medic recuperates 2 health!")
            medic.health += 2
            print("Medic now has " + str(medic.health) + " health")
            hero.health -= medic.power
            print("The medic does {} damage to you.".format(medic.power))
        else:
            hero.health -= medic.power
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
        hero.health -= paladin.power
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
        hero.health -= goblin.power
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
        hero.health -= warlock.power
        warlock.health += warlock.power
        print("The warlock steals {} life from you.".format(warlock.power))
        if hero.health <= 0:
            print("You are dead.")
    def print_status(self):
        print("The warlock has {} health and {} power|".format(warlock.health, warlock.power))

hero = Hero(10, 5, 0)
goblin = Goblin("Goblin", 6, 2, 5)
medic = Medic("Medic", 7, 2, 7)
shadow = Shadow("Shadow", 1, 1, 6)
zombie = Zombie("Zombie", 10, 1, 13)
paladin = Paladin("Paladin", 8, 1, 15)
warlock = Warlock("Warlock", 6, 2, 9)


def warlockFight():
    while warlock.alive() and hero.alive():
        hero.print_status()
        warlock.print_status()
        print("------------------------------------|")
        print("What do you want to do?             |              _,._    ")
        print("                                    |  .||,       /_ _\\  ")
        print("1. fight warlock                    | \.`',/      |'L'| |  ")
        print("2. do nothing                       | = ,. =      | -,| L   ")
        print("3. flee                             | / || \    ,-'\"/,'`.  ")
        print("                                    |   ||     ,'   `,,. `.  ")
        print("> ", end=' ')
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(warlock)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
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
        print("3. flee                             |    \/  <--->  \/")
        print("                                    |       \__,__/")
        print("> ", end=' ')
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
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
        print("3. flee                             |       \  --  /")
        print("                                    |        \_ ._/")
        print("> ", end=' ')
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(medic)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
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
        print("3. flee                             |     | \_.-;-'-,._")
        print("                                    |     |  '  o---o   )")
        print("> ", end=' ')
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(shadow)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
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
        print("3. flee                             |/(- /(\_\________   \    ")
        print("                                    |\ ) \ )_      \o     \    ")
        print("> ", end=' ')
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(zombie)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        zombie.attack(hero)

def paladinFight():
    while paladin.alive() and hero.alive():
        hero.print_status()
        paladin.print_status()
        print("------------------------------------|")
        print("What do you want to do?             | |\           _!_")
        print("                                    |  \\         /___\\")
        print("1. fight paladin                    |   \\        [+++]")
        print("2. do nothing                       |    \\    _ _\^^^/_ _")
        print("3. flee                             |     \\/ (    '-'  ( )")
        print("                                    |     /( \/ | {&}   /\ \\")
        print("> ", end=' ')
        raw_input = input()
        print("------------------------------------|")
        if raw_input == "1":
            hero.attack(paladin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if paladin.alive():
            paladin.attack(hero)


goblin_fight()
medicFight()
shadowFight()
zombieFight()
warlockFight()
paladinFight()