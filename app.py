from flask import Flask, render_template, url_for, request
from gan_work import *
import inflect

app = Flask(__name__)
app.static_folder = 'static'
p = inflect.engine()


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        label = request.form['labels']
        img = generate_fashion_using_CGAN(label)
        return render_template('gan_index.html', img=img, label=p.plural(str(label).upper()))
        # images = list()
        # for i in range(2):
        #     image = generate_fashion_using_CGAN()
        #     images.append(image)
        # return render_template("gan_index.html", images=images)
        # show_something()
        # print_hello()
    return render_template('gan_index.html')


if __name__ == '__main__':
    app.run(debug=True)
