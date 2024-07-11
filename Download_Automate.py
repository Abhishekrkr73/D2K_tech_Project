import os
import time
import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout

base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
save_dir = "D:/taxi"
os.makedirs(save_dir, exist_ok=True)

# List of file names to download

file_names = []
for taxi_color in ['green', 'yellow', 'fhv', 'fhvhv']:
    for month in range(1, 13):
        file  = '{}_tripdata_2019-{}.parquet'.format(taxi_color, str(month).zfill(2))
        file_names.append(file)


def download_file(file_name, retries=5, delay=3):
    url = f"{base_url}{file_name}"
    save_path = os.path.join(save_dir, file_name)

    for attempt in range(retries):
        try:
            print(f"Attempting to download {file_name}, Attempt {attempt + 1}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an exception for HTTP errors

            with open(save_path, 'wb') as file:
                file.write(response.content)

            print(f"Successfully downloaded {file_name}")
            break  # Break the loop if the download is successful
        except (HTTPError, ConnectionError, Timeout) as e:
            print(f"Error downloading {file_name}: {e}")
            if attempt < retries - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"Failed to download {file_name} after {retries} attempts.")
        except RequestException as e:
            print(f"RequestException occurred: {e}")
            break  # For other RequestExceptions, don't retry

if __name__ == "__main__":
    for file_name in file_names:
        download_file(file_name)
