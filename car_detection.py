import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

path = r'C:\Users\Jay Swaminarayan\.spyder-py3\cars.jpg'
 




im = cv2.imread(path)
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
cv2.imshow('mayur',output_image)

    
cv2.waitKey(0)
cv2.destroyAllWindows()
print('Number of cars in the image is '+ str(label.count('car')))