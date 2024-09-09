import os
import docx2txt

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

keywords = ['python', 'java', 'machine learning', 'data science']

def match_keywords(text, keywords):
    matches = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            matches.append(keyword)
    return matches

def process_resume(file_path):
    if os.path.exists(file_path):
        text = extract_text_from_docx(file_path)
        matched_keywords = match_keywords(text, keywords)
        return matched_keywords
    else:
        print(f'Error: File {file_path} not found.')
        return []

resumes = [
    r"C:\Users\darsh\Downloads\samresumes\resume2.docx",
    r"C:\Users\darsh\Downloads\samresumes\resume3.docx"ṇ,
    r"C:\Users\darsh\Downloads\samresumes\resume4.docx",
    r"C:\Users\darsh\Downloads\samresumes\resume5.docx",
]

selected_resumes = [
    r"C:\Users\darsh\Downloads\samresumes\resume5.docx"
]

for resume in resumes:
    matched_keywords = process_resume(resume)
    if all(keyword in matched_keywords for keyword in ['python', 'java', 'machine learning']):
        selected_resumes.append(resume)
        print(f'Resume {resume} matches keywords: {matched_keywords}')
    else:
        print(f'Resume {resume} didn\'t match the requirements.')

print("\nSelected Resumes:")
for selected_resume in selected_resumes:
    print(selected_resume)