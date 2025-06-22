import os


def write_file(working_directory, file_path, content):
    try:
        working_directory_absolute_path = os.path.abspath(working_directory)
        file_joined_path = os.path.join(working_directory_absolute_path, file_path)
        file_absolute_path = os.path.abspath(file_joined_path)

        if not file_absolute_path.startswith(working_directory_absolute_path):
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