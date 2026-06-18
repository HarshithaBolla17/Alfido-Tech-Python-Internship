import os
import shutil

# Folder containing files
source_folder = "test_folder"

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "PDFs": [".pdf"],
    "Videos": [".mp4"],
    "Audio": [".mp3"],
    "Text": [".txt"]
}

# Loop through all files
for file in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file)

    # Check if it's a file
    if os.path.isfile(file_path):

        # Get extension
        extension = os.path.splitext(file)[1].lower()

        moved = False

        # Match extension with category
        for folder_name, extensions in file_types.items():

            if extension in extensions:

                # Create folder if not exists
                target_folder = os.path.join(source_folder, folder_name)

                os.makedirs(target_folder, exist_ok=True)

                # Move file
                shutil.move(
                    file_path,
                    os.path.join(target_folder, file)
                )

                print(f"{file} moved to {folder_name}")

                moved = True
                break

        # Files with unknown type
        if not moved:
            print(f"No category found for {file}")