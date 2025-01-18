from PIL import Image

image = Image.open("monro.jpg")

red, green, blue = image.split()

coordinates = (50, 0, red.width, red.height)
red_left = red.crop(coordinates)
coordinates = (25, 0, 671, red.height)
red_middle = red.crop(coordinates)

red_shift = Image.blend(red_left, red_middle, 0.3)

coordinates = (0, 0, 646, blue.height)
blue_right = blue.crop(coordinates)
coordinates = (25, 0, 671, blue.height)
blue_middle = blue.crop(coordinates)

blue_shift = Image.blend(blue_right, blue_middle, 0.3)

coordinates = (25, 0, 671, green.height)
green = green.crop(coordinates)

stylized_image = Image.merge("RGB", (red_shift, green, blue_shift))
stylized_image.thumbnail((80, 80))
stylized_image.save("stylized_image.jpg")