GLASS = 0
PAPER = 1
CARDBOARD = 2
PLASTIC = 3
METAL = 4
TRASH = 5

DIM1 = 128
DIM2 = 128
# Convolutional Layer 1.
filter_size1 = 3 
num_filters1 = 32

# Convolutional Layer 2.
filter_size2 = 3
num_filters2 = 32

# Convolutional Layer 3.
filter_size3 = 3
num_filters3 = 64

# FCL
fc_size = 128


img_size = 128
num_channels = 3
batch_size =4
img_size_flat = img_size * img_size * num_channels

img_shape = (img_size, img_size)

validation_size = 0.16
early_stopping = None
classes = ['cardboard', 'glass','metal', 'paper', 'plastic','trash']
num_classes = len(classes)
train_path = 'data/train/'
test_path = 'data/test/'
checkpoint_dir = 'data/models/'
