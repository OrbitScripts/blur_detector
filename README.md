# Simple image blur using the OpenCV library
This library allows to determine the degree of focusing of the image based on the methods of the Fourier transform.
The higher the value, the less blurry the image is considered. The value for separating blurry images from non-blurred ones is set individually, for our project we used value 14. That is, everything less than 14 was considered blurry images.
To use it, just import the method `get_blur_point` this way `from blur_detector_image import get_blur_point`. This method takes 2 arguments as input:
1. URL or PATH of the image; 
2. The type of the transmitted string from 1 point: URL or path.
##### Dependencies:
- numpy
- cv2
- urllib.request
