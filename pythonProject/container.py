# ----------------------------------------------
class Container:
    def __init__(self):
        # Container for input data.
        self.store = []
        # Container for sorted output array of function.
        # In further, it's using for ques №2.
        self.store_digit = []

    # Print output data in console for question 1.
    def Print(self):
        print("Container is store", len(self.store), "shapes:")
        for shape in self.store:
            shape.Print()
        pass

    # Print output data in selected file for question 1.
    def Write(self, ostream):
        ostream.write("Container is store {} shapes:\n".format(len(self.store)))
        for shape in self.store:
            shape.Write(ostream)
            ostream.write("\n")
        ostream.write("Summa of Function  = {}\n".format(self.Function()))
        pass

    # Method for handle the sum of function.
    def Function(self):
        per = 0
        for shape in self.store:
            per += shape.Function()
            self.store_digit.append(shape.Function())
        return per

    # Method for handle question 2.
    def WriteSecond(self, ostream):
        store_digit = []
        for shape in self.store:
            store_digit.append(FuncCount(self, shape.Func()))
        quickSort(store_digit, 0, len(store_digit) - 1)
        for shape in store_digit:
            ostream.write(str(shape))
            ostream.write(" ")
        pass

    # Method for set the number of function for each object in container.
def FuncCount(self, str):
    punctuation = ['!', '.', ',', '-', '/', '#', '?', ';', ':']
    count = 0
    for i in str:
        if i in punctuation:
            count += 1
    if (count == 0):
        return 0
    function = len(str) / count
    return function

    # Handle quick sort method array of function.
def prepare(numbers, low, high):
    pivot = numbers[high]
    item = low - 1
    for i in range(low, high):
        if numbers[i] <= pivot:
            item = item + 1
            (numbers[item], numbers[i]) = (numbers[i], numbers[item])
    (numbers[item + 1], numbers[high]) = (numbers[high], numbers[item + 1])
    return item + 1

    # Quick sort method array of function.
def quickSort(numbers, lower, higher):
    if lower < higher:
        pivot = prepare(numbers, lower, higher)

        quickSort(numbers, lower, pivot - 1)

        quickSort(numbers, pivot + 1, higher)
