import random

class GuessGame:
    def __int__(self, difficulty):
        self.difficulty = difficulty
        self.secret_num = None

    def generate_num(self):
        self.secret_num = random.randint(1,self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {self.difficulty}:"))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print(f"please enter a number between 1 and {self.difficulty}")
            except ValueError:
                print("Invalid input. Please enter a number")

    def compare_result(self, guess):
        if guess == self.secret_num:
            print("congratulations! You have correctly guessed the number!")
            return True
        else:
            print(f"Sorry the correct number was {self.secret_num}. Try again maybe! ")
            return False

    def play(self):
        self.generate_num()
        guess = self.get_guess_from_user()
        return self.compare_result(guess)

