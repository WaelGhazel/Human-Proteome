from tkinter import *
from treatment import broad_words, broad_most_freq_word, search_word, broad_sequences,broad_seq_in_prot

l = broad_words()
words = "there is "+str(len(l))+" words in the file"
h = broad_most_freq_word()
y = list(h.keys())[0]+" repeated "+str(list(h.values())[0])+" times!"


window = Tk()
window.title("Fasta Project")
window.geometry("800x600")
window.configure(bg = "#E7C980")


canvas = Canvas(
    window,
    bg = "#E7C980",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    280.0,
    74.0,
    anchor="nw",
    text="Fasta Project",
    fill="#000000",
    font=("Ruda Regular", 40 * -1)
)

canvas.create_text(
    280.0,
    178.0,
    #496.0,
    #248.0,
    anchor="nw",
    text=str(words),
    fill="#000000",
    font=("Ruda Regular", 18 * -1)
    )

button_1 = Button(
    window,
    text="Click to see all Sequences",
    borderwidth=0,
    highlightthickness=0,
    font=("Ruda Regular", 20 * -1),
    command=lambda: opengui1(),
    relief="flat"

)
button_1.place(
    x=180.0,
    y=282.0,
    width=441.0,
    height=36.0
)

button_2 = Button(
    window,
    text="Click here to see words in proteome",
    borderwidth=0,
    highlightthickness=0,
    font=("Ruda Regular", 20 * -1),
    command=lambda: opengui2(),
    relief="flat"
)
button_2.place(
    x=180.0,
    y=336.0,
    width=441.0,
    height=36.0
)

def opengui1():
    newwindow = Toplevel(window)

    newwindow.title("Proteome Sequences")
    pr = broad_sequences()



    newwindow.rowconfigure(0, weight=1)
    newwindow.columnconfigure(0, weight=1)
    newwindow.geometry("800x600")
    vbar = Scrollbar(newwindow, orient=VERTICAL)
    vbar.grid(row=0, column=1, sticky=NW + SE)
    newwindow.configure(bg="#E7C980")

    canvas = Canvas(
        newwindow,
        bg="#E7C980",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    canvas.create_text(
        279.0,
        74.0,
        anchor="nw",
        text="Fasta Project",
        fill="#000000",
        font=("Ruda Regular", 40 * -1)
    )

    canvas.create_text(
        50.0,
        155.0,
        anchor="nw",
        text="These Are All The Sequences :",
        fill="#000000",
        font=("Ruda Regular", 18 * -1)
    )

    text = ""
    for key in pr:
        text += str(key + " : " + pr[key] + "\n\n")

    canvas.create_text(
        50.0,
        209.0,
        anchor="nw",
        text=text,
        fill="#000000",
        font=("Ruda Regular", 10 * -1),
        width=640.0
    )
    canvas.grid(row=0, column=0, sticky=NW + SE)
    canvas.configure(yscrollcommand=vbar.set,
                     scrollregion=(0, 0, 800, 600000)
                     )
    vbar.configure(command=canvas.yview)

    newwindow.resizable(False, False)


def opengui2():
    newwindow = Toplevel(window)

    newwindow.title("Words In Proteome")

    x = broad_seq_in_prot()


    newwindow.rowconfigure(0, weight=1)
    newwindow.columnconfigure(0, weight=1)
    newwindow.geometry("800x600")
    vbar = Scrollbar(newwindow, orient=VERTICAL)
    vbar.grid(row=0, column=1, sticky=NW + SE)
    newwindow.configure(bg="#E7C980")

    canvas = Canvas(
        newwindow,
        bg="#E7C980",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        279.0,
        74.0,
        anchor="nw",
        text="Fasta Project",
        fill="#000000",
        font=("Ruda Regular", 40 * -1)
    )

    canvas.create_text(
        50.0,
        155.0,
        anchor="nw",
        text="These Are All The words in proteome :",
        fill="#000000",
        font=("Ruda Regular", 18 * -1)
    )

    text = ""
    for key in x:
        text += str(key + " : " + str(x[key]) + "\n")

    canvas.create_text(
        312.0,
        209.0,
        anchor="nw",
        text=text,
        fill="#000000",
        font=("Ruda Regular", 10 * -1),
        width=640.0
    )
    canvas.grid(row=0, column=0, sticky=NW + SE)
    canvas.configure(yscrollcommand=vbar.set,
                     scrollregion=(0, 0, 800, 40000)
                     )
    vbar.configure(command=canvas.yview)

    newwindow.resizable(False, False)


def searchx():

    o = str(entry_1.get()).upper()
    spec = search_word(o)
    entry_1.delete(0, "end")

    entry_1.insert(0, "The word "+o+" is repeated " + str(list(spec.values())[0]) + " times !")


entry_1 = Entry(
    bd=0,
    bg="#E8E8E8",
    highlightthickness=0
)
entry_1.place(
    x=180.0,
    y=390.0,
    width=441.0,
    height=36.0
)

button_3 = Button(
    window,
    text="Search",
    borderwidth=0,
    highlightthickness=0,
    font=("Ruda Regular", 20 * -1),
    command=lambda :searchx(),
    relief="flat"
)
button_3.place(
    x=305.0,
    y=444.0,
    width=496.0-305.0,
    height=36.0
)


canvas.create_text(
    140.0,
    532.0,
    anchor="nw",
    text="The Most Accurate word in proteome is : "+str(y),
    fill="#000000",
    font=("Ruda Regular", 18 * -1)
)

canvas.create_text(
    318.0,
    123.0,
    anchor="nw",
    text="Made by Wael Ghazel & Ahmed Gara",
    fill="#000000",
    font=("Ruda Regular", 10 * -1)
)
window.resizable(False, False)
window.mainloop()
