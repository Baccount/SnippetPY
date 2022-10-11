# keep a saved list of code snippets for later use

import sqlite3
import tkinter as tk
from os import path


def close_window():
    # save on close
    save_snippet()
    window.destroy()


def about():
    about_window = tk.Toplevel()
    about_window.title("About")
    about_window.geometry("200x100")
    # center the window
    x = (window.winfo_screenwidth() // 2) - (200 // 2)
    y = (window.winfo_screenheight() // 2) - (100 // 2)
    about_window.geometry('{}x{}+{}+{}'.format(200, 100, x, y))
    about_window.resizable(False, False)
    about_window.grab_set()
    about_window.focus_set
    # add a label to the window
    about_label = tk.Label(about_window, text="Code Snippets")
    about_label.pack()
    # add name to the window
    name_label = tk.Label(about_window, text="By: Brandon Moore")
    name_label.pack()


def clear_textbox():
    # clear the textbox
    text.delete("1.0", "end")



# load the snippets from the database into the textbox
def load_snippets():
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    c.execute("SELECT * FROM snippets")
    result = c.fetchone()
    if result is not None:
        text.insert("end", result[0])
    conn.close()

def create_database():
    # create a new database and table if it doesn't exist
    if not path.exists("snippets.db"):
        conn = sqlite3.connect("snippets.db")
        c = conn.cursor()
        c.execute("CREATE TABLE snippets (snippet text)")
        conn.commit()
        conn.close()

def save_snippet():
    # Save everything in the textbox to the database
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    c.execute("DELETE FROM snippets")
    c.execute("INSERT INTO snippets VALUES (?)", (text.get("1.0", "end"),))
    conn.commit()
    conn.close()


### ? Main Program Entry Point ###
window = tk.Tk()
window.title("Code Snippets")
window.geometry("400x400")
window.protocol("WM_DELETE_WINDOW", close_window)
window.resizable(False, False)
# center the window
x = (window.winfo_screenwidth() // 2) - (400 // 2)
y = (window.winfo_screenheight() // 2) - (400 // 2)
window.geometry('{}x{}+{}+{}'.format(400, 400, x, y))


# * Load Snippets Button
button = tk.Button(window, text="Load Snippets", command=load_snippets)
button.place(x=0, y=25)

# * Clear text Button
button = tk.Button(window, text="Clear Text", command=clear_textbox)
button.pack()

# * Save Snippets Button
button = tk.Button(window, text="Save Snippets", command=save_snippet)
button.place(x=0, y=0)

# * About button
button = tk.Button(window, text="About", command=about)
button.place(x=320, y=0)


# * Text Box add to listbox on enter
text = tk.Text(window, wrap="word", yscrollcommand=True, width=200, height=40)
# shift cursor to the 0 in the text box
text.focus_set()
# text box fill the y axis
text.pack( side="bottom")


def main():
    try:
        create_database()
        load_snippets()
        window.mainloop()

    except Exception as e:
        print(e)
        print("Error: unable to start thread")


if __name__ == "__main__":
    main()
