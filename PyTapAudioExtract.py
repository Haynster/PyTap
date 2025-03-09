import os
import shutil
import zipfile
import subprocess
import sys

def extract_tap_as_zip(tap_file_path, extract_dir):
    if not os.path.isfile(tap_file_path):
        print(f"Error: The file '{tap_file_path}' does not exist.")
        return


    zip_file_path = tap_file_path[:-4] + ".zip"

    try:
        shutil.copyfile(tap_file_path, zip_file_path)

        os.makedirs(extract_dir, exist_ok=True)

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
            print(f"Extracted contents to '{extract_dir}'")

    except zipfile.BadZipFile:
        print(f"Error: The file '{tap_file_path}' is not a valid ZIP archive.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if os.path.exists(zip_file_path):
            os.remove(zip_file_path)

def clean_extracted_folder(extract_dir):
    for root, dirs, files in os.walk(extract_dir):
        if 'Assets' in dirs:
            assets_folder = os.path.join(root, 'Assets')
            parent_folder = root

            for item in os.listdir(parent_folder):
                item_path = os.path.join(parent_folder, item)
                if item != 'Assets':
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
            print(f"Cleaned up '{parent_folder}' to only contain 'Assets' folder.")
            break

def convert_m4a_to_mp3(assets_folder):
    for root, dirs, files in os.walk(assets_folder):
        for file in files:
            if file.endswith(".m4a"):
                m4a_path = os.path.join(root, file)
                mp3_path = os.path.join(root, file[:-4] + ".mp3")

                try:

                    command = [
                        "ffmpeg",
                        "-i", m4a_path,  
                        "-codec:a", "libmp3lame", 
                        "-qscale:a", "2",  # Quality setting (2 is good quality)
                        mp3_path 
                    ]
                    subprocess.run(command, check=True)
                    print(f"Converted '{m4a_path}' to '{mp3_path}'")

                    # Optionally, delete the original .m4a file after conversion
                    os.remove(m4a_path)
                    print(f"Deleted original file '{m4a_path}'")

                except subprocess.CalledProcessError as e:
                    print(f"Error converting '{m4a_path}': {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: PyTapAudioExtract.exe <tap_file>")
        return

    tap_file_path = sys.argv[1]
    extract_dir = "extracted_contents"

    extract_tap_as_zip(tap_file_path, extract_dir)
    clean_extracted_folder(extract_dir)

    for root, dirs, files in os.walk(extract_dir):
        if 'Assets' in dirs:
            assets_folder = os.path.join(root, 'Assets')
            convert_m4a_to_mp3(assets_folder)
            break

if __name__ == "__main__":
    main()