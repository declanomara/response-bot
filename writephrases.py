import sys
print("--Phrase/Response Setup Tool--")

def load_phrases(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]

    phrases = {}
    for line in lines:
        search, phrase = line.split(';')
        phrases[search] = phrase.strip()

    return(phrases)

def print_phrases(phrases):
    print("Currently responding to these phrases:\n")
    for phrase, response in phrases.items():
        print(f"    Phrase:{phrase}")
        print(f"    Response:{response}")
        print("")

def write_phrases(filename):
    done = False
    while(not done):
        with open(filename, 'a') as f:
            phrase = str(input("Enter a search phrase: "))
            response = str(input("Enter a corresponding response: "))
            f.write(phrase + "; " + response + "\n")

            choice = str(input("Add more? (Y/N)"))
            if(choice.lower() != "y"):
                done = True

def new_file(filename):
    with open(filename, 'w+') as f:
        f.write("")

def menu():
    print('''

    What would you like to do?
    (1) List phrases
    (2) Add phrases
    (3) Create new file (useful if bot is broken)
    (4) Quit''')

    choice = int(input())

    if(choice == 1):
        print_phrases(load_phrases('responses.txt'))
        #input("Press any key to continue...")
        menu()

    elif(choice == 2):
        write_phrases('responses.txt')
        menu()

    elif(choice == 3):
        new_file('responses.txt')
        write_phrases('responses.txt')
        menu()

    elif(choice == 4):
        sys.exit("Goodbye.")
    else:
        print("[ERROR] Input Error")
        menu()

menu()
