import jieba
import jieba.posseg as pseg
from datetime import datetime

def find_nouns(text):
    nouns = set()
    words = pseg.cut(text)
    for word, flag in words:
        if 'n' in flag:
            nouns.add(word)
    return nouns

def highlight_text(text, words_to_highlight):
    for word in words_to_highlight:
        if word in text:
            text = text.replace(word, f'<span class="highlight">{word}</span>')
    return text

def update_html_with_highlighted_nouns_and_date(source_file, html_file, output_file):
    with open(source_file, 'r', encoding='utf-8') as file:
        first_line = file.readline().strip()
        second_line = file.readline().strip()

    nouns = find_nouns(second_line)
    highlighted_first_line = highlight_text(first_line, nouns)

    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    updated_html = html_content.replace('{{title1}}', highlighted_first_line)
    current_date = datetime.now().strftime("%Y年%m月%d日")
    updated_html = updated_html.replace('{{date}}', current_date)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(updated_html)

    return current_date,first_line

def replace():
    source_file = r'google_trends\source.txt'
    html_file = r'google_trends\index.html'
    output_file = r'google_trends\filled_index.html'
    date, body = update_html_with_highlighted_nouns_and_date(source_file, html_file, output_file)
    return date, body
if __name__ == "__main__":
    replace()
