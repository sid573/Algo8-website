from flask import Flask, request, render_template,redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/ml_ai')
def ml_ai():
    return render_template('ml_ai.html')

@app.route('/manufacturing')
def manufacturing():
    return render_template('manufacturing.html')

@app.route('/banking')
def banking():
    return render_template('banking.html')

@app.route('/healthcare')
def healthcare():
    return render_template('healthcare.html')

@app.route('/insurance')
def insurance():
    return render_template('insurance.html')

@app.route('/retail')
def retail():
    return render_template('retail.html')

@app.route('/telecom')
def telecom():
    return render_template('telecom.html')

@app.route('/government')
def government():
    return render_template('government.html')

@app.route('/custom_ai')
def custom_ai():
    return render_template('custom_ai.html')

@app.route('/oil_natural_gas')
def oil_natural_gas():
    return render_template('oil_natural_gas.html')

@app.route('/loc8')
def loc8():
    return render_template('loc8.html')

@app.route('/vision8')
def vision8():
    return render_template('vision8.html')

@app.route('/opini8')
def opini8():
    return render_template('opini8.html')

@app.route('/career')
def career():
    return render_template('careers.html')

@app.route('/dimension')
def dimension():
    return render_template('dimension.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/events/')
def event():
    return redirect("/events", code=302)

@app.route('/dimension/gallery')
def dim_gallery():
    return render_template('dim_gallery.html')


if __name__ == '__main__':
    app.run()
