import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

model_name = "gemini-2.0-flash-001"
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Write or overwrite files
- Execute Python files with optional arguments

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose contents we want to read, relative to the working directory."
            )
        }
    )
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to which we want to write the content, relative to the working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content we want to write to the file specified by 'file_path'."
            )
        }
    )
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run Python files, with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to run, relative to the working direcory."
            )
        }
    )
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

arguments = sys.argv

if len(arguments) > 1:
    user_prompt = arguments[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
else:
    print("Please provide a prompt as the first command line argument")
    sys.exit(1)

response = client.models.generate_content(
    model=model_name, 
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
        )
    )

if len(arguments) > 2 and arguments[2] == "--verbose":
    print(f"User prompt: {arguments[1]}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if len(response.function_calls) > 0:
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")

else:
    print(response.text)