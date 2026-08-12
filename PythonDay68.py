# Exercise 7: Clutter Cleaner

import os

# Specify the path you want to check
folder_path = r"C:\Users\MasterofAsh\Desktop\Python Course\Exercise7Clutter"
folderName = os.path.basename(folder_path)
folderContents = os.listdir(folder_path)
# print(folderContents)

counter = 1

for file_name in folderContents:
    if file_name.lower().endswith(".png"):
        new_file_name = f"{counter}.png"

        old_full_path = os.path.join(folder_path, file_name)
        new_full_path = os.path.join(folder_path, new_file_name)

        os.rename(old_full_path, new_full_path)
        print(f"{file_name} renamed to {new_file_name}")
        counter += 1