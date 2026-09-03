import tkinter

import constants
from tkinter import *
from tkinter import messagebox
from requester import Requester


class AppGui(object):

    def __init__(self):
        self.option_dict = {
            constants.OPTIONS[0]: constants.ABBREVIATIONS[0],
            constants.OPTIONS[1]: constants.ABBREVIATIONS[1],
            constants.OPTIONS[2]: constants.ABBREVIATIONS[2],
            constants.OPTIONS[3]: constants.ABBREVIATIONS[3]
        }
        self.variable_value = None
        self.text_entry = None
        self.request = Requester()

    def colour_frame(self):
        if self.variable_value.get() == constants.ABBREVIATIONS[0]:
            frame_buttons["bg"] = "#B5AFAE"
        elif self.variable_value.get() == constants.ABBREVIATIONS[1]:
            frame_buttons["bg"] = "#1717D1"
        elif self.variable_value.get() == constants.ABBREVIATIONS[2]:
            frame_buttons["bg"] = "#751625"
        elif self.variable_value.get() == constants.ABBREVIATIONS[3]:
            frame_buttons["bg"] = "#206330"

    def colour_entry(self, *args):
        if self.text_entry.get().strip():
            entry_word.config(bg="#69CF32")
        else:
            entry_word.config(bg="#495E3D")

    def clear_text(self):
        entry_word.delete(0, "end")

    def show_results(self):
        results = self.request.make_request(entry_word.get(), self.variable_value.get())
        results_summary = self.request.extract_first_results(results)
        if results_summary is None:
            return
        if len(results_summary) == 0:
            message = f"Sorry, no results found for {entry_word.get()} regarding {self.variable_value.get()}"
            messagebox.showinfo("NO RESULTS", message)
            return
        results_txt = ""
        for i in range(0, len(results_summary)):
            if i == len(results_summary) - 1:
                results_txt += results_summary[i]
            else:
                results_txt += results_summary[i] + "\n"
        # add to text area
        area_result.delete("1.0",END)
        area_result["state"] = tkinter.NORMAL
        area_result.insert("end", results_txt)
        if self.variable_value.get() == constants.ABBREVIATIONS[0]:
            area_result["bg"] = "#B5AFAE"
        elif self.variable_value.get() == constants.ABBREVIATIONS[1]:
            area_result["bg"] = "#1717D1"
        elif self.variable_value.get() == constants.ABBREVIATIONS[2]:
            area_result["bg"] = "#751625"
        elif self.variable_value.get() == constants.ABBREVIATIONS[3]:
            area_result["bg"] = "#206330"
        #center text
        area_result.tag_configure("center", justify="center")
        area_result.tag_add("center", "1.0", "end")

    def create_logic(self, window):
        global entry_word
        global area_result

        global frame_buttons

        frame_buttons = LabelFrame(window, text="Options", width=700, height=80, cursor="star", fg="white",
                                   bg="#B5AFAE", relief="sunken", font=("Georgia", 14, "bold"), borderwidth=2, bd=4,
                                   labelanchor="n")
        frame_buttons.place(x=45, y=20)

        self.variable_value = StringVar(value=self.option_dict[constants.OPTIONS[0]])
        # variable_value.set(self.option_dict[constants.OPTIONS[0]])
        x_loop = 40
        for x in self.option_dict:
            radio_button = Radiobutton(frame_buttons, text=x, value=self.option_dict[x], variable=self.variable_value,
                                       background="#B5AFAE", font=("Arial", 12, "italic"), indicatoron=True,
                                       selectcolor="red", fg="white", command=lambda: self.colour_frame())
            radio_button.place(x=x_loop, y=20)
            x_loop += 175

        label_word = Label(window, text="Enter a word", bg="#B5AFAE", fg="#040717", cursor="arrow", width=10, height=2,
                           justify="center", bd=1, font=("Georgia", 12, "bold"))
        label_word.place(x=80, y=150)

        self.text_entry = StringVar()
        self.text_entry.trace_add("write", callback=self.colour_entry)

        entry_word = Entry(window, width=30, bg="#495E3D", fg="white", font=("Georgia", 12, "bold"), justify="center",
                           relief="groove", bd=3, textvariable=self.text_entry)
        entry_word.place(x=250, y=160)

        # buttons
        result_button = Button(window, text="Show", bg="#064515", fg="white", font=("Arial", 12, "bold"), bd=2, width=8,
                               height=1, justify="center", command=lambda : self.show_results())
        result_button.place(x=650, y=125)
        clear_button = Button(window, text="Clear", bg="#2D0933", fg="white", font=("Arial", 12, "bold"), bd=2, width=8,
                              height=1, justify="center", command=lambda: self.clear_text())
        clear_button.place(x=650, y=185)

        # textarea
        label_result = Label(window, text="RESULTS", bg="#B5AFAE", fg="#040717", cursor="arrow", width=10, height=2,
                             justify="center", bd=1, font=("Georgia", 12, "bold"))
        label_result.place(x=80, y=400)
        area_result = Text(window, width=30, height=8, font=("Georgia", 12, "bold"), wrap=tkinter.WORD, relief="groove", bd=1,
                           bg="#4A6A82", fg="white", highlightcolor="#D7D91C", highlightbackground="#4A1F8F",
                           highlightthickness=3, state="disabled")
        area_result.place(x=250, y=350)

    def create_window(self):
        root = Tk()
        root.title("Word analyser")
        root.geometry("800x600")
        root["bg"] = "#B5AFAE"
        self.create_logic(root)
        root.resizable(False, False)
        root.mainloop()


if __name__ == "__main__":
    app = AppGui()
    app.create_window()
