import ast

def parse_data(file_name):
    file_path = file_name
    with open(file_path, "r") as f:
        source_code = f.read()

    tree = ast.parse(source_code, filename=file_path)

if __name__ == "__main__":
    file_name = input()
    parse_data(file_name)