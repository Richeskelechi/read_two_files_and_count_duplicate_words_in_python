# Defining a function to read the two files.
def reading_the_two_files(fileone, filetwo):
    # i created a list where I will store the two files I want to read.
    word_container = []
    with open(fileone) as f1:
        # once the file is opened I want to read from the file and store the strings in a variable called contents
        content1 = f1.read()
        # here I am add the content of the file to the list called word_container
        word_container.append(content1)
    with open(filetwo) as f2:
        # once the file is opened I want to read from the file and store the strings in a variable called contents
        content2 = f2.read()
        # here I am add the content of the file to the list called word_container
        word_container.append(content2)
    # here I am returning the word_container to be used in another function.
    return word_container

# defining the function to check for duplicates in the two files and return the number of times the appear.


def count_duplicate_words(path1, path2):
    # here I am calling the function reading_the_two_files and passing the two files to read assigning them to a new variable word_list
    word_list = reading_the_two_files(path1, path2)
    # splitting the word_list to get each words from the two different files read
    first_list = word_list[0].split(" ")
    second_list = word_list[1].split(" ")
    # creating new lists for the filtered list
    filtered_first_list = []
    filtered_second_list = []
    # creating a dictionary for my duplicate word count
    duplicate_words_count = {}
    # looping through the first list to filter special characters and appending the filtred word to a new list
    for word in first_list:
        if(len(word)) != 0:
            word = word.lower()
            word = word.strip(" \n.?;,!-")
            word = word.replace("\n", "").replace(".", "").replace("?", "").replace(
                ";", "").replace(",", "").replace("!", "").replace("-", "")
            filtered_first_list.append(word)
    # looping through the first list to filter special characters and appending the filtred word to a new list
    for word in second_list:
        if(len(word)) != 0:
            word = word.lower()
            word = word.strip(" \n.?;,!-")
            word = word.replace("\n", "").replace(".", "").replace("?", "").replace(
                ";", "").replace(",", "").replace("!", "").replace("-", "")
            filtered_second_list.append(word)
    # looping through the first list and check if each word is in the second list. if yes I will count the number of times they appear together
    for eachWord in filtered_first_list:
        if(eachWord in filtered_second_list):
            num1 = filtered_first_list.count(eachWord)
            num2 = filtered_second_list.count(eachWord)
            if eachWord in duplicate_words_count:
                duplicate_words_count[eachWord] += 0
            else:
                duplicate_words_count[eachWord] = num1 + num2
    # returning the dictionary for my duplicate_word_count
    return duplicate_words_count


print(count_duplicate_words('./text1.txt', './text2.txt'))
