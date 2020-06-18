from flask import Flask, render_template, url_for, request
from gan_work import *

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        images = list()
        for i in range(2):
            image = generate_fashion_using_CGAN()
            images.append(image)
        return render_template("gan_index.html", images=images)
        # show_something()
        # print_hello()
    return render_template('gan_index.html')


if __name__ == '__main__':
    app.run(debug=True)
