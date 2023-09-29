from rembg import remove

from PIL import Image

input_path = 'image.jpg'
output_path = 'image_out.jpg'

inp = Image.open(input_path)
output = remove(inp)

output.save(output_path)
Image.open("image_out.jpg")