# Voice Verification Model

## Overview

A machine learning model for speaker identification and voice authentication using audio feature analysis. This model authenticates users by analyzing their voice patterns as part of a multimodal security system.

## Model Building Steps

### 1. **Data Collection & Loading**

• Collected audio samples from 3 speakers (Jeremiah, Armand, Christian)
• Recorded phrases: "Yes, approve" and "Confirm transaction"
• Applied audio augmentations (pitch shift, time stretch, background noise)
• Loaded and validated audio features dataset

### 2. **Feature Engineering**

• Extracted MFCC (Mel-Frequency Cepstral Coefficients) features from audio
• Enhanced features with statistical measures (standard deviation, range)
• Applied robust scaling to normalize feature values
• Generated 16 total features per audio sample

### 3. **Model Training & Optimization**

• Tested multiple algorithms: Random Forest, XGBoost, SVM, Logistic Regression
• Used stratified k-fold cross-validation (2-3 folds)
• Applied hyperparameter tuning with GridSearchCV
• Selected best model based on F1-score performance

### 4. **Model Selection & Evaluation**

• Compared models using multiple metrics
• Selected Random Forest as the best performing model
• Generated confusion matrix and classification reports
• Saved model, scaler, and label encoder for production use

## Final Model Type

**Random Forest Classifier** - An ensemble learning method that uses multiple decision trees for classification. This is a **classification model** (not regression) that predicts discrete speaker categories.

## Performance Metrics

| Metric        | Score | Description                                                |
| ------------- | ----- | ---------------------------------------------------------- |
| **Accuracy**  | 1.000 | Percentage of correct predictions out of total predictions |
| **F1-Score**  | 1.000 | Harmonic mean of precision and recall (balanced measure)   |
| **Precision** | 1.000 | True positives / (True positives + False positives)        |
| **Recall**    | 1.000 | True positives / (True positives + False negatives)        |

## What These Metrics Mean

• **Accuracy (100%)**: The model correctly identified the speaker in all test cases
• **F1-Score (100%)**: Perfect balance between precision and recall - no false positives or negatives
• **Precision (100%)**: When the model predicts a speaker, it's always correct
• **Recall (100%)**: The model successfully identifies all instances of each speaker

## Model Features

• **Speakers Supported**: 3 (Jeremiah, Armand, Christian)
• **Feature Count**: 16 MFCC-based audio features
• **Authentication Threshold**: 50% confidence for verification
• **Training Data**: Augmented audio samples with multiple variations per speaker

## Usage

The model serves as a voice verification component in a multimodal authentication system, confirming user identity through voice pattern analysis before approving transactions or system access.

## Files Generated

• `voiceprint_model.pkl` - Trained Random Forest model
• `voiceprint_scaler.pkl` - Feature scaling transformer
• `voiceprint_encoder.pkl` - Speaker label encoder
• `voiceprint_metadata.json` - Model performance and configuration data
