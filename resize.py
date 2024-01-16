from PIL import Image
import os

def resize_images(source_dir, output_dir, size=(256,256)):
    # if not os.path.exists(output_dir):
    #     os.mkdir(output_dir)
    
    for filename in os.listdir(source_dir):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"): # add any other image types if you need.
            print(f'Resizing image {filename}')
            img = Image.open(os.path.join(source_dir, filename))
            img = img.resize(size, Image.ANTIALIAS)
            img.save(os.path.join(output_dir, filename))

source_dir = 'to_resize'  # path to the directory with images
output_dir = 'resized'  # path to the directory where resized images will be saved
resize_images(source_dir, output_dir)

