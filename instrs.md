Note: you may need to install this repo
cd chocopy-python-compiler
pip install -r requirements.txt

Run: python3 chocopybril.py tests/add_one.py
This creates:
- tests/add_one.ast (the ast version of the python file, created using the parser chocopy-python-compiler)
- tests/add_one.bril and tests/add_one.json (the converted bril versions)
Run: brili 5 < tests/add_one.json

Note: need to make sure the python files given follow the valid Chocopy format. (it is a simplified python that requires certain rules such as declaring variables first, all functions must have a return type?, etc.). also make sure in the input python files all the code is in functions.

Generating Bril file for every file:
```
for file in tests/*.py; do
    echo "Running on $file"
    python3 chocopybril.py "$file"
done
```