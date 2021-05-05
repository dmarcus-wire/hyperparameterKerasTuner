# define the path to our output directory
OUTPUT_PATH = "output"

# initialize the input shape and number of classes
# spatial input of our data
# MNIST data is 28x28 with grayscale single channel
INPUT_SHAPE = (28, 28, 1)
# There are 10 classes
NUM_CLASSES = 10

# define the total number of epochs to train, batch size, and the
# early stopping patience
EPOCHS = 50
# batch size
BS = 32
# shortcuts training procedure if a metrics isn't improving, e.g. 5 epochs
EARLY_STOPPING_PATIENCE = 5