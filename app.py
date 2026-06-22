import pandas as pd
from services.persona_predictor import predict_persona
from services.pathway_generator import pathway_gen
from utils.persona_mapping import persona_types

df = pd.read_csv("data/student_performance.csv")
print("AI Personalized Learning Pathway Generator")
student = df.iloc[0]
student_features = [student['StudyHours'], student['Attendance'], student['Resources'], student['Extracurricular'], student['Motivation'], student['LearningStyle'], student['OnlineCourses'], student['Discussions'], student['AssignmentCompletion'], student['EduTech'], student['StressLevel']]
persona = predict_persona(student_features)
print(f"\nPredicted Persona: {persona}")
student_dict = student.to_dict()
student_dict["Persona"] = persona
print("Generating personalized learning pathway...")
pathway = pathway_gen(student_dict)
print(pathway)