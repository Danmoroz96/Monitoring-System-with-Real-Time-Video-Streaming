# Monitoring-System-with-Real-Time-Video-Streaming
In this lab, I will build a simple real-time home monitoring system.


# IoT Home Monitoring System Lab

## Team / Roles
* **Sender (Camera Node):** My Laptop (Tested on a single machine)
* **Viewer (Receiver Node):** My Laptop (Tested on a single machine)

## Network Details
* **Sender IP Address:** `127.0.0.1` (localhost) 
*(Note: Because this lab was completed on a single laptop acting as both the sender and the viewer, the loopback/localhost address was used instead of a local Wi-Fi IP address).*

## How the Stream Was Started
1. Opened Command Prompt and navigated to the project folder.
2. Started the Flask server by running the command: `python app.py`.
3. Verified the console output indicated the server was running on port `5000`.

## Results
* **Could the viewer watch the live stream?** Yes. By opening a web browser and navigating to `http://127.0.0.1:5000`, the live webcam video was successfully displayed and updated continuously in real-time.

## Problems or Fixes
* **Hardware limitation:** I only had access to one laptop for this lab. 
* **Fix:** I adapted the architecture by running the Flask server locally and viewing the stream via the `localhost` address. The underlying pipeline (Camera → Capture → Encode → Stream → Viewer) remained exactly the same as requested by the lab instructions.

* <img width="867" height="845" alt="Screenshot 2026-04-15 213743" src="https://github.com/user-attachments/assets/6187cf42-3c7a-405c-914a-c46921a5994e" />

<img width="567" height="957" alt="Screenshot 2026-04-15 213810" src="https://github.com/user-attachments/assets/98d282d6-4ccc-472c-817b-4efafb8d405c" />

<img width="1912" height="951" alt="Screenshot 2026-04-15 215017" src="https://github.com/user-attachments/assets/c899d1f8-b08a-42ba-a7c7-9691b04d2abf" />

<img width="1172" height="201" alt="Screenshot 2026-04-15 215051" src="https://github.com/user-attachments/assets/bad6a886-9dee-42f7-9374-d1978f62d4c1" />

<img width="1047" height="1020" alt="Screenshot 2026-04-15 221146" src="https://github.com/user-attachments/assets/130560e2-211b-4458-8e92-3dab61f5d133" />




