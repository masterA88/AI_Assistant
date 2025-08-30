# AI Assistant

**AI Assistant** is a Python-based application that uses **fuzzy matching** and **spell correction** to process user commands. It can open applications, websites, and even lock your computer with natural language commands. The assistant features a GUI built with **Tkinter** and integrates fuzzy matching and spell checking to handle common typos and command variations intelligently.

## Features:
- Open applications (e.g., **Visual Studio Code**, **Microsoft Word**, **Excel**).
- Open websites (e.g., **Instagram**, **Facebook**, **Twitter**).
- Lock the computer.
- Handle common typos and misspellings.
- Lightweight and easy to use.

## Requirements:
- Python 3.x
- **Tkinter** (usually included with Python)
- **fuzzywuzzy** (for fuzzy string matching)
- **pyspellchecker** (for spell correction)

## Installation:
1. **Clone the repository**:
```bash
https://github.com/masterA88/AI_Assistant.git
```

2. **Navigate to the project directory**:
```bash
cd AI_Assistant
```

3. **Create a virtual environment** (optional but recommended):
```bash
python -m venv venv
```

4. **Activate the virtual environment**:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

5. **Install the required dependencies**:
  ```
pip install -r requirements.txt
  ```


## How to Use:
1. **Run the application**:
  ```
pip install -r requirements.txt
  ```

2. **Type your command**:
- In the text input box, type one of the following commands (or any other valid command):
  - Open **Instagram**: Type **"instagram"** or **"insta"**.
  - Open **Facebook**: Type **"facebook"** or **"fbk"**.
  - Open **Twitter**: Type **"twitter"**.
  - Open **Google Drive**: Type **"drive"** or **"gdrive"**.
  - Lock the computer: Type **"lock"**.

3. **The assistant will process the command** and:
- Open the corresponding **application** or **website**.
- Lock your computer if you typed **"lock"**.
- Handle common **typos** such as **"instgram"**, **"intag"**, and **"twiter"**.

## Example Commands:
- **"insta"** → Opens **Instagram**.
- **"intag"** → Opens **Instagram**.
- **"fbk"** → Opens **Facebook**.
- **"mail"** → Opens **Gmail**.
- **"open vsc"** → Opens **Visual Studio Code**.
- **"lock"** → Locks the computer.

## Improvements:
- **Voice Command Integration**: Add voice recognition to process commands via speech.
- **Add More Commands**: Add more applications, websites, or custom actions.
- **Enhance Error Handling**: Add more detailed error messages for unsupported commands.
- **Context-Aware Commands**: Implement better natural language processing to understand more complex commands.

## Technologies Used:
- **Python**: The programming language used to build the assistant.
- **Tkinter**: Python's standard GUI library used to create the interface.
- **fuzzywuzzy**: A library for fuzzy string matching to handle typos and variations in user input.
- **pyspellchecker**: A library for correcting spelling errors in user input.
- **subprocess**: A module used to launch applications directly from the assistant.

## License:
This project is licensed under the MIT License.



