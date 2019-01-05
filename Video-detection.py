import cv2, math
import numpy as np
orig_img = cv2.imread('Image1.jpg')
while True:
      sobelx = cv2.Sobel(orig_img,cv2.CV_64F,1,0,ksize=5)
      sobely = cv2.Sobel(orig_img,cv2.CV_64F,0,1,ksize=5)
      img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)
            #  img = cv2.resize(img, (len(orig_img[0]) / self.scale_down, len(orig_img) / self.scale_down))
      boundaries = [([0, 150, 150], [5, 255, 255]),([40, 80, 10], [255, 255, 255]),([190, 150, 100], [255, 255, 255])]
      for (lower, upper) in boundaries:
            lower = np.array(lower,np.uint8)
            upper = np.array(upper,np.uint8)
            binary = cv2.inRange(img, lower, upper)
            dilation = np.ones((15, 15), "uint8")
            binary = cv2.dilate(binary, dilation)
                              #edge = cv2.Canny(red_binary,200,300,apertureSize = 3)
            image ,contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            max_area = 0
            largest_contour = None
      for idx, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > max_area:
                  max_area = area
                  largest_contour = contour
      if not largest_contour == None:
            moment = cv2.moments(largest_contour)
      if moment["m00"] > 1000 / self.scale_down:
            rect = cv2.minAreaRect(largest_contour)
            rect = ((rect[0][0] * self.scale_down, rect[0][1] * self.scale_down), (rect[1][0] * self.scale_down, rect[1][1] * self.scale_down), rect[2])
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(orig_img,[box], 0, (0, 0, 255), 2)
            cv2.imshow("ColourTrackerWindow", orig_img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
            break
capture.release()
cv2.destroyAllWindows()                                       

