Your code looks good for a simple image encryption and decryption tool using pixel manipulation. However, there are a few improvements and considerations you might want to keep in mind:

1. **Security**: The encryption method you're using is quite simple, adding a constant value to each pixel. This is susceptible to basic attacks. For better security, you might want to explore more robust encryption algorithms like AES.

2. **Key Management**: In real-world scenarios, key management is crucial. You might want to consider how keys are generated, stored, and exchanged securely.

3. **Error Handling**: It's always good practice to include error handling in your code, especially when dealing with file operations or image processing.

4. **User Interaction**: If you plan to expand this into a more user-friendly tool, you could add functionality for users to input their own image paths and keys.

5. **Testing**: Ensure to test your code thoroughly with different types of images and keys to ensure it works as expected in various scenarios.

Here's a slightly modified version of your code with some improvements:

```python
from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        encrypted_img_array = img_array + key
        encrypted_img = Image.fromarray(encrypted_img_array.astype(np.uint8))

        encrypted_img.save("encrypted_image.png")
        print("Image encrypted successfully.")
    except Exception as e:
        print("Error encrypting image:", e)

def decrypt_image(image_path, key):
    try:
        encrypted_img = Image.open(image_path)
        encrypted_img_array = np.array(encrypted_img)
        decrypted_img_array = encrypted_img_array - key
        decrypted_img = Image.fromarray(decrypted_img_array.astype(np.uint8))

        decrypted_img.save("decrypted_image.png")
        print("Image decrypted successfully.")
    except Exception as e:
        print("Error decrypting image:", e)

def main():
    try:
        image_path = input("Enter the path to the image: ")

        # Key for encryption (you can choose any integer value)
        key = int(input("Enter the encryption key: "))

        # Encrypt image
        encrypt_image(image_path, key)

        # Decrypt image
        decrypt_image("encrypted_image.png", key)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the key.")

if __name__ == "__main__":
    main()
```

These modifications enhance the error handling and allow user interaction for inputting image paths and keys.
