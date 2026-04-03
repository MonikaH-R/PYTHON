import cv2
import numpy as np

images = cv2.imread("images3.jpg")
cropped = images[50:100,100:300]

cropped_resize = cv2.resize(cropped,(cropped.shape[1],images.shape[0]))
combined = np.hstack((images,cropped_resize))
cv2.imshow("Display images", combined)
cv2.waitKey(0)  # Corrected function name
cv2.destroyAllWindows()