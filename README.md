# Overview


This repository contains code for an image caption generation system using deep learning techniques. The system leverages a pretrained VGG16 model for feature extraction and a custom captioning model which was trained using LSTM for generating captions. The model is trained on the Flickr8k dataset using an attention mechanism to improve caption quality.

Note: While using the VGG16 model for feature extraction provides accurate results, it's important to be mindful of memory usage. The VGG16 model can consume a significant amount of memory, potentially causing issues in resource-constrained environments. To address this, it's advised to consider using the MobileNetV2 model for feature extraction. MobileNetV2 strikes a balance between memory efficiency and performance, making it a practical choice for scenarios with limited resources. Consequently, in my deployed app, I've opted for MobileNetV2.

The key components of the project include:

-Image feature extraction using a pretrained VGG16 model (Consider using MobileNetV2 for memory efficiency)
-Caption preprocessing and tokenization
-Custom captioning model architecture with attention mechanism
-Model training and evaluation
-Flask + React app for interactive caption generation

![Screenshot][backend/Image_Web.png]
