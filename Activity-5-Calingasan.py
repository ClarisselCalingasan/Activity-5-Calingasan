import cv2 as cv
import numpy as np

img = cv.imread('panda.jpg')
windowTitle = "Hello Kitty After"

x = int(input("\nEnter X Value: "))
y = int(input("Enter Y Value: "))

c = int(input("\nInput color Attributes:"))

print("\nBefore: ", img[x,y])
img.itemset((x,y,c),120)

print("After: ", img[x,y])
sh = img.shape
sz = img.size
sz1 = 1000000
if sz > sz1:
    print("\nThe Image size is Validated\n")
else:
    print("\nThe image is invalid\n")
print(img.shape)
print(img.size)
print(img.dtype)
cv.imshow(windowTitle,img)
cv.waitKey(0)
cv.destroyAllWindows()