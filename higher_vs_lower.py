from game_data import data
import random

should_continue = True
count = 0
B = random.choice(data)
while should_continue:
    A = B
    B = random.choice(data)
    
    while A == B:
        B = random.choice(data)
    
    def check_answer(user_in , A_followers, B_followers):
        if A_followers > B_followers:
            return user_in == "A"   
        else:
            return user_in == "B"


    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    user_in = input("Who has more followers? Type 'A' or 'B': ").upper()

    A_followers_count = A["follower_count"]
    B_followers_count = B["follower_count"]
    is_correct = check_answer(user_in , A_followers_count, B_followers_count)

 

    if is_correct == True:
        count += 1
        print(f"you're right! Current score: {count}")

    else:
        should_continue = False
        print(f"Sorry, that's wrong, Final score: {count}")



