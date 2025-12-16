## Experience Report

### What was the goal?
The primary goal is to create a compiler frontend, named "ChocoPy2Bril," that translates a core subset of the ChocoPy language directly into the Bril representation. This project will focus on the AST traversal and code generation phase by leveraging an existing ChocoPy parser to handle lexical analysis and syntax analysis.

Specifically, we supported the following functionalities of ChocoPy:
- Primitive Types: Integers and Booleans (int, bool).
- Basic Operations: Arithmetic (+, -, *, /), Relational (==, !=, <, >, <=, >=), and Logical (and, or, not).
- Variables: Local variable declaration and assignment.
- Control Flow: Conditional statements (if/else) and simple iteration (while loops).
- Functions: Function definition, argument passing, and return statements.

Note: we were originally also planning on supporting modulo, but due to Bril not having a modulo operator, we were forced to leave it out.

### What did you do?
For the simplicity of this project, we decided to focus on a subset of ChocoPy that includes primitive types, basic operations, variable declarations and assignments, control flow statements, and function definitions. We decided on these primatives as we felt that we could cover a reasonable amount of simple program functionalities alone with these primativs. 

Without too much difficulty, we were able to familiarize ourselves with ChocoPy's grammar, and we had to settle on how we were planning on implementing the translation from ChocoPy to Bril. At the recommendation of Professor Sampson, we focused on efforts on the AST translation, instead of actually building the AST from scratch, as this would be a really tedious, time consuming, and fairly non-trivial task to do. This allowed us to focus on the code generation phase of the compiler, which was our main goal. The next step in the design would be to decide how we were going to generating the AST from the ChocoPy program. Originally, we thought that the simplest solution would be to use the built in Python AST module to generate the AST from the ChocoPy program. However, we soon realized that there were small nuances between the ChocoPy grammar and the Python grammar, which made this approach infeasible. After some research, we found that there were multiple existing ChocoPy parser implemented in Python, which we were able to leverage to generate the AST for us. We ended up deciding to use "yangdanny97/chocopy-python-compiler" as our ChocoPy parser, as it was fairly well documented and seemed easy to use.

For the implementation, we directly called the "yangdanny97/chocopy-python-compiler" code to generate the AST. Luckily, the AST that was generated was basically in JSON format. As a result, we just had to hard code the translation between the ChocoPy AST nodes and the Bril instructions. 

### What were the hardest parts to get right?
### Were you successful? (Report rigorously on your empirical evaluation.) 
