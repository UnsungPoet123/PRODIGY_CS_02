# Image Encryption Tool

A simple Python-based image encryption and decryption tool that uses pixel manipulation techniques to transform images securely.

---

## Overview

This project demonstrates how basic image encryption works by modifying pixel values using mathematical operations. The tool allows users to encrypt an image and later decrypt it back to its original form using the same key.

---

##  Features

* Encrypt images using a numeric key
* Decrypt images back to original form
* Simple and beginner-friendly logic
* Fast processing using pixel-level operations
* Works with common image formats like `.jpg` and `.png`

---

## Technologies Used

* Python
* Pillow (PIL)

---

## Project Structure

```
Image encryption/
│
├── image_encryption.py   # Main program
├── sample_image.jpg      # Input image
└── README.md             # Project documentation
```

---

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/image-encryption-tool.git
```

2. Navigate to the project folder:

```
cd image-encryption-tool
```

3. Install dependencies:

```
pip install pillow
```

---

## How to Use

1. Run the program:

```
python image_encryption.py
```

2. Choose an option:

```
Enter 'e' to encrypt or 'd' to decrypt
```

3. Provide:

* Input image path (e.g. `sample_image.jpg`)
* Output image path (e.g. `encrypted.jpg`)
* Encryption key (numeric value)

---

## Example

### Encryption:

* Input: `sample_image.jpg`
* Output: `encrypted.jpg`
* Key: `50`

### Decryption:

* Input: `encrypted.jpg`
* Output: `decrypted.jpg`
* Key: `50`

---

## How It Works

Each pixel in an image contains RGB (Red, Green, Blue) values ranging from 0 to 255.

### Encryption:

* Adds a key value to each RGB channel
* Uses modulo operation to keep values within range

### Decryption:

* Subtracts the same key value
* Restores original pixel values

---

## Note

This is a basic encryption technique for educational purposes and should not be used for real-world security applications.

---

## Learning Outcome

* Understanding of image processing basics
* Pixel-level data manipulation
* Implementation of simple encryption logic
* Working with external Python libraries

---

## Author

**John Apomah Elike**

---

## License

This project is open-source and available under the MIT License.
