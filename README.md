# Image-Based Plant Disease Detection Using Deep Learning

This repository contains the implementation of an image-based plant disease detection system using deep learning techniques. The system aims to recognize different types of plant diseases by analyzing images of plant leaves.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Models Implemented](#models-implemented)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [Future Scope](#future-scope)
- [References](#references)

## Introduction

Efficient plant disease detection is crucial for sustainable agriculture and to mitigate the negative effects of climate change on crop yields. This project leverages the latest advancements in deep learning, particularly convolutional neural networks (CNNs), to develop a robust plant disease recognition model. The model is trained to identify 13 different plant diseases using leaf images.

## Dataset

The dataset used for training and testing the model consists of about 87,000 RGB images of healthy and diseased crop leaves, categorized into 38 different classes. The dataset is available from the following sources:
- [Kaggle: New Plant Diseases Dataset](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset)
- [ResearchGate: Simple model of ANN](https://www.researchgate.net/figure/Simple-model-of-ANN_fig1_304308800)

## Models Implemented

The project implements the following machine learning and deep learning models:
1. **Convolutional Neural Network (CNN)**: Specifically, the VGG-16 architecture was used for image classification.
2. **Support Vector Machine (SVM)**: Used for classification tasks.
3. **K-Nearest Neighbors (K-NN)**: Another classification algorithm used in the project.

### 1. Convolutional Neural Network (CNN)

**Architecture:** VGG-16

**Description:**
- VGG-16 is a deep convolutional neural network architecture proposed by the Visual Geometry Group from the University of Oxford.
- It consists of 16 layers, including 13 convolutional layers and 3 fully connected layers.
- The architecture uses small 3x3 filters throughout the convolutional layers, which helps in capturing fine details in images.
- The network includes max-pooling layers to reduce the spatial dimensions of the feature maps.
- The final layers are fully connected, followed by a softmax layer for classification.

**Advantages:**
- High accuracy in image classification tasks.
- The small filter size (3x3) allows for deep network architectures with fewer parameters compared to larger filter sizes.
- Pre-trained versions of VGG-16 are available, which can be fine-tuned for specific tasks, reducing training time.

### 2. Support Vector Machine (SVM)

**Description:**
- SVM is a supervised machine learning algorithm used for classification and regression tasks.
- It works by finding the hyperplane that best separates the data points of different classes in the feature space.
- SVM aims to maximize the margin between the closest data points of different classes, known as support vectors.
- It can handle linear and non-linear data by using kernel functions to transform the data into a higher-dimensional space where a linear separator can be found.

**Advantages:**
- Effective in high-dimensional spaces and when the number of dimensions exceeds the number of samples.
- Memory efficient as it uses a subset of training points in the decision function (support vectors).
- Versatile with different kernel functions (linear, polynomial, RBF, etc.) for handling non-linear data.

### 3. K-Nearest Neighbors (K-NN)

**Description:**
- K-NN is a simple, instance-based learning algorithm used for classification and regression tasks.
- It classifies a data point based on the majority class among its k-nearest neighbors in the feature space.
- The algorithm calculates the distance (usually Euclidean) between the data point and all other points in the training set to find the nearest neighbors.
- The choice of k (number of neighbors) is critical and can be optimized through cross-validation.

**Advantages:**
- Simple and easy to implement.
- No explicit training phase; all computation is deferred to the prediction phase.
- Naturally handles multi-class classification problems.

## Detailed Architecture of VGG-16

### VGG-16 Layers:

1. **Input Layer:** 
   - Takes input images of fixed size 224x224x3 (RGB).
2. **Convolutional Layers:**
   - The first two convolutional layers use 64 filters of size 3x3.
   - Followed by max-pooling.
   - Next two convolutional layers with 128 filters of size 3x3.
   - Followed by max-pooling.
   - Then three convolutional layers with 256 filters of size 3x3.
   - Followed by max-pooling.
   - Finally, three convolutional layers with 512 filters of size 3x3.
   - Followed by max-pooling.
3. **Fully Connected Layers:**
   - The first two fully connected layers have 4096 neurons each.
   - The third fully connected layer has 1000 neurons, corresponding to the number of classes in the ImageNet dataset.
4. **Output Layer:**
   - Softmax layer for multi-class classification.

### Hyperparameters and Training:

- **Optimizer:** Adam optimizer is used for training.
- **Loss Function:** Categorical cross-entropy for multi-class classification.
- **Data Augmentation:** Techniques like rescaling, shear range, zoom range, and horizontal flipping are applied to augment the training data.
- **Training and Validation Split:** The dataset is divided into 80% for training and 20% for validation.

## Comparison of Models:

### Performance:

- **CNN (VGG-16):**
  - Achieves the highest accuracy among the three models.
  - Effective in capturing complex patterns and features in images due to its deep architecture.
  - Requires significant computational resources for training.

- **SVM:**
  - Provides good classification results, especially in high-dimensional spaces.
  - Performance depends on the choice of kernel and hyperparameters.
  - Less effective than CNN for image classification tasks where feature extraction is crucial.

- **K-NN:**
  - Simple and intuitive approach to classification.
  - Performance heavily depends on the choice of k and distance metric.
  - Computationally expensive during the prediction phase, especially with large datasets.

## Technologies Used

- **Programming Language**: Python 3.6
- **Libraries and Frameworks**: 
  - TensorFlow/Keras
  - NumPy
  - Pandas
  - OpenCV
  - PyQt5 for GUI
- **Integrated Development Environment (IDE)**: PyCharm
- **Front-End**: PyQt5

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/plant-disease-detection.git
    ```

2. Navigate to the project directory:
    ```bash
    cd plant-disease-detection
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Training the Model**: To train the CNN model, run the following command:
    ```bash
    python train_model.py
    ```

2. **Predicting Diseases**: Use the GUI to upload an image of a leaf and get the disease prediction:
    ```bash
    python gui.py
    ```

## Results

The trained model can recognize different plant diseases with high accuracy. Sample output images and performance metrics are included in the `results` directory.

## Discussion

The CNN model, particularly the VGG-16 architecture, outperformed traditional machine learning models like SVM and K-NN in terms of accuracy. The model was trained on a high-end GPU due to the computational requirements.

## Conclusion

The project demonstrates the effectiveness of deep learning techniques in accurately detecting plant diseases from images. The VGG-16 based model provided the best results compared to other models.

## References

- [Kaggle: New Plant Diseases Dataset](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset)
- [ResearchGate: Simple model of ANN](https://www.researchgate.net/figure/Simple-model-of-ANN_fig1_304308800)
