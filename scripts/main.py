from . import auth
import warnings

# Suppress the StandardScaler feature names warning
warnings.filterwarnings("ignore", category=UserWarning)

def get_image_input():
    """Gets the image file path from the user."""
    image_path = input("Please enter the path to your facial image to begin: ")
    return image_path

def main():
    """Main function to orchestrate the sequential authentication pipeline."""
    print("--- User Identity and Product Recommendation System ---\n")

    artifacts = auth.load_artifacts()
    if not artifacts:
        return

    # Step 1: Get image and perform facial recognition
    image_path = get_image_input()
    recognized_name = auth.run_face_auth(
        image_path,
        artifacts['face_model'],
        artifacts['face_scaler'],
        artifacts['face_encoder']
    )

    # Step 2: If face is recognized, proceed to voice verification
    if recognized_name:
        print(f"\nWelcome, {recognized_name}. Please verify your identity with your voice.")
        audio_path = input("Enter the path to your voice sample: ")
        
        voice_auth_passed = auth.run_voice_auth(
            recognized_name, # Use the name from the face scan for verification
            audio_path,
            artifacts['voice_model'],
            artifacts['voice_scaler'],
            artifacts['voice_encoder']
        )
        
        if voice_auth_passed:
            print("\n======================================")
            print(f"🔐 AUTHENTICATION SUCCESSFUL for {recognized_name}!")
            print("======================================")
            print("(Product recommendation model would be called here.)\n")
        else:
            print("\n--- Authentication Failed ---")
    else:
        print("\n--- Authentication Failed ---")


if __name__ == "__main__":
    main()