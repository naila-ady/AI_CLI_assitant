from email import message
from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging
import os
from config import config
from rich import print
enable_verbose_stdout_logging()
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())


@function_tool(strict_mode=False)
def file_and_folder_handler(
    file_name : str = None,
    folder_name: str = None,
    content : str = None,
    file_path : str = None,
    read : bool = None
):
    try:
        result_messages = []

        # Create folder 
        if folder_name:
            os.makedirs(folder_name, exist_ok=True)
            result_messages.append(f"Folder '{folder_name}' is ready")

        if read and file_path:
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    file_data = f.read()
                result_messages.append(f"content of {file_path} is {file_data}")
            else :
                result_messages.append(f"File {file_path} does not exist")
        if file_name:
            if folder_name:
                full_path = os.path.join(folder_name, file_name)
            else:
                full_path = file_name
            
            with open(full_path, "w") as f:
                f.write(content if content else "")

            result_messages.append(f"File '{full_path}' is created successfully")
            if content:
                result_messages.append(f"Content written to '{full_path}'")
        print (f"{result_messages}")
        return "\n".join(result_messages)
        

    except Exception as e:
        print(f"Error occurred: {e}")

file_handler_agent = Agent(
    name="FileHandlerAgent",

    instructions="""you are helpfull file management assistant.""",
    tools=[file_and_folder_handler]
)
    

result = Runner.run_sync(
    starting_agent=file_handler_agent,
    input="first create folder named 'ali' and inside it create a file 'naila.py' and inside it write my name is ali inside the file",
    run_config=config
)
print(result.last_agent)
# print (f"{result_messages}")

print(result.final_output)
