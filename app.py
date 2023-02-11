from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        n = request.form['n']
        p = request.form['p']
        k = request.form['k']
        temperature = request.form['temperature']
        humidity = request.form['humidity']
        ph = request.form['ph']
        rainfall = request.form['rainfall']
        return "N: {}, P: {}, K: {}, Temperature: {}, Humidity: {}, pH: {}, Rainfall: {}".format(n, p, k, temperature, humidity, ph, rainfall)
    return  '''
        <form method="post">
            N: <input type="text" name="n"><br>
            P: <input type="text" name="p"><br>
            K: <input type="text" name="k"><br>
            Temperature: <input type="text" name="temperature"><br>
            Humidity: <input type="text" name="humidity"><br>
            pH: <input type="text" name="ph"><br>
            Rainfall: <input type="text" name="rainfall"><br>
            <input type="submit" value="Submit"><br>
        </form>
    '''

if __name__ == '__main__':
    app.run()
