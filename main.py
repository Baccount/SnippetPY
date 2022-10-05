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
    about_window.geometry("300x100")
    about_window.resizable(False, False)
    about_window.grab_set()
    about_window.focus_set
    # add a label to the window
    about_label = tk.Label(about_window, text="Code Snippets")
    about_label.pack()
    # add name to the window
    name_label = tk.Label(about_window, text="By: Brandon Moore")
    name_label.pack()


def clear_listbox():
    listbox.delete(0, "end")


def add_snippet():
    # ? add each line in the text box to the listbox
    for line in text.get("1.0", "end").splitlines():
        if line != "":
            listbox.insert("end", line)
    # reset the text box and the cursor
    text.delete("1.0", "end")


def delete_snippet():
    # delete the selected snippet
    listbox.delete("active")


def load_snippets():
    # check if the database exists
    if path.isfile("snippets.db"):
        # clear the listbox
        clear_listbox()
        conn = sqlite3.connect("snippets.db")
        c = conn.cursor()
        c.execute("SELECT * FROM snippets")
        snippets = c.fetchall()
        for snippet in snippets:
            listbox.insert("end", snippet[0])
        conn.close()


def create_database():
    # create a new database if one doesn't exist
    if not path.isfile("snippets.db"):
        conn = sqlite3.connect("snippets.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE snippets (snippet text)""")
        conn.commit()
        conn.close()

def save_snippet():
    # Save everything in the listbox to the database
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    c.execute("DELETE FROM snippets")
    for i in range(listbox.size()):
        snippet = listbox.get(i)
        c.execute("INSERT INTO snippets (snippet) VALUES (?)", (snippet,))
    conn.commit()
    conn.close()


### ? Main Program Entry Point ###
window = tk.Tk()
window.title("Code Snippets")
window.geometry("600x600")
window.protocol("WM_DELETE_WINDOW", close_window)
window.resizable(False, False)

# * Add Snippet Button
button = tk.Button(window, text="Add Snippet", command=add_snippet)
button.place(x=0, y=0)

# * Load Snippets Button
button = tk.Button(window, text="Load Snippets", command=load_snippets)
button.place(x=0, y=25)

# * Clear Listbox Button
button = tk.Button(window, text="Clear Listbox", command=clear_listbox)
button.pack()

# * Save Snippets Button
button = tk.Button(window, text="Save Snippets", command=save_snippet)
button.place(x=470, y=00)

# * About button
button = tk.Button(window, text="About", command=about)
button.place(x=520, y=28)

# * Delete Snippet Button
button = tk.Button(window, text="Delete Snippet", command=delete_snippet)
button.pack()

# * Text Box add to listbox on enter
text = tk.Text(window, wrap="word", yscrollcommand=True, width=250, height=4)
text.bind("<Return>", lambda x: add_snippet())
# shift cursor to the 0 in the text box
text.focus_set()
# text box fill the y axis
text.pack( side="bottom")

# * Scrollbar and Listbox
scrollbar = tk.Scrollbar(window)
listbox = tk.Listbox(window, yscrollcommand=scrollbar.set)
listbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)
scrollbar.pack(side="right", fill="y")


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
