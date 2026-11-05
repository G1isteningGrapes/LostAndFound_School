import customtkinter
from pathlib import Path

import customtkinter as ctk
from assets.calendar.ctk_date_picker import CTkDatePicker
from pathlib import Path 


#----dealing with the fonts---------------------------
FONT_PATH = Path(__file__).parent / "assets" / "fonts" / "Avenir-Next-Demi.otf"
ctk.FontManager.load_font(str(FONT_PATH))
assert FONT_PATH.exists(), f"Font not found: {FONT_PATH}"
#------------------------------------------------------
cols = [  "#FDF0D5",  "#669BBC",   "#003049",   "#780000"] # colours
#      light yellow,  light blue,   dark blue    dark blue

locL = ["N/A", "Cafeteria"] # locations

#--------------------------------------------------------------

class App(customtkinter.CTk):
#------Variables-----------------------------------------------

cols = [  "#FDF0D5",  "#669BBC",   "#003049",   "#780000"] # colours
#      light yellow,  light blue,   dark blue    dark blue

locL = ["Other", "Athletics Complex", "BAC","Carnegie Hall", "Cafeteria", "KC Irving Center", "Huggins Science Hall","Patterson Hall", "U Hall", "Outside"] # locations

itmL = ["Other", "Bag" ,"Clothing item", "Water bottle", "Electronic",  "I.D.", "Card", "Keys"]

optL = [ "Submit Report", "Browse reports"]

location = "N/A"
item = "N/A"
date = "N/A"
#--------------------------------------------------------------



class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Lost and Found")
        self.configure(fg_color=cols[0])

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=10, border_color=cols[1])
        self.main_frame.pack()

        self.top_title = ctk.CTkLabel(self.main_frame, text="  Lost Report ", text_color=cols[1], bg_color="transparent", height = 20)
        self.top_title.grid(row=0, column=0, padx=20, pady=20, columnspan = 2)

        self.location_title = ctk.CTkLabel(self.main_frame, text="  Location : ", text_color=cols[1], bg_color="transparent", height = 20)
        self.location_title.grid(row=1, column=0, padx=20, pady=20)

        self.button = customtkinter.CTkButton(self, text="Submit",font=("Avenir Next W1G", 20), fg_color=c2 ,command = self.button_callbck)
        self.button.pack(padx=20, pady=20)
        self.optionmenu_var = ctk.StringVar(value = locL[0])#                     <-- default location is N/A
        self.location_optmenu = ctk.CTkOptionMenu(self.main_frame, values= locL,
                                                        command= self.locationOM_callback,
                                                        variable=self.optionmenu_var,
                                                        fg_color=cols[1])
        self.location_optmenu.grid(row=1, column=1, padx=20, pady=20)

        self.item_title = ctk.CTkLabel(self.main_frame, text="  Item : ", text_color=cols[1], bg_color="transparent", height = 20)
        self.item_title.grid(row=2, column=0, padx=20, pady=20)

        self.itemmenu_var = ctk.StringVar(value = itmL[0])#                     <-- default location is N/A
        self.item_optmenu = ctk.CTkOptionMenu(self.main_frame, values= itmL,
                                                        command= self.itemOM_callback,
                                                        variable=self.itemmenu_var,
                                                        fg_color=cols[1])
        self.item_optmenu.grid(row=2, column=1, padx=20, pady=20)

        self.date_title = ctk.CTkLabel(self.main_frame, text="  Date : ", text_color=cols[1], bg_color="transparent", height = 20)
        self.date_title.grid(row=3, column=0, padx=20, pady=20)

        self.calender = CTkDatePicker(self.main_frame, fg_color=cols[1])
        self.calender.set_allow_manual_input(False)
        self.calender.grid(row=3, column=1, padx=20, pady=20)


        self.button = ctk.CTkButton(self.main_frame, text="Submit",
                                                    font=("Avenir Next W1G", 20),
                                                    fg_color=cols[1],
                                                    command = self.button_callbck)

        self.button.grid(row=4, column=0, padx=20, pady=10, columnspan = 2)
        self.sumbit_button = self.button

        self.error_message = ctk.CTkLabel(self.main_frame, text=" ERROR", text_color=cols[1], bg_color="transparent", height = 20)
        self.error_message.grid(row=5, column=0, padx=20, pady=10, columnspan = 2)



        self.button.grid(row=4, column=0, padx=20, pady=20, columnspan = 2)
        self.sumbit_button = self.button

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
        print("Location:", choice)
        location = choice

    def itemOM_callback(self, choice):
        print("Item:", choice)
        item = choice

    
        

app = App()
app.mainloop()