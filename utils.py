import datetime
import os


def benedictus_ascii_art():
  benedictus = '''
     ___ ___ _  _ ___ ___ ___ ___ _____ _   _ ___ 
    | _ ) __| \| | __|   \_ _/ __|_   _| | | / __|
    | _ \ _|| .` | _|| |) | | (__  | | | |_| \__ \\
    |___/___|_|\_|___|___/___\___| |_|  \___/|___/
    
  Author: Benedictus ©
  Community: https://t.me/alex4ndriagroup
  Version: Beta 0.1
  '''
  print(benedictus)


def verified_folder(folder_path):
  if os.path.isdir(folder_path):
    return folder_path
  return


def get_exiftool_path():
  return os.path.join(os.path.dirname(__file__), 'bin', 'exiftool')


def get_file_paths(folder_path):
  return [os.path.join(root, file) for root, _, files in os.walk(folder_path) for file in files]


def log_error(error_message, error_file='exiftool_errors.txt'):
  with open(error_file, 'a') as file:
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file.write(f'{timestamp} - {error_message}\n')
