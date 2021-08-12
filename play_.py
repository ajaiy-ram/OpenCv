import cv2
from play2 import employee_finder

# image = cv2.imread('./TSHIRT_5.png')
# image = employee_finder(image)

image = cv2.imread('./images/TSHIRT_5.png')
# image = cv2.imread('./images/TSHIRT_5.png  ')
# image = cv2.imread('./cb.png')
cv2.imshow('input', image)
cv2.waitKey(-1)

image = employee_finder(image)

cv2.imshow('output', image)
cv2.waitKey(-1)
