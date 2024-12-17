
import random

user_choice=int(input("enter ur choice: 0 represents rock ,1 represents paper,2 represents scissors"))
print(user_choice)

computer_choice=random.randint(0,2)
print(computer_choice)

if(user_choice==computer_choice):
    print("It is draw")

elif(user_choice>computer_choice):
    print("user wins")
elif(user_choice<computer_choice):
    print("computer wins")
elif(user_choice==0 and computer_choice==2):
    print("user win")
elif(user_choice==2 and computer_choice==0):
    print("computer wins")
else:
    print("game over")