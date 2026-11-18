import tkinter as tk

app = tk.Tk()
app.title("calculator app")
app.geometry("360x520")
app.configure(bg="#e6e6e6")

expression = ""

def add(val):
    global expression
    expression += str(val)
    display_var.set(expression)

def clear_all():
    global expression
    expression = ""
    display_var.set("")

def calculate():
    global expression
    try:
        expression = str(eval(expression))
        display_var.set(expression)
    except:
        display_var.set("error")
        expression = ""

display_var = tk.StringVar()

display = tk.Entry(
    app,
    textvariable=display_var,
    font=("Times New Roman", 24),
    bd=0,
    justify="right",
    bg="#ffffff"
)
display.pack(fill="x",padx=20, pady=20, ipady=20)
container = tk.frame(app, bg="#e6e6e6")
container.pack(expand=True)

frame = tk.Frame(app, bg="#e6e6e6") 
frame.pack()

def btn(text, r, c, cmd, bg="white", fg="black", cs=1, rs=1):
    tk.Button(
        frame,
        text=text,
        command=cmd,
        bg=bg,
        fg=fg,
        
    )