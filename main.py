from os import system
import connect
import time
import buttons
import random


def count_matches(words):
    scores = []
    for i in range(len(words)):
        score = 0
        for j in range(len(words[i])):
            for k in range(len(words)):
                if i != k and words[i][j] == words[k][j]:
                    score += 1
                    break
        scores.append(score)
    return scores


def count_matches_with_word(words,word):
    res = []
    for i in range(len(words)):
        res.append(0)
        for j in range (len(words[i])):
            if words[i][j] == word[j]:
                res[i] += 1
    return res

results = []

def find_all_indexes(lst, value):
    return [index for index, element in enumerate(lst) if element == value]


def inc(arr):
    for i in range(len(arr)):
        arr[i]+=1
    return arr

def get_results(word_list):
    global results
    results = []
    for i in range(len(word_list)):
        results.append(count_matches_with_word(word_list, word_list[i]))
        #print(f"{results[i]} {word_list[i]} {i+1}")
    return results


def find_button(nums_of_sim,button_index):
    global results
    lst = results[button_index]
    index = lst.index(nums_of_sim)
    return index


def refresh(word_list):
    system('cls')
    print(count_matches(word_list))
    print("\n")
    get_results(word_list)


def get_max_index(word_list):
    max_index = 0
    max_value = word_list[0]

    for i in range(1, len(word_list)):
        if word_list[i] > max_value:
            max_value = word_list[i]
            max_index = i

    return max_index


def print_words(words, indexes):
    for index in indexes:
        if 1 <= index <= len(words):
            print(f"{words[index - 1]} - {index}")


while True:
    try:
        connect.start()
        break
    except:
        print("error")
while True:
    word_list = connect.get_words()
    while True:
        try:
            refresh(word_list)
            first_word_index = get_max_index(count_matches(word_list))
            print(word_list[first_word_index],first_word_index+1)
            chose_index = int(input("input 1 choosen word index"))
            try1 = (inc(find_all_indexes(results[chose_index-1],connect.get_coml(buttons.COMPL))))
            print_words(word_list,try1)
            chose_index = int(input("input 2 choosen word index"))
            try2 = (inc(find_all_indexes(results[chose_index-1],connect.get_coml(buttons.COMPL2))))
            common_elements = list(set(try1) & set(try2))
            print_words(word_list,common_elements)
            chose_index = int(input("input 3 choosen word index"))
            try3 = (inc(find_all_indexes(results[chose_index-1],connect.get_coml(buttons.COMPL3))))
            common_elements = list(set(try1) & set(try2) & set(try3))
            print_words(word_list,common_elements)
            input("Update")
        except:
            input("Update")
            break