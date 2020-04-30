# The Principle of Inpaint Algorithm
[reference](https://docs.opencv.org/master/df/d3d/tutorial_py_inpainting.html)
   - First algorithm is based on the paper **"An Image Inpainting Technique Based on the Fast Marching Method"** by Alexandru Telea in 2004. It is based on Fast Marching Method. Consider a region in the image to be inpainted. Algorithm starts from the boundary of this region and goes inside the region gradually filling everything in the boundary first. It takes a small neighbourhood around the pixel on the neighbourhood to be inpainted. This pixel is replaced by normalized weighted sum of all the known pixels in the neighbourhood. Selection of the weights is an important matter. More weightage is given to those pixels lying near to the point, near to the normal of the boundary and those lying on the boundary contours. Once a pixel is inpainted, it moves to next nearest pixel using Fast Marching Method. FMM ensures those pixels near the known pixels are inpainted first, so that it just works like a manual heuristic operation. This algorithm is enabled by using the flag, cv.INPAINT_TELEA.

  - Second algorithm is based on the paper **"Navier-Stokes, Fluid Dynamics, and Image and Video Inpainting"** by Bertalmio, Marcelo, Andrea L. Bertozzi, and Guillermo Sapiro in 2001. This algorithm is based on fluid dynamics and utilizes partial differential equations. Basic principle is heurisitic. It first travels along the edges from known regions to unknown regions (because edges are meant to be continuous). It continues isophotes (lines joining points with same intensity, just like contours joins points with same elevation) while matching gradient vectors at the boundary of the inpainting region. For this, some methods from fluid dynamics are used. Once they are obtained, color is filled to reduce minimum variance in that area. This algorithm is enabled by using the flag, cv.INPAINT_NS.


# Codeing Example

      import numpy as np
      import cv2

      # read image and do some damage on image
      img = cv2.imread('images/3627527276_6fe8cd9bfe_z.jpg')
      cv2.line(img, (10,70), (200,200), (0,0,255), 2, 4)
      cv2.line(img, (515,118), (434,372), (0,255,0), 2, 8)
      cv2.circle(img, (300,300), 5, (255,0,0), 5)
      #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


      # make mask, mask area must great than recover area
      mask = np.zeros(img.shape[:2], np.uint8)
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
        
# Test Result
<img src="https://github.com/xidaniel/OpenCV-Practices/blob/master/Images/inpaint.png"  alt="Person in right" align=center />
