import os

def create_file(filename):
  os.system(f'touch {filename}')

def add_line(file, text):
  with open(file, mode='a', encoding='utf-8') as log_file:
    log_file.write(text)
