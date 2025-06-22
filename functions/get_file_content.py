import os


MAX_CHARACTER = 10_000

def get_file_content(working_directory, file_path):
    try:
        working_directory_absolute_path = os.path.abspath(working_directory)
        file_joined_path = os.path.join(working_directory_absolute_path, file_path)
        file_absolute_path = os.path.abspath(file_joined_path)

        if not file_absolute_path.startswith(working_directory_absolute_path):
            print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
            return ""

        if not os.path.isfile(file_absolute_path):
            print(f'Error: File not found or is not a regular file: "{file_path}"')
            return ""

        with open(file_absolute_path, "r") as f:
            file_content_string = f.read()

            if len(file_content_string) > MAX_CHARACTER:
                file_content_string = file_content_string[:MAX_CHARACTER] + f'\n[...File "{file_path}" truncated at 10000 characters]'

            return file_content_string

    except Exception as e:
        print(f"Error: {e}")