# Coding Agent in Python

This project is part of the Boot.dev Backend developer Path: Course [Build an AI Agent with Python](https://www.boot.dev/courses/build-ai-agent-python)

If you are learning (or plan to learn) back-end development and didn't hear about Boot.dev, check out [their website](https://www.boot.dev).

## Installation

The project uses `uv` to manage dependencies. After installing [uv](), you can run `uv pip install -r pyproject.toml` to install dependencies

## Usage

You can run the AI Agent with `uv run main.py "How does the program in the root folder operate?"`

The root folder is hard coded in main.py: constant WORKING_DIRECTORY

See Warning, why working directory is hard coded.

## Built with

The AI Agent was built usint Python 3, and uses the Gemini Flash 2.0 AI Model.

The Agent is able to list the contents of a directory within the working directory, read and write the content of files, and execute Python files within the working directory and its subdirectories.

The functions for these operations can be found in the "functions" folder and access to these functions was given to the Agent by creating separate schemas for these functions, and adding these schemas as Tools. The actual calling of the functions is handled by a `call_function()` function, which runs the appropriate imported function based on the contents of the LLM's response.

The code uses a loop to keep track of the process, and makes it possible for the AI Agent to see its previous attempts and steps, including text messages by the model and results of the use of its tools.

## Warning

This is a toy project and not a "real" AI Agent. It is not intended for public use. The repo is more for the sake of documenting the process of building it and showcasing the result. The Agent is restricted to a hard coded working directory on purpose. You should not give it access to your file system!