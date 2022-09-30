# keep a saved list of code snippets for later use

from os import path
import tkinter as tk
import sqlite3

# clear the listbox
def clear_listbox():
    listbox.delete(0, "end")

# Add a new snippet
def add_snippet():
    # add all text to a variable
    txt = text.get("1.0", "end-1c")
    # save the text
    save_snippet(txt)
    load_snippets()

def delete_snippet():
    # delete the selected snippet in the listbox
    listbox.delete("active")
    # delete the snippet from the database
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    # delete the snippet from the database using the snippet name and index
    c.execute("DELETE FROM snippets WHERE snippet = ?", (listbox.get("active"),))
    conn.commit()
    conn.close()

# load all snippets from the database and show them in the listbox
def load_snippets():
    # check if the database exists
    if path.isfile("snippets.db"):
        # load the snippets from the database
        conn = sqlite3.connect("snippets.db")
        c = conn.cursor()
        c.execute("SELECT * FROM snippets")
        snippets = c.fetchall()
        # show the snippets in the listbox
        for snippet in snippets:
            listbox.insert("end", snippet[0])
        conn.close()


def save_snippet(text):
    # save the text using SQLite database
    # create a new database if one doesn't exist
    if not path.isfile("snippets.db"):
        conn = sqlite3.connect("snippets.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE snippets
                    (snippet text)''')
        conn.commit()
        conn.close()
    # add the snippet to the database
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    c.execute("INSERT INTO snippets VALUES (?)", (text,))
    conn.commit()
    
    





window = tk.Tk()
window.title("Code Snippets")
window.geometry("600x600")
window.resizable(False, False)
# add button to add new snippet
# add button to delete snippet
button = tk.Button(window, text="Add Snippet", command=add_snippet)
button.pack()
button = tk.Button(window, text="Delete Snippet", command=delete_snippet)
button.pack()
# load all snippets from the database button
button = tk.Button(window, text="Load Snippets", command=load_snippets)
button.pack()
# clear the listbox
button = tk.Button(window, text="Clear Listbox", command=clear_listbox)
button.pack()
# add text box to show snippet
text = tk.Text(window, height=10, width=50)
text.pack()
# add listbox to show saved snippets and scrollbar allow copy and paste
listbox = tk.Listbox(window, height=10, width=50, yscrollcommand=True, selectmode="single")
# place on bottom of window
listbox.pack(side="bottom")





def main():
    try: \
        window.mainloop()
        
    except Exception as e:
        print(e)
        print("Error: unable to start thread")



























if __name__ == "__main__":
    main()