from tensorflow.python.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.python.keras.applications import VGG16
from tensorflow.python.keras.optimizers import Adam


class Neural:
    def launch_neural(self):
        vgg16_net = VGG16(weights='imagenet', include_top=False, input_shape=(161, 161, 3))
        vgg16_net.trainable = False

        model = Sequential()
        model.add(vgg16_net)
        # Добавляем в модель новый классификатор
        model.add(Flatten())
        model.add(Dense(256))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(2))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy',
                      optimizer=Adam(lr=1e-5),
                      metrics=['accuracy'])
        model.load_weights("mnist_model.h5")
        return model

nPh = 6
for i in range (nPh):
    model = Neural().launch_neural()
    img = image.load_img('img/img-1.png', target_size=(161, 161))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x) / 255
    preds = model.predict(x)
    classes = ['утка', 'колесо', 'стерка', 'ничего']
    print(classes[np.argmax(preds)])