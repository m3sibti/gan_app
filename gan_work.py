import matplotlib.pyplot as plt
from tensorflow import keras
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import base64

models_dir = './pretrained_models/'


def print_hello():
    print('Hello')


# function to create inputs
def get_inputs(latent_dim=100, n_imgs=10, target_class='shirt'):
    # dictionary for labels
    labels_dict = {'tshirt': 0, 'trouser': 1, 'pullover': 2,
                   'dress': 3, 'coat': 4, 'sandal': 5,
                   'shirt': 6, 'sneaker': 7, 'bag': 8, 'ankle_boot': 9}

    # target class can be any label 0-9
    labels_to_generate = np.zeros((n_imgs, 1)) + labels_dict[target_class]
    z = np.random.normal(size=(n_imgs, latent_dim))
    return [z, labels_to_generate]


def generate_fashion_using_CGAN():
    # initialize Conditional-GAN
    fahion_generator = keras.models.load_model(f'{models_dir}conditional_fashion_gan.h5')
    # generate fake images
    tc = 'bag'  # for generating labels
    gen_imgs = fahion_generator(get_inputs(target_class=tc))
    # plot them
    plt.figure(figsize=(10, 10))
    for i in range(5):
        plt.subplot(1, 5, i + 1)
        plt.axis('off')
        plt.imshow(gen_imgs[1, :, :, 0], cmap='gray_r')
    # plt.show()
    pngImage = io.BytesIO()
    f = plt.savefig('k.')
    FigureCanvas(f).print_png(pngImage)
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String


def plot_view():
    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("title")
    axis.set_xlabel("x-axis")
    axis.set_ylabel("y-axis")
    axis.grid()
    axis.plot(range(5), range(5), "ro-")

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String
