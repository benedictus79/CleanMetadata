import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import benedictus_ascii_art, get_exiftool_path, get_file_paths, log_error, verified_folder
from tqdm import tqdm


def get_exiftool_config():
  return [
    '-charset', 
    'filename=utf8',
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


def clear_metadata(file_path):
  process = subprocess.run([get_exiftool_path()] + get_exiftool_config() + [file_path], stderr=subprocess.PIPE)
  if process.returncode != 0:
    log_error(process.stderr.decode())


def main(folder_path): 
  if verified_folder(folder_path):
    file_paths = get_file_paths(folder_path)
    with ThreadPoolExecutor(max_workers=5) as executor:
      futures = [executor.submit(clear_metadata, file_path) for file_path in file_paths]
      for future in tqdm(as_completed(futures), total=len(file_paths), desc='Processing'):
        future.result()


if __name__ == '__main__':
  benedictus_ascii_art()
  folder_path = input('Enter the folder path: ')
  main(folder_path)
