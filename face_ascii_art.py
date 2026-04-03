import cv2
import numpy as np
import os
import pygame
from datetime import datetime

# More expressive character set, from darkest to lightest
ASCII_CHARS = "@%#*+=-:. "
OUTPUT_DIR = "face_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

pygame.mixer.init()

def play_sound():
    pygame.mixer.music.load("capture_sound.mp3")
    pygame.mixer.music.play()

def enhance_contrast(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    return clahe.apply(gray)

def convert_to_ascii(image, scale=0.3, font_scale=0.6, font_thickness=1):
    gray = enhance_contrast(image)

    height, width = gray.shape
    new_width = int(width * scale)
    new_height = int(height * scale * 0.55)  # Compensate for font height
    resized_gray = cv2.resize(gray, (new_width, new_height))

    cell_w, cell_h = 10, 18
    ascii_image = np.ones((new_height * cell_h, new_width * cell_w, 3), dtype=np.uint8) * 255

    for y in range(new_height):
        for x in range(new_width):
            pixel = int(resized_gray[y, x])
            char = ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
            cv2.putText(
                ascii_image, char,
                (x * cell_w, y * cell_h),
                cv2.FONT_HERSHEY_SIMPLEX,
                font_scale, (0, 0, 0), font_thickness, lineType=cv2.LINE_AA
            )
    return ascii_image

def convert_to_ascii_string(image, scale=0.15):
    gray = enhance_contrast(image)

    height, width = gray.shape
    new_width = int(width * scale)
    new_height = int(height * scale * 0.5)
    resized_gray = cv2.resize(gray, (new_width, new_height))

    ascii_str = ""
    for y in range(new_height):
        for x in range(new_width):
            pixel = int(resized_gray[y, x])
            ascii_str += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
        ascii_str += "\n"
    return ascii_str

def save_ascii_html(ascii_str, filename):
    html_content = f"""
<html>
<head><title>ASCII Art</title></head>
<body style='background-color: black; color: white; font-family: monospace; white-space: pre;'>{ascii_str}</body></html>
"""
    with open(filename, "w") as f:
        f.write(html_content)

def scan_and_ascii_multiple_faces():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    print("\nWaiting for people...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for i, (x, y, w, h) in enumerate(faces):
            print(f"{len(faces)} Face(s) detected!")
            face_img = frame[y:y + h, x:x + w]

            play_sound()

            ascii_img = convert_to_ascii(face_img)
            ascii_str = convert_to_ascii_string(face_img)

            bw_face = cv2.resize(cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY), (300, 300))
            live_frame = cv2.resize(frame, (300, 300))
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            ascii_file = os.path.join(OUTPUT_DIR, f"ascii_{timestamp}_{i}.png")
            bw_file = os.path.join(OUTPUT_DIR, f"bw_{timestamp}_{i}.png")
            html_file = os.path.join(OUTPUT_DIR, f"ascii_{timestamp}_{i}.html")

            cv2.imwrite(ascii_file, ascii_img)
            cv2.imwrite(bw_file, bw_face)
            save_ascii_html(ascii_str, html_file)

            cv2.imshow(f"ASCII Face {i + 1}", ascii_img)
            cv2.imshow(f"BW Face {i + 1}", bw_face)
            cv2.imshow("Live Feed", live_frame)

        cv2.putText(frame, f"People Detected: {len(faces)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if len(faces) > 0:
            cv2.waitKey(0)
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the project
scan_and_ascii_multiple_faces()
