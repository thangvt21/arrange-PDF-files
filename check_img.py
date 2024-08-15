import hashlib


def calculate_md5(image_path):
    # Open the image file in binary mode
    with open(image_path, "rb") as image_file:
        # Read the file data
        file_data = image_file.read()
        # Generate the MD5 hash
        md5_hash = hashlib.md5(file_data).hexdigest()
    return md5_hash


def compare_images_md5(image1_path, image2_path):
    # Calculate MD5 hash for both images
    md5_image1 = calculate_md5(image1_path)
    print(md5_image1)
    md5_image2 = calculate_md5(image2_path)
    print(md5_image2)
    # Compare the hashes
    return md5_image1 == md5_image2


# Example usage
image1_path = "E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\LVVMX9OF9.png"
image2_path = "E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\LVVMX9OF9.png"

are_images_same = compare_images_md5(image1_path, image2_path)
if are_images_same:
    print("The images are same.")
else:
    print("The images are different.")
