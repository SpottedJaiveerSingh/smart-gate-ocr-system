import cv2
import time
import os
from datetime import datetime
from ocr_utils import extract_plate_text
from db import check_resident, log_outsider
import streamlit as st

os.makedirs('images', exist_ok=True)

def process_camera():
    cap = cv2.VideoCapture(0)
    vehicle_timer = {}
    threshold_time = 10
    st_frame = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to access the camera.")
            break

        resized = cv2.resize(frame, (640, 480))
        rgb_frame = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        st_frame.image(rgb_frame, channels="RGB")

        plate_number = extract_plate_text(resized)
        now = time.time()

        if plate_number:
            plate_number = plate_number.upper()
            if plate_number not in vehicle_timer:
                vehicle_timer[plate_number] = now
            else:
                duration = now - vehicle_timer[plate_number]
                if duration >= threshold_time:
                    time_in = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    image_name = f"images/{plate_number}_{int(now)}.jpg"
                    cv2.imwrite(image_name, resized)
                    if check_resident(plate_number):
                        print(f"[Resident] {plate_number} - No logging needed.")
                    else:
                        log_outsider(plate_number, time_in, int(duration), image_name)
                        print(f"[Outsider Logged] {plate_number} | Duration: {int(duration)}s")
                    del vehicle_timer[plate_number]

        # Add slight delay to avoid overloading the browser
        time.sleep(0.05)

    cap.release()
