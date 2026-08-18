\# 🇳🇬 Nigerian Language Classifier

A machine learning application that identifies whether a short text is written in English, Hausa, Igbo, or Yoruba. Built as a capstone project for the \*\*3MTT / NextGen AI \& Machine Learning\*\* program.



\## 📌 Project Overview

Language identification is an important component of many applications, including chatbots, translation systems, search engines, and other natural language processing (NLP) applications. This project develops a machine learning classifier that can identify four languages commonly used in Nigeria:

\- 🇬🇧 English

\- 🇳🇬 Hausa

\- 🇳🇬 Igbo

\- 🇳🇬 Yoruba



The application accepts a short text phrase and predicts the most likely language.



\## 🎯 Project Objective

The main objective is to build a working language classification system that can:

\- Accept a short text phrase as input

\- Identify the language of the text

\- Evaluate model performance using standard classification metrics

\- Provide an interactive user interface

\- Demonstrate the application of machine learning to a Nigerian context



\## ✨ Features

\- Text-based language identification

\- Supports English, Hausa, Igbo, and Yoruba

\- TF-IDF character n-gram feature extraction

\- Logistic Regression classification

\- Accuracy, precision, recall, and F1-score evaluation

\- Confusion matrix visualization

\- Manual testing with unseen phrases

\- Model confidence/probability estimates

\- Interactive Gradio web interface

\- Saved model and vectorizer for reuse



\## 🧠 How It Works

The application follows this pipeline:



User enters text

&#x20;      ↓

TF-IDF Character N-Gram Vectorization

&#x20;      ↓

Logistic Regression Classifier

&#x20;      ↓

Language Prediction

&#x20;      ↓

Confidence / Probability Scores



1\. Text Input - The user provides a short phrase. Example: Bawo ni o se wa loni?



2\. Feature Extraction

The text is converted into numerical features using TF-IDF with character n-grams. Character-level features are useful for language identification because languages often contain distinctive character sequences and spelling patterns.



3\. Classification

A Logistic Regression classifier uses the extracted features to predict one of the four supported languages.



4\. Prediction

The application returns the predicted language and model probability estimates.



📊 Dataset

The dataset contains 4,000 text samples:

|Language|Samples|
|-|-|
|English|1,000|
|Hausa|1,000|
|Igbo|1,000|
|Yoruba|1,000|



Each record contains:

id — unique sample identifier

text — language sample

language — target language

source — data source description

Data Source



The dataset used for this MVP consists of documented synthetically generated data. Synthetic data was used to create a balanced dataset across the four target languages within the available project timeframe. Because the dataset is synthetic, the evaluation results should not be interpreted as equivalent to performance on a large, naturally occurring Nigerian-language dataset.



🤖 Machine Learning Model (TF-IDF)



The project uses:

TfidfVectorizer(

&#x20;   analyzer="char",

&#x20;   ngram\_range=(2, 5),

&#x20;   min\_df=2

)



Character n-grams were selected because they can capture language-specific spelling and character patterns, which are useful when identifying languages from short text.



Classifier - The extracted features are passed into a Logistic Regression classifier. The model was selected because it is:

* Simple
* Efficient
* Suitable for text classification
* Easy to interpret and reproduce



📈 Model Evaluation

The dataset was divided into:

80% training data — 3,200 samples

20% testing data — 800 samples



The test set contained 200 samples from each language.



Results

The model achieved:

100% accuracy on the held-out synthetic test set.



Classification results:			

|Language|Precision|Recall|F1-Score|Support|
|-|-|-|-|-|
|English|1.00|1.00|1.00|200|
|Hausa|1.00|1.00|1.00|200|
|Igbo|1.00|1.00|1.00|200|
|Yoruba|1.00|1.00|1.00|200|



Overall:

Accuracy: 100%

Macro F1-score: 1.00

Weighted F1-score: 1.00



The confusion matrix showed no misclassification among the four language classes in the held-out synthetic test set.



🧪 Manual Testing

Additional phrases outside the formal test set were used to test the application.



Examples:

Input	Prediction	Result

Bawo ni o se wa loni?	Yoruba	✅

Ina kwana? Ya ya gida?	Hausa	✅

Kedu ka ị mere taa?	Igbo	✅

How are you doing today?	English	✅



A short-phrase stress test was also performed.



Results:

|Phrase|Prediction|Result|
|-|-|-|
|Mo wa|Yoruba|✅|
|Ina kwana|Hausa|✅|
|Ndewo|English|❌|
|Good morning|English|✅|
|Mo fẹ́ jẹun|Yoruba|✅|
|Ina son ruwa|Hausa|✅|
|Achọrọ m nri|Igbo|✅|
|Thank you very much|English|✅|



The model correctly classified 7 out of 8 short manually supplied phrases. The incorrect prediction of Ndewo demonstrates that performance can decrease when dealing with very short or unseen expressions.



🖥️ Interactive Application



The project includes a Gradio interface that allows users to enter a phrase and receive:



Predicted language

Model confidence

Probability estimates for all four languages



Example:

Input: Bawo ni o se wa loni?

Prediction: Yoruba



🛠️ Technologies Used

Python

Pandas

Scikit-learn

Joblib

Gradio

Matplotlib

Google Colab



📁 Project Structure

nigerian-language-identifier/

│

├── README.md

├── app.py

├── requirements.txt

│

├── data/

│   └── nigerian\_language\_dataset\_final.csv

│

├── models/

│   ├── nigerian\_language\_model.pkl

│   └── tfidf\_vectorizer.pkl

│

└── notebook/

&#x20;   └── Nigerian\_Language\_Identifier.ipynb



💾 Saved Model

The trained components are saved using Joblib:

* models/nigerian\_language\_model.pkl
* models/tfidf\_vectorizer.pkl



Saving these components allows the application to make predictions without retraining the model every time it is launched.



⚠️ Limitations

Synthetic Dataset - The current dataset is synthetically generated. Therefore, the 100% held-out test accuracy does not necessarily represent real-world language identification performance. A larger dataset containing naturally occurring Nigerian-language text would provide a stronger evaluation.



Short Text - Very short phrases can be difficult to classify because they contain fewer linguistic patterns. For example: Ndewo was incorrectly classified as English during manual testing.



Language Coverage - The current version supports only four languages:

* English
* Hausa
* Igbo
* Yoruba



Nigeria has many additional languages that could be supported in future versions.



🔮 Future Improvements - Potential improvements include:

* Collecting larger real-world Nigerian-language datasets
* Adding more Nigerian languages
* Comparing additional machine learning algorithms
* Improving classification of very short phrases
* Adding speech/audio language identification
* Deploying the model as an API
* Building a mobile application
* Integrating language detection into conversational AI systems
* Exploring transformer-based NLP models



🎓 Project Context - This project was developed as a capstone project for the 3MTT / NextGen AI \& Machine Learning program.

The project demonstrates the application of:

* Natural Language Processing
* Supervised Machine Learning
* Text Classification
* Model Evaluation
* Interactive AI Application Development



👤 Author - Damilola Amusan (AI / Machine Learning \& Automation Enthusiast)



📜 License - This project is intended for educational and demonstration purposes.

