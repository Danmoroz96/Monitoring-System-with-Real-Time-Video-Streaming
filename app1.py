from flask import Flask, Response
import cv2
from datetime import datetime  # Added for the bonus timestamp task

app = Flask(__name__)
camera = cv2.VideoCapture(0)

# Modification 1: Force a higher camera resolution (1280x720)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not camera.isOpened():
    raise RuntimeError("Could not open webcam.")

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Bonus Task: Add a live timestamp to the top-left of the frame
        # Get current time as a formatted string
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Draw the text on the frame (Image, Text, Position, Font, Scale, Color(B,G,R), Thickness, Line Type)
        cv2.putText(frame, current_time, (10, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Encode the modified frame
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def home():
    # Modification 2: Changed the HTML width from 640 to 800
    return """
    <html>
        <head>
            <title>Home Monitoring Stream</title>
        </head>
        <body>
            <h2>Live Camera Stream (High Res & Timestamp)</h2>
            <img src="/video_feed" width="800">
        </body>
    </html>
    """

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
