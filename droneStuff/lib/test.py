import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os

class Landing:
    def __init__(self):
        # Initialize
        self.knn_classifier = KNeighborsClassifier(n_neighbors=5)

        # Define sample images as class attributes
        self.test_img = cv2.imread("test_images/test_img.png")
        self.test_img2 = cv2.imread("test_images/test_img2.png")
        self.sample_img = cv2.imread("test_images/Landing1/img65.png")
        self.sample_img2 = cv2.imread("test_images/Landing2/img149.png")
        self.sample_img3 = cv2.imread("test_images/Control4/img65.png")
        self.sample_img4 = cv2.imread("test_images/Control3/img14.png")

    def load_and_preprocess_images_from_folder(self, folder):
        images = []
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, (128, 128))  # Resize
                images.append(img.flatten())
        return images

    def train_knn_classifier(self):
        # Load and preprocess
        control_images1 = self.load_and_preprocess_images_from_folder("control1")
        control_images2 = self.load_and_preprocess_images_from_folder("control2")
        control_images3 = self.load_and_preprocess_images_from_folder("control3")
        control_images4 = self.load_and_preprocess_images_from_folder("control4")
        landing_images1 = self.load_and_preprocess_images_from_folder("landing1")
        landing_images2 = self.load_and_preprocess_images_from_folder("landing2")
        landing_images3 = self.load_and_preprocess_images_from_folder("landing3")
        landing_images4 = self.load_and_preprocess_images_from_folder("landing4")

        # Create labels; (0 for "control", 1 for "landing")
        control_labels1 = np.zeros(len(control_images1))
        control_labels2 = np.zeros(len(control_images2))
        control_labels3 = np.zeros(len(control_images3))
        control_labels4 = np.zeros(len(control_images4))
        landing_labels1 = np.ones(len(landing_images1))
        landing_labels2 = np.ones(len(landing_images2))
        landing_labels3 = np.ones(len(landing_images3))
        landing_labels4 = np.ones(len(landing_images4))

        # Combine
        X = np.array(
            control_images1 + control_images2 + control_images3 + control_images4 + landing_images1 + landing_images2 + landing_images3 + landing_images4)
        y = np.concatenate((control_labels1, control_labels2, control_labels3, control_labels4, landing_labels1,
                            landing_labels2, landing_labels3, landing_labels4))

        # Split the data into training and testing sets
        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train KNN classifier
        self.knn_classifier.fit(X_train, y_train)

    def detect_target(self, image):
        # Preprocess
        processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        processed_image = cv2.resize(processed_image, (128, 128))  # Adjust

        # Visualize the preprocessed image
        plt.imshow(processed_image, cmap='gray')
        plt.title('Preprocessed Image')
        plt.show()

        processed_image = processed_image.flatten().reshape(1, -1)

        # Use the KNN classifier to predict
        prediction = self.knn_classifier.predict(processed_image)

        # If the prediction is 1, target is detected
        if prediction == 1:
            alert_message = "Target detected, drop the package!"
            return alert_message
        else:
            return None

# Example usage:
landing_detector = Landing()
landing_detector.train_knn_classifier()

# Assuming your input image is 'test_img'
alert_message = landing_detector.detect_target(landing_detector.test_img)

if alert_message:
    print(alert_message)
else:
    print("No target detected. Continue normal operation.")

