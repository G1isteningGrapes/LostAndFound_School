import customtkinter as ctk
from assets.calendar.ctk_date_picker import CTkDatePicker
from pathlib import Path 

#----dealing with the fonts---------------------------
FONT_PATH = Path(__file__).parent / "assets" / "fonts" / "Avenir-Next-Demi.otf"
ctk.FontManager.load_font(str(FONT_PATH))
assert FONT_PATH.exists(), f"Font not found: {FONT_PATH}"
#------------------------------------------------------


#------Variables-----------------------------------------------

cols = [  "#FDF0D5",  "#669BBC",   "#003049",   "#780000"] # colours
#      light yellow,  light blue,   dark blue    dark blue

locL = ["N/A", "Cafeteria", "Sigma", "Crowell"] # locations

itmL = ["N/A", "I.D.", "Clothing", "Water bottle", "Electronic"]

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

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent",border_width=10,border_color=cols[1])
        self.main_frame.pack()
        
        self.top_title = ctk.CTkLabel(self.main_frame, text="  Lost Report ", text_color=cols[1], bg_color="transparent", height = 20)
        self.top_title.grid(row=0, column=0, padx=20, pady=20, columnspan = 2)

        self.location_title = ctk.CTkLabel(self.main_frame, text="  Location : ", text_color=cols[1], bg_color="transparent", height = 20)
        self.location_title.grid(row=1, column=0, padx=20, pady=20)


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

        self.calender = CTkDatePicker(self.main_frame, fg_color=cols[1])
        self.calender.set_allow_manual_input(False)
        self.calender.grid(row=3, column=0, padx=20, pady=20)

        def print_date():
            print(f"Selected Date: {self.calender.get_date()}")

        self.btn = ctk.CTkButton(self.main_frame, text="Print Date", command=print_date)
        self.btn.grid(row=3, column=1, padx=20, pady=20)

        self.sumbit_button = ctk.CTkButton(self.main_frame, text="Submit",
                                                    font=("Avenir Next W1G", 20), 
                                                    fg_color=cols[1] ,
                                                    command = self.button_callbck)
        self.sumbit_button.grid(row=4, column=0, padx=20, pady=20, columnspan = 2)

        

    def button_callbck(self):
        print("button clicked")

    def locationOM_callback(self, choice):
        print("Location:", choice)
        location = choice
    def itemOM_callback(self, choice):
        print("Item:", choice)
        item = choice

    
        

app = App()
app.mainloop()