import pyautogui
import time
import random
from tkinter import Tk, Label, Entry, Button, filedialog, IntVar
import keyboard  # Requires `pip install keyboard`

# Constants for typing behavior
WORDS_PER_MINUTE = 25  # Default value
CHARS_PER_SECOND = WORDS_PER_MINUTE * 60
DELAY_BETWEEN_CHARS = 1 / CHARS_PER_SECOND
BREAK_AFTER_SENTENCES = 5  # Default value
BREAK_TIME = 2  # Default value
STOP_PROGRAM = False  # Global flag to stop the program

# Function to configure settings
def open_config_window():
    config_window = Tk()
    config_window.title("Typing Configuration")

    # Variables to hold user inputs
    wpm_var = IntVar(value=90)
    break_after_sentences_var = IntVar(value=5)
    break_time_var = IntVar(value=2)

    # Labels and input fields
    Label(config_window, text="Words Per Minute:").grid(row=0, column=0, padx=10, pady=5)
    Entry(config_window, textvariable=wpm_var).grid(row=0, column=1, padx=10, pady=5)

    Label(config_window, text="Break After Sentences:").grid(row=1, column=0, padx=10, pady=5)
    Entry(config_window, textvariable=break_after_sentences_var).grid(row=1, column=1, padx=10, pady=5)

    Label(config_window, text="Break Time (seconds):").grid(row=2, column=0, padx=10, pady=5)
    Entry(config_window, textvariable=break_time_var).grid(row=2, column=1, padx=10, pady=5)

    # Function to apply settings
    def apply_settings():
        global WORDS_PER_MINUTE, BREAK_AFTER_SENTENCES, BREAK_TIME
        WORDS_PER_MINUTE = wpm_var.get()
        BREAK_AFTER_SENTENCES = break_after_sentences_var.get()
        BREAK_TIME = break_time_var.get()
        config_window.destroy()

    Button(config_window, text="Apply", command=apply_settings).grid(row=3, column=0, columnspan=2, pady=10)

    config_window.mainloop()

# Function to check for the `Esc` key
def check_for_esc():
    global STOP_PROGRAM
    if keyboard.is_pressed('esc'):
        STOP_PROGRAM = True

# File selection dialog
def select_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")], title="Select a Text File")
    if not filepath:
        print("No file selected. Exiting...")
        exit()
    return filepath

# Main script
print("Configure typing settings.")
open_config_window()  # Open the configuration window

print("Select the text file to upload.")
file_path = select_file()

# Open and read the file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Adjust character speed based on updated WPM
CHARS_PER_SECOND = WORDS_PER_MINUTE * 60
DELAY_BETWEEN_CHARS = 1 / CHARS_PER_SECOND

# Split text into sentences for natural pauses
sentences = text.split('.')

sentence_count = 0

print("Focus on the window where you want to type. Starting in 5 seconds...")
time.sleep(5)

print("Starting to type...")
for sentence in sentences:
    if STOP_PROGRAM:
        print("Typing stopped by user.")
        break

    # Ensure spacing and natural pauses after sentences
    if sentence.strip():
        # Add sentence punctuation back if missing
        if not sentence.endswith('.'):
            sentence += '.'

        for char in sentence:
            check_for_esc()  # Check if `Esc` is pressed
            if STOP_PROGRAM:
                print("Typing stopped by user.")
                break

            pyautogui.typewrite(char)
            time.sleep(random.uniform(DELAY_BETWEEN_CHARS * 0.8, DELAY_BETWEEN_CHARS * 1.2))  # Adds variation in typing speed

        if STOP_PROGRAM:
            break

        # Pause slightly after completing a sentence
        time.sleep(random.uniform(0.8, 1.5))
        sentence_count += 1

    # Take a break after every few sentences
    if sentence_count >= BREAK_AFTER_SENTENCES:
        print(f"Taking a {BREAK_TIME}-second break...")
        time.sleep(BREAK_TIME)
        sentence_count = 0

print("Typing completed.")
