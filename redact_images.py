import os

print(os.getcwd())
from PIL import Image

# print(os.path.dirname())
dir_in = os.getcwd() + "\\images_in\\"
dir_out = os.getcwd() + "\\images_out\\"
files = os.listdir(dir_in)

for im in files:
    print("Start of image processing..." + im)
    img = Image.open(dir_in + im)
    img = img.convert("RGB")
    datas = img.getdata()
    new_image_data = []
    for item in datas:
        if item[0] in list(range(190, 256)):
            new_image_data.append((255, 255, 255))
        else:
            new_image_data.append(item)

    img.putdata(new_image_data)
    img.save(dir_out + "out_" + im)
    print("End ..." + im)
    # img.show()


print("Finish!")



# img.show()
