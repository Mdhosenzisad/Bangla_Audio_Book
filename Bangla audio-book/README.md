##Audio Book 
## Author
[Sultan Md. Ayman]

# Text-to-Speech GUI Application

This project is a simple Tkinter GUI application for text-to-speech conversion. Users can input text, and the application will convert it to speech. Additionally, it includes a slider to adjust the speech rate.

## Features

- **Text Input:** Enter the desired text in the provided entry widget.
- **Speech Output:** Click the "Speak" button to convert the entered text into speech.
- **Speech Rate Adjustment:** Use the slider to adjust the speech rate in real-time.

## Requirements

- Python 3.x
- `pyttsx3` library (install via `pip install pyttsx3`)

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `python main.py`.

## How to Use

1. Enter the text you want to convert into speech in the provided entry widget.
2. Click the "Speak" button to hear the converted speech.
3. Use the slider to adjust the speech rate according to your preference.

## Adjusting Speech Rate

Move the slider left or right to decrease or increase the speech rate, respectively. The initial rate is set to 150, and you can modify it according to your preference.

# Audio Book from PDF
## Introduction
This project converts a PDF file into an audio book using Python. It utilizes the pyttsx3 library for text-to-speech conversion and the PyPDF2 library for reading PDF files.

## Requirements
Python 3.x
pyttsx3 library
PyPDF2 library

## Install the required libraries using the following commands: 
  -pip install pyttsx3
  -pip install PyPDF2

## Usage
  1. Open the audio_book_from_pdf.py file.
  2. Replace the file path in the book = open('your_pdf_file.pdf', 'rb') line with the path to your PDF file.
  3. Run the script using the following command:
      - python audio_book_from_pdf.py

## Notes
  1. Ensure that your PDF file is accessible and readable.
  2. Adjust the page range in the for loop (range(start_page, end_page)) to specify which pages to include in the audio book.
  3. Feel free to customize the script according to your needs.

## Acknowledgments
This project was inspired by the need for converting PDF documents into audio books for accessibility and convenience.
