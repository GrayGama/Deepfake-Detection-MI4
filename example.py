import numpy as np
from classifiers import *
# from pipeline import *

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 1 - Load the model and its pretrained weights
# classifier = Meso4()
# classifier.load('weights/Meso_DF.h5')

# classifier = MesoInception4()
# classifier.load('weights/M4I_DF_retrained_galma_2.h5')

classifier = MesoInception4()
classifier.load('MesoNet/weights/M4I_DF_retrained_galma_best.h5')

# 2 - Minimial image generator
# We did use it to read and compute the prediction by batchs on test videos
# but do as you please, the models were trained on 256x256 images in [0,1]^(n*n)

test_dir = 'MesoNet/test_images'

dataGenerator = ImageDataGenerator(rescale=1./255)
generator = dataGenerator.flow_from_directory(
        test_dir,
        target_size=(256, 256),
        batch_size=4,
        class_mode='binary',
        # subset='training',
        shuffle=False
        )

# 3 - Predict
X, y = generator.next()
print('Predicted :', classifier.predict(X), '\nReal class :', y)

