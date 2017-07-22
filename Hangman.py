#DIY Hangman, by Joshua Curfman
#Guess letters before you run out of chances. Designed as a trial in class object structure. Python 3.6
class DiyHangman():
    #Start up routine, ask if player wishes to play
    def __init__(self):
        print("Are you ready to begin a new game of Hangman? '1':Yes, '2':No")
        choice=int(input("->"))
        if choice==1:
            self.core_game()
        elif choice==2:
            exit()
        else:
            self.__init__()
    #Game Logic.
    def core_game(self):
        import random
        from random import randint
        right_guesses=0
        wrong_guesses=0
        word=self.choose_word("list.txt")
        length=(len(word)-1)
        previous_guesses=""
        progress=["?"]*(length)
        while wrong_guesses<6 and right_guesses<length:
            progress_str="".join(progress)
            guess=input("Please guess a lowercase letter-> ")
            if guess in word and not guess in previous_guesses:
                print("\nCorrect.")
                self.track_letters(word,progress,guess)
                previous_guesses+=", "+guess
                self.hangman_print(wrong_guesses)
                print("Letters used: "+previous_guesses)
                print("Progress: "+"".join(progress))
                new_correct=self.word_complete(word,guess)
                right_guesses+=new_correct
            elif guess not in word and guess not in previous_guesses:
                wrong_guesses+=1
                previous_guesses+=", "+guess
                print("\nSorry, you've guessed wrong.")
                self.hangman_print(wrong_guesses)
                print("Progress: "+progress_str)
                print("Letters used: "+previous_guesses)
            elif guess=="quit":
                wrong_guesses=6
            else:
                print("\nTry again.")
        if right_guesses==length:
            print("\nYou Win!")
            self.__init__()
        elif wrong_guesses==6:
            print("\nYou've lost. Please try again.")
            print("Word was "+word)
            self.__init__()
    #Hangman Printout
    def hangman_print(self, guesses):
        if guesses==0:
            print("________")
            print("|      |")
            print("|       ")
            print("|       ")
            print("|       ")
            print("|       ")
        elif guesses==1:
            print("________")
            print("|      |")
            print("|      0")
            print("|       ")
            print("|       ")
            print("|       ")
        elif guesses==2:
            print("________")
            print("|      |")
            print("|      0")
            print("|     / ")
            print("|       ")
            print("|       ")
        elif guesses==3:
            print("________")
            print("|      |")
            print("|      0")
            print("|     /|")
            print("|       ")
            print("|       ")
        elif guesses==4:
            print("________  ")
            print("|      |  ")
            print("|      0  ")
            print("|     /|\ ")
            print("|         ")
            print("|         ")
        elif guesses==5:
            print("________  ")
            print("|      |  ")
            print("|      0  ")
            print("|     /|\ ")
            print("|     /   ")
            print("|         ")
        else:
            print("________  ")
            print("|      |  ")
            print("|      0  ")
            print("|     /|\ ")
            print("|     / \ ")
            print("|         ")
    #Letter Tracking and Progress
    def track_letters(self, word, progress, guess):
        i=0
        length=len(word)
        while i<length:
            if guess==word[i]:
                progress[i]=guess
                i+=1
            else:
                i+=1
        return "".join(progress)
    #Word Choosing
    def choose_word(self, word_bank):
        from random import randint
        file=open(word_bank,"r")
        num_lines = sum(1 for line in open('list.txt'))
        lines=file.readlines()
        file.close()
        phrase=lines[randint(0,(num_lines-1))]
        file.close()
        return phrase
    #check for word completion
    def word_complete(self, word, guess):
        i=0
        new_correct=0
        length=len(word)
        for i in range(0,length):
            if guess==word[i]:
                new_correct+=1
        return(new_correct)

game = DiyHangman()