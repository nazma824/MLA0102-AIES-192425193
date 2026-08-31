from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Circle image
img1 = Image.new("L", (100,100), "white")
d = ImageDraw.Draw(img1)
d.ellipse((25,25,75,75), outline="black", width=5)

# Square image
img2 = Image.new("L", (100,100), "white")
d = ImageDraw.Draw(img2)
d.rectangle((25,25,75,75), outline="black", width=5)

# Display images
plt.subplot(1,2,1)
plt.imshow(img1, cmap="gray")
plt.title("Circle")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(img2, cmap="gray")
plt.title("Square")
plt.axis("off")

plt.show()



import numpy as np
from sklearn.cluster import KMeans

# Convert images into feature vectors
X = np.array([
    np.array(img1).flatten(),
    np.array(img2).flatten()
])

# Apply K-Means
model = KMeans(n_clusters=2, random_state=42, n_init=10)
result = model.fit_predict(X)

print("PATTERN RECOGNITION RESULTS")
print("---------------------------")
print("Circle  -> Cluster", result[0] + 1)
print("Square  -> Cluster", result[1] + 1)
