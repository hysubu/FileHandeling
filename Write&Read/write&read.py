

'''
if we want to write and read any file in one time that time we use
How it work : when we write any data in existing file that time this process first delete the
existsing data from file
and then add  recent or new data in file
'''

# file  = open("file.txt" , "w+")
# file.write("Hii Iam Write and read process ")
#
# file.seek(0)
# # seek(0) mean its  update the file and start to first like after write the data then start to new m
# # method to read
# read_data = file.read()
# print(read_data)


#
# import cv2
#
# # Read an image from file
# image = cv2.imread('image.png')
#
# # Display the image
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#
# file = open("image.png" , "rb")
# image_byte = file.read()
# print(image_byte)
# import io
# from  PIL import  Image
# image_byte_io = io.BytesIO()
# Image.
# # Image.register_save(image_byte_io , format("JPEG"))
# image_byte =  image_byte_io.getvalue()
# print(image_byte)
