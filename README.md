### Installation Instructions
1. Clone https://github.com/yangdanny97/chocopy-python-compiler
2. cd chocopy-python-compiler
3. pip install -r requirements.txt
4. cd .. to go back to top directory
5. To test our code: python3 verifyTests.py

### Implementation details/running single test case
Run: python3 chocopybril.py tests/add_one.py
This creates:
- tests/add_one.ast (the ast version of the python file, created using the parser chocopy-python-compiler)
- tests/add_one.bril and tests/add_one.json (the converted bril versions)
Run: brili 5 < tests/add_one.json

### Generating Bril file for every file
```
for file in tests/*.py; do
    echo "Running on $file"
    python3 chocopybril.py "$file"
done
```
