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

    # clear the text box
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


window = tk.Tk()
window.title("Code Snippets")
window.geometry("600x600")
# float window to the top
window.attributes("-topmost", True)
window.protocol("WM_DELETE_WINDOW", close_window)
window.resizable(False, False)
button = tk.Button(window, text="Add Snippet", command=add_snippet)
button.place(x=0, y=0)

button = tk.Button(window, text="Load Snippets", command=load_snippets)
button.place(x=0, y=25)

button = tk.Button(window, text="Clear Listbox", command=clear_listbox)
# put button on the right side of the window
button.pack()
# save all snippets to the database
button = tk.Button(window, text="Save Snippets", command=save_snippet)
button.place(x=470, y=00)
# about the program
button = tk.Button(window, text="About", command=about)
button.place(x=520, y=28)
# delete the selected snippet
button = tk.Button(window, text="Delete Snippet", command=delete_snippet)
# put button on the upper right side of the window
button.pack()
# add text box to show snippet
text = tk.Text(window, height=10, width=50, wrap="word", yscrollcommand=True)
text.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)
# add listbox to show saved snippets and scrollbar allow copy and paste
listbox = tk.Listbox(
    window, height=15, width=65, yscrollcommand=True, selectmode="single"
)
# place on bottom of window
listbox.pack(side="bottom")


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
