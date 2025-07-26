# ---------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D):")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        
    display_score(correct_guesses, guesses)
#--------------------------------------------------------
def check_answer(answer,guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
# -----------------------------------------------
def display_score(correct_guesses, guesses):
    print("-----------------------------------")
    print("RESULT")
    print("----------------------------------")
    print("Answer: ", end = " ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print("Your score is: "+str(score)+"%")


def play_again():
    response = input("Do you want play again?  (yes/no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
    # ---------------------------------------------------------------
questions = {
    "Who is the mighty hunter before the Lord according to Genesis 10:9?   ": "D",
    "We should set our eye on things that are ______________ according 1 corinthians 4:18?  ": "A",
    "Where can this statement be found in the Bible , Therefore do not loose heart, Though outwardly we are wasting away,yet inwardly we are being renewed day by day ?   ": "C",  
    "Who made  this Statement, Naked i came from my  mother womb and naked i will depart the lord gave and the lord takes may the name of the lord be praised?  ": "D"
    
}

options = [["A.Abraham", "B. Noah", "C. Lamech",  "D. Nimrod" ],
           ["A. Unseen Things ", "B. The eternal things", "C. Spiritual things", "D. The Heavenly things."],
           ["A.  1 Corinthians 4:12", "B. 1 Corinthians 4:14", "C. 1 Corinthians 4:16", "D. 1 Corinthians 4:20"],
           ["A. Abraham", "B. Jeremiah", "C. Aristharcus", "D. Job"]]


new_game()
    
while play_again():
    new_game()
print("Byeeeeeee!")