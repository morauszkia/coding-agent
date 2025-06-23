import os
from functions.utils import get_absolute_path, is_outside_directory


def write_file(working_directory, file_path, content):
    try:
        file_absolute_path = get_absolute_path(working_directory, file_path)

        if is_outside_directory(working_directory, file_absolute_path):
            print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
            return ""

        if not os.path.exists(file_absolute_path):
            directories = os.path.dirname(file_path)
            if directories:
                os.makedirs(directories, exist_ok=True)
            
        with open(file_absolute_path, "w") as f:
            f.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: {e}")