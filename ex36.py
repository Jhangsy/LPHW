# Exercise 36
from sys import exit

def kiss():
    print """
    You write several good lover letters.
    She is willing to walking aroung with you.
    But she need some courage to accept you and herself.
    You are sitting under a tree. How tender the night. How beartiful the girl.
    Kiss her?
    """

    while True:
        choice = raw_input('> ')
        if choice == "yes":
            print """
            Good job. She loves you. You 're being together in the end.
            And You get married and have 3 kids.
            You spend a happy life together till death seperates you."""

            exit(0)

        else:
            print "Hey man, you know love needs courage. Try again!"


def love_letter():
    print "You've knowed her for a while. But she seems not be into you."
    print "Do you want to write a love letter for her?"
    choice = raw_input('> ')

    if choice == "yes":
        print "what do you want to tell her?"
        words = raw_input('> ')
        kiss()
    else:
        print "You lost the only love of your life."
        exit(0)


def pick():
    print "You met a beatiful girl. Do you want to talk to her ?"
    i = 1
    while True:
        choice = raw_input('> ')

        if choice == "yes":
            print "'Hi, nice to meet you.' you said and you introduce yourself. "
            print "Nice! Good for you! You get the beatiful girl's name and phone number."
            love_letter()
        elif choice == "no" and i < 3:
            print "Are you sure ? She is so charming that you can't even move."
            i += 1
        elif choice == "no" and i == 3:
            print "You don't know what you are missing."
            print "You spend your whole life lonely."
            exit(0)
        else:
            print "You 're a little hesitate."


def start():
    print "This might be the most import day of your life."
    pick()


start()
