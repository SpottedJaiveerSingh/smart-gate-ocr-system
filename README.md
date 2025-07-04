# 🚘 Smart Gate OCR Monitoring System

A real-time AI-powered vehicle number plate recognition system designed for gated societies and secure campuses. This project uses live camera feeds, OCR, and a Streamlit interface to automate vehicle logging, resident verification, and alerting for unauthorized vehicles.

---

## 🔧 Features

- 🔍 **OCR-based vehicle number detection** using live webcam
- 🏠 **Resident vehicle manager** with editable sidebar UI
- 🕵️ **Visitor/outsider log tracking** stored in SQLite
- 🚫 **Restricted vehicle list** with real-time siren alert
- 📊 View and manage all records from a clean Streamlit dashboard
- 💾 Data stored securely and persistently in `SQLite` database

---

## 🖥️ Technologies Used

- **Python 3.11+**
- **OpenCV** – Live camera and image handling
- **EasyOCR** – Optical character recognition (license plates)
- **Streamlit** – Frontend dashboard and interface
- **SQLite** – Database for storing residents and visitors
- **Pandas** – Data manipulation and table views
- **Playsound** – Siren audio alert for blocked vehicles

---

## 📁 Project Structure

smart_gate_ocr/
├── main.py # Main Streamlit app
├── camera_utils.py # Handles camera + OCR logic
├── db.py # SQLite database operations
├── background.jpeg # Optional background image
├── siren.mp3 # Siren for blocked vehicles
├── database.db # Auto-generated SQLite DB
├── requirements.txt # List of dependencies

yaml
Copy
Edit

---

## 🚀 How to Run Locally

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/smart_gate_ocr.git
cd smart_gate_ocr
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run main.py
Make sure your webcam is connected and working.

✍️ How It Works
Start the camera from the UI.

Vehicles stopping in front of the camera are scanned using OCR.

If the number matches:

A resident vehicle: No action is taken.

A blocked vehicle: A siren is triggered.

An outsider vehicle: Logged into the visitor table.

View or edit resident vehicles in the sidebar.

All data is stored locally in database.db.

📸 Demo Preview
Insert screenshots or a link to your demo video here.

📦 Future Improvements
Add YOLO-based plate detection for better accuracy

Facial recognition integration

Admin login system with role-based access

Cloud database support (e.g., Firebase, PostgreSQL)

Mobile app integration (Flutter/React Native)

📄 License
This project is open-source under the MIT License.

👨‍💻 Author
Jaiveer Singh
B.Tech CSE (AI & ML)
