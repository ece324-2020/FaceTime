
import PIL.Image
import PIL.ImageDraw
import face_recognition
# import cv2

# Load the jpg file into a numpy array

def get_faces(img_name):
	given_image = face_recognition.load_image_file(img_name)

	# Find all the faces in the image
	face_locations = face_recognition.face_locations(given_image)

	number_of_faces = len(face_locations)
	print("We found {} face(s) in this image.".format(number_of_faces))

	# Load the image into a Python Image Library object so that we can draw on top of it and display it
	pil_image = PIL.Image.fromarray(given_image)

	for face_location in face_locations:
		# Print the location of each face in this image. Each face is a list of pixel co-ordinates in (top, right, bottom, left) order.
		top, left, bottom, right = face_location
		print("A face is detected at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
		
		draw = PIL.ImageDraw.Draw(pil_image)
		draw.rectangle([left, top, right, bottom], outline="yellow", width=3)

	pil_image.save(img_name)
	# Display the image on screen with detected faces
	# pil_image.show()