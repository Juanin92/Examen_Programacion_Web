from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    nombre = ""
    edad = ""
    cantidad = ""

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        PRECIO_TARRO = 9000
        total_sin_desc = cantidad * PRECIO_TARRO

        if 18 <= edad <= 30:
            porcentaje_desc = 0.15
        elif 31 > 30:
            porcentaje_desc = 0.25
        else:
            porcentaje_desc = 0.0

        monto_desc = total_sin_desc * porcentaje_desc
        total_pagar = total_sin_desc - monto_desc

        resultado = {
            'nombre': nombre,
            'total_sin_desc': int(total_sin_desc),
            'monto_desc': int(monto_desc),
            'total_pagar': total_pagar
        }

    return render_template('ejercicio1.html', resultado = resultado, nombre=nombre, edad=edad,
                           cantidad=cantidad)

if __name__ == '__main__':
    app.run(debug=True)