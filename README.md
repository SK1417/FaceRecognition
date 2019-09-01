# FaceRecognition

Disclaimer: Referenece and credit to: https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/

The model uses the face_recognition wrapper package located in dlib. 
You can install dlib by:

    pip install dlib
    
#Important
dlib that comes with conda or pip, does not particularly come with gpu support. You can check this by printing 
     
     print(dlib.DLIB_USE_CUDA)

This should return True if you want to include gpu support. If you want so, you should build dlib from source. Same goes for opencv too. Also, many deep learning come included when you build it from source. No one can explain it better than Adrian: 

dlib installation: Given in the above face_recognition tutorial link.
opencv 4 (on ubuntu): https://www.pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/

Also, if you want to do this for other platforms, you can check the official opencv page:

https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html (for windows)

https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/ (for mac)

