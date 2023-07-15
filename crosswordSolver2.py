

def main():

    word_len = 7
    letter_position = {}


    full_word_database = create_full_word_db()

    word_choices = filter_words(full_word_database, word_len, letter_position)

    print(word_choices)


def filter_words(full_word_database, word_len, letter_position):

    new_database = filter_word_len(full_word_database, word_len)

    new_database = filter_letter_position(new_database, letter_position, word_len)

    return new_database


## filter_word_len
def filter_word_len(full_word_database, word_len):

    ## filter through every word
    for i in range(len(full_word_database)):
        
        new_database = []

        ## compare words to length
        if len(full_word_database[i]) == word_len:

            new_database.append(full_word_database[i])

    return new_database

def filter_letter_position (database, letter_position, word_len):

    new_database = []
        
    for i in range(word_len):
            
        if i in letter_position:

            for j in range(len(database)):

                if database[j][i] == letter_position[i]:

                    new_database.append(database[j])

    return new_database



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




main()