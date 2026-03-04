import os
import shutil

path = os.path.expanduser("~/Desktop")
destination = os.path.expanduser("~/Desktop/My_Analyst_Photos")

if not os.path.exists(destination):
    os.makedirs(destination)

files = os.listdir(path)

for file in files:
    # --- THE SAFETY CHECK ---
    # If "IMPORTANT" is in the filename, skip it!
    if "IMPORTANT" in file.upper():
        print(f"Skipping {file} because it is marked as important.")
        continue 
    # ------------------------

    if file.endswith(".png") or file.endswith(".jpg"):
        shutil.move(os.path.join(path, file), os.path.join(destination, file))
        print(f"Moved {file} to your new folder!")
