import customtkinter as ctk
from generator import generate_password
number_of_symbols = 18

def displey_password(number_of_symbols):
    text_output.delete(0, "end")
    text_output.insert(0, generate_password(number_of_symbols))
    




# тестовый комментарий



ctk.set_appearance_mode("dark")

root = ctk.CTk()

root.title("генератор паролей")
root.resizable(0,0)
root.configure(fg_color="#2E99B0")
text_output = ctk.CTkEntry(root,
                           placeholder_text="PASSWORD",
                           corner_radius=0,
                           width=14*number_of_symbols,
                           height=40,
                           justify="center",
                           font=("monospace",20,"bold"))
text_output.grid(column=0, row=0, padx=40, pady = 40)
pass_btn = ctk.CTkButton(root,
                        text="Genefate",
                        fg_color="#FF9B50",
                        hover_color="#C63D2F",
                        corner_radius=0,
                        height=40,
                        font=("sens-serif",20,"bold"),
                        command=lambda:displey_password(number_of_symbols))
pass_btn.grid(column=0, row=1, padx=40, pady = (0,40),sticky= "we")










# всегда последная строка
root.mainloop()