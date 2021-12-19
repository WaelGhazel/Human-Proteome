import functools
import operator

def read_words():
    file = open("english-common-words.txt","r")
    list_word = []
    for line in file:
        if len(line) > 3:
            x = line[:-1]
            list_word.append(x.upper())
    file.close()
    return list_word

def read_sequence(file):
    proteome = {}
    y = ""
    for line in file:
        if line[0] == ">":
            ch = line.split("|")[1]
            y = ""
            continue
        else:
            y += line[:-1]
        proteome[ch]=y
    return proteome

def search_specific_word_in_proteome(o,dict):
    x = {}
    x[o]=functools.reduce(operator.add,map(lambda k:k.count(o),dict.values()))
    return x


def search_words_in_proteome(L,dict):
    x = {}
    for j in L :
        x[j]=functools.reduce(operator.add,map(lambda k:k.count(j),dict.values()))
    return x

def find_most_frequent_word(dict):
    max_value = max(dict.values())
    max_key = max(dict , key=dict.get)
    x = {}
    x[max_key]=max_value
    return x
