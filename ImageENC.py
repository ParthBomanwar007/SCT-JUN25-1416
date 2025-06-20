from PIL import Image
def process_image(image_path, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    for y in range(img.height):
        for x in range(0, img.width - 1, 2):
            # Swap each pair of left-right pixels
            pixels[x, y], pixels[x + 1, y] = pixels[x + 1, y], pixels[x, y]

    img.save(output_path)
    print("Image saved as:", output_path)

print("Simple Image Tool")
print("1.encrypt\n2.decrypt")
action = input("Choose Option:").strip().lower()
input_file = input("Enter input image filename (e.g., input.png): ")
output_file = input("Enter output image filename (e.g., output.png): ")

if action in ['1', '2']:
    process_image(input_file, output_file)
else:
    print("Invalid input! Please type 'encrypt' or 'decrypt'.")
