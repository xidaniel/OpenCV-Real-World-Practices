# Background
  - restriction: 
    - Object must be largest object on image
    - Background should as clean as possible
  - Main Method  [reference](https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html)
    - Simple Thresholding: If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value. The function cv.threshold is used to apply the thresholding. The first argument is the source image, which should be a grayscale image. The second argument is the threshold value which is used to classify the pixel values. The third argument is the maximum value which is assigned to pixel values exceeding the threshold. OpenCV provides different types of thresholding which is given by the fourth parameter of the function.


## [Coding Example](https://github.com/xidaniel/OpenCV-Practices/blob/master/sources%20code/crop.py)


# Test Result
<img src="https://github.com/xidaniel/OpenCV-Practices/blob/master/Images/tick_crop.png"  alt="Person in right" align=center />
