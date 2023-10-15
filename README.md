# Waste Classification Web Application

# Description
This web application provides an intuitive interface for users to upload an image of waste. Once uploaded, the application employs a deep learning model to classify the waste, determining its category and whether it can be recycled.

# Task
The primary objective was to:
Create an accessible platform for users to determine the category of waste via image uploads.
Apply machine learning to classify waste into distinct categories, aiding in waste management and promoting recycling.

# Solution
1. Web Interface: Developed using HTML and CSS, the interface allows seamless image uploads and displays classification results.
2. Backend with Flask: The Flask framework serves the application, handling image uploads and displaying prediction results.
3. Deep Learning with CNN: Started with a basic Convolutional Neural Network (CNN) model to classify waste images.
4. Transfer Learning with VGG16: Enhanced the model's performance using the VGG16 architecture, a renowned model for image classification. This approach leverages pre-trained weights to improve accuracy and efficiency.
5. Dataset Management: Used the "garbage_classification_enhanced" dataset containing 12 waste categories. The dataset was split, stratified, and images were pre-processed to fit the model's requirements.
6. Training & Evaluation: The model was trained, validated, and evaluated using metrics like precision, recall, and F1-score. Additionally, the learning rate was adjusted during training to optimize performance.
7. Prediction Interface: Integrated the trained model into the web interface, allowing users to get real-time classifications for uploaded waste images.

# Tech Stack & Languages Used
- Backend: Python with the Flask framework
- Deep Learning: Keras (CNN and VGG16 for Transfer Learning)
- Frontend: HTML and CSS

# Screenshots 

