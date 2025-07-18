import tkinter as tk
import random
import numpy as np

'''
now my idea: make +- 10 "ai"(logic base) which is going to change picture for different size of scale 
then I want to add function which is going to move pictures to one pixel every time
to see which place going to be the bests by pro cents and then I just going to sub all pro cents from different ai and get result cleanlier
'''

rows = 601
cols = 401

newx = [0]*10
newy = [0]*10
newx[0] = 200
newx[1] = 180
newx[2] = 160
newx[3] = 140
newx[4] = 120
newx[5] = 100
newx[6] = 80
newx[7] = 60
newx[8] = 40
newx[9] = 20

newy[0] = 300
newy[1] = 270
newy[2] = 240
newy[3] = 210
newy[4] = 180
newy[5] = 150
newy[6] = 120
newy[7] = 90
newy[8] = 60
newy[9] = 30


class Digit:
    def __init__(self, file_name):
        self.file_name = file_name
        self.digit = []
        self.empty = True


number = np.zeros((rows, cols), dtype=int)

digit_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = [Digit(digit_names[i]+'p.npy') for i in range(10)]

# for i in range(10):
#     for iy in range(newy[i]):
#         for ix in range(newx[i]):
#             zero[i] = np.zeros((newy[i], newx[i]), dtype=int)
#             one[i] = np.zeros((newy[i], newx[i]), dtype=int)
#             two[i] = np.zeros((newy[i], newx[i]), dtype=int)
#             three[i] = np.zeros((newy[i], newx[i]), dtype=int)
#             four[i] = np.zeros((newy[i], newx[i]), dtype=int)
#             five[i] = np.zeros((newy[i], newx[i]), dtype=int)
#             six[i] = np.zeros((newy[i], newx[i]), dtype=int)
#             seven[i] = np.zeros((newy[i], newx[i]), dtype=int)
#             eight[i] = np.zeros((newy[i], newx[i]), dtype=int)
#             nine[i] = np.zeros((newy[i], newx[i]), dtype=int)


# number.append(34)
# number[0] = 45


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Простое Приложение для Рисования")

        self.canvas = tk.Canvas(root, bg='white', width=cols-1, height=rows-1)
        self.canvas.pack()

        self.canvas.bind('<ButtonPress-1>', self.start_drawing)
        self.canvas.bind('<B1-Motion>', self.draw)

        self.last_x, self.last_y = None, None
        root.bind("<Return>", self.on_enter_key)

    def start_drawing(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        global number
        if self.last_x and self.last_y:
            self.canvas.create_oval(self.last_x, self.last_y, event.x, event.y, fill='black', width=100)
            evex = event.x - 10
            evey = event.y - 10
            # print("x: "+evex+10)
            # print("y: "+evey+10)
            for i in range(50):
                for ii in range(50):
                    if 0 <= evex+i <= cols-1 and 0 <= evey+ii <= rows-1:
                        # print(evex+i)
                        # print(evey+ii)
                        number[evey+ii][evex+i] = 1
            self.last_x, self.last_y = event.x, event.y

    # def erase(self, event):
    #     if self.last_x and self.last_y:
    #         self.canvas.line(self.last_x, self.last_y, event.x, event.y, fill='white', width=100)
    #         self.last_x, self.last_y = event.x, event.y

    def on_enter_key(self, event):
        print("Enter key was pressed!")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()



upzz = None
upnn = None
downzz = None
downnn = None
shouldbreak = False

for i in range(rows-1):
    for ii in range(cols-1):
        if number[i][ii] == 1:
            upzz = i
            shouldbreak = True
            break
    if shouldbreak:
        shouldbreak = False
        break


for i in range(rows-1):
    for ii in range(cols-1):
        if number[(rows-1)-i][(cols-1)-ii] == 1:
            upnn = (rows-1)-i
            shouldbreak = True
            break
    if shouldbreak:
        shouldbreak = False
        break


for i in range(cols-1):
    for ii in range(rows-1):
        if number[ii][i] == 1:
            downzz = i
            shouldbreak = True
            break
    if shouldbreak:
        shouldbreak = False
        break


for i in range(cols-1):
    for ii in range(rows-1):
        if number[(rows-1) - ii][(cols-1) - i] == 1:
            downnn = (cols-1)-i
            shouldbreak = True
            break
    if shouldbreak:
        shouldbreak = False
        break


def scaleChanger(cutnumf, newxf, newyf, firsty, firstx):
    for _ in range(10):
        print(" ")
    ysizef = newyf / firsty
    xsizef = newxf / firstx
    sizenumf = np.zeros((newyf+1, newxf+1), dtype=int)

    for i in range(firsty):
        for ii in range(firstx):
            if cutnumf[i][ii] == 1:
                for p in range(int(ysizef + 1)):
                    for pp in range(int(xsizef + 1)):
                        if (int((i * ysizef) + 0.5)) + p >= 0 and (int((i * ysizef) + 0.5)) + p <= newyf and (
                        int((ii * xsizef) + 0.5)) + pp >= 0 and (int((ii * xsizef) + 0.5)) + pp <= newxf:
                            sizenumf[(int((i * ysizef) + 0.5)) + p][(int((ii * xsizef) + 0.5)) + pp] = 1
    for i in range(newyf):
        print(" ")
        for ii in range(newxf):
            print(sizenumf[i][ii], end=' ')
    return sizenumf


cutnum = np.zeros((upnn-upzz+1, downnn-downzz+1), dtype=int)

for i in range(upnn - upzz + 1):
    print(" ")
    for ii in range(downnn - downzz + 1):
        cutnum[i][ii] = number[upzz + i][downzz + ii]
        print(cutnum[i][ii], end=' ')
number = cutnum

#I need to choose a good combination of numbers newxf newyf which is future size of scale of picture FIX FIX FIX
allNumbersDraw = np.zeros((10, newy[0], newx[0]), dtype=int)
# for i in range(10):
#     i_number = scaleChanger(number, newx[i], newy[i], len(number), len(number[0]))
#     allNumbersDraw.append(i_number)
for i in range(10):
    i_number = scaleChanger(number, newx[i], newy[i], len(number), len(number[0]))
    for ii in range(newy[i]):
        for iii in range(newx[i]):
            allNumbersDraw[i][ii][iii] = i_number[ii][iii]



for _ in range(10):
    print(" ")


def load_digit(digit):
    try:
        digit.digit = []
        digit.empty = True
        with open(digit.file_name, 'rb') as f:
            count = np.load(f)
            for i in range(count[0]):
                digit.digit.append(np.load(f))
        print(f"Array loaded successfully from {digit.file_name}")
        digit.empty = False
    except (IOError, ValueError, EOFError) as e:
        print(f"Error loading array from file: {e}")


'''
def save_zerop(zeropp, file_base_name='zerop'):
try:
    for i, element in enumerate(zeropp):
        file_name = f'{file_base_name}_{i}.txt'  # save each element to a different file
        with open(file_name, 'w') as file:
            np.savetxt(file, element)
except IOError as e:
    print(f"Error saving the score to {file_name}: {e}")
'''


def save_digit(digit, data):
    try:
        digit.digit.append(data)
        count = np.zeros((1,), dtype=int)
        count[0] = len(digit.digit)

        with open(digit.file_name, 'wb') as f:
            np.save(f, count)
            for d in digit.digit:
                np.save(f, d)

        print(f"Array saved successfully to {digit.file_name}")
    except IOError as e:
        print(f"Error saving array: {e}")


for digit in digits:
    load_digit(digit)


def procentFind(num):
    global allNumbersDraw
    global newx
    global newy

    resnumber = [0]*10
    for p in range(len(allNumbersDraw)):
        numberto = allNumbersDraw[p]
        numof = num[0][p]
        mid = 0
        for i in range(newy[p]):
            for ii in range(newx[p]):
                mid += (numberto[i][ii] + 1)
        mid = 100 / mid
        for i in range(newy[p]):
            for ii in range(newx[p]):
                if numof[i][ii] >= 1 and numberto[i][ii] >= 1:
                    resnumber[p] += mid * (numof[i][ii] + 1)
        rslt = 0
        for x in range(len(resnumber)):
            rslt += resnumber[x]
        rslt = rslt/len(resnumber)
        return rslt
'''
mid = 0
    for i in range(201):
        for ii in range(151):
            mid += (zero[i][ii] + 1)
    mid = 100 / mid
    reszero = 0
    for i in range(201):
        for ii in range(151):
            if number[i][ii] >= 1 and zero[i][ii] >= 1:
                reszero += mid * (zero[i][ii] + 1)

'''


if all(not d.empty for d in digits):

    reszero = procentFind(digits[0].digit)
    resone = procentFind(digits[1].digit)
    restwo = procentFind(digits[2].digit)
    resthree = procentFind(digits[3].digit)
    resfour = procentFind(digits[4].digit)
    resfive = procentFind(digits[5].digit)
    ressix = procentFind(digits[6].digit)
    resseven = procentFind(digits[7].digit)
    reseight = procentFind(digits[8].digit)
    resnine = procentFind(digits[9].digit)


    print(" ")
    print(" ")
    print("Zero: ", reszero, "%")
    print("One: ", resone, "%")
    print("Two: ", restwo, "%")
    print("Three: ", resthree, "%")
    print("Four: ", resfour, "%")
    print("Five: ", resfive, "%")
    print("Six: ", ressix, "%")
    print("Seven: ", resseven, "%")
    print("Eight: ", reseight, "%")
    print("Nine: ", resnine, "%")
    print(" ")
    if reszero >= resone and reszero >= restwo and reszero >= resthree and reszero >= resfour and reszero >= resfive and reszero >= ressix and reszero >= resseven and reszero >= reseight and reszero >= resnine:
        print('It\'s ZERO with a chance of ' + str(reszero) + '%')
    elif resone >= reszero and resone >= restwo and resone >= resthree and resone >= resfour and resone >= resfive and resone >= ressix and resone >= resseven and resone >= reseight and resone >= resnine:
        print('It\'s ONE with a chance of ' + str(resone) + '%')
    elif restwo >= reszero and restwo >= resone and restwo >= resthree and restwo >= resfour and restwo >= resfive and restwo >= ressix and restwo >= resseven and restwo >= reseight and restwo >= resnine:
        print('It\'s TWO with a chance of ' + str(restwo) + '%')
    elif resthree >= reszero and resthree >= resone and resthree >= restwo and resthree >= resfour and resthree >= resfive and resthree >= ressix and resthree >= resseven and resthree >= reseight and resthree >= resnine:
        print('It\'s THREE with a chance of ' + str(resthree) + '%')
    elif resfour >= reszero and resfour >= resone and resfour >= restwo and resfour >= resthree and resfour >= resfive and resfour >= ressix and resfour >= resseven and resfour >= reseight and resfour >= resnine:
        print('It\'s FOUR with a chance of ' + str(resfour) + '%')
    elif resfive >= reszero and resfive >= resone and resfive >= restwo and resfive >= resthree and resfive >= resfour and resfive >= ressix and resfive >= resseven and resfive >= reseight and resfive >= resnine:
        print('It\'s FIVE with a chance of ' + str(resfive) + '%')
    elif ressix >= reszero and ressix >= resone and ressix >= restwo and ressix >= resthree and ressix >= resfour and ressix >= resfive and ressix >= resseven and ressix >= reseight and ressix >= resnine:
        print('It\'s SIX with a chance of ' + str(ressix) + '%')
    elif resseven >= reszero and resseven >= resone and resseven >= restwo and resseven >= resthree and resseven >= resfour and resseven >= resfive and resseven >= ressix and resseven >= reseight and resseven >= resnine:
        print('It\'s SEVEN with a chance of ' + str(resseven) + '%')
    elif reseight >= reszero and reseight >= resone and reseight >= restwo and reseight >= resthree and reseight >= resfour and reseight >= resfive and reseight >= ressix and reseight >= resseven and reseight >= resnine:
        print('It\'s EIGHT with a chance of ' + str(reseight) + '%')
    else:
        print('It\'s NINE with a chance of ' + str(resnine) + '%')



    while True:
        name = input('It was from 0:9?(or if you dont want to save it just write "n" (from word none))')
        if name == '0' or name == '1' or name == '2' or name == '3' or name == '4' or name == '5' or name == '6' or name == '7' or name == '8' or name == '9' or name == 'n':
            break
    if name != 'n':
        print(" ")
        print(" ")
        print(" ")
        num_to_safe = 0
        safenum = [0]*10
        digit_name = int(name)

        save_digit(digits[digit_name], allNumbersDraw)
        #
        # for p in range(len(allNumbersDraw)):
        #     for i in range(newy[p]):
        #         print(' ')
        #         for ii in range(newx[p]):
        #             num_to_safe = allNumbersDraw[p]
        #             check_num = digits[digit_name].digit[p]
        #             num_to_safe[i][ii] += check_num[i][ii]
        #             print(num_to_safe[i][ii], end=' ')
        #     safenum[p] = num_to_safe
        # save_digit(safenum, digits[digit_name].file_name)
        print(" ")
        print(f"Number {digit_name} was added")

else:
    while True:
        name = input('What is this from 0 to 9 (0:9)?(or if you dont want to save it just write "n" (from word none))')
        if name == '0' or name == '1' or name == '2' or name == '3' or name == '4' or name == '5' or name == '6' or name == '7' or name == '8' or name == '9' or name == 'n':
            break
    if name != 'n':
        save_digit(digits[int(name)], allNumbersDraw)
        # save_digit(allNumbersDraw, digits[int(name)].file_name)
        print(" ")
        print(f"Number {int(name)} was saved")


# for i in range(len(numberx)):
#     if i == 0:
#         print(numberx[i], end=" ")
#     else:
#         print(numberx[i])
#     for n in range(len(numbery)):
#         print(numbery[n], end=" ")
