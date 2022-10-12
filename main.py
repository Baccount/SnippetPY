import sqlite3
import tkinter as tk
from os import path
VERSION = 0.01


def close_window():
    # save on close
    save_snippet()
    window.destroy()

def check_for_updates() -> bool:
        import urllib.request
        # get the contents of the update.txt file
        url = "https://raw.githubusercontent.com/Baccount/SnippetPY/main/update.txt"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        # decode the bytes
        the_page = the_page.decode("utf-8")
        # strip the newline
        the_page = the_page.strip()
        # check if the version is the same
        if float(the_page) > VERSION:
            return True
        return False

def open_Updates():
    import webbrowser
    webbrowser.open("https://github.com/Baccount/SnippetPY/tree/main")

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
    about_window.focus_set()
    # add a label to the window
    about_label = tk.Label(about_window, text="Code Snippets")
    about_label.pack()
    # add a button to check for updates if check_for_updates() returns True
    if check_for_updates():
        # make the label blue and clickable
        update_label = tk.Label(about_window, text="Update Available")
        update_label.pack()
        open_Updates()
    else:
        update_label = tk.Label(about_window, text="No Updates")
        update_label.pack()
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
        text.insert("1.0", result[0])
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
    # Save all the text in the textbox to the database
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    c.execute("DELETE FROM snippets")
    # get the text from the textbox without the newline
    snippet = text.get("1.0", "end-1c")
    c.execute("INSERT INTO snippets VALUES (?)", (snippet,))
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

# * Clear text Button
button1 = tk.Button(text="Clear Text", command=clear_textbox)
button1.place(x=0, y=0)


# * About button
button2 = tk.Button(window, text="About", command=about)
button2.pack()
button2.place(x=320, y=0)


# * Text Box add to listbox on enter
text = tk.Text(window, wrap="word", yscrollcommand=True)
# shift cursor to the 0 in the text box
text.focus_set()
# text box fill under the buttons
text.place(x=0, y=30, width=400, height=370)


def main():
    try:
        create_database()
        load_snippets()
        window.mainloop()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
