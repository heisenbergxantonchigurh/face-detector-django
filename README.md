# Face Detector Django

## Overview

This project is a Django-based web application for detecting faces in images. It allows users to upload an image and then displays the image with bounding boxes around the detected faces. This project utilizes OpenCV for face detection.

## Features

- **Image Upload:** Users can upload images through a simple web interface.
- **Face Detection:** The application uses OpenCV's Haar Cascade classifier for face detection.
- **Bounding Boxes:** Detected faces are highlighted with bounding boxes on the image.
- **Simple User Interface:** Easy-to-use web interface for image upload and result display.

## Technologies Used

- **Django:** A high-level Python web framework.
- **OpenCV (cv2):** A library of programming functions mainly aimed at real-time computer vision.
- **Python:** The programming language used for the backend.
- **HTML/CSS/JavaScript:** For the front-end user interface. (Likely minimal, but present).
- **PIL (Pillow):** Python Imaging Library to manage images.

## Setup and Installation

1.  **Clone the repository:**

    ```
    git clone https://github.com/heisenbergxantonchigurh/face-detector-django.git
    cd face-detector-django
    ```

2.  **Create a virtual environment (recommended):**

    ```
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

    _It is assumed a `requirements.txt` file exists. Example contents might be:_

    ```
    Django>=3.0
    opencv-python>=4.0
    Pillow>=9.0
    ```

4.  **Apply migrations:**

    ```
    python manage.py migrate
    ```

5.  **Create a superuser (optional, but recommended for initial access):**

    ```
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```
    python manage.py runserver
    ```

7.  **Access the application in your browser:** Go to `http://127.0.0.1:8000/`

## Usage

1.  Navigate to the application in your web browser.
2.  Upload an image using the file upload form.
3.  The application will process the image and display the image with the detected faces highlighted.

## Face Detection Implementation Details

The core face detection logic is likely implemented in `face_app/views.py`. It probably uses OpenCV's `cv2.CascadeClassifier` to load a pre-trained Haar Cascade XML file (e.g., `haarcascade_frontalface_default.xml`). The `detectMultiScale` method is used to detect faces in the image.

## Customization

- **Haar Cascade File:** You can try different Haar Cascade XML files for different types of face detection (e.g., profile faces). Modify the path to the XML file in `face_app/views.py`.
- **Detection Parameters:** Adjust the `scaleFactor`, `minNeighbors`, and `minSize` parameters in the `detectMultiScale` method to fine-tune the face detection.
- **Styling:** Modify the HTML templates and CSS files to customize the appearance of the application.

## Potential Improvements

- **More Robust Face Detection:** Explore more advanced face detection algorithms (e.g., deep learning-based detectors) for better accuracy.
- **Face Recognition:** Implement face recognition to identify detected faces.
- **Database Storage:** Store uploaded images and detection results in a database.
- **Asynchronous Processing:** Use Celery or other task queues to process images asynchronously, especially for large images.
- **Error Handling:** Implement more robust error handling and user feedback.
