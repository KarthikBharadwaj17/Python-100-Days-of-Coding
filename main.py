import random
from hangman_words import word_list
from hangman_art import logo,stages

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)
display = []
lives = 6

for i in range(len(chosen_word)):
    display.insert(i, "_")

user_guess = ""
end_of_game = False
while end_of_game == False:
    user_guess = input("Guess the letter: ")

    if user_guess in display:
        print(f"You have already guessed {user_guess}")
    
    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            display[i] = user_guess

    if user_guess not in chosen_word:
        if user_guess not in chosen_word[i]:
            print(f"You guessed {user_guess}, that's not in this word. You lose a life")
        lives -= 1
        print(stages[lives])

        if lives == 0:
            end_of_game = True
            print("You Lose")
    
    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(f"{' '.join(display)}")
    
    

   

   



    







    
