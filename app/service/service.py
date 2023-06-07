import random 
import os

def get_filename_ext(file_path):
    # имя файла без расширения и само расширение файла из заданного пути к файлу.
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, file_name):
    # определениe пути загрузки изображений
    new_file_name = random.randint(1, 1_000_000_000)
    name, ext = get_filename_ext(file_name)
    file_name_done = f'{new_file_name}{ext}'
    return f'property/{new_file_name}/{file_name_done}'

def upload_avatar_path(instance, file):
    # Построение пути к файлу, format: (media)/avatar/user_id/photo.jpg
    return f'avatar/user_{instance.id}/{file}'