from PIL import Image

filename = "istockphoto-2086363366-612x612.jpg"

img = Image.open(filename)

img.show(img)
print(
    img.format,
    img.size,
    img.mode)