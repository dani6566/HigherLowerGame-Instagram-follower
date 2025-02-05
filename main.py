from art import logo,vs
import random
from Instagram_follower_data import data



print(logo)

compareA = random.choice(data)
compareB = random.choice(data)

print(f"Compare A: {compareA['name']},{compareA['description']},from {compareA['country']}")

count_right = 0 
def fcount_B(choose):
    if choose == 'B':
            count_right += 1
            compareA = compareB
            compareB = random.choice(data)
            print(f"{count_right}")
            print(f"Compare A: {compareA['name']},{compareA['description']},from {compareA['country']}")
            compare(compareA,compareB)
            
    elif choose == 'A':
        print(f"Sorry, that's wrong. Final score: {count_right}")

def compare(compareA,compareB):
    global count_right
    print(vs)
    print(f"Against B: {compareB['name']},{compareB['description']},from {compareB['country']}")
    choose = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    fcount_A = compareA['follower_count']
    fcount_B = compareB['follower_count']
    if fcount_A < fcount_B:
        if choose == 'B':
            count_right += 1
            compareA = compareB
            compareB = random.choice(data)
            print(f"{count_right}")
            print(f"Compare A: {compareA['name']},{compareA['description']},from {compareA['country']}")
            compare(compareA,compareB)
            
        elif choose == 'A':
            print(f"Sorry, that's wrong. Final score: {count_right}")
    else:
        if choose == 'A':
            count_right += 1
            compareB = random.choice(data)
            print(f"{count_right}")
            print(f"Compare A: {compareA['name']},{compareA['description']},from {compareA['country']}")
            compare(compareA,compareB)
            
        elif choose == 'B':
            print(f"Sorry, that's wrong. Final score: {count_right}")

compare(compareA,compareB)