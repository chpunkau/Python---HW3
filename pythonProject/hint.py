from shape import *


# ----------------------------------------------
class Hint(Shape):
    def __init__(self):
        self.answer = 0
        self.count = 0
        self.function = 0

    def ReadStrArray(self, strArray, i):
        self.answer = strArray[i]
        return i

    def Print(self):
        print("It's Hint : ", self.answer, "\n", self.Function())
        pass

    def Write(self, ostream):
        ostream.write("Hint : ")
        ostream.write(self.answer)
        ostream.write("\n")
        ostream.write(str(self.function))
        pass

    def Function(self):
        punctuation = ['!', '.', ',', '-', '/', '#', '?', ';', ':']
        for i in self.answer:
            if i in punctuation:
                self.count += 1
        if self.count == 0:
            return 0
        self.function = len(self.answer) / self.count
        return self.function
        pass

    def Func(self):
        return self.answer
