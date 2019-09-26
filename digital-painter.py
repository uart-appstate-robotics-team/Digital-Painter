import sys
import edgepoints as ep
import cv2


class DigitalWriter:
    image_dir = ""

    def __init__(images_relative_path="./"):
        image_dir = images_relative_path

    def plot_lines(self, lines, image_in, image_out):
        img = cv2.imread(image_dir + image_dirimage_in)

        for line in lines:
            if len(line) % 2 == 1:
                del line[-1]
            pt = 0
            for pt1, pt2 in zip(line[0::2], line[1::2]):
                print(pt1, pt2)
                cv2.line(img, pt1, pt2, [0, 255, 0], thickness=2)

        cv2.imwrite(image_dir + image_out, img)
