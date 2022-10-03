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
        c.execute("""CREATE TABLE snippets ( 
            snippet text
            )""")
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
window.resizable(False, False)
button = tk.Button(window, text="Add Snippet", command=add_snippet)
button.pack()

button = tk.Button(window, text="Load Snippets", command=load_snippets)
button.pack()

button = tk.Button(window, text="Clear Listbox", command=clear_listbox)
# put button on the right side of the window
button.pack()
# save all snippets to the database
button = tk.Button(window, text="Save Snippets", command=save_snippet)
button.pack()
# delete the selected snippet
button = tk.Button(window, text="Delete Snippet", command=delete_snippet)
# put button on the upper right side of the window
button.pack()
# add text box to show snippet
text = tk.Text(window, height=10, width=50, wrap="word", yscrollcommand=True)
text.pack(side = "bottom", fill = "both", expand = True, padx=10, pady=10)
# add listbox to show saved snippets and scrollbar allow copy and paste
listbox = tk.Listbox(window, height=10, width=65, yscrollcommand=True, selectmode="multiple")
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