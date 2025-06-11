import os


def get_files_info(working_directory, directory=None):
    try:
        working_directory_absolute_path = os.path.abspath(working_directory)
        directory_joined_path = os.path.join(working_directory_absolute_path, directory)
        directory_absolute_path = os.path.abspath(directory_joined_path)

        if not directory_absolute_path.startswith(working_directory_absolute_path):
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

