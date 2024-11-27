# SKRYBE

This Python script simulates typing text into any application (e.g., text editors or chat windows) by reading a `.txt` file and typing its contents with adjustable speed and breaks between sentences.

## Features
- **Typing Speed Configuration**: Set the typing speed (Words Per Minute).
- **Breaks Between Sentences**: Configure how many sentences to type before taking a break.
- **Customizable Break Time**: Set how long the break lasts between groups of sentences.
- **Graceful Stop**: Press the `Esc` key at any time to stop the typing process.
- **File Upload**: Select a `.txt` file to upload and type its contents.

## Requirements
- Python 3.x
- `pyautogui`: For simulating keyboard typing.
- `keyboard`: To detect the `Esc` key press.

To install the necessary dependencies, you can use `pip`:

```bash
pip install pyautogui keyboard
