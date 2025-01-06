# Python OCR

## Overview
Example of Optical Character Recognition. Converts an image to text.

## Implementation
Simply uses the Open Source Tesseract OCR library.


## Installation

Just clone this repository

```bash
$ git clone https://github.com/richardadalton/sudoku_solver.git
```

Create a virtual environment using your preferred method. E.g.

```bash
$ python3 -m venv .venv
$ . .venv/bin/activate
```

Install dependencies

```bash
$ pip install -r requirements.txt
```

If there are any problems running the project, try updading to the latest versions of Pillow, and pytesseract.

## Running Python OCR

```bash
$ python pyocr.py [-h] [-f FILE]

arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to image file containing text
```

