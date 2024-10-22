import customtkinter as ctk
from tkinter import font

def main():
    # Window
    window = ctk.CTk()
    window.title('Font Previewer')
    
    x_pos = window.winfo_screenwidth() // 2 - 600 // 2
    y_pos = int(window.winfo_screenheight() * 0.1)
    window_size = "600x400"
    geometry = "+".join([window_size, str(x_pos), str(y_pos)])
    window.geometry(geometry)
    
    def update_text(text):
        for widget in fonts_frame.winfo_children():
            if int(widget.grid_info()["column"]) == 1:
                widget.destroy()
        
        for i, font_name in enumerate(fonts):
            ctk.CTkLabel(master=fonts_frame, text=text, font=(font_name, 16)).grid(column=1, row=i, sticky='nsew')
        
    # Variable
    text = ctk.StringVar(value='Testing fonts')
    
    # Get Fonts
    fonts=list(font.families())
    fonts.sort()
    
    # Input Frame
    input_frame = ctk.CTkFrame(master=window)
    input_frame.pack(pady=8, padx=40, fill='x', expand=True)
    
    ctk.CTkLabel(master=input_frame, text='Text to preview').pack(pady=4, padx=10)
    text_entry = ctk.CTkEntry(master=input_frame, textvariable=text)
    text_entry.pack(pady=4, padx=10)
    ctk.CTkButton(master=input_frame, text='Preview', command=lambda: update_text(text.get())).pack(pady=4, padx=10)
    
    # Fonts Frame
    fonts_frame = ctk.CTkScrollableFrame(master=window)
    fonts_frame.pack(pady=8, padx=40, fill='both', expand=True)
    fonts_frame.grid_columnconfigure([0,1], weight=1)
    listnumber = 0
    for item in fonts:
        ctk.CTkLabel(master=fonts_frame, text=item).grid(column=0, row=listnumber, sticky='nsew')
        ctk.CTkLabel(master=fonts_frame, text=text.get(), font=(item, 16)).grid(column=1, row=listnumber, sticky='nsew')
        listnumber += 1
    
    window.mainloop()
    
    
if __name__ == "__main__":
    main()