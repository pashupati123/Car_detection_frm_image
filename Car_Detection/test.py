import cv2
import numpy as np

THRESH_TYPE=cv2.THRESH_BINARY_INV

def show(name,obj):
    cv2.imshow(name,obj)
    cv2.moveWindow(name, 100, 100)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_end(new):
    drawing = np.zeros(o.shape,np.uint8)     # Image to draw the contours
    contours,hierarchy =cv2.findContours(new,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#find connected borders
    for cnt in contours:
        color = np.random.randint(0,255,(3)).tolist()  # Select a random color
        cv2.drawContours(drawing,[cnt],0,color,2)
    print "processing done"
    return drawing

def process(name,path):
    global o
    print "Started!!! processing "+name
    ratio=1#change according to image size
    o=cv2.imread("car.jpg")#open image
    print type(o)
    show("original",o)
    w,h=o.shape[1]/ratio,o.shape[0]/ratio#resize ratio for width and height
    new=cv2.resize(o,(w,h))#resize image
    #show("Resized",new)
    new=cv2.cvtColor(new,cv2.COLOR_RGB2GRAY)#grey scale image
    show("grey",new)
    cv2.imwrite("grey.jpg",new)
    new1 = cv2.GaussianBlur(new,(5,5),0)#gaussians Blurs Image
    show("blurred1",new1)
    cv2.imwrite("gblur_"+name,new1)#save image
    new2 = cv2.medianBlur(new,7)#Median Blurs Image
    show("blurred2",new1)
    cv2.imwrite("mblur_"+name,new2)#save image
    #new=cv2.equalizeHist(new,)#do image histogram equalisation to better the contrast
    #show("hist equal otsu",new)
    ##cv2.imwrite("otsu_"+name,new)#save image

    a,new=cv2.threshold(new,0,255,THRESH_TYPE | cv2.THRESH_OTSU)#OTSU thresholding
    show("otsu",new)
    cv2.imwrite("otsu_"+name,new)#save image
    return new,name



new,name=process("car.jpg","C:\\Users\\XOR\\Desktop\\file\\")#Change the Name and path accordingly
new=cv2.Canny(new, 100,200)#canny edge detection technique
show("canny",new)
cv2.imwrite("canny_"+name,new)#save image
new=process_end(new)
show("blobed",new)
cv2.imwrite("blob_"+name,new)#save image
new=cv2.Sobel(new,-1,1,0,3,BORDER_WRAP)
show("sobel",new)
cv2.imwrite("sobel_"+name,new)#save image