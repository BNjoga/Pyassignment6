import requests
import os
from urllib.parse import urlparse
import hashlib

def fetch_image(url):
    """Download and save an image from a given URL."""
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image with timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # Generate fallback filename if none found
        if not filename:
            filename = "downloaded_image.jpg"

        # Prevent duplicate images by hashing content
        file_hash = hashlib.md5(response.content).hexdigest()
        name, ext = os.path.splitext(filename)
        filename = f"{name}_{file_hash[:6]}{ext or '.jpg'}"

        filepath = os.path.join("Fetched_Images", filename)

        # Check if file already exists
        if os.path.exists(filepath):
            print(f"⚠ Image already exists: {filename}")
            return

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Allow multiple URLs separated by space
    urls = input("Please enter one or more image URLs (separated by space): ").split()

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
