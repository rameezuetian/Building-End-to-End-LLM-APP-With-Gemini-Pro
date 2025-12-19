# Building End-to-End LLM App with Gemini Pro 🚀

This project is an end-to-end Generative AI application built using **Google Gemini Pro** and **Streamlit**. It demonstrates how to integrate large language models (LLMs) and vision capabilities into an interactive web application. The project is part of the Udemy course **“Building Gen AI App: 12+ Hands-on Projects with Gemini Pro (2024)”**.

---

## 📌 Project Overview

The application allows users to:

* Interact with **Gemini Pro / Gemini Pro Vision** models
* Upload images and provide prompts for AI-based visual understanding
* Generate intelligent, contextual responses using Google’s Generative AI
* Use a clean and simple **Streamlit UI** for interaction

This project is designed to help learners understand the **complete workflow** of building, running, and deploying a GenAI-powered application.

---

## 🛠️ Tech Stack

* **Python 3.10**
* **Google Generative AI (Gemini Pro / Vision)**
* **Streamlit** – Web UI
* **Pillow (PIL)** – Image processing
* **Git & GitHub** – Version control

---

## 📂 Project Structure

```
Building-End-to-End-LLM-APP-With-Gemini-Pro/
│── app.py                 # Main Streamlit application
│── requirements.txt       # Project dependencies
│── README.md              # Project documentation
│── .gitignore             # Ignored files
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rameezuetian/Building-End-to-End-LLM-APP-With-Gemini-Pro.git
cd Building-End-to-End-LLM-APP-With-Gemini-Pro
```

### 2️⃣ Create & Activate Conda Environment

```bash
conda create -n gen_ai python=3.10 -y
conda activate gen_ai
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Google API Key

**Windows (PowerShell / CMD):**

```bash
set GOOGLE_API_KEY=your_api_key_here
```

**macOS / Linux:**

```bash
export GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the provided local URL in your browser to start using the app.

---

## 🖼️ Features

* 📤 Upload images for analysis
* 💬 Prompt-based interaction with Gemini Pro Vision
* ⚡ Fast and interactive Streamlit interface
* 🔐 Secure API key handling using environment variables

---

## 🎯 Learning Outcomes

* Understanding Gemini Pro & Vision APIs
* Building GenAI-powered applications
* Integrating LLMs with frontend tools
* Managing environments and dependencies
* Using GitHub for project versioning

---

## 🚧 Future Improvements

* Add chat history support
* Enable camera capture
* Deploy on Streamlit Cloud
* Add multiple Gemini models selection

---

## 👨‍💻 Author

**Muhammad Rameez**
Computer Science Student | Data Scientist | AI/ML Enthusiast
University of Engineering & Technology (UET)

---

## 📜 License

This project is for **educational purposes**. Feel free to fork and modify it for learning and personal use.

---

⭐ If you find this project useful, don’t forget to **star the repository**!
