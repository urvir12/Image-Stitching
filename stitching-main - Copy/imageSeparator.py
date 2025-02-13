from PIL import Image
import random

def split_image_random(image_path, output_dir):
    original_image = Image.open(image_path)
    width, height = original_image.size

    # Calculate the height of each segment
    segment_height = height // 3

    # Generate random widths for the three components with overlap
    left_width = random.randint(50, width // 2)  # Adjust the range as needed
    right_width = random.randint(50, width // 2)  # Adjust the range as needed
    middle_width = width - left_width - right_width + width*.3*random.random()  # Slightly differing widths with overlap

    # Split the image into three components with overlap
    left_image = original_image.crop((0, 0, left_width, height))
    overlap1 = width*.3*random.random()
    overlap2 = width*.3*random.random()
    middle_image = original_image.crop((left_width - overlap1, 0, left_width + middle_width + overlap2, height))
    right_image = original_image.crop((left_width + middle_width - overlap2, 0, width, height))

    # Save the three components
    left_image.save(f"left_image.jpg")
    middle_image.save(f"middle_image.jpg")
    right_image.save(f"right_image.jpg")

if __name__ == "__main__":
    image_path = "weir_1.jpg"  # Replace with the path to your input image
    output_directory = '..'  # Replace with the directory where you want to save the output images

    split_image_random(image_path, output_directory)
