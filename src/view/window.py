from tkinter import Tk, Entry, Label, Frame, Button, Radiobutton, X, Y, BOTH, END, StringVar
from tkinter.scrolledtext import ScrolledText

from src.service.enum import SearchType
from src.config.const import app_icon_path, app_title, font_type, font_size


class MainWindow():
    def __init__(self, execute_callback, clear_callback, export_callback) -> None:
        self.execute_callback = execute_callback
        self.clear_callback = clear_callback
        self.export_callback = export_callback
        self.tk = Tk()
        self.initialize_components()

    def initialize_components(self):
        self.tk.geometry('800x600+50+50')
        self.tk.title(app_title)
        self.tk.iconbitmap(app_icon_path)

        input_font = (font_type, font_size)
        button_font = (font_type, font_size)
        results_font = (font_type, font_size)

        self.selected_type = StringVar(value=SearchType.ALL)

        type_frame = Frame(self.tk)
        type_frame.pack(side='top', fill=X)
        
        input_frame = Frame(self.tk)
        input_frame.pack(side='top', fill=X)

        execute_command_frame = Frame(self.tk)
        execute_command_frame.pack(side='top', fill=X)

        results_frame = Frame(self.tk)
        results_frame.pack(side='top', fill=X)

        action_buttons_frame = Frame(self.tk)
        action_buttons_frame.pack(side='bottom', fill=X)

        labels_frame = Frame(input_frame)
        labels_frame.pack(side='left')

        entries_frame = Frame(input_frame)
        entries_frame.pack(side='left')

        all_radio = Radiobutton(type_frame, text='Todas', value=SearchType.ALL, variable=self.selected_type)
        all_radio.pack(side='left')

        img_radio = Radiobutton(type_frame, text='Imagens', value=SearchType.IMAGE, variable=self.selected_type)
        img_radio.pack(side='left')

        news_radio = Radiobutton(type_frame, text='Notícias', value=SearchType.NEWS, variable=self.selected_type)
        news_radio.pack(side='left')

        vid_radio = Radiobutton(type_frame, text='Vídeos', value=SearchType.VIDEO, variable=self.selected_type)
        vid_radio.pack(side='left')


        search_text_label = Label(labels_frame, text='Texto da pesquisa: ', font=input_font)
        search_text_label.pack(side='top')

        prompt_text_label = Label(labels_frame, text='Texto do prompt: ', font=input_font)
        prompt_text_label.pack(side='top')

        self.search_text_entry = Entry(entries_frame, font=input_font, width=100)
        self.search_text_entry.pack(side='top')

        self.prompt_text_entry = Entry(entries_frame, font=input_font, width=100)
        self.prompt_text_entry.pack(side='top')

        execute_button = Button(execute_command_frame, text='Executar', font=button_font, command=self.execute_button_clic)
        execute_button.pack(side='right')

        self.results_text = ScrolledText(results_frame, font=results_font, height=18)
        self.results_text.pack(side='top', fill=X)

        clear_button = Button(action_buttons_frame, text='Limpar', font=button_font, command=self.clear_button_clic)
        clear_button.pack(side='right')

        export_button = Button(action_buttons_frame, text='Exportar', font=button_font, command=self.export_button_clic)
        export_button.pack(side='right')
    
    def show(self):
        self.tk.mainloop()

    def execute_button_clic(self):
        self.execute_callback(self)

    def export_button_clic(self):
        self.export_callback(self)

    def clear_button_clic(self):
        self.clear_callback(self)

    def get_search_text(self):
        return self.search_text_entry.get()
    
    def get_prompt_text(self):
        return self.prompt_text_entry.get()
    
    def get_selected_type(self):
        return self.selected_type.get()
    
    def get_result_text(self):
        return self.results_text.get(1.0, END)

    def set_result_text(self, result_text):
        self.results_text.delete(1.0, END)
        self.results_text.insert(END, result_text)

    def clear_all(self):
        self.search_text_entry.delete(0, END)
        self.prompt_text_entry.delete(0, END)
        self.results_text.delete(1.0, END)