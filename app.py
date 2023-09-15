#importa o framkework Flask e o outro importa a renderização de templates
#que estão na pasta templates
from flask import Flask, render_template

app = Flask(__name__)

#rotas de html
@app.route('/')
#essa função importa a pagina inicial
def index():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)