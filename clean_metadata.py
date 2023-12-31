import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import benedictus_ascii_art
import os
from tqdm import tqdm


def get_exiftool_config():
  return [
    '-charset', 'filename=utf8',
    '-all=',
    '-q',
    '-overwrite_original',
    '-m',
    '-FileCreateDate="1973:09:30 01:00:00"',
    '-FileModifyDate="1973:09:30 01:00:00"', 
    '-DateTimeOriginal="1973:09:30 01:00:00"',
    '-CreateDate="1973:09:30 01:00:00"',
    '-ModifyDate="1973:09:30 01:00:00"',
  ]


def get_exiftool_path():
  return os.path.join(os.path.dirname(__file__), 'bin', 'exiftool')


def get_file_paths(folder_path):
  file_paths = []
  for root, dirs, files in os.walk(folder_path):
    for file in files:
      file_path = os.path.join(root, file)
      file_paths.append(file_path)
  return file_paths


def clear_metadata(file_path):
  subprocess.run([get_exiftool_path()] + get_exiftool_config() + [file_path], stderr=subprocess.DEVNULL)


def main(folder_path):
  if os.path.isdir(folder_path):
    file_paths = get_file_paths(folder_path)
    with ThreadPoolExecutor(max_workers=5) as executor:
      futures = [executor.submit(clear_metadata, file_path) for file_path in file_paths]
      for future in tqdm(as_completed(futures), total=len(file_paths), desc="Processing"):
        future.result()


if __name__ == "__main__":
  benedictus_ascii_art()
  folder_path = input("Enter the folder path: ")
  main(folder_path)
  print()
  print(f'FINISHED SCRIPT')
