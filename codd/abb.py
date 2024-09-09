def evaluate_quiz(q1, q2, q3, q4, q5, q6, q7, q8, answers):
    score = 0
    correct_answers = []
    
    if q1 == answers['q1']:
        score += 1
    else:
        correct_answers.append('q1')
    
    if q2 == answers['q2']:
        score += 1
    else:
        correct_answers.append('q2')
    
    if q3 == answers['q3']:
        score += 1
    else:
        correct_answers.append('q3')
    
    if q4 == answers['q4']:
        score += 1
    else:
        correct_answers.append('q4')
    
    if q5 == answers['q5']:
        score += 1
    else:
        correct_answers.append('q5')
    
    if q6 == answers['q6']:
        score += 1
    else:
        correct_answers.append('q6')
    
    if q7 == answers['q7']:
        score += 1
    else:
        correct_answers.append('q7')
    
    if q8 == answers['q8']:
        score += 1
    else:
        correct_answers.append('q8')
    
    return score, correct_answers
