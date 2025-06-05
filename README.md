# NaturalLanguageCoder
[![Python Application CI](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/actions/workflows/main.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/actions/workflows/main.yml)

## Description
A Python utility that converts natural language instructions into a basic code structure. It uses NLTK for tokenization and part-of-speech tagging to perform a rudimentary analysis and conversion. This tool is an initial exploration and has significant room for improvement in terms of accuracy, complexity of conversions, and user interface.

## Current Features
*   Accepts natural language input via a simple Tkinter GUI.
*   Tokenizes and tags words using NLTK.
*   Converts verbs into function calls (e.g., "print" -> "print()").
*   Treats nouns as potential variables or objects.
*   Allows saving the generated code snippet to a file named `output.py`.

## Limitations
*   The conversion logic is very basic and rule-based. It does not understand context, complex grammar, or specific programming language syntax beyond simple function calls and variable names.
*   Error handling is minimal.
*   The GUI is very basic.

## Installation
1.  Clone the repository: `git clone <repository-url>`
2.  Navigate to the project directory: `cd NaturalLanguagecoder`
3.  Install required libraries: `pip install nltk tkinter`
4.  The first time you run the script, NLTK will download necessary resources ('punkt' and 'averaged_perceptron_tagger'). If this fails, you may need to run Python interactively and execute:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    ```

## Usage
1.  Run the script: `python chatcoder.py`
2.  Enter your natural language instruction in the input field (e.g., "create variable data and print hello").
3.  Click "Convert to Code".
4.  The generated code structure will appear in the text area below.
5.  Click "Save" to save the output to `output.py` in the same directory.

## Example Conversion
*   Input: `define function process data`
*   Output: `define() function() process() data ` (Illustrative of current simple logic)

## Contributing
Contributions are welcome! If you'd like to improve NaturalLanguageCoder, please consider:
    *   Enhancing the parsing and code generation logic.
    *   Adding support for more complex programming constructs.
    *   Improving the user interface.
    *   Adding comprehensive error handling.
    *   Expanding test coverage.
Please fork the repository, make your changes on a new branch, and submit a pull request.

## License
This project is licensed under the terms of the LICENSE file.
