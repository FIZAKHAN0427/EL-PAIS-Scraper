import requests
import os


def download_image(image_url, index):

    try:

        if not image_url:
            return ""

        os.makedirs("images", exist_ok=True)

        image_path = os.path.join("images", f"article_{index}.jpg")

        response = requests.get(image_url, timeout=15)

        response.raise_for_status()

        with open(image_path, "wb") as f:
            f.write(response.content)

        print(f"✓ Image saved: {image_path}")

        return image_path

    except Exception as e:

        print(f"Image download failed: {e}")

        return ""