from operator import truediv
import getpass



print("Quiz Time")
print("1.ask")
print("2.pass")
print("3.change_question")
print("4.I know the answer")
print("t.Exit")

while True:
    choice = input("Enter choice (1/2/3/4) ")
    
    if choice == '1':
        question = input("Insert your question")
        answer = getpass.getpass("Inserisci la risposta alla domanda")
        point = answer

    elif choice == '2':
        print("What you want to do? ")
        choice 
    elif choice == '3':
        print("You want to change question? ")
        if choice == 'yes':
            question
    elif choice == '4':
        answer = input("Do you know the answer? ")
        if answer == point:
            print("CONGRATULATION YOU ARE RIGHT!!!!")
        else:
            print("SORRY MAYBE NEXT TIME :(")
        next_game = input("you want to play again? ")

        if next_game == "no":
            print("See youuuu")
            break
        
