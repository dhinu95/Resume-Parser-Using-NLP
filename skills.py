import pandas as pd
import spacy
nlp = spacy.load('en_core_web_sm')
noun_chunks = nlp.noun_chunks

def extract_skills(resume_text):
    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    colnames = ['skill']
    # reading the csv file
    data = pd.read_csv('skill.csv', names=colnames) 
    
    # extract values
    skills = data.skill.tolist()
    print(skills)
    skillset = []
    
    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
   
    for token in noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)
    return [i.capitalize() for i in set([i.lower() for i in skillset])]
  
print ('Skills',extract_skills(textinput))
