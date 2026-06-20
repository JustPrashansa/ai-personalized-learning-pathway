from openai import OpenAI
from utils.persona_mapping import persona_text
client=OpenAI(api_key='YOUR_GROQ_API_KEY',base_url="https://api.groq.com/openai/v1")
def pathway_gen(student):
    persona=student["Persona"]
    prompt=f"""
    You are an AI educational mentor and these are the details of a student :-
    Persona = {persona}
    Persona Text = {persona_text[persona]}
    Student's details :- 
    	StudyHours={student['StudyHours']},
        Attendance={student['Attendance']},
        Motivation={student['Motivation']},
        LearningStyle={student['LearningStyle']},
        OnlineCourses={student['OnlineCourses']},
        AssignmentCompletion={student['AssignmentCompletion']}
        StressLevel={student['StressLevel']}
        Motivation Levels:
        0 = Low
        1 = Medium
        2 = High
        Motivation Levels:
        0 = Low
        1 = Medium
        2 = High
    Generate Profile summary, Weaknesses, Strengths, Areas to work on, Resources, a personalized learning pathway
    And generate all this information in a structured way.
    """

    response=client.chat.completions.create(model="llama-3.3-70b-versatile",messages=[{"role":"user","content":prompt}])
    return response.choices[0].message.content