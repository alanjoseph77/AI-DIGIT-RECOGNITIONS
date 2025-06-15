import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
import tensorflow as tf
import numpy as np
import cv2

model_path = os.path.join(settings.BASE_DIR, 'digitrecognition', 'digit_model.h5')
print(f"Loading model from: {model_path}")
model = tf.keras.models.load_model(model_path)

def home(request):
    return render(request, 'index.html')



def digitreco(request):
    return render(request, 'digitreco.html')

def predict_digit(image_path):
    try:
        print(f"Loading image from: {image_path}")
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"Image load failed for {image_path}")
            return "Error: Could not load image."
        print(f"Image shape: {img.shape}")
        img = cv2.resize(img, (28, 28))
        img = img / 255.0
        img = img.reshape(1, 28, 28, 1)
        print(f"Reshaped image shape: {img.shape}")
        prediction = model.predict(img)
        print(f"Prediction raw: {prediction}")
        digit = np.argmax(prediction) + 1
        print(f"Predicted digit: {digit}")
        return digit
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return f"Error: {str(e)}"

def predict(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)
        print(f"Saving file to: {file_path}")
        os.makedirs(os.path.dirname(file_path) or '.', exist_ok=True)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        print(f"File saved, size: {os.path.getsize(file_path)} bytes")  # Check file size
        digit = predict_digit(file_path)
        if isinstance(digit, str) and digit.startswith("Error"):
            return JsonResponse({'error': digit}, status=400)
        return JsonResponse({'digit': str(digit)})
    return JsonResponse({'error': 'No file uploaded'}, status=400)