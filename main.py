import customtkinter
from pathlib import Path

#----dealing with the fonts---
FONT_PATH = Path(__file__).parent / "assets" / "fonts" / "Avenir-Next-Demi.otf"
customtkinter.FontManager.load_font(str(FONT_PATH))
assert FONT_PATH.exists(), f"Font not found: {FONT_PATH}"
#-----Global colours to use--------

c1 = "#FDF0D5"
c2 = "#669BBC"
c3 = "#003049"
c4 = "#780000"


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.title("Lost and Found")
        self.configure(fg_color=c1)

        self.button = customtkinter.CTkButton(self, text="Submit",font=("Avenir Next W1G", 20), fg_color=c2 ,command = self.button_callbck)
        self.button.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")

app = App()
app.mainloop()