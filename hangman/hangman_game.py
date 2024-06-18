import random

class HangmanGame:
    def __init__(self, secret_word:str, lives_left:int):
        self.secret_word:str = secret_word
        self.lives_left:int= lives_left
        self.suggested_letters = []

    def assess_guess(self, guessed_letter:str)-> None:
        if guessed_letter in self.secret_word:
            print("Your guessed letter is in the secret word.")
        else:
            print(f"{guessed_letter} is not in the secret word.")
            self.lives_left -= 1

    def get_guess(self)->str:
        while True:
            guess:str = input("Enter your letter: ").lower()
            if len(guess) > 1:
                print("Only one letter allowed.")

            elif guess== " ":
                print("Invalid input.Try again !")

            elif not guess.isalpha():
                print("Invalid input. Please enter JUST LETTER!")

            elif guess in self.suggested_letters:
                print("Already guessed that letter.")
            else:
                self.suggested_letters.append(guess)
                return guess

    def draw_hangman(self)-> None:

        chances:int = self.lives_left
        if chances == 6:
            print("______________")
            print("|            |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
        elif chances == 5:
            print("______________")
            print("|            |")
            print("|            O")
            print("|")
            print("|")
            print("|")
            print("|")
        elif chances == 4:
            print("______________")
            print("|            |")
            print("|            O")
            print("|            |")
            print("|")
            print("|")
            print("|")
        elif chances == 3:
            print("______________")
            print("|            |")
            print("|            O")
            print("|           /|")
            print("|")
            print("|")
            print("|")
        elif chances == 2:
            print("______________")
            print("|            |")
            print("|            O")
            print("|           /|\\")
            print("|")
            print("|")
            print("|")
        elif chances == 1:
            print("______________")
            print("|            |")
            print("|            O")
            print("|           /|\\")
            print("|           /")
            print("|")
            print("|")
        elif chances == 0:
            print("______________")
            print("|            |")
            print("|            O")
            print("|           /|\\")
            print("|           / \\")
            print("|")
            print("|")


class HangmanGame_Display:
    @staticmethod
    def display(secret_word:str, suggested_letters:str):
        display_word:list[str]= []

        for letter in secret_word:
            if letter in suggested_letters:
                display_word.append(letter)
            else:
                display_word.append("_")

        return " ".join(display_word)

def play_game():
    random_word:list[str] = ['becode', 'learning', 'mathematics', 'sessions']
    secret_word:str = random.choice(random_word)
    lives_left:int = 7
    print(f"you started with {lives_left} lives ")
    print("______________")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")

    game = HangmanGame(secret_word, lives_left)
    display = HangmanGame_Display()

    while True:
        current_display:str = display.display(game.secret_word, game.suggested_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You found the word.")
            break

        if game.lives_left == 0:
            game.draw_hangman()
            print(f"Game over! The secret word was {secret_word}.")
            break

        game.draw_hangman()
        guessed_letter:str= game.get_guess()
        game.assess_guess(guessed_letter)

play_game()
