# -*- coding: iso-8859-2 -*-
import gensim
import pickle

from trie import Trie
import pickle

corola_file = 'corola.100.10.vec'


# 'corola.300.20.vec'

class WordEmbedding:
    def __init__(self):
        self.model = gensim.models.KeyedVectors.load_word2vec_format(corola_file, binary=False,
                                                                     encoding='iso-8859-2')

    def get_similar_words(self, word):
        try:
            return self.model.similar_by_word(word, topn=20)
        except:
            return ["Word not in dictionary"]

    def predict_words_by_sentence(self, words):
        try:
            return self.model.most_similar(words, topn=10)
        except:
            return ["Word not in dictionary"]

    @staticmethod
    def dump_vocabulary_and_trie():
        keys = []
        trie = Trie()

        with open(corola_file, 'r', encoding='utf-8') as rp:
            for line in rp.readlines():
                keys.append(str(line.split(' ')[0]))
        trie.insert_words([word for word in keys if len(word) > 1])

        with open('vocabulary.txt', 'w', encoding='iso-8859-2') as fp:
            for word in keys:
                fp.write(word)
                fp.write(' ')

        file_handler = open('trie.obj', 'wb')
        pickle.dump(trie, file_handler)
        file_handler.close()

    @staticmethod
    def dump_trie_obj():
        trie = Trie()
        with open('vocabulary.txt', 'r', encoding='utf-8') as fp:
            for words in fp.readlines():
                trie.insert_words([word for word in words.split(' ') if len(word) > 1])
        file_handler = open('trie.obj', 'wb')
        pickle.dump(trie, file_handler)
        file_handler.close()

    @staticmethod
    def load_trie():
        file_handler = open('trie.obj', 'rb')
        trie = pickle.load(file_handler)
        file_handler.close()
        return trie


#WordEmbedding.dump_trie_obj()
