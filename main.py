import cv2
from tkinter import filedialog

asciiList = R""".'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"""

asciiNums = [round((255 / len([*asciiList])) * i) for i in range(len([*asciiList]))]

reqimg = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files", "*.png"),("all files","*.*")))
if( reqimg != "" ):
    ogimg = cv2.imread(reqimg)
    img = cv2.cvtColor(ogimg, cv2.COLOR_BGR2GRAY)

    with open(reqimg.split(".")[0] + "_ascii" + ".txt", "x") as f:
        for h in range(img.shape[0]):
            for w in range(img.shape[1]):
                f.write(asciiList[asciiNums.index(min(asciiNums, key=lambda x: abs(x - (img[h][w]))))])
            f.write("\n")
else:
    print( "User canceled" )