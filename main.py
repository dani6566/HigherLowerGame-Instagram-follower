from art import logo,vs
import random
from Instagram_follower_data import data

print(logo)

compareA = random.choice(data)
compareB = random.choice(data)

if compareA == compareB:
    compareB = random.choice(data)
print(f"Compare A: {compareA['name']},{compareA['description']},from {compareA['country']}")

count_right = 0 

def compare(compareA,compareB):
    global count_right
    fcount_A = compareA['follower_count']
    fcount_B = compareB['follower_count']
    print(vs)
    print(f"Against B: {compareB['name']},{compareB['description']},from {compareB['country']}")
    choose = input("Who has more followers? Type 'A' or 'B': ").upper()
    if fcount_A < fcount_B  and (choose == "B"):
        count_right += 1
        compareA = compareB
        compareB = random.choice(data)
        if compareA == compareB:
            compareB = random.choice(data)
        print("\n"*20)
        print(logo)
        print(f"Compare A: {compareA['name']},{compareA['description']},from {compareA['country']}")
        compare(compareA,compareB)

    elif fcount_A > fcount_B  and(choose == "A"):
        count_right += 1
        compareB = random.choice(data)
        if compareA == compareB:
            compareB = random.choice(data)
       
        print("\n"*20)
        print(logo)
        print(f"Compare A: {compareA['name']},{compareA['description']},from {compareA['country']}")
        compare(compareA,compareB)
    else:
        print(f"Sorry, that's wrong. Final score: {count_right}")

compare(compareA,compareB)