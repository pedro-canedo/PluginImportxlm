from ast import If
from flask import Flask
import pandas as pd
from Excel import Import

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Api de importações de arquivos conveste serviços financeiros'

@app.route('/importfiles', methods=['POST'])
def importFiles():
    Import()
    return 'Arquivos importados com sucesso'



app.run(host='0.0.0.0')