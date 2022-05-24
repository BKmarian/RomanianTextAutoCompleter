# -*- coding: iso-8859-2 -*-
import tkinter as tk
from tkinter import *

import re
from WordEmbedding import WordEmbedding
from levenstein import levenshtein, search
import json
from gensim.utils import unicode

trie_fst = WordEmbedding.load_trie()


# word_emb = WordEmbedding()

# .encode().decode("iso-8859-2")
def correct(event):
    sentences = area1.get("1.0", END).splitlines()
    try:
        for sentence in sentences:
            sentence = [re.sub("[^a-z??ăîâ\\-]", "", word.lower()) for word in sentence.split()]
            #sentence = [re.sub("[^a-z??ăîâ\\-]", "", word.lower()) for word in sentence.split("\\W+")]
            false_words = [word for word in sentence if trie_fst.find_word(word) is False and len(word) > 2]
            print(false_words)
            true_words = [word for word in sentence if trie_fst.find_word(word) is True]
            false_words_levenstein = {false_word: [w for w in search(false_word, 5)] for false_word in false_words}
            # predicted_words = set(word_emb.predict_words_by_sentence(true_words))
            # print(predicted_words)
            # most_sim_words = list(set().union(false_words_levenstein, predicted_words))
            # most_sim_words.append(set(false_words_levenstein) - predicted_words)
            area2.insert(INSERT, "\n".join("=".join((k, str(v))) for k, v in false_words_levenstein.items()))
    except Exception as e:
        print(e)


# def get_similarity(word):
#     return [(ws, levenshtein(ws, word)) for ws in word_emb.get_similar_words(word)].sort(key=lambda x: x[1])[:5]


root = tk.Tk()
area1 = tk.Text(root, height=50, width=80)
area2 = tk.Text(root, height=10, width=80)
area1.pack()
area2.pack()

widget = tk.Button(text="Correct")
widget.bind('<Button-1>', correct)
widget.place(anchor=S, height=5, width=20)
widget.pack()

tk.mainloop()
