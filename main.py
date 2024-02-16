from os import system
import connect
import buttons


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
    return results


def find_button(nums_of_sim,button_index):
    global results
    lst = results[button_index]
    index = lst.index(nums_of_sim)
    return index


def get_max_index(word_list):
    max_index = 0
    max_value = word_list[0]

    for i in range(1, len(word_list)):
        if word_list[i] > max_value:
            max_value = word_list[i]
            max_index = i

    return max_index


def print_words(words, indexes:list):
    system('cls')
    indexes.sort()
    newindx = []
    for index in indexes:
        if 1 <= index <= len(words):
            newindx.append(index)
            print(f"{words[index - 1]} - {index}")

    newindx.reverse()
    return newindx


def full_next():
    try:
        connect.element_click(buttons.NEXT)
        input("press enter")
        return True
    except:
        return False

connect.start()
while True:
    word_list = connect.get_words()
    while True:
        try:
            get_results(word_list)
            chose_index = len(word_list)
            connect.word_click(chose_index)
            try1 = (inc(find_all_indexes(results[chose_index-1],connect.get_coml(buttons.COMPL))))
            indexes = print_words(word_list,try1)
            chose_index = indexes[0]
            connect.word_click(chose_index)
            try2 = (inc(find_all_indexes(results[chose_index-1],connect.get_coml(buttons.COMPL2))))
            common_elements = list(set(try1) & set(try2))

            indexes = print_words(word_list,common_elements)
            chose_index = indexes[0]
            connect.word_click(chose_index)
            try3 = (inc(find_all_indexes(results[chose_index-1],connect.get_coml(buttons.COMPL3))))
            common_elements = list(set(try1) & set(try2) & set(try3))
            indexes = print_words(word_list,common_elements)
            
            chose_index = indexes[0]
            connect.word_click(chose_index)
            input("Press Enter")
            break
        except:
            input("Press Enter")
            break