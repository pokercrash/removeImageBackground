# https://github.com/danielgatis/rembg
from rembg import remove
from PIL import Image

# replace file name
input_path = 'test.jpg'
output_path = 'removedBG.png'
input = Image.open(input_path)
print("opening image....")

output = remove(input)
print("removing background....")

output.save(output_path)
print("finished")