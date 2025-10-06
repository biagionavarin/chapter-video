from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/methodology')
def methodology():
    return render_template('methodology.html')

@app.route('/carbon_app')
def carbon_app():
    return render_template('carbon_app.html')
@app.route("/car-emission")
def car_emission():
    return render_template("links/car_emission.html")

@app.route("/electric-car-emission")
def electric_car_emission():
    return render_template("links/electric_car_emission.html")

@app.route("/bus-emission")
def bus_emission():
    return render_template("links/bus_emission.html")

@app.route("/airplane-emission")
def airplane_emission():
    return render_template("links/airplane_emission.html")

@app.route("/train-emission")
def train_emission():
    return render_template("links/train_emission.html")

@app.route("/electric-scooter-emission")
def electric_scooter_emission():
    return render_template("links/electric_scooter_emission.html")

@app.route("/bicycle-emission")
def bicycle_emission():
    return render_template("links/bicycle_emission.html")


@app.route('/logout')
def logout():
    return render_template('buttons/logout.html')

@app.route('/register')
def register():
    return render_template('buttons/register.html')

@app.route('/logreg')
def logreg():
    return render_template('buttons/logreg.html')

@app.route('/meet_us')
def meet_us():
    return render_template('buttons/meet_us.html')

@app.route('/paper')
def paper():
    return render_template('buttons/paper.html')

if __name__ == '__main__':
    app.run(debug=True)
