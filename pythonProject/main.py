import sys
from extender import *

#----------------------------------------------
if __name__ == '__main__':
    # Argument value handling.
    if len(sys.argv) == 4:
        # In case if user has input data.
        inputFileName = sys.argv[1]
        outputFileName = sys.argv[2]
        outputFileName2 = sys.argv[3]
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()
        strArray = str.split("\n")
    elif len(sys.argv) == 3:
        # In case if user wants generate the data
        outputFileName = sys.argv[1]
        outputFileName2 = sys.argv[2]
        random = Randomizer()
        strArray = random.Function()
        strArray.pop(len(strArray) - 1)
    elif len(sys.argv) != 4:
        print("Incorrect command line! You must write: python main "
              "(<inputFileName> [<outputFileName>] [<outputFileName2>])"
              "or ([<outputFileName>] [<outputFileName2>])")
        exit()

    print('==> Start')

    # Creating new container for processing data.
    container = Container()
    # Output all data in container.
    figNum = ReadStrArray(container, strArray)
    # Print input data.
    container.Print()

    print('==> Start processing')

    # Open the file and establishing new data.
    ofile = open(outputFileName, 'w')
    # Write current 1 question if file.
    container.Write(ofile)
    ofile.close()

    print('==> Finish 1 part')

    # Open second file and establishing sorted array.
    ofile_second = open(outputFileName2, 'w')
    # Output 2 part into selected file.
    container.WriteSecond(ofile_second)
    ofile_second.close()

    print('==> Finish 2 part')