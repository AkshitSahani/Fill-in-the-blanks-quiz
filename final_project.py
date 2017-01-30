#Create three different quizzes, one for each difficulty.
easy_quiz = "__1__ are sequences of anything, just as strings are seuqences of characters. __2__ loops can be used to iterate through each element in a list, making it easier to do so than using a while loop. __3__ are simply assigned memory locations to store any kind of values. __4__ lists can have one or more lists inside them, while __4__ loops can also have one or more loops inside them."
medium_quiz = "A specific kind of loop is a __1__ loop, which repeats a statement or group of statements while a given condition is TRUE. A loop statment can be terminated by the __2__ command, which moves execution to the statement immediately following the __2__ command. __3__ are among the most widely seen types of elements in Python. They can be created by simply enclosing characters within quotes. The list.append() function does __4__ the list instead of creating a new one, unlike the + function which doesn't __4__, but creates a new list."
hard_quiz = "The value of operands can be manipulated by constructs called __1__. Let's consider the expression 2 + 3 = 5. Here, + is called the operator while 2 and 3 are called __2__. Any function block contains the function name and parentheses but always begins with the keyword __3__. __4__ is an object-oriented, interactive and high-level programming language that was used for this project. It was created by Guido van Rossum."

blank_num = ['__1__','__2__','__3__','__4__'] # Create a list of all the blank numbers that will be seen in each version of the quiz (easy, medium or hard)

answers_easy = ['lists','for','variables','nested'] #Create a list of answers each corresponding to the level of difficults
answers_medium = ['while','break','string','mutate']
answers_hard=['operators','operands','def','python']

#Create a game difficulty function that asks for user input and depending on that gives the correct quiz to play.
def game_difficulty(player_input):
    if player_input=="easy":
        return easy_quiz
    if player_input=="medium":
        return medium_quiz
    if player_input=="hard":
        return hard_quiz

#Create an answer difficulty function which uses the correct list of answers to check according to the quiz difficulty chosen.
def answer_difficulty(player_input):
    if player_input=="easy":
        return answers_easy
    if player_input=="medium":
        return answers_medium
    if player_input=="hard":
        return answers_hard

#Gives prompt to player for difficulty level, followed by intended max no. of attempts. Then prints the quiz chosen
#and asks for user input to substitute for blank from list blank_num. If user input matches the designated index on
#the correct answers list, the player answer is used to replace the blank, followed by prompt for next blank. If incorrect, player
#is prompted to try again, for a max number of times as he/she has chosen at the beginning. If they reach the max number of tries,
#program shuts down saying they failed.
def play_quiz():
    print "Welcome to Akshit Sahani's fill-in-the-blanks quiz. Good luck! :)"

    player_input = raw_input("What difficulty would you like to play? Type easy, medium or hard to continue.")

    print game_difficulty(player_input)

    max_tries = int(raw_input("How many maximum attempts would you like?"))

    quiz = game_difficulty(player_input)

    answers = answer_difficulty(player_input)

    min_tries = 0

    beginning_index_of_blank_num = 0

    for i in range(beginning_index_of_blank_num, len(blank_num)):
        index = "__" + str(i + 1) + "__"
        correct = False
        while (correct == False):
            if (max_tries <= min_tries):
                print "Too many incorrect attempts. You Lose!"
                return
            input = raw_input("What should be substituted in for: " + index)
            if answers[i] == input:
                correct = True
                print "Correct! Good job."
                quiz = quiz.replace(index, input)
                print quiz
            else:
                print "Wrong answer! Try again!"
                max_tries = max_tries-1

play_quiz()
