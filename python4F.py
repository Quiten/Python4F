import os.path

lijst = {}
fileName = "NL-ENG.txt"
schermbreedte = 60

check = { "read":False, "dele":False, "toev":False, "overh":False,}

def begin_code():
    leeg_scherm()
    funct = ""
    commandos = ["toev", "read", "clear", "esc", "maak", "change", "test", "overhoor", "del"]
    while not funct in commandos:
        leeg_scherm()
        print("+" + "-"*(schermbreedte - 2) + "+")    
        print("| {:<56} |".format("toev : woord toevoegen"))
        print("| {:<56} |".format("read : regels lezen"))
        print("| {:<56} |".format("maak : maak nieuwe txt bestand aan"))
        print("| {:<56} |".format("esc  : Programma stoppen"))
        print("| {:<56} |".format("change : verander woordenlijst"))
        print("| {:<56} |".format("ovehroor : start overhoren"))
        print("|" + "-"*(schermbreedte ))
        print("| {:<10}{:<46} |".format("lijst: ", fileName))
        print("+" + "~"*(schermbreedte - 2) + "+")
        funct = input("| {:<10}".format("keuze  : "))
        print("+" + "~"*(schermbreedte - 2) + "+")    
        if (funct in commandos):
            functies(funct)
        else:
            print("Zit niet in de commandos lijst")

def functies(funct):
    while(funct != "esc"):
        if (funct == "toev"):
            check["toev"] = True
            functies_toev()
        elif (funct == "read"):
            check["read"] = True
            functies_read()
        elif (funct == "maak"):
            functies_maak()
        elif (funct == "change"):
            functies_change()
        elif (funct == "clear"):
            leeg_scherm()
        elif (funct == "test"):
            functies_test()
        elif(funct == "overhoor"):
            antiLoop = False
            lijst = {}
            functies_overhoor(antiLoop, lijst)
        elif(funct == "del"):
            functies_delete0()
    else :
        functies_end()


def functies_read():
    leeg_scherm()
    while (check["read"] == True):
            with open(fileName, "r") as b:
                line = b.readlines()
                print("+" + "~"*(schermbreedte - 2) + "+")
                print("| {:^56} |".format("Welke regel?"))
                print("| {:^56} |".format("[Alles/[getal]] of om te stoppen [esc/stop] : "))
                print("+" + "~"*(schermbreedte - 2) + "+")
                regel = input()
                if (regel == "esc" or regel == "stop" or regel == "q" or regel == "Q"):
                    check["read"] = False
                    begin_code()
                elif (regel == "alles"):
                    leeg_scherm()
                    for i, value in enumerate(line,1):
                        print(i, value)
                    check["read"] = False
                    herstart = input("")
                    begin_code()
                if (regel.isnumeric()):
                    regel2 = int(regel)
                    leeg_scherm()
                    print(line[regel2-1])
                    check["read"] = False
                    herstart = input("")
                else:
                    print("false")
                    check["read"] = False
                    input()
                    begin_code()

def functies_delete1():
    leeg_scherm()
    print("+" + "~"*(schermbreedte - 2) + "+")
    print("| {:<10}{:<46} |".format("lijst: ", fileName))
    print("|" + "-"*(schermbreedte - 1))
    print("| {:>58}".format("|"))
    print("| {:^56} |".format("Wilt u een woord verwijderen? "))
    print("| {:^56} |".format("Y / N"))
    print("+" + "~"*(schermbreedte - 2) + "+")
    del_vrg = input("")
    return(del_vrg)

def functies_delete2():
    leeg_scherm()
    print("+" + "~"*(schermbreedte - 2) + "+")
    print("| {:<10}{:<46} |".format("lijst: ", fileName))
    print("|" + "-"*(schermbreedte - 1))
    print("| {:>58}".format("|"))
    print("| {:^56} |".format("Woord moet in de lijst zitten"))
    print("| {:^56} |".format("Welk woord wilt u verwijderen?"))
    print("+" + "~"*(schermbreedte - 2) + "+")
    del_wrd = input("")
    return(del_wrd)

def functies_toev():
    lijst = lijst_maken()
    toev_wrd = fnct_toev1()
    
    if (toev_wrd == "Y" or toev_wrd == "y"):
        nieuw_wrd = nieuw_wrd1()
        vrtl_nwrd = nieuw_wrd2()
        
        lijst[nieuw_wrd] = vrtl_nwrd
        
        with open(fileName, "r+") as fnct_tv:
            fnct_tv.truncate(0)
            for i in lijst:
                fnct_tv.write(i + " " + lijst[i] + "\n")

    elif (toev_wrd == "N" or toev_wrd == "n"):
        begin_code()

    elif (toev_wrd == "q" or toev_wrd == "Q"):
        begin_code()

def nieuw_wrd1():
        leeg_scherm()
        print("+" + "~"*(schermbreedte - 2) + "+")
        print("| {:<56} |".format("Wat woord wilt u toevoegen? "))
        print("+" + "~"*(schermbreedte - 2) + "+")
        nieuw_wrd = input("")
        return(nieuw_wrd)

def nieuw_wrd2():
        leeg_scherm()
        print("+" + "~"*(schermbreedte - 2) + "+")
        print("| {:<56} |".format("Wat is de vertaling? "))
        print("+" + "~"*(schermbreedte - 2) + "+")
        nieuw_wrd = input("")
        return(nieuw_wrd)

def fnct_toev1():
    leeg_scherm()
    print("+" + "~"*(schermbreedte - 2) + "+")
    print("| {:<10}{:<46} |".format("lijst: ", fileName))
    print("|" + "-"*(schermbreedte - 1))
    print("| {:>58}".format("|"))
    print("| {:^56} |".format("Wilt u een woord toevoegen? "))
    print("| {:^56} |".format("Y / N"))
    print("+" + "~"*(schermbreedte - 2) + "+")
    toev_wrd = input("")
    return(toev_wrd) 
    
def functies_maak():
    global fileName
    leeg_scherm()
    print("+" + "~"*(schermbreedte - 2) + "+")
    nieuwBestand = print("| {:^56} |".format("Hoe moet het nieuwe bestand heten?"))
    print("+" + "~"*(schermbreedte - 2) + "+")
    nieuwBestand = input()
    fileName = nieuwBestand + ".txt"
    create = open(fileName,"w+")
    leeg_scherm()
    print("+" + "~"*(schermbreedte - 2) + "+")
    print("| {:^56} |".format("Het bestand " + fileName + " is aangemaakt"))
    woordenlijst = fileName
    print("| {:^56} |".format("Woordenlijst is veranderd naar " + fileName))
    print("+" + "~"*(schermbreedte - 2) + "+")
    input()
    begin_code()

def functies_change():
    leeg_scherm()
    global fileName
    global change_tester
    print("+" + "~"*(schermbreedte - 2) + "+")
    print("| {:^56} |".format("We gebruiken op dit moment file = " + fileName))
    print("| {:^56} |".format("Wil je het veranderen ? ja / nee "))
    print("+" + "~"*(schermbreedte - 2) + "+")
    question = input("")
    
    if (question == "ja"):
        leeg_scherm()
        print("+" + "~"*(schermbreedte - 2) + "+")
        print("| {:^56} |".format("Naar welk bestand wil je het veranderen ?"))
        print("+" + "~"*(schermbreedte - 2) + "+")
        change = input()
        change_tester = os.path.isfile(change + ".txt")   #test of de file bestaat
        if (change_tester == True):
            fileName = change + ".txt"
        else:
            print("+" + "~"*(schermbreedte - 2) + "+")
            print("| {:^56} |".format("file bestaat niet"))
            print("+" + "~"*(schermbreedte - 2) + "+")
            input("")
    elif (question == "nee"):
        print("+" + "~"*(schermbreedte - 2) + "+")
        print("| {:^56} |".format("Dan gaan we nu terug naar het begin"))
        print("+" + "~"*(schermbreedte - 2) + "+")
        begin_code()

def leeg_scherm():
    print("\n" * 40)

def functies_end():
    leeg_scherm()
    print("+" + "~"*(schermbreedte - 2) + "+")    
    print("| {:<56} |".format("Stopping code"))
    print("+" + "~"*(schermbreedte - 2) + "+")    
    funct = "esc"
    exit()

def functies_overhoor(antiLoop, lijst):
    question = ""
    restart = ""
    overhoor = True
    global counter
    global kansen
    
    leeg_scherm()
    for i in range(1):
        lijst = lijst_maken()
        i += 1
    
    if (overhoor == True):
        starten = phase_begin()
        counter = 0
        kansen = 5
        
        if (starten == "Y" or starten == "y"):
            for i in lijst:
                if (kansen == 0):
                    leeg_scherm()
                    GAMEOVER()
                    return()

                antwoord = phase_one(i)
                if(antwoord == "q" or antwoord == "Q"):
                    return()
                
                elif (antwoord == lijst[i]):
                    counter = phase_two(i, counter, lijst)
                        
                elif (antwoord != lijst[i]):
                    kansen = phase_three(i, kansen, lijst)
                
                else:
                    print("Error - overhoor 3")

            phase_end()
            
        elif (starten == "N" or starten == "n"):
            leeg_scherm()
            print("+" + "~"*(schermbreedte - 2) + "+")
            input("| {:^56} |".format("We gaan nu terug naar het startmenu "))
            print("+" + "~"*(schermbreedte - 2) + "+")
            begin_code()
        else:
            print("Error - overhoor 2 ")
    else:
        print("Error - overhoor 1 ")


def GAMEOVER():
    print("+" + "~"*(schermbreedte - 2) + "+")
    print("| {:<10}{:<46} |".format("lijst: ", fileName))
    print("|" + "-"*(schermbreedte - 1))
    print("| {:^56} |".format("GAME OVER"))
    print("| {:^56} |".format("punten: " + str(counter)))
    print("| {:^56} |".format("kansen " + str(kansen)))
    print("+" + "~"*(schermbreedte - 2) + "+")
    print("| {:^56} |".format("kansen zijn op"))
    print("+" + "~"*(schermbreedte - 2) + "+")
    input("")
    return()

def phase_one(i):
    #vertaal woord
    leeg_scherm()
    print("+" + "~"*(schermbreedte - 2) + "+")
    print("| {:<10}{:<46} |".format("lijst: ", fileName))
    print("|" + "-"*(schermbreedte - 1))
    print("| {:^56} |".format("woord:  " + i))
    print("| {:^56} |".format("punten: " + str(counter)))
    print("| {:^56} |".format("kansen " + str(kansen)))
    print("+" + "~"*(schermbreedte - 2) + "+")
    antwoord = input("Wat is de vertaling: ")
    return(antwoord)

def phase_two(i, counter, lijst):
    #Goede antwoorden 
    leeg_scherm()
    counter += 1
    print("+" + "~"*(schermbreedte - 2) + "+")
    print("| {:<10}{:<46} |".format("lijst: ", fileName))
    print("|" + "-"*(schermbreedte - 1))
    print("| {:^56} |".format("woord:  " + lijst[i]))
    print("| {:^56} |".format("punten: " + str(counter)))
    print("| {:^56} |".format("kansen " + str(kansen)))
    print("+" + "~"*(schermbreedte - 2) + "+")
    input("")
    return(counter)

def phase_three(i, kansen, lijst):
    #Foute antwoorden 
    leeg_scherm()
    kansen -= 1
    print("+" + "~"*(schermbreedte - 2) + "+")
    print("| {:<10}{:<46} |".format("lijst: ", fileName))
    print("|" + "-"*(schermbreedte - 1))
    print("| {:^56} |".format("woord:  " + lijst[i]))
    print("| {:^56} |".format("punten: " + str(counter)))
    print("| {:^56} |".format("kansen " + str(kansen)))
    print("+" + "~"*(schermbreedte - 2) + "+")
    input("")
    return(kansen)

def phase_end():
    #einde 
    leeg_scherm()
    print("+" + "~"*(schermbreedte - 2) + "+")
    print("| {:^56} |".format("Je bent nu klaar"))
    print("| {:^56} |".format("Dit is jouw score: " + str(counter)))
    print("| {:^56} |".format("Dit zijn jouw overgebleven levens: " + str(kansen)))
    print("+" + "~"*(schermbreedte - 2) + "+")
    input("| {:^56} |".format("We gaan nu terug naar het startmenu "))
    print("+" + "~"*(schermbreedte - 2) + "+")
    begin_code()

def phase_quit():
    return()

def phase_begin():
        overhoor = False
        leeg_scherm()
        print("+" + "~"*(schermbreedte - 2) + "+")
        print("| {:<10}{:<46} |".format("lijst: ", fileName))
        print("| ")
        print("| ")
        print("+" + "~"*(schermbreedte - 2) + "+")
        starten = input("Starten met overhoring? Y/N :  ")
        return(starten)


def lijst_maken():
    lijst = {}
    with open(fileName, "r") as f:
        for line in f:
           (key, val) = line.split()
           lijst[key] = val
    return(lijst)

begin_code()

