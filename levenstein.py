# -*- coding: iso-8859-2 -*-
import time

MAX_COST = 4

neighbours = ['qwertyuiop',
              'asdfghjkl',
              'zxcvbnm']


def get_input():
    with open("vocabulary.txt", "r",encoding="utf-8") as ins:
        for line in ins.read().split(' '):
            word = line.strip()
            if len(word) > 2:
                yield word


def get_cost(letter1, letter2):
    pos1 = neighbours[0].find(letter1)
    string1 = 0
    if pos1 == -1:
        string1 = 1
        pos1 = neighbours[1].find(letter1)
    if pos1 == -1:
        string1 = 2
        pos1 = neighbours[2].find(letter1)

    pos2 = neighbours[0].find(letter2)
    string2 = 0
    if pos2 == -1:
        string2 = 1
        pos2 = neighbours[1].find(letter2)
    if pos2 == -1:
        string2 = 2
        pos2 = neighbours[2].find(letter2)

    if pos1 == -1 or pos2 == -1:
        return 1

    if abs(pos1 - pos2) <= 1 and abs(string1 - string2) <= 1:
        return 1
    return 2


def levenshtein(word1, word2):
    columns = len(word1) + 1
    rows = len(word2) + 1

    # build first row
    current_row = [0]
    for column in range(1, columns):
        current_row.append(current_row[column - 1] + 1)

    for row in range(1, rows):
        previous_row = current_row
        current_row = [previous_row[0] + 1]

        for column in range(1, columns):

            insert_cost = current_row[column - 1] + 1
            delete_cost = previous_row[column] + 1

            if word1[column - 1] != word2[row - 1]:
                cost = get_cost(word1[column - 1], word2[row - 1])
                replace_cost = previous_row[column - 1] + cost
            else:
                replace_cost = previous_row[column - 1]

            current_row.append(min(insert_cost, delete_cost, replace_cost))

    return current_row[-1]


def search(target, first_n_words):
    results = []
    for word in list(get_input()):
        if abs(len(word) - len(target)) > MAX_COST:
            continue

        cost = levenshtein(target, word)

        if cost <= MAX_COST:
            results.append((word, cost))

    results.sort(key=lambda tup: tup[1], reverse=False)
    results = [res[0] for res in results]
    return results[:first_n_words]


def main():
    start = time.time()
    results = search("asd")
    end = time.time()

    for result in results:
        print(result)

    print("Search took %g s" % (end - start))


if __name__ == '__main__':
    main()
