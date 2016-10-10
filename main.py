from PIL import Image
import numpy as np
import os,sys


def enlargeImage(npArray,factor):
    values = npArray.tolist()
    ## Intialize new Array with 3x number of rows of original array
    newArray = [[] for x in range(len(values)*factor)]
    ## For each row in the new Array:
    for i in range(len(newArray)):
        ## Loop through 3x number of columns of original array
        for j in range(len(values[0])*factor):
            newArray[i].append(values[int(i/factor)][int(j/factor)])

    return np.asarray(newArray)

def mainShell():
    try:
        file = sys.argv[1]
        image = Image.open(file)
        factor = int(sys.argv[2])
    except FileNotFoundError:
        sys.stdout.write("No such file exists: \"{}\"\n".format(sys.argv[1]))
        return
    except ValueError:
        sys.stdout.write("Invalid Factor - Must be Integer")
        return
    except IndexError:
        sys.stdout.write("Invalid Factor - Specify +Integer Value")
        return

    imageNp = np.asarray(image)
    enlargedNp = enlargeImage(imageNp,factor)

    imageOut = Image.fromarray(enlargedNp.astype("uint8")).convert("RGBA")
    fileOut = os.path.splitext(file)[0]+"_new"+os.path.splitext(file)[1]
    imageOut.save(fileOut)
    sys.stdout.write("Success - Saved as: \"{}\"\n".format(fileOut))
    
def mainUI():
    try:
        file = str(input("File name:"))
        image = Image.open(file)
        factor = int(input("Enlargement Factor:"))
    except FileNotFoundError:
        sys.stdout.write("No such file exists: \"{}\"\n".format(file))
        return
    except ValueError:
        sys.stdout.write("Invalid Factor - Must be Integer")
        return

    imageNp = np.asarray(image)
    enlargedNp = enlargeImage(imageNp,factor)

    imageOut = Image.fromarray(enlargedNp.astype("uint8")).convert("RGBA")
    fileOut = os.path.splitext(file)[0]+"_new"+os.path.splitext(file)[1]
    imageOut.save(fileOut)
    sys.stdout.write("Success - Saved as: \"{}\"\n".format(fileOut))

if __name__ == "__main__":
    ## Executed if 1 or more arguments in Shell
    if len(sys.argv)>1:
        mainShell()
    else:
        ## Executed if no shell arguments provided (Usually from IDLE)
        while True:
            mainUI()
    
