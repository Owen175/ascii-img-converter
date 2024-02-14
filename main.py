from PIL import Image

im = Image.open('./input_image.jpg')
output_res = 100, 100
im = im.resize(output_res, Image.ANTIALIAS)
gradient = 'Ñ@#W$9876543210?!abc;:+=-,._ '
lines = []
for x in range(output_res[0]):
    line = ''
    for y in range(output_res[1]):
        brightness = sum(im.getpixel((x, y))) / 3 / 255
        # gets a brightness between 0 and 1
        line += gradient[round(brightness * (len(gradient) - 1))]
    lines.append(line)
with open('output.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
print('Done')