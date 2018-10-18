from flask import Flask,render_template

app = Flask(__name__,static_folder='static')


@app.route('/')
def hello_world():
    return render_template('/index.html')

@app.route('/community')
def community():
    return render_template('/community.html')


if __name__ == '__main__':
    app.run(debug=True)
