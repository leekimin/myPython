from PIL import Image
import os

img = Image.open("test2.png")

img_resize = img.resize((305, 100))

print(img_resize.size)

img_resize.save("test2_1.png")
os.path.isfile("test2_1.png")


