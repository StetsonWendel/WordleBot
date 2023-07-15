##Stetson Wendel
##Wordle Bot







def main():
    ## Declare Variables
    guess = ""
    result_of_guess = ""
    guessed_it = "n"
    filtered_database = []
    full_word_database = []
    least_common_letter_index = 0
    guess_number = 1
    answer = "gamer"
    print(answer)
    ## Create word database.
    full_word_database = create_full_word_db()

    filtered_database = full_word_database

    # letters_and_places = count_letters_in_places(filtered_database)
    # guess = begin_guess_format(letters_and_places)
    # # guess = check_for_duplicates(letters_and_places,guess)
    # least_common_letter_index = find_least_common_letter(letters_and_places, guess)
    # guess = get_real_word(filtered_database, guess, least_common_letter_index)
    guess = "stare"
    print(guess)

    # guess = create_guess(full_word_database) will return start switch to stare
    # guess = "stare"
    # print(guess)

    # guessed_it = input("Was that it? y/n ")

    while result_of_guess != "ggggg":
        

        result_of_guess = get_results()

        filtered_database = filter_results(filtered_database, guess, result_of_guess)
        
        letters_and_places = count_letters_in_places(filtered_database)

        guess = begin_guess_format(letters_and_places)

        # if guess_number < 3:
        #     guess = check_for_duplicates(letters_and_places,guess)

        least_common_letter_index = find_least_common_letter(letters_and_places, guess)

        guess = get_real_word(filtered_database, guess, least_common_letter_index)

        

        

        print(answer)
        guess_number += 1
        print("\n"+guess)

        # guessed_it = input("Was that it? y/n ")
    
    print(guess_number)

def get_real_word(database, guess, least_common_letter_index):
    match_three = False
    real_word_guess = "NONE"
    back_up_guess = "NONE"
    guess_made = False
    match = 0

    for i in database:
        if i == guess:
            real_word_guess = guess
            guess_made = True
    
    if guess_made == False:
        for i in database:


            for j in range(0,len(i)):
                if j != least_common_letter_index and guess[j] == i[j]:
                    match += 1
            
            if match > (len(i) - 1):
                return i

            elif match > (len(i) - 2):
                real_word_guess = i
                match_three = True
            
            elif (match_three == False) and (match > (len(i) - 3)):
                real_word_guess = i

            match = 0              



    return real_word_guess




def begin_guess_format(letters_and_places):

    guess = ""
    # first_letter = ""
    # first_letter_i = 0
    # second_letter = ""
    # second_letter_i = 0
    # new_guess = ""
    # change_made = True

    for i in range(0,len(letters_and_places)):
        guess += find_most_common_letter(letters_and_places[i])

    # new_guess = guess

    # if 
    # while change_made:
    #     change_made = False
    #     guess = new_guess

    #     for i in range(0,len(guess)):
    #         for j in range(0,len(guess)):
    #             if i < j and guess[i] == guess[j]:
    #                 first_letter = guess[i]
    #                 first_letter_i = i
    #                 second_letter = guess[j]
    #                 second_letter_i = j
    #                 new_guess = change_duplicates(letters_and_places,
    #                 first_letter, first_letter_i, second_letter, second_letter_i,
    #                 guess)
    #                 change_made = True
            

    # print(new_guess)
    return guess
    
def check_for_duplicates(letters_and_places, guess):

    first_letter = ""
    first_letter_i = 0
    second_letter = ""
    second_letter_i = 0
    new_guess = guess
    change_made = True



    while change_made:
        change_made = False
        guess = new_guess

        for i in range(0,len(guess)):
            for j in range(0,len(guess)):
                if i < j and guess[i] == guess[j]:
                    first_letter = guess[i]
                    first_letter_i = i
                    second_letter = guess[j]
                    second_letter_i = j
                    new_guess = change_duplicates(letters_and_places,
                    first_letter, first_letter_i, second_letter, second_letter_i,
                    guess)
                    change_made = True

    return new_guess




def change_duplicates(letters_and_places, first_letter, first_letter_i,
 second_letter, second_letter_i, guess):

    # print(first_letter_i, first_letter)
    # print(letters_and_places[first_letter_i])
    if first_letter in letters_and_places[first_letter_i]:
        num_first_letter = letters_and_places[first_letter_i][first_letter]
    else: 
        num_first_letter = 0
    
    if second_letter in letters_and_places[second_letter_i]:
        num_second_letter = letters_and_places[second_letter_i][second_letter]
    else:
        num_second_letter = 0
    new_letter = ""
    new_letter_i = ""
    new_guess = ""

    if num_first_letter > num_second_letter:
        if num_second_letter != 0:
            del letters_and_places[second_letter_i][second_letter]

        new_letter = find_most_common_letter(letters_and_places[second_letter_i])
        new_letter_i = second_letter_i

    
    else: 
        if num_first_letter != 0:
            del letters_and_places[first_letter_i][first_letter]
        new_letter = find_most_common_letter(letters_and_places[first_letter_i])
        new_letter_i = first_letter_i

    for i in range(0,len(guess)):
        if i != new_letter_i:
            new_guess += guess[i]
        else:
            new_guess += new_letter


    return new_guess



## find_least_common_letter
## Find and return the most common letter.
## Input: dict letters
## Output: char most_common_letter
def find_least_common_letter(letters_and_places, guess):
    # print(letters_and_places)
    ## Declare variables.
    least_common_letter_index = 0
    times_occurred = letters_and_places[0][guess[0]]

    ## Loop through every letter.
    for i in range(0,len(letters_and_places)):  
        ## See witch letter occurs the most and save it.
        if letters_and_places[i][guess[i]] < times_occurred:
            least_common_letter_index = i
            times_occurred = letters_and_places[i][guess[i]]

    # print(guess[least_common_letter_index], times_occurred, least_common_letter_index)
    ## Return most_common_letter
    return least_common_letter_index









def clean_dict(letters_and_places, total_words):
    bad_data_keys = []
    ten_percent = total_words * .05

    for i in range(0,len(letters_and_places)):
        for j in letters_and_places[i]:

            if letters_and_places[i][j] < ten_percent:
                bad_data_keys.append(j)
        
        
        for j in range(0,len(bad_data_keys)):
            del letters_and_places[i][bad_data_keys[j]]
        
        bad_data_keys.clear()

    return letters_and_places

       
## count_common_word
## Count the letters and their occurrences in each spot.
## Input:Array of strings
## Returns:String
def count_letters_in_places (database):

    ## Define Variables.
    guess = ""
    letters_and_places = [{},{},{},{},{}]

    ## Nested for loop to iterate through each word.
    ## i cover ever single word.
    for i in range (0,len(database)):
        for j in range(0,len(database[i])):
            
            # if j < 4:
            #     letter_pair = database[i][j] + database[i][j + 1]
            #     letters_and_places[j][letter_pair]  = incrament_letters(letters_and_places[j], letter_pair)

            
            ## Find common letters.
            letters_and_places[j][database[i][j]]  = incrament_letters(letters_and_places[j], database[i][j]) 

    # letters_and_places = clean_dict(letters_and_places, len(database))   


    return letters_and_places


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


## find_most_common_letter
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

    # print(most_common_letter, times_occurred)
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