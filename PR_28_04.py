class Dictionary:
    def __init__(self):
        self.dictionary = {}
        self.popularity_counter = {}

    def add_translate(self, word, trans):
        if word in self.dictionary:
            self.dictionary[word].append(trans)
        else:
            self.dictionary[word] = [trans]
        self.popularity_counter.setdefault(word, 0)

    def remove_translate(self, word, trans):
        if word in self.dictionary:
            if trans in self.dictionary[word]:
                self.dictionary[word].remove(trans)
                if not self.dictionary[word]:
                    del self.dictionary[word]
                return True
        return False

    def add_word(self, word):
        if word not in self.dictionary:
            self.dictionary[word] = []
            self.popularity_counter.setdefault(word, 0)
            return True
        return False

    def remove_word(self, word):
        if word in self.dictionary:
            del self.dictionary[word]
            del self.popularity_counter[word]
            return True
        return False

    def translate(self, word):
        if word in self.dictionary:
            self.popularity_counter[word] += 1
            return self.dictionary[word]
        return None

    def top_10(self):
        words = sorted(self.popularity_counter.items(), key=lambda x: x[1], reverse=True)
        return [word[0] for word in words[:10]]
    def low_10(self):
        words = sorted(self.popularity_counter.items(), key=lambda x: x[1])
        return [word[0] for word in words[:10]]

if __name__ == '__main__':
    dictionary = Dictionary()

    dictionary.add_translate("hello", "hola")
    dictionary.add_translate("hello", "buenos dias")
    dictionary.add_translate("world", "mundo")

    dictionary.remove_translate("hello", "buenos dias")

    dictionary.add_word("goodbye")
    dictionary.remove_word("world")

    print(dictionary.translate("hello"))
    print(dictionary.translate("world"))
    print(dictionary.top_10())
    print(dictionary.low_10())





















