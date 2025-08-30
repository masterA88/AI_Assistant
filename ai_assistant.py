import tkinter as tk
import subprocess
import webbrowser
import os
from fuzzywuzzy import process
from spellchecker import SpellChecker

# Dictionary to map commands to actions
commands = {
    "vsc": r"C:\Users\maste\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk",  # VS Code shortcut
    "instagram": "https://www.instagram.com",  # Instagram
    "facebook": "https://www.facebook.com",  # Facebook
    "twitter": "https://www.twitter.com",  # Twitter
    "linkedin": "https://www.linkedin.com",  # LinkedIn
    "gmail": "https://mail.google.com",  # Gmail
    "drive": "https://drive.google.com",  # Google Drive
    "notepad": "notepad",  # Notepad
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",  # Microsoft Word
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",  # Microsoft Excel
    "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",  # PowerPoint
    "teams": r"C:\Program Files (x86)\Microsoft Teams\Teams.exe",  # Microsoft Teams
    "lock": "rundll32.exe user32.dll,LockWorkStation",  # Lock Windows
    "tiktok": "https://www.tiktok.com"  # TikTok website
}

# Initialize SpellChecker and Fuzzy Matching
spell = SpellChecker()

# Function to correct typos using fuzzy matching and spelling correction
def correct_typo(command):
    # First, check if the command is one of the common short commands
    if command in ["insta", "intagram", "intag"]:
        corrected_command = "instagram"  # Manually correct common short commands
    else:
        # Apply fuzzy matching for commands (this should work for short words like 'inta')
        best_match = process.extractOne(command, commands.keys())

        # If fuzzy match confidence is high (80% or more), return the match
        if best_match and best_match[1] > 80:
            corrected_command = best_match[0]
        else:
            # Otherwise, apply SpellChecker for each word in the command
            words = command.split()
            corrected_words = []

            for word in words:
                # Use SpellChecker to correct individual words
                corrected_word = spell.correction(word)
                
                # Check again if corrected word matches a valid command using fuzzy matching
                best_match = process.extractOne(corrected_word, commands.keys())
                if best_match and best_match[1] > 80:
                    corrected_word = best_match[0]
                
                corrected_words.append(corrected_word)

            corrected_command = " ".join(corrected_words)

    return corrected_command

# Function to process commands with spell correction and fuzzy matching
def process_command(event=None):
    user_input = entry.get().lower()  # Get the input text and convert to lowercase

    # Correct typos before processing the command
    corrected_input = correct_typo(user_input)

    print(f"Original Command: {user_input}")  # For debugging
    print(f"Corrected Command: {corrected_input}")  # For debugging
    
    # Check if the corrected command matches any available command
    for key, value in commands.items():
        if key in corrected_input:
            if key == "lock":
                os.system(value)  # Lock the computer
                response_label.config(text="Locking your computer...")
            elif key in ["vsc", "notepad", "word", "excel", "powerpoint", "teams"]:
                try:
                    subprocess.Popen([value])  # Open application using subprocess
                    response_label.config(text=f"Opening {key.capitalize()}...")
                except FileNotFoundError:
                    response_label.config(text=f"Error: {key.capitalize()} not found.")
            else:
                webbrowser.open(value)  # Open website URLs
                response_label.config(text=f"Opening {key.capitalize()}...")
            return  # Exit after executing the command
    response_label.config(text="Sorry, command not recognized.")  # If command is not found

# Set up the main window
window = tk.Tk()
window.title("AI Assistant")
window.geometry("500x250")

# Instruction Label
instruction_label = tk.Label(window, text="Type your command:", font=("Helvetica", 12))
instruction_label.pack(pady=10)

# Text input box
entry = tk.Entry(window, width=40, font=("Helvetica", 12))
entry.pack(pady=10)

# Bind Enter key to process command
entry.bind("<Return>", process_command)

# Response Label (where the assistant's response will appear)
response_label = tk.Label(window, text="", font=("Helvetica", 12))
response_label.pack(pady=10)

# Start the GUI loop
window.mainloop()
