import pytesseract as pt
from PIL import Image
from matplotlib import pyplot as plt

img = Image.open("echo.png")
hist = img.histogram()
print (hist)
print(len(hist))
plt.hist(hist)
text = pt.image_to_string(img)
print(text)