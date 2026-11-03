
# WARDROBE ASSISTANT
# tkinter app that lets you:
#   1. add clothing items (name, category, pattern, colour)
#   2. generate a random outfit


# the main GUI toolkit
# ttk = themed widgets
# messagebox = popup warnings
# colorchooser = the system colour picker
import tkinter as tk
from tkinter import ttk, messagebox, colorchooser

    # used for timestamps & outfits
from datetime import datetime
import random    #used to pick randomised clothes

# =======
# COLOURS
# =======
# All of the colouring throughout the app stored with hex code in a theme of pink colours
BG = "#F8E8EE"
ACCENT = "#E8A0BF"      # buttons & tabs
ACCENT_DARK = "#D4769F" # selected tabs
TEXT = "#4A2C3A"        # default text
FIELD = "#FFF5F8"       # background of entry boxs/listboxes

# ==================
# DATABASE & DICTIONARY
# ==================
# where everythings lives in memory when it resets

CATEGORIES = ["Shirt", "Skirt", "Pants", "Jumper", "Shoes", "Jacket"]
wardrobe = []
outfit_history = []

# Colour opened in the colour picker (stored as a pink hex colour)
chosen_colour = "#E8A0BF"
# ============
# FUNCTIONS
# ==========

# Dictionary & labeled values
     #Includes datetime - when things are added
     #Worn history = fills timestamp when its in an outfit
def add_item(name, category, colour, pattern):

    wardrobe.append({
        "name": name,
        "category": category,
        "colour": colour,    # Hex strings
        "pattern": pattern,
        "date_added": datetime.now(),
        "worn_history": []
    })


# returns text to b/w whichever is easiest to read
# hex_colour details that also show pest percived brightness that allow humans too the text properly
#
def text_on(hex_colour):
    r = int(hex_colour[1:3], 16)
    g = int(hex_colour[3:5], 16)
    b = int(hex_colour[5:7], 16)

    brightness = (r * 299 + g * 587 + b * 114) / 1000
    # Bright background -> dark text; dark background -> light text.
    return "black" if brightness > 150 else "white"

def update_preview():   # Repaints preview box and & hex label w chosen colour
    preview.config(bg=chosen_colour)               # repaint preview box


def open_chooser():
    global chosen_colour
#change the display colour
    _rgb, hex_colour = colorchooser.askcolor(
        color=chosen_colour,        # open the picker on current colour
        title="Choose a colour"
    )

    # only acts if user selected a colour
    if hex_colour:
        chosen_colour = hex_colour
        update_preview()

    _rgb, hex_colour = colorchooser.askcolor(
        color=chosen_colour,        # open the picker on current colour
        title="Choose a colour"
    )

    # only acts if user selected a colour
    if hex_colour:
        chosen_colour = hex_colour

def update_listbox():
    # CLEAR the listbox & after REBUILd = keep display &  data in sync
    listbox_items.delete(0, tk.END)   # delete from first row to the end

    # enumerate= gives row number (index) & the item
    for index, item in enumerate(wardrobe):
        listbox_items.insert(
            tk.END,   # tk.END = "add at the bottom"
            f"{item['name']} | {item['category']} | {item['colour'].upper()} | {item['pattern']}"
        )
        # itemconfig into one row of listbox
        # Shade the row in item's own colour & pick readable text for it
        listbox_items.itemconfig(
            index, bg=item["colour"], fg=text_on(item["colour"])
        )



def save_item():
    # Runs when "Add Item" is clicked
    name = entry_name.get().strip() #Reads whats currently in entry box & removes spaces from both ends
    category = combo_category.get()

#Warnings
    # VALIDATION -  check the input before saving
    if name == "":
        messagebox.showwarning("Missing Name", "Please enter an item name.")
        return

    if category not in CATEGORIES:
        messagebox.showwarning("Missing Category", "Please choose a category.")
        return

    # Save item using colour from picker
    add_item(name, category, chosen_colour, entry_pattern.get().strip())
    update_listbox()

    # Reset form so it's ready for next item to be added
    entry_name.delete(0, tk.END)
    entry_pattern.delete(0, tk.END)
    combo_category.set("")


def pick_random(category):
    # Returns one random item of the given category
    # Builds a new list containing only the items whose category match
    options = [item for item in wardrobe if item["category"] == category]
    return random.choice(options) if options else None


def random_outfit():
    # choose one top, one jumper, and either skirt/pants
    bottom_category = random.choice(["Skirt", "Pants"])
    picks = [
        pick_random("Shirt"),
        pick_random(bottom_category),
        pick_random("Jumper"),
    ]
    # some picks may be none if user hasnt input enough clothes
    return [item for item in picks if item is not None]


def generate_outfit():
    # Runs when "Generate Outfit" is clicked

    # wipe the previous outfit off the screen
    for widget in result_frame.winfo_children():
        widget.destroy()

    outfit = random_outfit()

    # empty list= False in Python
    # redirects users to add more items
    if not outfit:
        tk.Label(result_frame, text="Add some items first!",
                 font=("Arial", 14), bg=BG, fg=TEXT).pack()
        return

    for item in outfit:
        tk.Label(
            result_frame,
            text=f"{item['category']}: {item['name']} ({item['colour'].upper()})",
            font=("Arial", 13),
            bg=item["colour"], fg=text_on(item["colour"]),
            padx=10, pady=4
        ).pack(pady=3, fill="x")



def apply_theme(widget):
    # RECURSION = function starts at the main window and works its way through every widget.
    # If it finds widgets inside another, it calls itself again to style those too.
    for child in widget.winfo_children():

        if isinstance(child, ttk.Widget):
            pass  # ttk widgets  are styled by ttk.Style
        elif isinstance(child, tk.Entry):
            child.config(bg=FIELD, fg=TEXT, relief="flat")
        elif isinstance(child, tk.Button):
            # highlightbackground
            child.config(bg=ACCENT, fg=TEXT, activebackground=ACCENT_DARK,
                         activeforeground="white", highlightbackground=ACCENT,
                         relief="flat", padx=10, pady=4)
        elif isinstance(child, tk.Listbox):
            child.config(bg=FIELD, fg=TEXT, selectbackground=ACCENT,
                         selectforeground=TEXT, relief="flat")
        elif isinstance(child, tk.Label):
            child.config(bg=BG, fg=TEXT)
        elif isinstance(child, tk.Frame):
            child.config(bg=BG)
        apply_theme(child)  # go into nested widgets too


# =======
# WINDOW
# ========

root = tk.Tk()                   # creates main window
root.title("Wardrobe Assistant") # titles the app
root.geometry("700x650")         # width x height
root.configure(bg=BG)

# ttk widgets styled through a Style object instead of bg=/fg= options.
style = ttk.Style()
# "clam" is a built-in theme that allows custom colours.
style.theme_use("clam")
style.configure("TNotebook", background=BG, borderwidth=0)   # strip behind tabs
style.configure("TNotebook.Tab", background=ACCENT, foreground=TEXT,
                padding=[15, 6], font=("Arial", 11))          # every tab's look
# style.map changes a style depending on STATE - when tab is "selected", use the darker colour & white text.
style.map("TNotebook.Tab",
          background=[("selected", ACCENT_DARK)],
          foreground=[("selected", "white")])
style.configure("TCombobox", fieldbackground=FIELD, background=ACCENT, foreground=TEXT)

#Set colours for the combobox drop-down list before creating it.
root.option_add("*TCombobox*Listbox.background", FIELD)
root.option_add("*TCombobox*Listbox.foreground", TEXT)
root.option_add("*TCombobox*Listbox.selectBackground", ACCENT)

# ===============
# NOTEBOOK (TABS)
# =================

#creating the tabs
notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

# adding the tab titles
notebook.add(tab1, text="Add Outfit")
notebook.add(tab2, text="Generator")

# expand + fill=  makes  notebook stretch to fill window
notebook.pack(expand=True, fill="both")

# --------------------
# TAB 1: ADD ITEMS
# --------------------

tk.Label(tab1, text="Wardrobe Items", font=("Arial", 18)).pack(pady=10) #How tab 1 is displayed

tk.Label(tab1, text="Item Name").pack()
entry_name = tk.Entry(tab1)   # saved in a variable because save_item() reads it later
entry_name.pack()

tk.Label(tab1, text="Category").pack()
#user can only pick from the list, not type.
combo_category = ttk.Combobox(tab1, values=CATEGORIES, state="readonly")
combo_category.pack()

tk.Label(tab1, text="Pattern").pack()
entry_pattern = tk.Entry(tab1)
entry_pattern.pack()

# === Colour picker
tk.Label(tab1, text="Colour").pack(pady=(10, 0))   # pady=(top, bottom)
preview = tk.Canvas(tab1, width=120, height=40, highlightthickness=1,
                    highlightbackground=TEXT)
preview.pack(pady=5)

hex_label = tk.Label(tab1, text="")   # text is filled in by update_preview()
hex_label.pack()

# Opens colour picker
# command= has no brackets: pass the function itself to be called on click.
tk.Button(tab1, text="Pick from palette", command=open_chooser).pack(pady=3)

update_preview()   # paint the preview with the starting colour

# passing the function itself to be called later on click
tk.Button(tab1, text="Add Item", command=save_item).pack(pady=10)

listbox_items = tk.Listbox(tab1, width=60, height=8)
listbox_items.pack(pady=10)
#creating the listbox


#==================
# TAB 2: GENERATOR
# ================
tk.Button(tab2, text="Generate Outfit", command=generate_outfit).pack(pady=20)
#craeting the second tab
result_frame = tk.Frame(tab2)
result_frame.pack()

# ========
# RUN APP
# ========

apply_theme(root)   # colour everything that exists so far
update_preview()    # re-apply preview colour

# mainloop() starts the app and keeps it running, waiting for clicks and
# typing
root.mainloop()