import os
import random
from PIL import Image, ImageEnhance

def scatter_images(input_folder, output_folder, num_images_to_generate):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all image files from input folder with valid image extensions
    valid_image_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # Add more extensions if needed
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f)) and os.path.splitext(f)[1].lower() in valid_image_extensions]

    # Generate the specified number of scattered images
    for i in range(num_images_to_generate):
        # Determine the number of images to use for this scatter generation (random from 1 to 4)
        num_images_used = random.randint(1, 4)

        # Adjust density based on the number of assets used
        if num_images_used == 1:
            density = 1.5
        elif num_images_used == 2:
            density = 1
        elif num_images_used == 3:
            density = .8
        else:
            density = .6

        # Select random image files for this scatter generation
        selected_files = random.sample(image_files, num_images_used)

        # Create a new canvas for each scattered image
        canvas = Image.new("RGBA", (1700, 2000), (0, 0, 0, 0))

        # Paste randomly selected images onto the canvas
        for image_file in selected_files:
            # Load image
            image_path = os.path.join(input_folder, image_file)
            image = Image.open(image_path).convert("RGBA")

            # Calculate number of repetitions based on density
            repetitions = int((density / 100) * 1700 * 2000 / (image.width * image.height))

            # Paste images randomly on canvas
            for _ in range(repetitions):
                x_offset = random.randint(0, 1700 - image.width)
                y_offset = random.randint(0, 2000 - image.height)

                # Create a copy of the image
                image_copy = image.copy()

                # Randomize image size
                random_size = random.uniform(0.5, 7)
                new_size = (int(image_copy.width * random_size), int(image_copy.height * random_size))
                image_copy = image_copy.resize(new_size, Image.LANCZOS)

                # Randomize image rotation
                random_rotation = random.randint(0, 360)
                image_copy = image_copy.rotate(random_rotation, expand=True)

                # Randomize image color adjustments
                image_copy = ImageEnhance.Color(image_copy).enhance(random.uniform(0.5, 2.0))

                # Randomize transparency
                alpha = image_copy.split()[3]  # Get the alpha channel
                alpha = ImageEnhance.Brightness(alpha).enhance(random.uniform(0.2, 1))  # Random transparency
                image_copy.putalpha(alpha)

                # Paste the image onto canvas
                canvas.paste(image_copy, (x_offset, y_offset), image_copy)

        # Save scattered image as PNG with transparent background
        scattered_image_path = os.path.join(output_folder, f"scattered_{i + 1}.png")
        canvas.save(scattered_image_path)

    print(f"Scattering completed. {num_images_to_generate} images saved in:", output_folder)

if __name__ == "__main__":
    input_folder = input("Enter the path to the input folder: ").strip()  # Prompt user for input folder path
    num_images_to_generate = int(input("Enter the number of scattered images to generate: ").strip())  # Prompt user for number of images to generate
    output_folder = os.path.join(input_folder, "scattered_images")
    scatter_images(input_folder, output_folder, num_images_to_generate)
