# AI Personalized Learning Pathway Generator

## Overview

This project is a hybrid Artificial Intelligence system that combines Machine Learning and Large Language Models (LLMs) to generate personalized learning pathways for students. The system analyzes student behavioral and academic data, identifies learner personas using K-Means Clustering, and generates personalized recommendations, strengths, weaknesses, resources and learning pathways using the Llama 3.3 70B Versatile Large Language Model.

## Features

* Student behavior analysis
* Learner persona identification using K-Means Clustering
* Data preprocessing and feature scaling
* Persona-based student segmentation
* AI-generated profile summaries
* Personalized learning recommendations
* Strength and weakness analysis
* Learning pathway generation
* Data visualization and analytics

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Groq API
* Llama 3.3 70B Versatile LLM

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
│   └── Training.ipynb
│
├── services/
│   ├── persona_predictor.py
│   └── pathway_generator.py
│
├── utils/
│   └── persona_mapping.py
│
└── app.py
```

## Workflow

Student Dataset
→ Data Preprocessing
→ Feature Selection & Scaling
→ K-Means Clustering
→ Learner Persona Generation
→ Llama 3.3 LLM
→ Personalized Learning Pathway

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

The project successfully identified five learner personas:

* Self Learner
* Social Learner
* Silent Learner
* Balanced Learner
* Elite Learner

The generated learner personas were further utilized by the LLM to produce personalized learning recommendations and pathways tailored to individual student needs.

## Future Improvements

* Web-based user interface
* Real-time student progress tracking
* Retrieval-Augmented Generation (RAG)
* Integration with Learning Management Systems (LMS)
* Additional clustering and classification models
* Larger real-world educational datasets


Krishna Institute of Engineering and Technology (KIET)
