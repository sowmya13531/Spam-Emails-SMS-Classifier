# 📧 Spam Emails and SMS Classifier
A machine learning-based web application that classifies text messages and emails as Spam or Ham (Not Spam) using Natural Language Processing (NLP) techniques and a pre-trained classifier. Built with Python and Streamlit.

## 📖 Overview
This project applies Natural Language Processing (NLP) and machine learning techniques to detect spam in both emails and SMS messages. A trained model is used in a Streamlit web app that allows users to paste or type a message and classify it in real-time.


# 🧰 Tech Stack
## Technology	Description
->Python	Core programming language
->Scikit-learn	For ML modeling and TF-IDF vectorization
->NLTK	Text preprocessing (tokenization, cleaning)
->Streamlit	Web UI for user interaction
->Pandas	Data manipulation and analysis
->Pickle	Save/load model and vectorizer

## 🧠 NLP Techniques Used

The following NLP techniques were applied to preprocess the data:

- 🔤 **Lowercasing**
- ✂️ **Punctuation and Special Character Removal**
- 🧹 **Stopword Removal**
- 🔄 **Stemming** using PorterStemmer (NLTK)
- 🔢 **TF-IDF Vectorization** to convert text to numeric format

## ⚙️ How It Works

1. **Data Loading** – Reads datasets (`spam.csv`, exception -`emails.csv`)
2. **Data Preprocessing** – Applies text cleaning and NLP techniques
3. **Feature Extraction** – Transforms text using TF-IDF
4. **Model Training** – Uses classification algorithms like:
   - Multinomial Naive Bayes
   - Logistic Regression
   - Binomial Regression 
5. **Evaluation** – Accuracy, Confusion Matrix, Precision, Recall
6. **Prediction** – Classifies new messages/emails
6. **Save model & vectorizer**
With pickle for reuse in the app.
7. **Build the web app**
Using Streamlit for input, prediction, and display.

## 📈 Results

- Achieved **high accuracy** (>95%) on both Email and SMS datasets
- Models are lightweight and efficient
- Performs well even on small messages

---

## 🛠 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/sowmya13531/Spam-Emails-SMS-Classifier.git
   cd Spam-Emails-SMS-Classifier
   


# 🖼️ Sample Output
Input: "Congratulations! You’ve won a $1000 Walmart gift card. Click here to claim."
Output: 🚫 This is Spam (96.23% confidence)

Input: "Let’s meet for dinner tomorrow."
Output: ✅ This is Ham (98.45% confidence)
