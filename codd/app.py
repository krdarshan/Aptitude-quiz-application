from flask import Flask, render_template, request
import abb

app = Flask(__name__)

# A simple schedule dictionary. You can replace this with a more sophisticated system.
schedule = {
    '9:00 AM - 10:00 AM': None,
    '10:30 AM - 11:30 AM': None,
    # Add more time slots as needed
}

@app.route('/')
def index():
    return render_template('name.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    q5 = request.form['q5']
    q6 = request.form['q6']
    q7 = request.form['q7']
    q8 = request.form['q8']
    
    answers = {
        'q1': 'c',
        'q2': 'c',
        'q3': 'a',
        'q4': 'a',
        'q5': 'b',
        'q6': 'b',
        'q7': 'a',
        'q8': 'b'
    }
    
    score, correct_answers = abb.evaluate_quiz(q1, q2, q3, q4, q5, q6, q7, q8, answers)
    if len(correct_answers) == 0:
        for slot, status in schedule.items():
            if status is None:
                schedule[slot] = 'Booked'
                return render_template('schedule.html', slot=slot)
    
    return render_template('result.html', score=score, correct_answers=correct_answers)

if __name__ == '__main__':
    app.run(debug=True)
