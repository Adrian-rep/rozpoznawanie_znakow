import numpy as np
import cv2
import tensorflow as tf
from gs_functions import preprocessing, get_class_name
import os

model = tf.keras.models.load_model('./CNN_model_1_main_colab.hdf5')

for file_name in os.listdir('check_model'):
    print(file_name)
    image = cv2.imread(f'check_model/{file_name}')
    img = np.array(image)
    img = cv2.resize(img, (28, 28))
    img = preprocessing(img)
    img = img.reshape(1, 28, 28, 1)

    threshold = 0.90
    predictions = model.predict(img)
    class_index = np.argmax(predictions, axis=1)  # index max value
    probability = np.amax(predictions)
    if probability > threshold:
        print(f'{class_index} {get_class_name(class_index)}')
        print(f'{round(probability * 100, 2)}%')
    else:
        print(f"I don't know, max value:{class_index}  {get_class_name(class_index)}")
        print(f'{round(probability * 100, 2)}%')



# Część kodu do rozpoznania znaku z kamery

"""
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)

while True:

    # read image
    ret, frame = cap.read()

    # preprocessing
    img = np.asarray(frame)
    img = cv2.resize(img, (28, 28))
    img = preprocessing(img)
    img = img.reshape(1, 28, 28, 1)
    cv2.putText(frame, "CLASS: ", (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "PROBABILITY: ", (20, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)

    # predict
    threshold = 0.90
    predictions = model.predict(img)
    class_index = np.argmax(predictions, axis=1)
    probability = np.amax(predictions)
    if probability > threshold:
        cv2.putText(frame, str(class_index) + " " + str(get_class_name(class_index)),
                    (120, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, str(round(probability * 100, 2)) + "%", (180, 75),
                    font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Result", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""