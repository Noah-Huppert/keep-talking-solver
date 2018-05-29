#!/usr/bin/env python3
#
# Manual: 421
#
possible_words = {"about","every","large","plant","spell","these","where","after","first",
         "learn","point","still","thing","which","again","found","never","right",
         "study","think","world","below","great","other","small","their","three",
         "would","could","house","place","sound","there","water","write"}

def get_column(col):
    in_letters = input("Enter column {}: ".format(col))

    letters = set()

    for in_letter in in_letters:
        letters.add(in_letter)

    return letters

def match_words(words, pos, col):
    possible = set()

    for word in words:
        if word[pos] in col:
            possible.add(word)

    print(possible)
    return possible

first_col = get_column("first")
second_col = get_column("second")
third_col = get_column("third")
fourth_col = get_column("fourth")
fifth_col = get_column("fifth")

guess_words = match_words(possible_words, 0, first_col)
guess_words = match_words(guess_words, 1, second_col)
guess_words = match_words(guess_words, 2, third_col)
guess_words = match_words(guess_words, 3, fourth_col)
guess_words = match_words(guess_words, 4, fifth_col)

print("Password: {}".format(guess_words))
