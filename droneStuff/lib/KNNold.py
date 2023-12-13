import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Load and preprocess the updated dataset (128x128 images)
def load_and_preprocess_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.resize(img, (128, 128))  # Resize to the desired size
            images.append(img.flatten())
    return images

control_images1 = load_and_preprocess_images_from_folder("control1")
control_images2 = load_and_preprocess_images_from_folder("control2")
control_images3 = load_and_preprocess_images_from_folder("control3")
control_images4 = load_and_preprocess_images_from_folder("control4")
landing_images1 = load_and_preprocess_images_from_folder("landing1")
landing_images2 = load_and_preprocess_images_from_folder("landing2")
landing_images3 = load_and_preprocess_images_from_folder("landing3")
landing_images4 = load_and_preprocess_images_from_folder("landing4")

# Create labels for your images (0 for "control", 1 for "landing")
control_labels1 = np.zeros(len(control_images1))
control_labels2 = np.zeros(len(control_images2))
control_labels3 = np.zeros(len(control_images3))
control_labels4 = np.zeros(len(control_images4))
landing_labels1 = np.ones(len(landing_images1))
landing_labels2 = np.ones(len(landing_images2))
landing_labels3 = np.ones(len(landing_images3))
landing_labels4 = np.ones(len(landing_images4))

# Combine control and landing data and labels
X = np.array(control_images1 + control_images2 + control_images3 + control_images4 + landing_images1 + landing_images2 + landing_images3 + landing_images4)
y = np.concatenate((control_labels1, control_labels2, control_labels3, control_labels4, landing_labels1, landing_labels2, landing_labels3, landing_labels4))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the KNN classifier with the updated data
knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(X_train, y_train)

# Now, your KNN classifier is retrained with the 128x128 images

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a KNN classifier with a specified number of neighbors (e.g., 5)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)


# Predict on the test set
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = np.mean(y_pred == y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Load the KNN classifier (assuming it's already trained)

# Load a sample image (replace 'sample_image.jpg' with the path to your image)
test_img = cv2.imread("test_img.png")
test_img2 = cv2.imread("test_img2.png")
sample_img = cv2.imread("Landing1\img65.png")
sample_img2 = cv2.imread("Landing2\img149.png")
sample_img3 = cv2.imread("Control4\img65.png")
sample_img4 = cv2.imread("Control3\img14.png")

current_img = sample_img

# Assuming your input image is 'sample_image'
processed_image = cv2.cvtColor(current_img, cv2.COLOR_BGR2GRAY)
processed_image = cv2.resize(processed_image, (128, 128))
processed_image = processed_image.flatten().reshape(1, -1

def detect_target(knn_classifier, image):
    # Preprocess the image (e.g., grayscale, flatten, resize if needed)
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.resize(processed_image, (128, 128))  # Adjust the size as needed
    
    # Visualize the preprocessed image
    plt.imshow(processed_image, cmap='gray')
    plt.title('Preprocessed Image')
    plt.show()

    processed_image = processed_image.flatten().reshape(1, -1)

    # Use the KNN classifier to predict the label
    prediction = knn_classifier.predict(processed_image)

    # If the prediction is 1, it means the target is detected
    if prediction == 1:
        # You can send a signal or return something to alert the drone
        alert_message = "Target detected, drop the package!"
        return alert_message
    else:
        # If no target is detected, continue normal operation
        return None

# Assuming your input image is 'sample_image'
alert_message = detect_target(knn_classifier, current_img)

if alert_message:
    print(alert_message)
else:
    print("No target detected. Continue normal operation.")



import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

class Detection():
	def load_and_preprocess_images_from_folder(folder):
		images = []
		for filename in os.listdir(folder):
			img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
			if img is not None:
				img = cv2.resize(img, (128, 128))  # Resize
				images.append(img.flatten())
		return images

	def create_labels(self):
		control_labels1 = np.zeros(len(control_images1))
		control_labels2 = np.zeros(len(control_images2))
		control_labels3 = np.zeros(len(control_images3))
		control_labels4 = np.zeros(len(control_images4))
		landing_labels1 = np.ones(len(landing_images1))
		landing_labels2 = np.ones(len(landing_images2))
		landing_labels3 = np.ones(len(landing_images3))
		landing_labels4 = np.ones(len(landing_images4))

	def combine(self):
		X = np.array(
			control_images1 + control_images2 + control_images3 + control_images4 + landing_images1 + landing_images2 + landing_images3 + landing_images4)
		y = np.concatenate((control_labels1, control_labels2, control_labels3, control_labels4, landing_labels1,
							landing_labels2, landing_labels3, landing_labels4))

	def train_test_split(self):
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

	def detect_target(knn_classifier, image):
		# Preprocess the image
		processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		processed_image = cv2.resize(processed_image, (128, 128))  # Adjust
		# Visualize the preprocessed image
		plt.imshow(processed_image, cmap='gray')
		plt.title('Preprocessed Image')
		plt.show()
		processed_image = processed_image.flatten().reshape(1, -1)

		# Use the KNN classifier to predict the label
		prediction = knn_classifier.predict(processed_image)

		# If the prediction is 1, it means the target is detected
		if prediction == 1:
		 # You can send a signal or return something to alert the drone
			alert_message = "Target detected, drop the package!"
			return alert_message
		else:
	# If no target is detected, continue normal operation
			return None