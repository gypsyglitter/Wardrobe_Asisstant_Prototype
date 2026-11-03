# Wardrobe Assistant

A Python desktop app that stores your clothes as structured data and generates a random outfit from them. 

## Table of Contents
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Project Files](#project-files)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)

## General Information
The Wardrobe Assistant allows you to add your clothing items by documenting them by pattern, name and choosing each item's colour with a colour picker. After adding enough items the application can generate a random outfit from what you've added, build on a graphical interface with Tkinter.

## Technologies Used
* Python 3 (developed with Python 3.14)
* Tkinter, including `ttk`, `messagebox` and `colorchooser` (built into Python)
* Python standard library: `random`, `datetime`

## Features
* Add an item with a name, category, pattern and colour
* Pick a colour using the system colour picker
* A list of all items, with each row shaded in its item's colour and readable black or white text
* Warnings if the name or category is missing
* A Generator tab that picks a shirt, a jumper, and either a skirt or pants at random
* A consistent pink theme applied to every widget

## Screenshots
<img width="698" height="675" alt="Screenshot 2026-11-03 at 1 46 39 pm" src="https://github.com/user-attachments/assets/34ae34f7-603b-467f-8626-17f149746bfc" />
<img width="695" height="676" alt="Screenshot 2026-11-03 at 1 46 19 pm" src="https://github.com/user-attachments/assets/65bffac3-7779-4102-833c-da02f3b6190d" />


## Project Files
* `main.py`: the complete app (data, functions, and interface)
* `pyproject.toml`, `uv.lock`: project settings for the `uv` tool

## Setup
1. Install Python 3 from [python.org](https://www.python.org/downloads/). Tkinter is included.
2. Download or clone this repository.
3. Open a terminal in the project folder.

## Usage
Run:

```
python3 main.py
```

(or `uv run main.py` if you use `uv`).

1. On the Add Outfit tab, enter a name, choose a category, add a pattern, and click 'Pick from palette' to choose a colour.
2. Click Add Item. It appears in the list.
3. Add a few shirts, jumpers, and skirts or pants.
4. Open the Generator tab and click Generate Outfit

Items are stored in memory only, so the wardrobe resets when the app closes.

## Project Status
Complete as a prototype for my assessment.

## Room for Improvement
* Save the wardrobe to a file so it isn't lost when the app closes
* Log worn outfits using the `worn_history` field and the `outfit_history` list
* Remind users about items unworn for 30 days (cut from this version)
* Match outfits by colour and pattern instead of choosing at random

## Acknowledgements
* Tab layout based on the [Bro Code Tkinter tabs tutorial](https://www.youtube.com/watch?v=4bMU1xAolSg).
* Help for formatting themed widgets (`ttk.Style`, notebook tabs, combobox) from the [Python documentation: tkinter.ttk, Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html).
* Clearing the previous outfit with `winfo_children()` and `destroy()` follows Elder's tutorial, [Delete frame children widgets - Python Tkinter GUI tutorial #50](https://www.youtube.com/watch?v=A6m7TmjuNzw).
* Ideas for the pink colour scheme and applying colours across the app come from NeuralNine's video, [Color schemes for Tkinter Python applications](https://www.youtube.com/watch?v=hOE4KPToIuY).
* Understanding hex colour strings was supported by the [Hex to String Converter Online](https://www.hextostring.com/).
* The text-colour brightness formula follows the W3C method described in Shanley's article, [Mixing Colours of Equal Luminance, Part 2](https://medium.com/sketch-app-sources/mixing-colours-of-equal-luminance-part-2-3e10c07c947c).
* Learning PyCharm and setting up my environment: Rohowsky's video, [PyCharm tutorial | Introduction to PyCharm | Basics in 10 minutes](https://www.youtube.com/watch?v=HHcZbXsZtm0), and [PyCharm Help](https://www.jetbrains.com/help/pycharm/getting-started.html).
* Generative AI (Claude) was used for proofreading my written reflection and debugging help. This is declared in my reflection.
## Contact
Created by Gypsy Gilbert (25875079), University of Technology Sydney.
