import tkinter as tk
from tkinter import Tk, Label, Button, Entry

#Initialize
root = tk.Tk()
root.title("TicTacToe")
root.geometry("500x600")
root.configure(bg="light yellow")

# Variable to keep track of the selected Entry widget
selected_entry = None
r=-1
c=-1
arr=[[0,0,0],[0,0,0],[0,0,0]]
check=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
X=[]
O=[]

def clear_entries():
    """Clears all Entry fields in the Tic-Tac-Toe grid."""
    for row in entries:
        for entry in row:
            entry.delete(0, tk.END)  # Delete all text in the entry


def reset():
    global X
    global O
    global arr
    global r
    global c
    X=[]
    O=[]
    arr=[[0,0,0],[0,0,0],[0,0,0]]
    r=-1
    c=-1
    
def select_entry(event):
    """Set the selected entry when clicked."""
    global selected_entry
    selected_entry = event.widget  # Store the clicked Entry widget


def printXO(symbol):
    """Insert 'X' or 'O' into the selected Entry box."""
    if selected_entry is None:
        return  # Prevent further execution
    if selected_entry:
        selected_entry.delete(0, tk.END)  # Clear previous value
        selected_entry.insert(0, symbol)  # Insert new symbol
    # Get row and column from grid info
    global r
    global c
    r = selected_entry.grid_info()["row"]
    c = selected_entry.grid_info()["column"]
    arr[r-1][c]=symbol
    if symbol=="X":X.append(3*(r-1)+c+1)
    if symbol=="O":O.append(3*(r-1)+c+1)
    X.sort()
    O.sort()
    checkWin()
    checkDraw()

def checkDraw():
    if not checkWin():
        c=0
        for j in entries:
            for i in j:
                if i.get() in ["X","O"]:
                    c+=1
        if c==9:
            status_label.config(text="Draw Match", font=("Arial", 12, "bold"), fg="blue")
            clear_entries()
            reset()

def checkWin():
    flag=0
    if X in check and O not in check:
        flag=1
        status_label.config(text="X:Winner of the Match", font=("Arial", 12, "bold"), fg="blue")
        clear_entries()
        reset()
        return True
    elif O in check and X not in check:
        flag=1
        status_label.config(text="O:Winner of the Match", font=("Arial", 12, "bold"), fg="blue")
        clear_entries()
        reset()
        return True
    elif X not in check and O not in check:
        for i in range(0,len(X)-2):
            for j in range(1,len(X)-1):
                for k in range(2,len(X)):
                    test=[X[i],X[j],X[k]]
                    if test in check:
                        flag=1
                        status_label.config(text="X:Winner of the Match", font=("Arial", 12, "bold"), fg="blue")
                        clear_entries()
                        reset()
                        return True
        for i in range(0,len(O)-2):
            for j in range(1,len(O)-1):
                for k in range(2,len(O)):
                    test=[O[i],O[j],O[k]]
                    if test in check:
                        flag=1
                        status_label.config(text="O:Winner of the Match", font=("Arial", 12, "bold"), fg="blue")
                        clear_entries()
                        reset()
                        return True
    if flag==0:return False

# Configure the root window to allow resizing and expand the grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a frame that will contain the grid content
frame = tk.Frame(root, bg="light yellow")
frame.grid(row=0, column=0, padx=10, pady=10)

# Configure grid in the frame to center it
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

#UI
message_label = Label(frame, text="Press X/O", fg="maroon", font=("Arial", 16), bg="light yellow")
message_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

entries = []
for row in range(3):
    row_entries = []
    for col in range(3):
        entry = Entry(frame, width=2, fg="maroon", font=("Lucida Calligraphy", 15), justify="center")
        entry.grid(row=row+1, column=col, padx=5, pady=5)  # Adjust row index
        entry.bind("<Button-1>", select_entry)  # Bind left click to track selected entry
        row_entries.append(entry)
    entries.append(row_entries)

buttonX = Button(frame, text="X", command=lambda: printXO("X"), bg="blue", fg="white", font=("Monotype Corsiva", 16))
buttonX.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

buttonO = Button(frame, text="O", command=lambda: printXO("O"), bg="blue", fg="white", font=("Monotype Corsiva", 16))
buttonO.grid(row=4, column=2, columnspan=1, padx=5, pady=5)

status_label = Label(root, text="Status: Waiting for action...", bg="light yellow", fg="maroon", font=("Arial", 10, "bold"))
status_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

#Run App
if __name__ == "__main__":
    root.mainloop()  # This ensures the GUI only starts when run directly
