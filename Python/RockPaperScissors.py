import random as ran

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

values={1:"Rock",2:"Paper",3:"Scissors"}

def user_input():
    '''To get user choce'''
    print("Enter your choice from below\n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    return int(input("Enter your choice: "))
    
def comp_input():
    '''Computer genrated random choice'''
    return ran.randint(1,3)

while True:
    user_choice=user_input()
    if user_choice not in (1,2,3):
        print(str(user_choice) + " is not a valid choice")
        continue
    comp_choice=comp_input()
    print("User select "+values[user_choice]+" and Computer select "+values[comp_choice])
    if user_choice==comp_choice:
        print(values[user_choice]+" VS "+values[comp_choice]+"\n==> It's a tie! <==")
    elif user_choice==2 and comp_choice==1:
        print(values[user_choice]+" VS "+values[comp_choice]+"\n==> User WIN!!! <==")
    elif user_choice==1 and comp_choice==3:
        print(values[user_choice]+" VS "+values[comp_choice]+"\n==> User WIN!!! <==")
    elif user_choice==3 and comp_choice==2:
        print(values[user_choice]+" VS "+values[comp_choice]+"\n==> User WIN!!! <==")
    else:
        print(values[user_choice]+" VS "+values[comp_choice]+"\n==> Computer WIN!!! <==")
    # Ask if the user wants to play again
    print("Press ENTER to play again? or any other key to STOP)")
    ans = input().lower()
    if ans != "":
        break

print("Thanks for playing!")