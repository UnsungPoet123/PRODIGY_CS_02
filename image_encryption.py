# Import the Image module from Pillow library
from PIL import Image


# =========================
# FUNCTION: ENCRYPT IMAGE
# =========================
def encrypt_image(input_path, output_path, key):
    """
    Encrypts an image by adding a key value to each pixel.

    Parameters:
    input_path (str): Path to the original image
    output_path (str): Path to save the encrypted image
    key (int): Encryption key (number)
    """

    # Open the image
    img = Image.open(input_path)

    # Load pixel data so we can modify it
    pixels = img.load()

    # Loop through every pixel (width x height)
    for x in range(img.width):
        for y in range(img.height):
            # Get the RGB values of the current pixel
            r, g, b = pixels[x, y]

            # Modify each color channel by adding the key
            # % 256 ensures values stay within 0–255 range
            new_r = (r + key) % 256
            new_g = (g + key) % 256
            new_b = (b + key) % 256

            # Assign the new encrypted values back to the pixel
            pixels[x, y] = (new_r, new_g, new_b)

    # Save the encrypted image
    img.save(output_path)

    print("✅ Image encrypted successfully!")


# =========================
# FUNCTION: DECRYPT IMAGE
# =========================
def decrypt_image(input_path, output_path, key):
    """
    Decrypts an image by subtracting the key value from each pixel.

    Parameters:
    input_path (str): Path to the encrypted image
    output_path (str): Path to save the decrypted image
    key (int): Encryption key (must be same as used in encryption)
    """

    # Open the encrypted image
    img = Image.open(input_path)

    # Load pixel data
    pixels = img.load()

    # Loop through every pixel
    for x in range(img.width):
        for y in range(img.height):
            # Get current pixel values
            r, g, b = pixels[x, y]

            # Reverse the encryption by subtracting the key
            new_r = (r - key) % 256
            new_g = (g - key) % 256
            new_b = (b - key) % 256

            # Assign decrypted values back to pixel
            pixels[x, y] = (new_r, new_g, new_b)

    # Save the decrypted image
    img.save(output_path)

    print("✅ Image decrypted successfully!")


# =========================
# MAIN PROGRAM
# =========================
def main():
    print("=== Image Encryption Tool ===")

    # Ask user what they want to do
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()

    # Get file paths from user
    input_image = input("Enter input image path (e.g. sample.jpg): ")
    output_image = input("Enter output image path: ").strip().strip('"')

    # Ensure file has an extension
    if not (output_image.endswith(".jpg") or output_image.endswith(".png")):
        output_image += ".jpg"

    # Get encryption key from user
    try:
        key = int(input("Enter a numeric key (e.g. 50): "))
    except ValueError:
        print("❌ Invalid key! Please enter a number.")
        return

    # Perform operation based on user choice
    if choice == 'e':
        encrypt_image(input_image, output_image, key)

    elif choice == 'd':
        decrypt_image(input_image, output_image, key)

    else:
        print("❌ Invalid choice! Please enter 'e' or 'd'.")


# Run the program
if __name__ == "__main__":
    main()