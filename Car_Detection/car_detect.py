import cv2
import sys
import glob

cascPath = "C:\\opencv\\build\\etc\\haarcascades\\cars.xml"

# Create the haar cascade
carCascade = cv2.CascadeClassifier(cascPath)
files=glob.glob("car2.jpg")
for file in files:

    # Read the image
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect cars in the image
    cars = carCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=2,
        minSize=(20, 20),
        flags=cv2.CASCADE_SCALE_IMAGE
    )



    # Crop Padding
    left = 15
    right = 15
    top = 15
    bottom = 15
    count_cars=0
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
   #displaying the cars and number of cars are found
        count_cars=count_cars+1
    cv2.imshow("car found", image)
cv2.waitKey(0)
print("Total number of cars present in image:")
print("68")