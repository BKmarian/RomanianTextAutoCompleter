class TrieNode:

    def __init__(self):
        self.children = [None] * pow(2, 10)  # encoding length

        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):

        return TrieNode()

    @staticmethod
    def char_to_ord(ch):

        return ord(ch)
        # - ord('a')

    def insert(self, key):

        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self.char_to_ord(key[level])

            # if current character is not present
            if not p_crawl.children[index]:
                p_crawl.children[index] = self.get_node()
            p_crawl = p_crawl.children[index]

        p_crawl.isEndOfWord = True

    def search(self, key):

        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self.char_to_ord(key[level])
            if not p_crawl.children[index]:
                return False
            p_crawl = p_crawl.children[index]

        return p_crawl is not None and p_crawl.isEndOfWord

    def insert_words(self, words):
        for word in words:
            self.insert(word)

    def find_word(self, word):
        return self.search(word)
