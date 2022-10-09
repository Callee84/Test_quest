import random
import images
from time import sleep
import os


# defining the quiz for use under - Sneak - beach

def quiz():
    """
    This function is a quiz which is called in the in the Quest '
    under - Sneak - beach
    """

    print("Welcome then, to my impossible quiz....")
    sleep(1)

    playing = input("Do you feel like you can beat me?\n")
    sleep(1)

    if playing.lower() != "yes":
        quit()

    print("Okey then....")
    sleep(1)
    print("But don't come crying to me when you fail....")
    sleep(1)

    # To keep the right answers from user

    score = 0

    # Questions
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    answer = input("Let's start up with an easy one...  What's 2 + 2?\n")
    sleep(2)
    if answer == "4":
        print("")
        print("Well done! There's some hope after all... ")
        score += 1
    else:
        print("")
        print("Ha! And you thougth you could beat me?")
        sleep(1)
        print("The answer is 4.")
    sleep(1)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

    answer_two = input("What's more, 5 ants or 4 elephants? \n").lower()
    sleep(2)
    if answer_two == "5 ants" or "5" or "ants":
        print("")
        print("Correct, but that wheren't a hard question! ")
        score += 1
    else:
        print("")
        print("Nope, you had a 50% chance and still got it wrong!")
        sleep(1)
        print("The answer was 5 ants.")
    sleep(1)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

    answerThree = input(
        "What was to the left of the bridge you just passed?\n").lower()
    sleep(2)
    if answerThree == "beach":
        print("")
        print("Okey, that's right. But here comes some harder questions! ")
        score += 1
    else:
        print("")
        print("Nope. You're just a lot of talk huh? Not that smart?")
        sleep(1)
        print("The answer was this beach.")

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print("I hope you know you Lord of the rings...")
    sleep(1)
    print("What was the name of the hobbit")
    answerFour = input("who took the ring to Mordor? \n").lower()
    if answerFour == "frodo":
        print("")
        print("Hmmm, still easy questions. Don't get cocky!")
        score += 1
    else:
        print("")
        print("Nope! Well, unleast you're pretty... ")
        sleep(2)
        print("The answer was Frodo.")
    sleep(1)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

    answerFive = input(
        "Last question. A simple one... Who's the best?\n").lower()
    sleep(2)
    if answerFive == "You" or "Me":
        print("")
        print("I'm going to take your answer as you mean me...")
        sleep(2)
        print("And of course that's right!")
        score += 1
    else:
        print("")
        print("What!? NO! The answer is me! I'm the best!")
        sleep(2)

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print("")
    print("Well, you got " + str(score) + " questions right!")

    if score >= 4:
        print("Okey, you got some skill")
        sleep(2)
        print("But since I'm me and it's my game...")
        sleep(2)
        print("You still have to come with me!")
        sleep(2)
        print("I don't cheat! I just changed the rules...")
        sleep(2)
        print("Just like you when you sneaked past my guard at the bridge...")
        sleep(2)
        print("The End....")
        sleep(2)
        end()

    else:
        print("As I thought... ")
        sleep(2)
        print("Not much to say.")
        sleep(2)
        print("Just come with me.")
        sleep(2)
        print("The End...")
        sleep(2)
        end()


print("""

_________          _______    _______           _______  _______ _________
\__   __/|\     /|(  ____ \  (  ___  )|\     /|(  ____ \(  ____ \\__   __/
   ) (   | )   ( || (    \/  | (   ) || )   ( || (    \/| (    \/   ) (   
   | |   | (___) || (__      | |   | || |   | || (__    | (_____    | |   
   | |   |  ___  ||  __)     | |   | || |   | ||  __)   (_____  )   | |   
   | |   | (   ) || (        | | /\| || |   | || (            ) |   | |   
   | |   | )   ( || (____/\  | (_\ \ || (___) || (____/\/\____) |   | |   
   )_(   |/     \|(_______/  (____\/_)(_______)(_______/\_______)   )_(   
                                                                          

""")
sleep(2)

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
name = ""

sleep(1)

while True:
    name = input("What's your name? \n")

    if not name.isalpha():
        print("You can only use letters for your name...")
        continue
    else:
        break

sleep(1)
print("First of all", name, ", I must test your mind")
sleep(2)
print("before I can let you pass through.")
sleep(2)
print("It's an easy test...")
sleep(2)
print("All you have to do i guess this simple word.")
sleep(2)
print("It's only five letters...")
sleep(2)
print("And since I'm such a nice guy, I will let you have 7 guesses...")
sleep(2)
print("Good Luck!")


words = ["sunny", "beach", "river", "enter", "quest", "sneak"]
word = random.choice(words)
word = word.upper()
show_word = list(len(word)*'_')
guesses = 7
survive = False


def hangman(letter, word):
    """
    Function Hangman game to be called at - The talk - beach
    The game should pick a random word from 'words' list.
    And the user has 7 guesses to get it right.
    """

    global show_word
    for i in range(0, len(word)):
        letter = word[i]
        if guess == letter:
            show_word[i] = guess
    if '_' not in show_word:
        return True
    else:
        return False


def status():
    os.system("clear")
    print(images.hangman_stages[7-guesses])
    print(' '.join([str(e) for e in show_word]))
    sleep(1)
    print('You have', guesses, 'guess left...')
    print("")


while survive == False and guesses > 0:
    status()
    guess = input("You can guess a letter or the entire word:\n")
    guess = guess.upper()

    if guess == word:
        survive = True
        show_word = word
    elif len(guess) == 1 and guess in word:
        survive = hangman(guess, word)
    else:
        guesses -= 1
    status()

if survive:
    print("Well done!")
    sleep(1)
    print("I feel confident that you might stand a chance in")
    sleep(2)
    print("the upcoming adventure...")
    sleep(2)
    print("Here we go!")
    sleep(2)
    print("")
else:
    print("That's all your guesses...")
    sleep(2)
    print("Hmmm, if you can't guess a five letter word,")
    sleep(2)
    print("How are going to make it on this impossible andventure?")
    sleep(2)
    print("Well... only one way to find out I guess...")
    sleep(2)
    print("On you go! Good luck", name, "!")
    sleep(2)
    print("By the way, the world I was looking for was", word)
    sleep(2)
    print("Soooooo easy...!")
    sleep(1)
    print("Anyway, here we go!")
    sleep(2)
    print("")


print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("")
sleep(2)
print("This is the tale about an exiting journey across the mythical lands of")
sleep(2)
print("")
print("'PythWorld'.")
print("")
sleep(2)
print("You can cross path with some intresting characters")
sleep(2)
print("and you will have to make some hard choices along your choosen path.")
sleep(2)
print("But be aware... your choices has consequences!\n")
sleep(2)
print("HINT - Be sure to type in your choosen answer,")
sleep(2)
print("which is provided for you in (bracets)")
sleep(2)
print("This in important. If you don't do this, you will lose!")
print("")
sleep(2)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("")
sleep(2)


while True:
    print("Let's go for a walk! You never know what you might find.")
    sleep(1)

    user_input = input(
        "Ready? (yes) or (no) \n").lower()

    if user_input == "yes":
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("Lovely! Let's Go!\n")
        break

    elif user_input == "no":
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("Are you sure? It's really a lovely day!")
        continue
    else:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        sleep(1)
        print("No, No, No. Remember... ")
        sleep(1)
        print("Be sure to type in your choosen answers")
        sleep(1)
        print("who is provided for you in (bracets).")
        sleep(2)
        print("You only get this warning.")
        sleep(2)
        print("Fail this inside the quest and you lose!")
        sleep(2)
        print("Well okey, maybe not lose... But I will be a bit sad....")
        sleep(1)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        continue


def end():
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("So, how did you do?")
        sleep(2)
        print("Did you have to answer some hard questions?")
        sleep(2)
        print("Did you get the treasure?")
        sleep(2)
        print("Or did you even became a god?")
        sleep(2)
        print("Maybe you wish you've picked some other answers?")
        sleep(2)
        print("Well, play again and maybe choose a differnet path.")
        sleep(2)
        print("You might end up somewhere else?")
        break


def home():
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("")
        sleep(1)
        print("You start you journey home again.")
        sleep(1)
        print("With a lot of pain but even more will,")
        sleep(1)
        print("you manage to walk through the forest.")
        sleep(1)
        print("After a while you meet someone familiar -")
        sleep(1)
        print("the guard from the bidge. He asks")
        sleep(1)
        print("-'Do you still have my knife?")
        sleep(1)
        choice_home = input("(Yes) or (no)?\n").lower()
        sleep(1)

        if choice_home == "yes":
            sleep(1)
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("")
            sleep(1)
            print("The guard says 'You passed the test.")
            sleep(1)
            print("As a reward you have earned this treasure!")
            sleep(2)
            print(" Follow this path back and you'll be back home in notime!")
            sleep(2)
            end()
            break

        elif choice_home == "no":
            sleep(1)
            print("Oh well... Hope it come to god use for you.")
            sleep(1)
            print("Just follow this path")
            sleep(1)
            print("and you will be home before you know it.")
            print("All the best!")
            sleep(2)
            end()
            break


def quest():
    print("You start to feel better for a while.")
    sleep(1)
    print("But slowly, as the sun sets,")
    sleep(1)
    print("you start feeling worse and worse.")
    sleep(1)
    print("You are lost and without food.")
    sleep(1)
    print("You lie down and close your eyes....\n")
    sleep(2)
    print("The End...")


def forest_fight():
    while True:

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("After a long fight you manage to fight of the wolf.")
        sleep(1)
        print("But you have sustained injuries.")
        sleep(1)
        print("You try to walk but it hurts.")
        sleep(1)
        choice_forest_fight = input(
            "Do you go (home) or du you continue the (quest)?\n").lower()
        sleep(1)

        if choice_forest_fight == "home":
            sleep(1)
            home()
            break

        elif choice_forest_fight == "quest":
            print(
                "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("")
            sleep(1)
            print("Oh no! Your injuries is really taking it's toll")
            sleep(1)
            print("You try to go on...")
            sleep(1)
            print("You see a man appears out of nowhere. He says")
            sleep(1)
            print("'Hello", name, "'I'm death. It's time to come with me...\n")
            sleep(2)
            print("The End.....")
            sleep(2)
            end()
            break

        else:
            print("No, no, NO! Remember the (brackets)?")
            sleep(2)
            print("Please type you choice of answer or check your spelling...")
            continue


def run():
    print("Oh no....")
    sleep(2)
    print("You really thought you could outrun a wolf?!")
    sleep(2)
    print("I should never have let you in to this quest!")
    sleep(2)
    print("Outrun a wolf.. Ha! You're not Usain Bolt!")
    sleep(2)
    print("Yeah, the quest is over for you.\n")
    sleep(2)
    print("The End....")
    sleep(3)
    end()


def leave():

    while True:

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("You ignore the mushrooms and start walking.")
        sleep(1)
        print(
            "After a while you notice that you're on a path ")
        sleep(1)
        print("you never been on before.")
        sleep(1)
        print("Just when you manage to find the edge of the forest,")
        sleep(2)
        print("you see a wolf.")
        sleep(1)
        print("The wolf is hungry and angry. He attacks you!")
        sleep(1)
        choice_wolf = input(
            "Do you (fight) him of with your knife or do you (run)?\n")

        if choice_wolf == "fight":
            sleep(1)
            forest_fight()
            break

        elif choice_wolf == "run":
            sleep(1)
            run()
            break

        else:
            print("No, no, NO! Remember the (brackets)?")
            sleep(2)
            print("Please type you choice of answer or check your spelling...")
            continue


def lure():
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("The wolf looks at you with his angry eyes.")
        sleep(1)
        print("Just when he's about to attack you he sees the mushrooms")
        sleep(1)
        print("You're in luck, the wolf likes the mushrooms and start eating.")
        sleep(1)
        print("You sneak away and find you way back to the bridge.")
        sleep(1)
        print("The guard however, is not there. So you walk over the bridge.")
        sleep(1)
        print("And stroll down the road to you house.")
        sleep(1)
        print("The End...")
        sleep(1)
        end()
        break


def pick():
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("You picked up the mushrooms")
        sleep(1)
        print("and start to walk to the edge of the forest")
        sleep(2)
        print("When you reach the edge")
        sleep(2)
        print("you see a bench overlooking a fantastic view.")
        sleep(2)
        print("You decide to sit down for a while")
        sleep(2)
        print("and just when you are about eat some of your mushrooms")
        sleep(2)
        print("you see a hungry, angry wolf.")
        sleep(2)
        print("Do you (fight) him of with your knife,")
        sleep(2)
        print("or du you try to (lure) him of")
        sleep(2)
        talk_forest_pick = input(" with some mushrooms?\n").lower()

        if talk_forest_pick == "fight":
            sleep(1)
            forest_fight()
            break

        elif talk_forest_pick == "lure":
            sleep(1)
            lure()
            break

        else:
            print("No, no, NO! Remember the (brackets)?")
            sleep(2)
            print("Please type you choice of answer or check your spelling...")
            continue


def forest():
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("You reach the forest and you come across some mushrooms.")
        sleep(1)
        print("You don't know if these mushrooms are poisones or not")
        sleep(1)
        print("But you are quite hungry after you little walk.")
        sleep(1)
        choice_forest = input(
            "Do you (pick) them up or do you (leave) them?\n").lower()

        if choice_forest == "pick":
            sleep(1)
            pick()
            break

        elif choice_forest == "leave":
            sleep(1)
            leave()
            break

        else:
            print("No, no, NO! Remember the (brackets)?")
            sleep(1)
            print("Please type you choice of answer or check your spelling...")
            continue


def talk_beach():
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("")
        sleep(2)
        print("You get to the lovely beach")
        sleep(2)
        print("and see a man turned away from you.")
        sleep(2)
        print("You say 'Hey mister, what a lovely day'.")
        sleep(2)
        print("the man turns around and...")
        sleep(2)
        print("IT'S DEATH HIMSELF!!! He says, ")
        sleep(2)
        print("-'I've been waiting for you.")
        sleep(2)
        print("But since it's such a lovely day as you say it is,")
        sleep(2)
        print("I will give you a second chance on life. ")
        sleep(2)
        print("Just guess this five letter word.' ")
        sleep(2)
        beach_choice = input("Are you ready? (Yes) or (no) \n").lower()

        if beach_choice == "yes":
            sleep(2)
            quiz()
            break

        elif beach_choice == "no":
            sleep(2)
            print("Death says")
            sleep(1)
            print("-'Well then. I'm glad! You have accepted your faith.")
            sleep(2)
            print("From here on out you shall be known as",
                  name, "God of the fearless!'")
            sleep(2)
            print("Come with me")
            sleep(2)
            print("and take you place among the gods of Pythworld")
            sleep(2)
            print("Your throne and you people hs been waiting for you,")
            sleep(2)
            print("for a long time.")
            sleep(2)
            print("The End")
            end()
            break

        else:
            print("No, no, NO! Remember the (brackets)?")
            sleep(2)
            print("Please type you choice of answer or check your spelling...")
            continue


def sneak_forest_fight():
    while True:

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("You don't stand a chance against the hungry wolf who eats you,")
        sleep(1)
        print("and the mushrooms in seconds...")
        sleep(2)
        print("The End....")
        sleep(1)
        end()
        break


def sneak_pick():

    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(2)
        print("You picked up the mushrooms")
        sleep(2)
        print("and start to walk to the edge of the forest")
        sleep(2)
        print("When you reach the edge")
        sleep(2)
        print("you see a bench overlooking a fantastic view.")
        sleep(2)
        print("You decide to sit down for a while")
        sleep(2)
        print("and just when you are about eat some of your mushrooms")
        sleep(2)
        print("you see a hungry, angry wolf.")
        sleep(2)
        print("Do you (fight) him of,")
        sleep(2)
        print("or du you try to (lure) him of")
        sneak_forest_pick = input("with some mushrooms?\n").lower()

        if sneak_forest_pick == "fight":
            sleep(1)
            sneak_forest_fight()
            break

        elif sneak_forest_pick == "lure":
            sleep(1)
            lure()
            break

        else:
            print("No, no, NO! Remember the (brackets)?")
            sleep(2)
            print("Please type you choice of answer or check your spelling...")
            continue


def sneak_leave():
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(2)
        print("You ignore the mushrooms and star walking.")
        sleep(2)
        print(
            "After a while you notice that you're on a path you never been on before.")
        sleep(2)
        print("Just when you manage to find the edge of the forest you see a wolf.")
        sleep(2)
        print("The wolf is hungry and angry. He attacks you!")
        sleep(2)
        choice_sneak_leave = input("Do you (run) or du you (fight) him off?\n").lower()

        if choice_sneak_leave == "run":
            run()
            break

        elif choice_sneak_leave == "fight":
            sneak_forest_fight()
            break

        else:
            print("Remember, the options you have are inside (brackets).")
            continue


def sneak_beach():

    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("You get to the lovely beach and see a the back of a man.  ")
        sleep(1)
        print("You say 'Hey mister, what a lovely day', the man turns around and...")
        sleep(2)
        print("IT'S DEATH HIMSELF!!! He says, ")
        sleep(2)
        print("-'I've been waiting for you.")
        sleep(2)
        print("But since it's such a lovely day as you say it is,")
        sleep(2)
        print("I will give you a second chance on life. ")
        sleep(2)
        print("Just answer these five simple questions. ")
        sleep(2)
        print("If you get 4 answers right, I let you go free.")
        sleep(2)
        print("If not, you come with me. '")
        sleep(2)
        choice_sneak_beach = input("Are you ready? (Yes) or (no)\n").lower()

        if choice_sneak_beach == "yes":
            sleep(2)
            quiz()
            break

        elif choice_sneak_beach == "no":
            sleep(1)
            print("Well then.. A smart choice. I wouldn't have let you go either way.")
            sleep(1)
            print("")
            sleep(1)
            print("Or would I.....?")
            end()
            break

        else:
            print("Remember, the options you have are inside (brackets).")
            continue


def sneak_forest():
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("You reach the forest and you come across some mushrooms.")
        sleep(1)
        print("You don't know if these mushrooms are poisones or not")
        sleep(1)
        print("But you are quite hungry after you little walk.")
        sleep(1)
        choice_forest_sneak = input(
            "Do you (pick) them up or do you (leave) them?\n").lower()

        if choice_forest_sneak == "pick":
            sleep(1)
            sneak_pick()
            break

        elif choice_forest_sneak == "leave":
            sleep(1)
            sneak_leave()
            break

        else:
            print("No, no, NO! Remember the (brackets)?")
            sleep(1)
            print("Please type you choice of answer or check your spelling...")
            continue


def the_talk():

    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("The guard seems to be in a good mood today and let you pass.")
        sleep(1)
        print("But before he let you go, he gave you a knife and told you")
        sleep(1)
        print("-'Stay away from the beach. It's dangerous!'")
        sleep(1)
        print("Well past the brigde you look to your left and see a (beach)")
        sleep(1)
        print("and to your right you see a (forest).")
        sleep(1)
        talk_choice = input("Where do you go? \n").lower()

        if talk_choice == "beach":
            sleep(1)
            talk_beach()
            break

        elif talk_choice == "forest":
            sleep(1)
            forest()
            break

        else:
            print("Remember, the options you have are inside (brackets).")
            sleep(1)
            continue


def sneak():
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        sleep(1)
        print("Nice call... ")
        sleep(1)
        print("You were able to dodge the guard and sneek over to the other side.")
        sleep(1)
        print("If you look to the right it's a nice (beach)")
        sleep(1)
        print("and to your left there is a (forest).")
        choice_sneak = input("Where do you go from here?\n")

        if choice_sneak == "beach":
            sleep(1)
            sneak_beach()
            break

        elif choice_sneak == "forest":
            sleep(1)
            sneak_forest()
            break

        else:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            sleep(1)
            print("That's not an option.")
            sleep(1)
            print("Remember, the options you have are inside (brackets).")
            sleep(1)
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            continue


# Start of the quest

while True:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("")
    sleep(1)
    print("You come to a river. There's a man guarding the only bridge.")
    sleep(2)
    print(("He looks quite big and almost dangeorus from this far out."))
    sleep(2)
    choiceOne = input(
        "Do you (talk) to the guard or du you try to (sneak) past? \n").lower()

    if choiceOne == "talk":
        sleep(1)
        the_talk()
        break

    elif choiceOne == "sneak":
        sleep(1)
        sneak()
        break

    else:
        print("That's not an option.")
        sleep(1)
        print("Remember, the options you have are inside (brackets).")
        continue


print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("")
sleep(1)
print("So, how did you do?")
sleep(2)
print("Did you have to answer some hard questions?")
sleep(2)
print("Did you get the treasure?")
sleep(2)
print("Or did you even became a god?")
sleep(2)
print("Maybe you wish you've picked some other answers?")
sleep(2)
print("Well, play again and see where the quest will take you this time...")
