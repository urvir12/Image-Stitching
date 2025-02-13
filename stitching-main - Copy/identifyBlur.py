import cv2
import numpy as np

def calculate_laplacian_variance(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the Laplacian
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    # Calculate the variance of the Laplacian
    variance = laplacian.var()

    return variance

def identify_blurry_areas(panorama_path, images_paths):
    # Load the panorama
    panorama = cv2.imread(panorama_path)

    # Initialize a list to store blurry areas
    blurry_areas = []

    # Loop through the images in the panorama
    for image_path in images_paths:
        # Load the individual image
        image = cv2.imread(image_path)

        # Resize the image to match the panorama size (assuming the images have the same dimensions)
        image = cv2.resize(image, (panorama.shape[1], panorama.shape[0]))

        # Calculate the Laplacian variance for the image
        variance = calculate_laplacian_variance(image)

        # Define a threshold for blur (you can adjust this threshold based on your needs)
        blur_threshold = 1000.0

        # If the variance is below the threshold, mark the area as blurry
        if variance < blur_threshold:
            blurry_areas.append(image_path)

    return blurry_areas

if __name__ == "__main__":
    # Provide the path to the panorama image and the list of image paths
    panorama_path = 'path/to/panorama.jpg'
    images_paths = ['path/to/image1.jpg', 'path/to/image2.jpg', 'path/to/image3.jpg']

    # Identify blurry areas in the panorama
    blurry_areas = identify_blurry_areas(panorama_path, images_paths)

    # Print the paths of blurry areas
    print("Blurry areas in the panorama:")
    for area in blurry_areas:
        print(area)
