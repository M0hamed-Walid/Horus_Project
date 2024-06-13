import base64

def image_to_base64(image_path):
 
    try:
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        base64_data = base64.b64encode(image_data)
        return base64_data.decode('utf-8')
    except Exception as e:
        print(f"Error converting image to base64: {e}")
        return None

# Example usage
image_path = 'nev2.jpg'
base64_image = image_to_base64(image_path)
if base64_image:
    # Save the base64 encoded image to a text file
    with open('image_base64.txt', 'w') as text_file:
        text_file.write(base64_image)
    print("Base64 encoded image saved to image_base64.txt")