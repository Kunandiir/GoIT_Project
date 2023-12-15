
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout
        self.grid_columnconfigure(0, weight=1,)
        self.grid_columnconfigure(1, weight=5)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self)
        self.sidebar_frame.grid(row=0,column=0,rowspan=4,padx=0,pady=0,sticky='nsew')
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid_rowconfigure(4, weight=1)


        # add sidebar functions
        self.sidebar_logo = customtkinter.CTkLabel(self.sidebar_frame, text='Functions',font=customtkinter.CTkFont(size=20, weight="bold"))
        self.sidebar_logo.grid(row=0,column=0,padx=0,pady=(10,10),sticky='new')
        self.sidebar_addphone_button =customtkinter.CTkButton(self.sidebar_frame,text='Add new phone')
        self.sidebar_addphone_button.grid(row=1,column=0,padx=0,pady=(0,10),sticky='new')


        # add logo
        self.logo_label = customtkinter.CTkLabel(self, text="ProjectX", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0,column=1,padx=0, pady=(10, 5),sticky='n')

        # create tabview
        self.tabview = customtkinter.CTkFrame(self,fg_color='transparent')
        self.tabview.grid(row=0, column=1, padx=(10,10), pady=(40, 10),sticky='nsew')
        self.tabview.grid_columnconfigure((0,1,2,3,4), weight=1)# configure grid of individual tabs

        
        # create scrollable frame
        self.phones_list = customtkinter.CTkScrollableFrame(self.tabview,height=350, label_text="Phone list", fg_color='black')
        self.phones_list.grid(row=0,column=0,columnspan=5, padx=0, pady=(5,0), sticky="ew")
        self.phones_list.grid_columnconfigure(0, weight=1)

        self.phones_list_frames = []
        for i in range(10):
            self.phone_frame =  customtkinter.CTkFrame(self.phones_list)
            self.phone_frame.grid_columnconfigure((0,1), weight=20)
            self.phone_frame.grid_columnconfigure(2,weight=1)
            self.phone_frame.grid(row=i,column=0,padx=10,pady=(0,20),sticky='new')
            self.name_label = customtkinter.CTkLabel(self.phone_frame, text='name'+str(i),font=customtkinter.CTkFont(size=18, weight="bold"))
            self.name_label.grid(row=0,column=0,rowspan=2,padx=0,pady=0, sticky='nsw')
            self.adress_label = customtkinter.CTkLabel(self.phone_frame, text='address'+str(i),font=customtkinter.CTkFont(size=15, weight="bold"))
            self.adress_label.grid(row=0,column=1,padx=0,pady=0,sticky='nse')
            self.birthday_label = customtkinter.CTkLabel(self.phone_frame, text='birthday'+str(i),font=customtkinter.CTkFont(size=15, weight="bold"))
            self.birthday_label.grid(row=1,column=1,padx=0,pady=0,sticky='nse')
            for r in range(3):
                self.phone_label = customtkinter.CTkLabel(self.phone_frame, text='num'+str(r),font=customtkinter.CTkFont(size=10, weight="bold"))
                self.phone_label.grid(row=3+r,column=0,padx=0,pady=1,sticky='ns')
            self.edit_button = customtkinter.CTkButton(self.phone_frame, text='Edit')
            self.edit_button.grid(row=0,column=2,padx=0,pady=0,sticky='nsew')
        # create input path element
        self.entry = customtkinter.CTkEntry(self.tabview, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=0, columnspan=4, padx=(10, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self.tabview, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=4, padx=(5, 10), pady=(20, 20), sticky="nsew")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100

    def sidebar_button_event(self):
        print("sidebar_button click")



def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()