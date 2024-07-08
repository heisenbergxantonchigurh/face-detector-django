from django.shortcuts import render
from .forms import UploadImageForm
from PIL import Image
import cv2
import numpy as np
from django.core.files.uploadedfile import InMemoryUploadedFile
import io
import base64
import requests

def detect_faces(image):
    img = np.array(Image.open(image))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    result_image = Image.fromarray(img).convert('RGB')
    return result_image

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            url = form.cleaned_data.get('url')
            
            if url:
                response = requests.get(url)
                image = io.BytesIO(response.content)
            
            result_image = detect_faces(image)
            
            buffer = io.BytesIO()
            result_image.save(buffer, format='JPEG')
            image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

            return render(request, 'detect/result.html', {'image_base64': image_base64})
    else:
        form = UploadImageForm()
    return render(request, 'detect/upload.html', {'form': form})
