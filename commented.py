import ast

with open("ex.py") as f:
    code = f.read()

tree = ast.parse(code)
new_code = ast.unparse(tree)

print(new_code)
