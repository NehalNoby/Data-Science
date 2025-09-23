import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt 


(X_train,y_train),(X_test,y_test)=tf.keras.datasets.mnist.load_data()

X_train=X_train.astype("float32")/255.0
X_test=X_test.astype("float32")/255.0

#Reshape data (CNN exkpects 3D:height,width,channels)
X_train=X_train.reshape(-1,28,28,1)   
#-1 means "figure this dimension out automatically"
X_test=X_test.reshape(-1,28,28,1)     #1 is the number of channels

#5.Build simple CNN model
model=models.Sequential([
    layers.Conv2D(32,(3,3),activation="relu",input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),

    layers.Dense(64,activation="relu"),
    layers.Dense(10,activation="softmax")
])

#6.Compile Model
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

#7.Train Model
history=model.fit(
    X_train,y_train,
    epochs=5,
    batch_size=64,
    validation_data=(X_test,y_test),
    verbose=1)

#8.Evaluate on test data
test_loss,test_acc=model.evaluate(X_test,y_test,verbose=0)
print("Test accuracy:",round(test_acc*100,2),"%")

#9.Predict Example
prediction =model.predict(X_test[:1])
predicted_label=prediction.argmax()

plt.imshow(X_test[0].reshape(28,28),cmap="gray")
plt.title("Prediction: "+str(predicted_label))
plt.axis("off")
plt.show()