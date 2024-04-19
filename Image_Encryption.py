#Pratham Koturwar
#Develop a simple image encryption tool using pixel manipulation.
from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img_array = np.array(img)
    encrypted_img_array = img_array + key
    encrypted_img = Image.fromarray(encrypted_img_array.astype(np.uint8))

    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(image_path, key):
    encrypted_img = Image.open(image_path)
    encrypted_img_array = np.array(encrypted_img)
    decrypted_img_array = encrypted_img_array - key
    decrypted_img = Image.fromarray(decrypted_img_array.astype(np.uint8))

    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")

def main():
    image_path = "OIP.jpeg"#image path

    # Key for encryption (you can choose any integer value)
    key = 50

    # Encrypt image
    encrypt_image(image_path, key)

    # Decrypt image
    decrypt_image("encrypted_image.png", key)

if __name__ == "__main__":
    main()