from agents import Agent,function_tool,Runner
from config import config
import os

@function_tool
def create_file(
    file_name:str=None,
    folder_name:str=None,
    content:str=None,
    file_path:str=None,
    read_content:bool=None,
):
    try:
        message=[]
        if folder_name:
            os.makedirs(folder_name,exist_ok=True)
            message.append(f"folder{folder_name} created")
            
        if read_content and file_path:
            if os.path.exists(file_path):
                with open(file_path,"r")as f:
                    file_content=f.read()
                    return f"content of {file_path} is {file_content}"
            else:
                return f"File {file_path} not found"
        if file_name:
            if folder_name:
                full_path=os.path.join(folder_name,file_name)
            else:
                full_path=file_name
            with open(full_path,"w")as f:
                f.write(content if content else "no content provided")
            
    except:
        print("Error creating file")

file_handling_agent=Agent(
    name="File Handling Agent",
    instructions="A file handling assistant that can help you with your tasks",
    # tools=[function_tools.get_current_weather],
)
res=Runner.run_sync(
           starting_agent=file_handling_agent,
            input="hello",
            run_config=config
               )
print(res.final_output)

