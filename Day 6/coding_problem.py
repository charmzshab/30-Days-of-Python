# my_sentence = Sentence("This is a test")
# my_string = "This is a test"
# str_fmt = my_string.split(" ")
# print(str_fmt[len(str_fmt) - 1].index())

# def Sentence(str_fmt):
#     start = str_fmt[0].
#     end = str_fmt[len(str_fmt) - 1]

#     while


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split(" ")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


my_sentence = Sentence("This is a test")
# for sents in my_sentence:
#     print(sents)

# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))

# generator
def sentence(my_sentence):
    for word in my_sentence.split():
        yield word


my_senti = sentence("Shaban is so cool")
for word in my_senti:
    print(word)

