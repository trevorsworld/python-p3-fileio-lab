def write_file(file_name, file_content):
     with open(f'{file_name}.txt', mode='w') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a') as file:
        file.write(append_content)

def read_file(file_name):
     with open(f'{file_name}.txt', 'r') as file:
        return file.read()



file_name = "example"
file_content = "This is the content of the file."

write_file(file_name, file_content)