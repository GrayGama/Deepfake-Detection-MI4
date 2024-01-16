import os

def rename_files(directory):
    """
    Renames all files in the given directory with a specified prefix.

    :param directory: Path to the directory containing the files.
    :param prefix: The prefix to be added to each file.
    """
    for i, filename in enumerate(os.listdir(directory)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            name, ext = os.path.splitext(filename)
            # new_name = f"real_{i}{ext}"
            new_name = f"df{name}_{i+5102}{ext}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed '{filename}' to '{new_name}'")

# Example usage
directory = 'MesoNet/deepfake_database_v3/augmentation_data/train/df'  # Replace with the path to your directory
# prefix = 'image'                       # Replace with your desired prefix

rename_files(directory)

print("Done")