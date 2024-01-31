from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("base.html")


@app.route('/introduccion')
def about():
  return render_template('about.html')


@app.route('/Activos')
def Activos():
  return render_template('Activos.html')


@app.route('/registrar')
def registrar():
  return render_template('registrar.html')


@app.route('/eliminar')
def eliminar():
  return render_template('eliminar.html')


#ejecutar desde el editor de texto preferible visual estudio code#
if __name__ == '__main__':
  app.run(debug=True, port=5017)