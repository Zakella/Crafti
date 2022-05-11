import os

print(os.getcwd())
from PIL import Image

# print(os.path.dirname())
dir_in = os.getcwd() + "\\images_in\\"
dir_out = os.getcwd() + "\\images_out\\"
files = os.listdir(dir_in)

r = []
for i in range(219, 247):
    r.append(i)


g = []
for i in range(222, 247):
    g.append(i)


b = []
for i in range(215, 247):
    b.append(i)


for im in files:
    try:
        print("Start of image processing..." + im)
        img = Image.open(dir_in + im)
        img = img.convert("RGB")
        datas = img.getdata()
        new_image_data = []
        for item in datas:
            # print(item[0], item[1], item[2])
            if item[0] in r and item[1] in g and item[2] in b:
                new_image_data.append((255, 255, 255))
            else:
                new_image_data.append(item)
        img.putdata(new_image_data)
        img.save(dir_out + "out_" + im)
        print("End ..." + im)
    except:
        print("fail" + im)


        # except:
        # print("fail" + im)


# img.show()


print("Finish!")



# img.show()
