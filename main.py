from CTkMenuBar import *
import customtkinter as ctk
from assets.calendar.ctk_date_picker import CTkDatePicker
from pathlib import Path 


#----dealing with the fonts---------------------------
FONT_PATH = Path(__file__).parent / "assets" / "fonts" / "Avenir-Next-Demi.otf"
ctk.FontManager.load_font(str(FONT_PATH))
assert FONT_PATH.exists(), f"Font not found: {FONT_PATH}"

#------Variables-----------------------------------------------

colours =   config.colours
locations = config.locations
items =     config.items
tabOptions = config.tabOptions

location = "N/A"
item = "N/A"
date = "N/A"

fontSize = [ 10, 15, 20]
#--------------------------------------------------------------



class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Lost and Found")
        self.configure(fg_color=colours[0])

        self.menu_bar = CTkMenuBar(master=self,bg_color = colours[1],height = 30)
        self.menu_bar.add_cascade(tabOptions[0],)
        self.menu_bar.add_cascade(tabOptions[1])

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=10, border_color=colours[1])
        self.main_frame.pack(side = "left", padx=20, pady = 20)

        self.top_title = ctk.CTkLabel(self.main_frame, text="  Lost Report ",font=("Avenir Next W1G", fontSize[2]), text_color=colours[1], bg_color="transparent", height = 20)
        self.top_title.grid(row=0, column=0, padx=20, pady=20, columnspan = 2)

        self.location_title = ctk.CTkLabel(self.main_frame, text="  Location : ", text_color=colours[1], bg_color="transparent", height = 20)
        self.location_title.grid(row=1, column=0, padx=20, pady=20)

        self.optionmenu_var = ctk.StringVar(value = locations[0])#                     <-- default location is N/A
        self.location_optmenu = ctk.CTkOptionMenu(self.main_frame, values= locations,
                                                    font=("Avenir Next W1G", fontSize[1]),
                                                    command= self.locationOM_callback,
                                                    variable=self.optionmenu_var,
                                                    fg_color=colours[1])
        self.location_optmenu.grid(row=1, column=1, padx=20, pady=20)

        self.item_title = ctk.CTkLabel(self.main_frame, 
                                       text="  Item : ", 
                                       font=("Avenir Next W1G", fontSize[1]),
                                       text_color=colours[1], 
                                       bg_color="transparent", 
                                       height = 20)
        self.item_title.grid(row=2, column=0, padx=20, pady=20)

        self.itemmenu_var = ctk.StringVar(value = items[0])#                     <-- default location is N/A
        self.item_optmenu = ctk.CTkOptionMenu(self.main_frame, values= items,
                                                        command= self.itemOM_callback,
                                                        variable=self.itemmenu_var,
                                                        fg_color=colours[1])
        self.item_optmenu.grid(row=2, column=1, padx=20, pady=20)

        self.date_title = ctk.CTkLabel(self.main_frame, 
                                       text="  Date : ", 
                                       font=("Avenir Next W1G", fontSize[1]),
                                       text_color=colours[1], 
                                       bg_color="transparent", 
                                       height = 20)
        self.date_title.grid(row=3, column=0, padx=20, pady=20)

        self.calender = CTkDatePicker(self.main_frame, fg_color=colours[1])
        self.calender.set_allow_manual_input(False)
        self.calender.grid(row=3, column=1, padx=20, pady=20)


        self.submit_button = ctk.CTkButton(self.main_frame, text="Submit",
                                                    font=("Avenir Next W1G", fontSize[1]),
                                                    fg_color=colours[1],
                                                    command = self.submit_button_callbck)

        self.submit_button.grid(row=4, column=0, padx=20, pady=10, columnspan = 2)
    

        self.error_message = ctk.CTkLabel(self.main_frame, text=" ERROR",
                                          font=("Avenir Next W1G", fontSize[1] ),
                                          text_color=colours[1], 
                                          bg_color="transparent",
                                          height = 20)
        self.error_message.grid(row=5, column=0, padx=20, pady=10, columnspan = 2)



    def submit_button_callbck(self):
        date = self.calender.get_date()
        print(f"submit button clicked ( date : {date}, location : {location}, Item : {item} )")

    def locationOM_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)
        print("Location:", choice)
        location = choice

    def itemOM_callback(self, choice):
        print("Item:", choice)
        item = choice

      

app = App()
app.mainloop()