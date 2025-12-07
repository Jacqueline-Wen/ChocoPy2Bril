Run: python3 chocopybril.py tests/add_one.py
This creates:
- tests/add_one.ast (the ast version of the python file, created using the parser chocopy-python-compiler)
- tests/add_one.bril and tests/add_one.json (the converted bril versions)
Run: brili 5 < tests/add_one.json