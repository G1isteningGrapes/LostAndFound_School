import customtkinter
from pathlib import Path 

#----dealing with the fonts---------------------------
FONT_PATH = Path(__file__).parent / "assets" / "fonts" / "Avenir-Next-Demi.otf"
customtkinter.FontManager.load_font(str(FONT_PATH))
assert FONT_PATH.exists(), f"Font not found: {FONT_PATH}"
#------------------------------------------------------


#------Variables-----------------------------------------------

cols = [  "#FDF0D5",  "#669BBC",   "#003049",   "#780000"] # colours
#      light yellow,  light blue,   dark blue    dark blue

locL = ["N/A", "Cafeteria"] # locations

#--------------------------------------------------------------



class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.title("Lost and Found")
        self.configure(fg_color=cols[0])

        self.button = customtkinter.CTkButton(self, text="Submit",
                                                    font=("Avenir Next W1G", 20), 
                                                    fg_color=cols[1] ,
                                                    command = self.button_callbck)
        self.button.pack(padx=20, pady=20)

        self.optionmenu_var = customtkinter.StringVar(value = locL[0])#                     <-- default location is N/A
        self.locationOM = customtkinter.CTkOptionMenu(self, values= locL,
                                                        command= self.locationOM_callback,
                                                        variable=self.optionmenu_var,
                                                        fg_color=cols[1])
        self.locationOM.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")

    def locationOM_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)

    
        

app = App()
app.mainloop()