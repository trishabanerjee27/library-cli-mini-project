# library-cli-mini-project
# LATEST VERSION

A modular command-line library management system written in Python. It supports adding, listing, borrowing, and returning books, with storage using a .json file.

---

## Features

- Add books with title, author, and ISBN
- List all books with status like available/borrowed
- Borrow a book using its ISBN
- Return a borrowed book
- All data is saved and loaded from a JSON file under `library/data/library_data.json`
- Modularized using Python packages
- Installable locally via `setup.py` with a custom CLI command (`library-cli`)

---

## Project Structure

This repo is organized into a modular Python package:
- `library/` - Contains all source code
  - `book.py` - `Book` class
  - `library.py` - `Library` class
  - `data/library_data.json` - persistent JSON storage
- `main.py` - CLI entry point
- `tests/` - Contains the unit test suite
  - `test_library.py` - test file
- `setup.py` - For local installation
- `README.md` - You're here c-:


## Installation

Make sure you have Python 3.7+ and pip installed.

1. Clone or download this repo
2. Navigate to the directory containing `setup.py`
3. Run:

```bash
pip install -e .
```
4. Once installed, you can run:
```
library-cli
```

You'll see a menu like this:

```
~~~~~~~~~ LIBRARY MENU ~~~~~~~~~~~
1. Add Book
2. List Books
3. Borrow Book
4. Return Book
5. Exit

```


### Example
```
Add a book → The Great Gatsby, F. Scott Fitzgerald, ISBN 12345

Borrow a book → Enter ISBN 12345

Return a book → Enter ISBN 12345

List books → View all with status
```

### To Uninstall
```
pip uninstall library-cli
```

<details>
<summary> to run tests </summary>
```
python -m unittest discover tests
```

- The setUp method initializes a fresh state for every test

- The tearDown method clears it afterward

- The test file assumes no external file I/O — just in-memory testing

- simulate exceptions (e.g., duplicate or missing ISBN) by checking return state
</details>




<details>
<summary> Outdated Section (click to expand)</summary>

# PREVIOUS VERSION
# CLI Library System

A simple Python command-line library system with:

- Add, list, lend, and return books
- Data saved in `library_data.json`
- Organized structure with code in `library.py` and CLI in `main.py`

All book operations update a local JSON file for data persistence between sessions..

## Repo Structure
```
library_cli_project/
├── main.py
├── library.py
├── README.md
└── data/
    └── library_data.json
```

## Usage

## Navigate to the project directory
cd library_cli_project

## Run the CLI application
python main.py

</details>


