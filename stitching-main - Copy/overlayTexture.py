import cv2
import os
import numpy as np

def overlay_texture(texture_path, image_paths, output_folder='output'):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load texture image
    texture = cv2.imread(texture_path)
    texture_height, texture_width, _ = texture.shape

    # Loop through the list of images
    for i, image_path in enumerate(image_paths):
        # Load the image
        image = cv2.imread(image_path)
        image_height, image_width, _ = image.shape

        # Calculate the overlap size (10% of the texture size)
        overlap_size = int(0.1 * texture_height)

        # Resize the texture to match the overlap size
        texture_resized = cv2.resize(texture, (image_width, overlap_size))

        # Create a mask for the texture
        mask = (texture_resized[:, :, 0] != 0)

        # Calculate the region to overlay on the image
        start_row = max(0, i * overlap_size)
        end_row = min(image_height, start_row + overlap_size)

        # Resize the mask to match the region size
        mask_resized = cv2.resize(mask.astype(np.uint8), (image_width, end_row - start_row))

        # Overlay the texture on the image
        image[start_row:end_row, :, :] = (1 - mask_resized[:, :, None]) * image[start_row:end_row, :, :] + \
                                          mask_resized[:, :, None] * texture_resized

        # Save the resulting image
        output_path = os.path.join(output_folder, f'output_image_{i + 1}.png')
        cv2.imwrite(output_path, image)


if __name__ == "__main__":
    # Provide the path to the texture image and the list of image paths
    texture_path = 'weir_1.jpg'
    image_paths = ['PhoneArm1.jpg', 'PhoneArm2.jpg', 'PhoneArm3.jpg']

    # Overlay the texture onto each image
    overlay_texture(texture_path, image_paths)
