import cv2
image = cv2.imread("image_Rs.png")   # taking image as input for resizing
scale_percent = 80
new_wid = (image.shape[1]*scale_percent//100)
new_ht = (image.shape[0]*scale_percent//100)
# output as resized image
output = cv2.resize(image,(new_wid,new_ht))
cv2.imwrite('Resized_file.jpeg',output)  # to write the name of output file
cv2.imshow("picture",output)  # to show the image
cv2.waitKey(0) # wait period ==0