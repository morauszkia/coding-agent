import os
from functions.utils import get_absolute_path, is_outside_directory


def get_files_info(working_directory, directory=None):
    try:
        directory_absolute_path = get_absolute_path(working_directory, directory)

        if is_outside_directory(working_directory, directory_absolute_path):
            print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
            return ""

        if not os.path.isdir(directory_absolute_path):
            print(f'Error: "{directory}" is not a directory')
            return ""

        directory_contents = os.listdir(directory_absolute_path)

        contents_string = ""

        for item in directory_contents:
            item_path = os.path.join(directory_absolute_path, item)
            contents_string += (f"- {item}: file_size={os.path.getsize(item_path)} bytes , is_dir={os.path.isdir(item_path)}\n")

        return contents_string

    except Exception as e:
        print(f"Error: {e}")

