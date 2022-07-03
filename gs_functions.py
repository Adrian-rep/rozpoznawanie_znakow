import cv2


def preprocessing(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.equalizeHist(image)
    image = image / 255.0
    return image


def get_class_name(class_number):
    if class_number == 0:
        return 'Speed Limit 20 km/h'
    elif class_number == 1:
        return 'Speed Limit 30 km/h'
    elif class_number == 2:
        return 'Speed Limit 50 km/h'
    elif class_number == 3:
        return 'Speed Limit 60 km/h'
    elif class_number == 4:
        return 'Speed Limit 70 km/h'
    elif class_number == 5:
        return 'Speed Limit 80 km/h'
    elif class_number == 6:
        return 'End of Speed Limit 80 km/h'
    elif class_number == 7:
        return 'Speed Limit 100 km/h'
    elif class_number == 8:
        return 'Speed Limit 120 km/h'
    elif class_number == 9:
        return 'No passing'
    elif class_number == 10:
        return 'No passing for vehicles over 3.5 metric tons'
    elif class_number == 11:
        return 'Right-of-way at the next intersection'
    elif class_number == 12:
        return 'Priority road'
    elif class_number == 13:
        return 'Yield'
    elif class_number == 14:
        return 'Stop'
    elif class_number == 15:
        return 'No vehicles'
    elif class_number == 16:
        return 'Vehicles over 3.5 metric tons prohibited'
    elif class_number == 17:
        return 'No entry'
    elif class_number == 18:
        return 'General caution'
    elif class_number == 19:
        return 'Dangerous curve to the left'
    elif class_number == 20:
        return 'Dangerous curve to the right'
    elif class_number == 21:
        return 'Double curve'
    elif class_number == 22:
        return 'Bumpy road'
    elif class_number == 23:
        return 'Slippery road'
    elif class_number == 24:
        return 'Road narrows on the right'
    elif class_number == 25:
        return 'Road work'
    elif class_number == 26:
        return 'Traffic signals'
    elif class_number == 27:
        return 'Pedestrians'
    elif class_number == 28:
        return 'Children crossing'
    elif class_number == 29:
        return 'Bicycles crossing'
    elif class_number == 30:
        return 'Beware of ice/snow'
    elif class_number == 31:
        return 'Wild animals crossing'
    elif class_number == 32:
        return 'End of all speed and passing limits'
    elif class_number == 33:
        return 'Turn right ahead'
    elif class_number == 34:
        return 'Turn left ahead'
    elif class_number == 35:
        return 'Ahead only'
    elif class_number == 36:
        return 'Go straight or right'
    elif class_number == 37:
        return 'Go straight or left'
    elif class_number == 38:
        return 'Keep right'
    elif class_number == 39:
        return 'Keep left'
    elif class_number == 40:
        return 'Roundabout mandatory'
    elif class_number == 41:
        return 'End of no passing'
    elif class_number == 42:
        return 'End of no passing by vehicles over 3.5 metric tons'

