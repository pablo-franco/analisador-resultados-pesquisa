from datetime import datetime
from os import path

from src.config.const import results_folder

def export_to_md(search_type, search_text, prompt_text, results):
    file_path = path.join(results_folder, generate_file_name())
    header = f'## Tipo de busca\n{search_type}\n## Texto da busca\n{search_text}\n## Texto do prompt\n{prompt_text}\n\n'
    with open(file_path, mode='wt', encoding='utf-8') as f:
        f.write(header)
        f.write(results)
    return file_path

def generate_file_name():
    return f"{datetime.now().strftime('%Y%Y%Y%Y%m%d%H%M%S')}.md"