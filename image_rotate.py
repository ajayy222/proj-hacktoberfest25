from PIL import Image

def rotate_image(input_path, output_path, angle):
    try:
        # Open image
        img = Image.open(input_path)

        # Rotate (expand=True keeps full image after rotation)
        rotated = img.rotate(angle, expand=True)

        # Save rotated image
        rotated.save(output_path)
        print(f"✅ Image rotated by {angle}° and saved as {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    # Example usage
    input_file = "myphoto.jpg"     # your image file
    output_file = "rotated.jpg"    # save result
    angle = 90                     # rotate by 90°, can be any number

    rotate_image(input_file, output_file, angle)
