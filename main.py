import random
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def intro():
    slow_print("WELCOME TO ESCAPE HUNT GAME")
    slow_print("You are locked inside a mysterious terminal room.")
    slow_print("Solve 3 puzzles to escape.\n")


def puzzle_1():
    slow_print("PUZZLE 1: Number Lock")
    num = random.randint(1, 10)
    attempts = 3
    
    slow_print("Guess the correct number between 1 and 10")
    
    while attempts > 0:
        guess = int(input("Your guess: "))
        if guess == num:
            slow_print("Correct! Door unlocked part 1.\n")
            return True
        else:
            attempts -= 1
            slow_print(f"Wrong! Attempts left: {attempts}")
    
    slow_print("Failed puzzle 1. Game Over.")
    return False


def puzzle_2():
    slow_print("PUZZLE 2: Word Decode")
    words = {
        "PYTHON": "A popular programming language",
        "DEBUG": "Finding and fixing errors",
        "LOOP": "Repetition structure in coding"
    }
    
    word, hint = random.choice(list(words.items()))
    slow_print(f"Hint: {hint}")
    
    answer = input("Decode the word: ").upper()
    
    if answer == word:
        slow_print("Correct decode! System access granted.\n")
        return True
    else:
        slow_print("Wrong decode. Game Over.")
        return False


def puzzle_3():
    slow_print("FINAL PUZZLE: Secret Password")
    password = "QERA"
    
    slow_print("Clue: This is the name of a powerful AI assistant system.\n")
    
    attempt = input("Enter password: ").upper()
    
    if attempt == password:
        slow_print("ACCESS GRANTED. YOU ESCAPED SUCCESSFULLY!")
        return True
    else:
        slow_print("Wrong password. Locked forever.")
        return False


def game():
    intro()
    
    if not puzzle_1():
        return
    if not puzzle_2():
        return
    puzzle_3()

if __name__ == "__main__":
    game()
