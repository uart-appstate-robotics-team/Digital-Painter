import sys

sys.path.append('../EdgePoints/')

import edgepoints as ep

import cv2

lines = ep.generate_edge_lines('./flower.jpg')
img = cv2.imread('./flower.jpg')
#print(lines)
for line in lines:
    if len(line) % 2 == 1:
        del line[-1]
    pt = 0
    for pt1,pt2 in zip(line[0::2], line[1::2]):
        print(pt1,pt2)
        cv2.line(img, pt1,pt2, [0,255,0], thickness=2)

cv2.imwrite('./output.jpg',img)
