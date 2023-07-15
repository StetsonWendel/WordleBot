import random
import wordelBotTwo
import wordelBotOne

def main(bot_num):
    guesses_taken = 0
    all_guesses_taken = 0
    fails = 0
    failed_words = []
    num_guess_avg = 0
    

    db = create_full_word_db()
    CASES = len(db)

    for i in range(0,CASES):
        
        # rand_word = random.choice(db)
        rand_word = db[i]

        guesses_taken = bot_num.main(rand_word)

        if guesses_taken > 6:
            fails += 1
            all_guesses_taken += 7
            if rand_word not in failed_words:
                failed_words.append(rand_word)
        else:
            if rand_word in failed_words:
                print(rand_word,"guessed")

            all_guesses_taken += guesses_taken
    
    num_guess_avg = all_guesses_taken / CASES
    print("\n"+str(bot_num))
    print(f"On average it took {round(num_guess_avg,3)} guesses.")
    print(f"With {fails} failed attempts {round(fails / CASES, 4)}% failier.")
    print(failed_words)
    return(failed_words)






    


## create_word_db
## Create a database of all possible words.
## Input: None
## Return: list
def create_full_word_db ():
    ##Declare Variables
    database = []

    ##Open file and read in data
    with open("6_letter_words.csv") as words_file:

        ##Read in each line
        for line in words_file:

            ##Clean white space
            clean_line = line.strip()

            ##Append data into array
            database.append(clean_line)
    ##End open file


    return database

print("\n")

failed_words_one = main(wordelBotOne)
failed_words_two = main(wordelBotTwo)
shared = []
in_one = []
in_two = []

for i in failed_words_one:

    if i in failed_words_two:
        shared.append(i)
    else:
        in_one.append(i)

for i in failed_words_two:
    if i not in failed_words_one:
        in_two.append(i)

print("Shared: ", shared)
print("One: ", in_one)
print("Two: ", in_two)
        
            
print("\n")