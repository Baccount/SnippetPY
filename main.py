# keep a saved list of code snippets for later use


import tkinter as tk



# Add a new snippet
def add_snippet():
    # add each line of text to a list
    txt = text.get("1.0", "end-1c")
    lines = txt.splitlines()
    print(lines)










window = tk.Tk()
window.title("Code Snippets")
window.geometry("500x500")
window.resizable(False, False)
# add button to add new snippet
# add button to delete snippet
button = tk.Button(window, text="Add Snippet", command=add_snippet)
button.pack()
button = tk.Button(window, text="Delete Snippet")
button.pack()
# add text box to show snippet
text = tk.Text(window, height=10, width=50)
text.pack()


def main():
    window.mainloop()



























if __name__ == "__main__":
    main()