
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1,)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.logo_label = customtkinter.CTkLabel(self, text="ProjectX", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0,column=1,padx=0, pady=(0, 5),sticky='n')

        # create tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=0, column=1, padx=(10,10), pady=(25, 10),sticky='nsew')
        self.tabview.add("Phone list")
        self.tabview.add("Notes")
        self.tabview.add("Folder sort")
        self.tabview.tab("Phone list").grid_columnconfigure(0, weight=1)# configure grid of individual tabs
        self.tabview.tab("Notes").grid_columnconfigure(0, weight=1)

        
        self.entry = customtkinter.CTkEntry(self.tabview.tab('Phone list'), placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=0, columnspan=2, padx=(10, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self.tabview.tab('Phone list'), text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(5, 10), pady=(20, 20), sticky="nsew")

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