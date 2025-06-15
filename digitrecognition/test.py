import tensorflow as tf
model = tf.keras.models.load_model('digit_model.h5')
print("Model loaded successfully")