# importing required library
from PIL import Image

# path of the image
image_path = "image1.png"
# assigning image to object
image_file = Image.open(image_path)

# resizing the image
new_image = image_file.resize((1920,1080))
# saving the image
new_image.save("newImage.png")