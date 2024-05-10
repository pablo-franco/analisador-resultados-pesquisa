from src.view.window import MainWindow
from tkinter.messagebox import showinfo

from src.service.gemini_service import analyse_search_results
from src.service.http_service import google_search
from src.service.file_service import export_to_md

def show():
    main_window = MainWindow(execute_callback=execute_command, clear_callback=clear_command, export_callback=export_command)
    main_window.show()

def execute_command(window:MainWindow):
    search_type = window.get_selected_type()
    search_text = window.get_search_text()
    prompt = window.get_prompt_text()
    search_results = google_search(search_text, search_type)
    results = analyse_search_results(search_results, prompt)
    window.set_result_text(results)

def clear_command(window:MainWindow):
    window.clear_all()

def export_command(window:MainWindow):
    search_type = window.get_selected_type()
    search_text = window.get_search_text()
    prompt_text = window.get_prompt_text()
    results = window.get_result_text()
    file = export_to_md(search_type, search_text, prompt_text, results)
    showinfo('Exportar', f'Resultados exportados com sucesso: {file}')