from flask import Flask, render_template_string

app = Flask(__name__)

# Função pra ler os arquivos HTML e CSS
def get_file_content(filename):
    with open(filename, encoding='utf-8') as f:
        return f.read()

# Página inicial
@app.route('/')
def home():
    html = get_file_content('Games.html')
    css = get_file_content('eric.css')
    page = html.replace('</head>', f'<style>{css}</style></head>')
    return render_template_string(page)

# Página de contato
@app.route('/contato')
def contato():
    html = get_file_content('contato.html')
    css = get_file_content('eric.css')
    page = html.replace('</head>', f'<style>{css}</style></head>')
    return render_template_string(page)

if __name__ == '__main__':
    app.run(debug=True)
