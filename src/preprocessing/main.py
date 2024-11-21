import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

print("Caminho Atual:", sys.path)

from src.preprocessing.video_capture_emotion import capture_emotion

def main():
    capture_emotion()

if __name__ == "__main__":
    main()