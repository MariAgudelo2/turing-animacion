from flask import Flask, request, render_template
from Maquina_Turing import Maquina_Turing

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entrada = request.form['entrada']
        mt = Maquina_Turing(entrada)
        mt.procesar_cadena()

        pasos = mt.pasos
        transiciones = mt.transiciones_completas
        return render_template('index.html', pasos=pasos, transiciones=transiciones, entrada=entrada)

    # Si es GET, solo muestra el formulario
    return render_template('index.html', pasos=[], transiciones=[], entrada="")

if __name__ == '__main__':
    app.run(debug=True)
