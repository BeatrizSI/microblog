from datetime import datetime
import json
from flask import Flask, render_template, request

from forms import ContatoForm

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Abri o arquivo de posts
    f = open('posts.json', 'r')
    # Converti o texto em lista
    posts = json.loads(f.read())
    # Quando chamou o POST para salvar um novo arquivo
    if request.method == 'POST':
        # Adicionei na lista de posts
        hoje = datetime.now()
        posts.append({
            'content': request.values['content'],
            'date': hoje.strftime("%d/%m/%Y %H:%M"),
            'like': 0,
            'unlike': 0,
        })
        # Salvei tudo no banco
        f = open('posts.json', 'w')
        f.write(json.dumps(posts))
        f.close()
    return render_template('index.html', titulo="Microblog de PWEB1", posts=posts)


@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = ContatoForm(csrf_enabled=False)
    if form.validate_on_submit():
        return 'Formulário enviado com sucesso, por %s/%s' % (form.data['nome'], form.data['email'])
    return render_template('contato.html', titulo="Contato", form=form)    


@app.route('/sobre/')
def sobre():
    return 'Este é o nosso primeiro projeto Flask!'