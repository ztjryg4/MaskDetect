import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image

def detect_img(yolo):
    list_file = open("_mask_test.txt","r")
    detect_list = [i.split(" ")[0] for i in list_file.readlines()]
    output_dir = "./logs/output/"
    print("Testing on %d images." % len(detect_list))
    cnt = 1
    for img in detect_list:
        print("%d/%d" % (cnt,len(detect_list)))
        cnt = cnt + 1
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            # r_image.show()
            r_image.save(output_dir+img.split("/")[-1])
    yolo.close_session()


if __name__ == '__main__':
    detect_img(YOLO())