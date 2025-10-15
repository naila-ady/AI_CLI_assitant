def create_file(file_name:str,read_content:bool):
    with open(file_name,"w")as f:
        f.write("print('Hello, Paki_World!')")
    if read_content:
        with open(file_name,"r")as f:
            content=f.read()
            print(content)
    else:
        print("File not allowed to read")
create_file("mustafa.py",False)