import os
import subprocess
from functions.utils import get_absolute_path, is_outside_directory


def run_python_file(working_directory, file_path):
    try:
        file_absolute_path = get_absolute_path(working_directory, file_path)

        if is_outside_directory(working_directory, file_absolute_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(file_absolute_path):
            return f'Error: File "{file_path}" not found.'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        process_result = subprocess.run(["python3", file_absolute_path], capture_output=True, timeout=30, cwd=working_directory)

        result_string = ""

        if process_result.stdout:
            result_string += f"STDOUT: {process_result.stdout.decode()}\n"

        if process_result.stderr:
            result_string += f"STDERR: {process_result.stderr.decode()}\n"

        if process_result.returncode != 0:
            result_string += f"Process exited with code {process_result.returncode}\n"

        if result_string == "":
            return "No output produced."
        
        return result_string

    except Exception as e:
        print(f"Error: executing Python file: {e}")