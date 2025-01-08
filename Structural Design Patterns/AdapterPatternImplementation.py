Adapter code

# Target Interface: ImageProcessor (expects JPEG images)
class ImageProcessor:
    def process_jpeg(self, file_name):
        pass


# Adaptee: PngImage (handles PNG images, not compatible with the system)
class PngImage:
    def process_png(self, file_name):
        print(f"Processing PNG image: {file_name}")


# Adapter: PngToJpegAdapter (converts PNG to JPEG format)
class PngToJpegAdapter(ImageProcessor):
    def __init__(self, png_image):
        self.png_image = png_image
    
    def process_jpeg(self, file_name):
        print(f"Converting PNG to JPEG and processing: {file_name}")
        self.png_image.process_png(file_name)  # Convert PNG to JPEG and call the PNG method


# Client Code
def client_code():
    # Suppose Rahul uploads a PNG image
    png_image = PngImage()
    
    # The system expects JPEG images, but the uploaded image is in PNG format
    image_processor = PngToJpegAdapter(png_image)
    
    # The system now processes the image as if it was in JPEG format
    image_processor.process_jpeg("image.png")


if __name__ == "__main__":
    client_code()

