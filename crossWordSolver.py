##Stetson Wendel
##Crossword Bot





def main():
    ## Declare Variables
    guess = ""
    result_of_guess = ""
    guessed_it = "n"
    filtered_database = []
    full_word_database = []
    guess_number = 1
    words_removed = 0
    # answer = ""

    ## Create word database.
    full_word_database = create_full_word_db()

    filtered_database = full_word_database
    words_removed = len(filtered_database)
    
    # print(answer)
    # guess = create_guess(full_word_database) will return start switch to stare
    guess = "   d   "
    word_length = 7

    print(guess)
    # result_of_guess = get_results()

    filtered_database = filter_word_len(filtered_database, word_length)

    # while result_of_guess != "ggggg":
        
        
    filtered_database = filter_results(filtered_database, guess, result_of_guess)

        # guess = create_guess(filtered_database)
        # print("\n"+answer)
        # print(guess)
        
        # print(len(filtered_database))
    print("\n",filtered_database)
    guess_number += 1

    result_of_guess = get_results()
        

    print(guess_number)


##filter_word_len
## Filter out the wrong size words.
## Input: Array database, word_len.
## Output: Array filtered_database.
def filter_word_len(database, word_len):

    filtered_database = []

    for i in range(0, len(database)):

        if database[i] == word_len:
            filtered_database.append(database[i])

    return filtered_database



## count_common_word
## Count the letters and their occurrences in each spot.
## Input:Array of strings
## Returns:String
def create_guess (database, guess = "", place = 0):

    ## Define Variables.
    new_db = []
    letter = ""
    letters_and_places = [{},{},{},{},{}]

    ## Nested for loop to iterate through each word.
    ## i cover ever single word.
    for i in range (0,len(database)):

        ## Find common letters.
        letters_and_places[place][database[i][place]]  = incrament_letters(letters_and_places[place], database[i][place]) 

    ## Find the most common letter then add it to guess.
    letter = find_most_common_letter(letters_and_places[place])
    guess += letter

    ## If guess is not finished.
    if place < 4:
        ## Create a new db using the most common letter pattern so far.
        new_db = set_letter_position(database, place, letter)

        ## Incrament place.
        place +=1

        ## Call this funcion again.
        guess = create_guess(new_db, guess, place)
    
    ## Return guess.
    return guess


## create_word_db
## Create a database of all possible words.
## Input: None
## Return: list
def create_full_word_db ():
    ##Declare Variables
    database = []

    ##Open file and read in data
    with open("names.csv") as words_file:

        ##Read in each line
        for line in words_file:

            ##Clean white space
            clean_line = line.strip()

            ##Append data into array
            database.append(clean_line)
    ##End open file


    return database


## filter_results
## Filters the results of the last query.
## Input: list database, str last_guess, str result_of_guess
## Output: list filtered_db
def filter_results(database, last_guess, result_of_guess):

    filtered_db = database

    for i in range(0,len(last_guess)):
        match result_of_guess[i]:
            case "g":
                ## set_letter_query
                filtered_db = set_letter_position(filtered_db, i, last_guess[i])

            case "y":
                ## remove_letter_from_position
                filtered_db = remove_letter_from_position(filtered_db, i, last_guess[i])

                ## remove_words_without_letter
                filtered_db = remove_words_without_letter(filtered_db, last_guess[i])

            case "b":
                ## remove_letter_function
                filtered_db = remove_words_with_letter(filtered_db, last_guess[i])

    return filtered_db


## most_common_letter
## Find and return the most common letter.
## Input: dict letters
## Output: char most_common_letter
def find_most_common_letter(letters):

    ## Declare variables.
    most_common_letter = ""
    times_occurred = 0

    ## Loop through every letter.
    for i in letters:  
        ## See witch letter occurs the most and save it.
        if letters[i] > times_occurred:
            most_common_letter = i
            times_occurred = letters[i]

    ## Return most_common_letter
    return most_common_letter


## results
## Get results from user from last guess.
## Inputs: None
## Output: str result
def get_results():

    ## Declare variables.
    result = ""

    ## Ask user for last result.
    print("What was your last result? answer in G, Y, B.\n")
    result = input("")

    ## Return last result.
    return result


## incrament_letters
## Incrament by one the occurrence of the letter.
## Input: dict letters, char dic_letter
## Output: int +1
def incrament_letters(letters, dic_letter):

    ## If instance already exists increment by 1.
    if dic_letter in letters:

        return letters[dic_letter] +1

    ## If it doesn't exist create and set to one.
    else:

        return 1


## remove_letter_from_position
## Remove words with a letter in a certain position.
## Input: list database, int position, char letter
## Output: list new_db
def remove_letter_from_position(database, position, letter):
    ## Declare variables.
    new_db = []

    ## If a letter doesn't occur in the set place add to the new db.
    for i in range(0, len(database)):
        if database[i][position] != letter:
            new_db.append(database[i])

    ## return new_db
    return new_db


## remove_words_with_letter
## Removes any words with a certain letter.
## Input: list database, char letter
## Output: list new_db
def remove_words_with_letter(database, letter):
    ## Declare variables.
    contains_letter = False
    new_db = []

    ## Iterate through every word in db.
    for i in range(0, len(database)):
        
        ## Set contains_letter to false for each word.
        contains_letter = False

        ## Iterate through every letter in word.
        for j in range(0, len(database[i])):

            ## If letter is in word make true.
            if database[i][j] == letter:
                contains_letter = True

        ## If the letter was in the word add to new db.
        if contains_letter == False:
            new_db.append(database[i])

    ## return new_db
    return new_db


## remove_words_without_letter
## Removes any words without a certain letter.
## Input: list database, char letter
## Output: list new_db
def remove_words_without_letter(database, letter):
    ## Declare variables.
    contains_letter = False
    new_db = []

    ## Iterate through every word in db.
    for i in range(0, len(database)):
        
        ## Set contains_letter to false for each word.
        contains_letter = False

        ## Iterate through every letter in word.
        for j in range(0, len(database[i])):

            ## If letter is in word make true.
            if database[i][j] == letter:
                contains_letter = True

        ## If the letter was in the word add to new db.
        if contains_letter:
            new_db.append(database[i])

    ## return new_db
    return new_db


## set_letter_query
## Create a new db with a letter in a set place.
## Input: list database, int place, char letter
## Output: list new_db
def set_letter_position(database, place, letter):

    ## Declare variables.
    new_db = []

    ## If a letter occurs in the set place add to the new db.
    for i in range(0, len(database)):
        if database[i][place] == letter:
            new_db.append(database[i])

    ## return new_db
    return new_db

print("\n")
main()
print("\n")