This folder will host all the trained models.

# Voice Verification Model

Note: more info in the models/audio/README.md

## Overview

A machine learning model for speaker identification and voice authentication using audio feature analysis. This model authenticates users by analyzing their voice patterns as part of a multimodal security system.

## Best Model Type

**Random Forest Classifier** - An ensemble learning method that uses multiple decision trees for classification. This is a **classification model** (not regression) that predicts discrete speaker categories.

## Performance Metrics

| Metric        | Score | Description                                                |
| ------------- | ----- | ---------------------------------------------------------- |
| **Accuracy**  | 1.000 | Percentage of correct predictions out of total predictions |
| **F1-Score**  | 1.000 | Harmonic mean of precision and recall (balanced measure)   |
| **Precision** | 1.000 | True positives / (True positives + False positives)        |
| **Recall**    | 1.000 | True positives / (True positives + False negatives)        |
