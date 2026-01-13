# 🔐 Phishing URL Detection using CNN

A deep learning–based system to classify URLs as **Phishing** or **Legitimate** using a **Convolutional Neural Network (CNN)**.  
The project includes URL preprocessing, model training with TensorFlow/Keras, a Flask REST API for real-time detection, and a simple web-based user interface.

---

## 📌 Features
- Detects phishing URLs using deep learning
- CNN-based model trained on real phishing & legitimate datasets
- URL preprocessing and tokenization
- Flask REST API for real-time predictions
- Simple HTML/CSS/JS frontend
- Modular and clean project structure

---

## 🗂 Project Structure
phishing-url-cnn/
│
├── dataset/
│ ├── raw/
│ └── processed/
│
├── src/
│ ├── preprocessing/
│ ├── model/
│ ├── utils/
│ └── api/
│
├── saved_models/
│ ├── cnn_url_model.h5
│ └── tokenizer.pkl
│
├── ui/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── notebooks/
├── requirements.txt
├── README.md
└── .gitignore

## ⚙️ Requirements
- Python **3.10**
- TensorFlow
- Flask

---

## 🛠 Installation

### 1️⃣ Clone the repository
bash
git clone https://github.com/Vikaymaker/Phishing-URL-Detection-using-CNN.git
cd Phishing-URL-Detection-using-CNN

### 2️⃣ Create virtual environment
py -3.10 -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

🧠 Train the Model

(Required only once)

python src/model/train.py

This will generate:

saved_models/
 ├── cnn_url_model.h5
 └── tokenizer.pkl

 🚀 Run Flask API
python src/api/app.py


API will run at:

http://127.0.0.1:5000

🌐 Run Frontend

Open the following file in a browser:

ui/index.html


Enter a URL to check whether it is Phishing or Legitimate.

🧪 Technologies Used

Python

TensorFlow / Keras

Flask

Scikit-learn

HTML, CSS, JavaScript

🎯 Use Cases

Cybersecurity applications

Phishing detection systems

Educational ML/DL projects

Resume & academic projects

👤 Author

Vijay B
Bachelor of Engineering – Computer Science
GitHub: https://github.com/Vikaymaker
