# Email-Spam-Detector
# 📧 Email Spam Detector

A machine learning web application that classifies messages as **Spam** or **Not Spam** using Natural Language Processing (NLP) and the Multinomial Naive Bayes algorithm.

The project provides a simple web interface built with Flask, allowing users to enter a message and view its predicted category.

## ✨ Features

- **Spam Detection:** Classifies messages as Spam or Not Spam.
- **Machine Learning Model:** Uses TF-IDF for text feature extraction and Multinomial Naive Bayes for classification.
- **Web Interface:** Simple interface powered by Flask, HTML, and CSS.
- **Reset Functionality:** Reset the interface to check another message.
- **Local Execution:** Run the application locally on your computer.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| Scikit-learn | Machine learning and text vectorization |
| TF-IDF | Converts text into numerical features |
| Multinomial Naive Bayes | Message classification |
| HTML | Web page structure |
| CSS | Interface styling |
| Kaggle Dataset | Training data source |

## 📂 Project Structure

```text
Email-Spam-Detector/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── SMSSpamCollection
└── spam_model.pkl
```

**File descriptions:**

- `app.py` — Runs the Flask web application.
- `train_model.py` — Contains the model training code.
- `spam_model.pkl` — Stores the saved machine learning model.
- `SMSSpamCollection` — Dataset file used by the project.
- `templates/index.html` — Contains the web interface.
- `static/style.css` — Defines the interface styling.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.9 or later recommended
- pip package manager
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Email-Spam-Detector.git
```

Navigate to the project directory:

```bash
cd Email-Spam-Detector
```

Replace `YOUR-USERNAME` with your GitHub username and use your actual repository name if it differs.

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask pandas scikit-learn
```

If your code imports additional libraries, install those dependencies too.

### 4. Train the model (if required)

```bash
python train_model.py
```

This should generate or update `spam_model.pkl` if the training script is configured to save the model at that location.

If the provided model file is already available and compatible with your application, you may not need to retrain it.

### 5. Run the application

```bash
python app.py
```

Open the local URL shown in your terminal, typically:

```text
http://127.0.0.1:5000/
```

## 🚀 How to Use

1. Start the Flask application.
2. Open the application in your browser.
3. Enter a message in the input area.
4. Submit the message for classification.
5. View the prediction: **Spam** or **Not Spam**.
6. Use the reset button to clear the interface and check another message.

## 🧠 How It Works

The application follows a basic machine learning text-classification pipeline:

1. **Dataset Preparation:** Load and prepare the labelled dataset.
2. **Text Feature Extraction:** TF-IDF converts text into numerical features based on word importance.
3. **Model Training:** Multinomial Naive Bayes learns patterns from the labelled training data.
4. **Model Saving:** The trained model is saved for reuse.
5. **Prediction:** The Flask application processes the entered message and displays the predicted category.

## 🔮 Future Improvements

- Display prediction confidence or probability, if appropriately calibrated.
- Add model evaluation metrics such as precision, recall, F1-score, and a confusion matrix.
- Improve the interface for mobile devices.
- Add a prediction history feature.
- Deploy the application online.

## 🎯 Project Objective

The objective of this project is to demonstrate how machine learning and natural language processing can be used to classify text messages through a simple, interactive web application.

## 👩‍💻 Author

**Chandani**

- GitHub: [Chandani](https://github.com/chandnii207)
- Project Repository: [Email Spam Detector](https://github.com/chandnii207/Email-Spam-Detector)

## 📄 License

This project is available for educational and learning purposes. Add a license file if you intend to distribute it under a specific open-source license.
