import numpy as np
  import cv2

  # read image and do some damage on image
  img = cv2.imread('images/3627527276_6fe8cd9bfe_z.jpg')
  cv2.line(img, (10,70), (200,200), (0,0,255), 2, 4)
  cv2.line(img, (515,118), (434,372), (0,255,0), 2, 8)
  cv2.circle(img, (300,300), 5, (255,0,0), 5)
  #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


  # make mask, mask area must great than recover area
  height, width = img.shape[:2]
  mask = np.zeros((height, width, 1), np.uint8)
  cv2.line(mask, (10,70), (200,200), (255,255,255), 2, 4)
  cv2.line(mask, (515,118), (434,372), (255,255,255), 2, 8)
  cv2.circle(mask, (300,300), 5, (255,255,255), 5)

  # use dilate to extend area of mask
  kernel = np.ones((3,3), np.uint8)
  mask = cv2.dilate(mask, kernel, iterations=1)

  # try to use two different kinds of algorithm
  dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
  dst1 = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)


  cv2.imshow('original',img)
  cv2.imshow('dst', dst)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
