# Rekomai
Welcome to our repository for the **Formative 2 Assignment** on **Multimodal Data Preprocessing**. This project simulates a system that verifies a user's identity using both facial recognition and voice validation before recommending products tailored to them. It brings together different types of data — tabular, image, and audio — to demonstrate a real-world, intelligent authentication and recommendation workflow.

---

## 🚀 Project Summary

The goal of this system is to ensure that product recommendations are shown **only** to verified users. This is done by passing through multiple checkpoints:

1. The system first checks if the user is recognized by their **face**.
2. If successful, it allows the user to proceed to the **product recommendation model**.
3. Before the final prediction is shown, the system performs **voice validation**.
4. If either check fails, access is denied.

You can see this visually explained in the system flow diagram included in this repo.

---

## 📁 Project Structure

.
├── data/
│   ├── customer_social_profiles.csv
│   ├── customer_transactions.csv
│   ├── merged_dataset.csv
│   ├── image_features.csv
│   └── audio_features.csv
├── images/
│   └── [facial images from all members]
├── audio/
│   └── [voice recordings from all members]
├── notebooks/
│   └── preprocessing_and_analysis.ipynb
├── scripts/
│   ├── facial_recognition.py
│   ├── voice_verification.py
│   ├── product_recommendation.py
│   └── app_cli.py
├── models/
│   └── [saved trained models]
├── flowchart/
│   └── system_flow_diagram.png
├── README.md
└── requirements.txt

---

## 🔍 Features

- **Image Data**: Each team member submitted facial images (neutral, smiling, surprised) with added augmentations like grayscale, flipping, and rotation. Features were extracted and saved for training.
- **Audio Data**: Each member recorded key voice phrases with enhancements like noise addition and pitch shift. Audio features like MFCCs were extracted for voice validation.
- **Tabular Data**: Social and transactional datasets were merged and cleaned to create the training data for our product recommendation model.
- **ML Models**: We trained separate models for facial recognition, voice verification, and product recommendation using classifiers like Random Forest and XGBoost.
- **System Simulation**: The entire process is simulated through a script where users interact via the command line — including unauthorized attempts and full successful transactions.

---

## 📹 Demo

🎥 **[Link to Demo Video](#)**  
_This video shows the entire process, from identity verification to product recommendation._

---

## 👥 Team Contributors

- Clinton Pikita  
- Christian Iradukunda Byiringiro  
- Benitha Rutagengwa  
- Armand Kayiranga

---

## 📦 Setup

Install the required dependencies using:

```bash
pip install -r requirements.txt

Thanks for checking out our project!
