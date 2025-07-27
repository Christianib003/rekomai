import librosa
import cv2
import numpy as np

def extract_image_features(image_path, bins=(8, 8, 8)):
    """Loads a single image and extracts its histogram features."""
    try:
        image = cv2.imread(image_path)
        if image is None: return None
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1, 2], None, bins, [0, 180, 0, 256, 0, 256])
        cv2.normalize(hist, hist)
        return hist.flatten().reshape(1, -1)
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def extract_audio_features(audio_path):
    """Loads a single audio file and extracts its features."""
    try:
        y, sr = librosa.load(audio_path, sr=None)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfccs_mean = np.mean(mfccs.T, axis=0)
        
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        rolloff_mean = np.mean(rolloff)
        
        features = np.hstack((mfccs_mean, rolloff_mean))
        mfcc_std = np.std(mfccs_mean)
        mfcc_range = np.max(mfccs_mean) - np.min(mfccs_mean)
        
        enhanced_features = np.hstack((features, mfcc_std, mfcc_range))
        return enhanced_features.reshape(1, -1)
    except Exception as e:
        print(f"Error processing audio: {e}")
        return None