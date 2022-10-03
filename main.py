# keep a saved list of code snippets for later use

from os import path
import tkinter as tk
import sqlite3

# clear the listbox
def clear_listbox():
    listbox.delete(0, "end")

def add_snippet():
    # ? add each line in the text box to the listbox
    for line in text.get("1.0", "end").splitlines():
        if line != "":
            listbox.insert("end", line)
    
    # clear the text box
    text.delete("1.0", "end")


# load all snippets from the database and show them in the listbox
def load_snippets():
    # check if the database exists
    if path.isfile("snippets.db"):
        # clear the listbox
        clear_listbox()
        # load the snippets from the database
        conn = sqlite3.connect("snippets.db")
        c = conn.cursor()
        c.execute("SELECT * FROM snippets")
        snippets = c.fetchall()
        # show the snippets in the listbox
        for snippet in snippets:
            listbox.insert("end", snippet[0])
        conn.close()

def create_database():
    # create a new database if one doesn't exist
    if not path.isfile("snippets.db"):
        conn = sqlite3.connect("snippets.db")
        c = conn.cursor()
        # create new database with one column for the snippet
        c.execute("""CREATE TABLE snippets ( 
            snippet text
            )""")
        conn.commit()
        conn.close()




def save_snippet():
    # Save everything in the listbox to the database
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    # delete all snippets from the database
    c.execute("DELETE FROM snippets")
    # add all snippets from the listbox to the database
    for i in range(listbox.size()):
        snippet = listbox.get(i)
        c.execute("INSERT INTO snippets (snippet) VALUES (?)", (snippet,))
    conn.commit()
    conn.close()



window = tk.Tk()
window.title("Code Snippets")
window.geometry("600x600")
window.resizable(False, False)
# add button to add new snippet
# add button to delete snippet
button = tk.Button(window, text="Add Snippet", command=add_snippet)
button.pack()
# load all snippets from the database button
button = tk.Button(window, text="Load Snippets", command=load_snippets)
button.pack()
# clear the listbox
button = tk.Button(window, text="Clear Listbox", command=clear_listbox)
# put button on the right side of the window
button.pack(padx=10)
# save all snippets to the database
button = tk.Button(window, text="Save Snippets", command=save_snippet)
button.pack()
# add text box to show snippet
text = tk.Text(window, height=10, width=50)
text.pack()
# add listbox to show saved snippets and scrollbar allow copy and paste
listbox = tk.Listbox(window, height=10, width=50, yscrollcommand=True, selectmode="single")
# place on bottom of window
listbox.pack(side="bottom")


def create_database():
    # create a new database if one doesn't exist
    if not path.isfile("snippets.db"):
        conn = sqlite3.connect("snippets.db")
        c = conn.cursor()
        # create new database with one column for the snippet
        c.execute("""CREATE TABLE snippets ( 
            snippet text
            )""")
        conn.commit()
        conn.close()



def main():
    try:
        create_database()
        window.mainloop()
        
    except Exception as e:
        print(e)
        print("Error: unable to start thread")



























if __name__ == "__main__":
    main()