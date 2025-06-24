## 📧 Spam Emails and SMS Classifier
A machine learning-based web application that classifies text messages and emails as Spam or Ham (Not Spam) using Natural Language Processing (NLP) techniques and a pre-trained classifier. Built with Python and Streamlit.

# 📖 Overview
This project applies Natural Language Processing (NLP) and machine learning techniques to detect spam in both emails and SMS messages. A trained model is used in a Streamlit web app that allows users to paste or type a message and classify it in real-time.

# 🧰 Tech Stack
## Technology	Description
->Python	Core programming language
->Scikit-learn	For ML modeling and TF-IDF vectorization
->NLTK	Text preprocessing (tokenization, cleaning)
->Streamlit	Web UI for user interaction
->Pandas	Data manipulation and analysis
->Pickle	Save/load model and vectorizer

# 📊 Dataset Used
->SMS Spam Collection Dataset
->Emails(CSV)

# 📁 Spam-Emails-SMS-Classifier
│
├── app.py                # Streamlit app UI
├── model.pkl             # Trained ML model (e.g. Multinomial Naive Bayes)
├── vectorizer.pkl        # Saved TF-IDF vectorizer
├── train_model.py        # (Optional) model training script
├── spam.csv              # Dataset (or another .csv file)
├── requirements.txt      # List of required libraries
└── README.md             # This file

# ⚙️ How It Works
1.Load data
Labeled SMS/email text with spam and ham categories.
2.Preprocess text
Remove punctuation, lowercase, remove stopwords, lemmatization.
3.Convert text into TF-IDF vectors
Represent text numerically using TfidfVectorizer.
4.Train the classifier
Commonly used: Multinomial Naive Bayes or Logistic Regression.
5.Save model & vectorizer
With pickle for reuse in the app.
6.Build the web app
Using Streamlit for input, prediction, and display.

# 💻 Installation
Clone the repository

bash
'''
git clone https://github.com/sowmya13531/Spam-Emails-SMS-Classifier.git
cd Spam-Emails-SMS-Classifier
'''

# 🚀 Usage



# 🖼️ Sample Output
Input: "Congratulations! You’ve won a $1000 Walmart gift card. Click here to claim."
Output: 🚫 This is Spam (96.23% confidence)

Input: "Let’s meet for dinner tomorrow."
Output: ✅ This is Ham (98.45% confidence)
