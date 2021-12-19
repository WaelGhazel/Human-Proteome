from words_in_proteome import read_words, read_sequence, search_words_in_proteome, find_most_frequent_word,search_specific_word_in_proteome

with open("human-proteome.fasta") as file:
    l = read_words()
    pr = read_sequence(file)
    x = search_words_in_proteome(l,pr)
    h = find_most_frequent_word(x)
    base = sum(x.values())


def broad_words():
    return l
def broad_sequences():
    return pr
def broad_seq_in_prot():
    return x
def broad_most_freq_word():
    return h
def search_word(o):
    v=search_specific_word_in_proteome(o, broad_sequences())
    return v



