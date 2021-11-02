from shape import *

# ----------------------------------------------
class Aphorism(Shape):
    def __init__(self):
        # Input string.
        self.feature = 0
        # Count of punctuation terms.
        self.count = 0
        # Function for current object.
        self.function = 0

    # Handle input string.
    # Cover it in container.
    def ReadStrArray(self, strArray, i):
        self.feature = strArray[i]
        return i

    # Print information in console.
    def Print(self):
        print("It's Aphorism : ", self.feature, "\n", self.Function())
        pass

    # Outputting information in selected file.
    def Write(self, ostream):
        # Output current information in format :
        # Aphorism : <String> \n <Output function>.
        ostream.write("Aphorism : ")
        ostream.write(self.feature)
        ostream.write("\n")
        ostream.write(str(self.function))
        pass

    # Method for function handling.
    def Function(self):
        punctuation = ['!', '.', ',', '-', '/', '#', '?', ';', ':']
        for i in self.feature:
            if i in punctuation:
                self.count += 1
        if self.count == 0:
            return 0
        self.function = len(self.feature) / self.count
        return self.function

    # Returns the current string.
    def Func(self):
        return self.feature
