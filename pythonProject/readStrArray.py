from extender import *


def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0
    figNum = 0
    while i < arrayLen:
        if i % 2 == 0:
            key = int(strArray[i])
            # Handle all case of input data.
            # For 1 - Aphorism, 2 - Word, 3 - Hint.
            if key == 1:
                i += 1
                shape = Aphorism()
                i = shape.ReadStrArray(strArray, i)
            elif key == 2:
                i += 1
                shape = Word()
                i = shape.ReadStrArray(strArray, i)
            elif key == 3:
                i += 1
                shape = Hint()
                i = shape.ReadStrArray(strArray, i)
            else:
                # If input data was incorrect, return number of object.
                return figNum
            if i == 0:
                return figNum
            i += 1
            figNum += 1
            # Append new data with container.
            container.store.append(shape)
    return figNum
