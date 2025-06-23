import os


def get_absolute_path(working_directory, relative_path):
    working_directory_absolute_path = os.path.abspath(working_directory)
    joined_path = os.path.join(working_directory_absolute_path, relative_path)
    absolute_path = os.path.abspath(joined_path)

    return absolute_path
    

def is_outside_directory(outer_directory, absolute_path):
    outer_directory_absolute_path = os.path.abspath(outer_directory)

    return not absolute_path.startswith(outer_directory_absolute_path)