import sys
import random

def main():
    print("Welcome to the shit show of practice programs")
    print("A random name generator with confusing choice of names")

    first = ('Baby Oil', 'Bad news', 'Big burps')
    last = ('Appleyard', 'Vinaigrette', 'Woolysocks')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        #print("\n")    
        #Trick IDLE by using "fatal error" setting to print name in red
        print("{} {}".format(first_name,last_name), file=sys.stderr)
        #print("\n")

        try_again = input("\nTry Again? Type n to Exit\n")

        if try_again.lower() == 'n':
            break
if __name__ == "__main__":
    main()
   


