
#code by agen LLM
# def example_function():
#     with open("example.txt", "w") as f_write:
#         f_write.write("This is an example of writing to a file.")

#     with open("example.txt", "r") as f_read:
#         content = f_read.read()
#         print(content)
 
 
 #code by my self for writing a file and then oepning it and reading its content       
# yeh function aik file banata hai aur optionally uska content read bhi karta hai
def create_file(file_name: str, read_content: bool):
    # 'w' mode ka matlab hai likhna (agar file na ho to new file banay ga)
    with open(file_name, "w") as f:
        # file ke andar ek simple print statement likhi ja rahi hai
        f.write("print('Hello, Paki_World!')")
    
    # agar read_content True ho to file ka content dobara read karo
    if read_content:
        # 'r' mode ka matlab hai read karna
        with open(file_name, "r") as f:
            content = f.read()
            # file ka content print karo
            print(content)
    else:
        # agar read_content False ho to yeh message print karo
        print("File not allowed to read")

# function ko call kar rahe hain file name aur permission ke sath
create_file("mustafa.py", False)
