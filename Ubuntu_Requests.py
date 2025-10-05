import requests
import os
import hashlib
from urllib.parse import urlparse
from requests.exceptions import RequestException, Timeout, ConnectionError, HTTPError

# Global set to track downloaded image hashes and prevent duplicates
downloaded_hashes = set()


def get_image_hash(content):
    """Generate a unique MD5 hash for the image content."""
    return hashlib.md5(content).hexdigest()


def is_duplicate_image(content):
    """Check if an image with the same content has already been downloaded."""
    image_hash = get_image_hash(content)
    if image_hash in downloaded_hashes:
        return True
    downloaded_hashes.add(image_hash)
    return False


def is_safe_to_download(response, max_size_mb=10):
    """
    Perform safety checks before saving the file.
    Returns (is_safe: bool, message: str)
    """
    # Check Content-Type header
    content_type = response.headers.get('Content-Type', '')
    if not content_type.startswith('image/'):
        return False, f"Unsupported file type: {content_type}"

    # Check Content-Length header
    content_length = response.headers.get('Content-Length')
    if content_length:
        max_size_bytes = max_size_mb * 1024 * 1024
        if int(content_length) > max_size_bytes:
            return False, f"File too large: {content_length} bytes"

    return True, "OK"


def fetch_single_image(url, download_folder="Fetched_Images"):
    """
    Fetches and saves a single image from a URL with safety checks.
    """
    try:
        print(f"\n🔄 Attempting to fetch: {url}")

        # Create directory if it doesn't exist
        os.makedirs(download_folder, exist_ok=True)

        # Fetch the image with a timeout and stream to avoid loading large files into memory at once
        response = requests.get(url, timeout=15, stream=True)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx/5xx)

        # Read a small chunk first for initial checks
        chunk = next(response.iter_content(chunk_size=1024))

        # Combine the first chunk with the rest of the content for hash checking
        full_content = chunk + b''.join(response.iter_content(chunk_size=1024))

        # Safety check 1: Validate HTTP headers
        safe, message = is_safe_to_download(response)
        if not safe:
            print(f"✗ Safety check failed for {url}: {message}")
            return False

        # Safety check 2: Check for duplicate image
        if is_duplicate_image(full_content):
            print(f"⏭️ Duplicate image skipped: {url}")
            return True  # Not an error, but no download needed

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename or '.' not in filename:
            # Use the content type to generate a proper extension
            content_type = response.headers.get(
                'Content-Type', '').split('/')[-1]
            ext = content_type if content_type in [
                'jpeg', 'png', 'gif', 'webp'] else 'jpg'
            filename = f"downloaded_image.{ext}"

        # Save the image
        filepath = os.path.join(download_folder, filename)

        # Write the already downloaded content to file
        with open(filepath, 'wb') as f:
            f.write(full_content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        return True

    except Timeout:
        print(f"✗ Request timed out for: {url}")
    except ConnectionError:
        print(
            f"✗ Connection error for: {url} - Please check the URL and your network.")
    except HTTPError as e:
        print(
            f"✗ HTTP error for {url}: {e.response.status_code} - {e.response.reason}")
    except RequestException as e:
        print(f"✗ Request error for {url}: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred with {url}: {e}")

    return False


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web")
    print("\"A person is a person through other persons.\" - Ubuntu philosophy\n")

    # Get URLs from user
    url_input = input(
        "Please enter image URLs (separate multiple URLs with commas): ").strip()

    if not url_input:
        print("No URLs provided. Exiting.")
        return

    urls = [url.strip() for url in url_input.split(',') if url.strip()]
    successful_downloads = 0

    print(f"\n🔄 Preparing to fetch {len(urls)} image(s)...")

    for url in urls:
        if fetch_single_image(url):
            successful_downloads += 1

    # Final summary
    print(f"\n{'='*50}")
    print("Download Summary:")
    print(f"✓ Successful: {successful_downloads}")
    print(f"✗ Failed: {len(urls) - successful_downloads}")
    print(f"📂 Total images in collection: {len(downloaded_hashes)}")

    if successful_downloads > 0:
        print("\nConnection strengthened. Community enriched.")
    else:
        print("\nNo images were fetched this time, but the connection remains.")


if __name__ == "__main__":
    main()

