# SKRYBE

This Python script simulates typing text into any application (e.g., text editors or chat windows) by reading a `.txt` file and typing its contents with adjustable speed and breaks between sentences.

## Features
- **Typing Speed Configuration**: Set the typing speed (Words Per Minute).
- **Breaks Between Sentences**: Configure how many sentences to type before taking a break.
- **Customizable Break Time**: Set how long the break lasts between groups of sentences.
- **Fast Stop**: Press the `Esc` key at any time to stop the typing process.
- **File Upload**: Select a `.txt` file to upload and type its contents.

## Requirements
- Python 3.x
- `pyautogui`: For simulating keyboard typing.
- `keyboard`: To detect the `Esc` key press.

To install the necessary dependencies, you can use `pip`:

```bash
pip install pyautogui keyboard
```

## Full Install and First Run Guide

1. Get [main.py](https://github.com/literal-gargoyle/Skrybe/blob/main/main.py)
2. Import the needed dependencies from the console. you will first need to install [python3](https://www.python.org/downloads/).
3. Get the text you want in a .txt format; just make a new file a copy the tetx you want into it.
4. Copy the file path of the text file. Click the file once and then Copy it (Ctrl+c)
5. Run the program, using python. If you want to run it from the console (EI no ide, run this command
```bash
sudo python3 <path to main.py>
```
6. Choose the settings you want (WPM, Break after # amt of sentances, Break time, Auto Delete)
7. Start the program (click the "apply" button in the GUI)
8. Paste in your text document file location, (Ctrl+V) into the text box.
9. And quickly switch over to the document you want to "type" in!
10. Thats it! Pretty simple or what it is.
