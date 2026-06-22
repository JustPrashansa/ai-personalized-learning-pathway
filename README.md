# AI Personalized Learning Pathway Generator

## Overview

This project is a hybrid Artificial Intelligence system that combines Machine Learning and Large Language Models (LLMs) to generate personalized learning pathways for students. The system analyzes student behavioral and academic data, identifies learner personas using K-Means Clustering, and generates personalized recommendations, strengths, weaknesses, resources, and learning pathways using the Llama 3.3 70B Versatile Large Language Model via the Groq API.

Built as part of my exploration into combining traditional Machine Learning with Generative AI to solve real personalization problems in education.

## Features

* Student behavior and academic data analysis
* Learner persona identification using K-Means Clustering
* Data preprocessing, cleaning, and feature scaling (StandardScaler)
* Cluster validation using Silhouette Score
* Persona-based student segmentation across 5 distinct learner types
* AI-generated profile summaries via LLM
* Personalized learning recommendations
* Strength and weakness analysis per student
* Short-term, mid-term, and long-term learning pathway generation
* Data visualization and analytics (cluster distribution, exam score by persona, stress level by persona, feature correlation heatmap)

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-Learn (K-Means Clustering, StandardScaler, Silhouette Score)
* Matplotlib, Seaborn
* Groq API
* Llama 3.3 70B Versatile LLM
* python-dotenv (for secure API key management)

## Project Structure

```text
AI-Personalized-Learning-Pathway/
│
├── data/
│   └── student_performance.csv
│
├── models/
│   ├── kmeans_model.pkl
│   └── scaler.pkl
│
├── notebook/
│   └── training.ipynb
│
├── services/
│   ├── persona_predictor.py
│   └── pathway_generator.py
│
├── utils/
│   └── persona_mapping.py
│
├── .env (not tracked — holds API key)
├── .gitignore
└── app.py
```

## Workflow

```text
Student Dataset
  → Data Preprocessing & Cleaning
  → Feature Selection & Scaling
  → K-Means Clustering (validated via Silhouette Score)
  → Learner Persona Generation (5 personas)
  → Llama 3.3 70B LLM (via Groq API)
  → Personalized Learning Pathway Output
```

## Dataset Features

The dataset contains behavioral and academic attributes including:

* Study Hours
* Attendance
* Resources
* Extracurricular Activities
* Motivation
* Learning Style
* Online Courses
* Discussions
* Assignment Completion
* EduTech Usage
* Stress Level
* Exam Score

## Results

The K-Means model successfully identified five distinct learner personas:

| Persona          | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| Self Learner     | Independent and self-motivated, mostly studies individually |
| Social Learner   | Learns best through collaboration and discussion            |
| Silent Learner   | Learns mostly by observing, limited collaboration           |
| Balanced Learner | Balances self-study and collaboration effectively           |
| Elite Learner    | Highly focused, strong performance and discipline           |

Each identified persona is passed to the LLM along with the student's individual data (study hours, attendance, motivation, stress level, etc.) to generate a fully personalized output — including a profile summary, strengths, weaknesses, recommended resources, and a structured learning pathway with short-term (6 weeks), mid-term (12 weeks), and long-term (6 months) goals.

## Security Note

API keys are managed through environment variables using `python-dotenv` and excluded from version control via `.gitignore`, following standard security practices for credential management.

## Future Improvements

* Web-based user interface (Streamlit/Flask)
* Real-time student progress tracking
* Retrieval-Augmented Generation (RAG) for resource recommendations
* Integration with Learning Management Systems (LMS)
* Additional clustering and classification model comparisons
* Larger, more diverse real-world educational datasets
