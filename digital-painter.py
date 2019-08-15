import sys

sys.path.append('../AreaFill/')

import areafill as af
import cv2

def paint(canvas, lines, color_dict):
    canvas_copy = canvas
    color = [0,0,0]
    #print(len(lines))
    for i in range(len(lines)):
        #print(i)
        color = color_dict[lines[i][0]]
        del lines[i][0]
        
        if len(lines[i]) % 2 == 1:
            del lines[i][-1]
        #pt = 0
        #for pt1,pt2 in zip(lines[i][0::2], lines[i][1::2]):
        #    print(pt1,pt2)
        #    cv2.line(canvas_copy, pt1,pt2, color, thickness=1)
        for point in lines[i]:
            canvas_copy[point[1]][point[0]] = color 
        #print('line done')

    return canvas_copy

#print("Hello")
#colors = {'red':[255,0,0], 'green':[0,255,0], 'blue':[0,0,255],'magenta':[255,0,255], 'tomato':[255,99,71], 'lawn green':[124,252,0], 'yellow':[255,217,0], 'forest green':[2,77,7]}
#
#img = cv2.imread('./flower.jpg')
#lines = af.generate_diagnol_fill(img, colors)
#
##print(lines)
#
#image = paint(img, lines, colors) 
#cv2.imwrite('./output.jpg',image)

