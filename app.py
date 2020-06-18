from flask import Flask, render_template, url_for, request
from gan_work import *

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        image = generate_fashion_using_CGAN()
        return render_template("gan_index.html", image=image)
        # show_something()
        # print_hello()
    return render_template('gan_index.html')


if __name__ == '__main__':
    app.run(debug=True)
