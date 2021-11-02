from shape import *


# ----------------------------------------------
class Word(Shape):
    def __init__(self):
        self.word = 0
        self.count = 0
        self.function = 0

    def ReadStrArray(self, strArray, i):
        self.word = strArray[i]
        return i

    def Print(self):
        print("It's Word : ", self.word, "\n", self.Function())
        pass

    def Write(self, ostream):
        ostream.write("Word : ")
        ostream.write(self.word)
        ostream.write("\n")
        ostream.write(str(self.function))
        pass

    def Function(self):
        punctuation = ['!', '.', ',', '-', '/', '#', '?', ';', ':']
        for i in self.word:
            if i in punctuation:
                self.count += 1
        if self.count == 0:
            return 0
        self.function = len(self.word) / self.count
        return self.function
        pass

    def Func(self):
        return self.word
