# -------------------------- Description ---------------------------
# 
# For when you want to steal other people's files from the internet.
# Should be able to download most file types provided the names
# are in a predictable format.
#
# ------------------------------------------------------------------

import requests
import os

base_url = "https://example.com/path/to/assets/"

# Create a folder to store images
folder_name = "assets"
os.makedirs(folder_name, exist_ok=True)

i = 1
while(1):
    image_url = f"{base_url}/imageName{i}.png"
    i += 1

    try:
        response = requests.get(image_url)

        if response.status_code == 200:
            file_path = os.path.join(folder_name, os.path.basename(image_url))
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"Image {os.path.basename(image_url)} downloaded successfully!")

        else:
            print(f"Failed to download image at: {image_url}")
            print("Possibly downloaded all assets")
            break

    except Exception as e:
        print("An error occurred: ", e)
        break
