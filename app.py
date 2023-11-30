from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample user data (for educational purposes only, not for production)
user_data = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3',
}

# Sample syllabus for Artificial Intelligence
ai_syllabus = [
    {
        'topic': 'Week 1-2: Introduction to Artificial Intelligence',
        'content': [
            '- Definition and History of AI',
            '- AI Applications and Impact on Society',
            '- Types of AI: Narrow AI vs. General AI',
            '- AI in Everyday Life',
        ],
        'references': [
            'IBM AI - An overview: https://www.ibm.com/cloud/learn/ai-an-overview',
            'History of AI: https://www.ibm.com/cloud/learn/history-of-ai',
            # Add more IBM references as needed
        ],
    },
    {
        'topic': 'Week 3-4: Problem Solving and Search Algorithms',
        'content': [
            '- Problem-solving approaches',
            '- Search algorithms: Uninformed and Informed search',
            '- Heuristics and Optimization',
        ],
        'references': [
            'IBM Watson - Solving problems with AI: https://www.ibm.com/cloud/learn/problem-solving-with-ai',
            'AI search algorithms: https://www.ibm.com/cloud/learn/ai-search-algorithms',
            # Add more IBM references as needed
        ],
    },
    # ... (continue with the rest of the AI syllabus)
]

# Sample syllabus for Machine Learning
ml_syllabus = [
    {
        'topic': 'Week 1-2: Introduction to Machine Learning',
        'content': [
            '- Definition and Types of Machine Learning',
            '- Machine Learning Workflow',
            '- Types of Data and Features',
        ],
        'references': [
            'IBM Machine Learning - An introduction: https://www.ibm.com/cloud/learn/machine-learning-an-introduction',
            'Types of Machine Learning: https://www.ibm.com/cloud/learn/types-of-machine-learning',
            # Add more IBM references as needed
        ],
    },
    {
        'topic': 'Week 3-4: Supervised Learning',
        'content': [
            '- Linear Regression',
            '- Logistic Regression',
            '- Decision Trees and Random Forests',
        ],
        'references': [
            'IBM Watson Studio - Introduction to supervised learning: https://www.ibm.com/cloud/learn/intro-to-supervised-learning',
            'Decision Trees with IBM Watson: https://www.ibm.com/cloud/learn/decision-trees-watson',
            # Add more IBM references as needed
        ],
    },
    # ... (continue with the rest of the Machine Learning syllabus)
]

# Sample syllabus for Natural Language Processing
nlp_syllabus = [
    {
        'topic': 'Week 1-2: Introduction to Natural Language Processing',
        'content': [
            '- Definition and Applications of NLP',
            '- Challenges in NLP',
            '- Text Preprocessing',
        ],
        'references': [
            'IBM Natural Language Processing: https://www.ibm.com/cloud/learn/natural-language-processing',
            'Challenges in NLP: https://www.ibm.com/cloud/learn/challenges-in-nlp',
            # Add more IBM references as needed
        ],
    },
    {
        'topic': 'Week 3-4: Text Representation and Classification',
        'content': [
            '- Bag-of-Words',
            '- TF-IDF',
            '- Word Embeddings (Word2Vec, GloVe)',
            '- Text Classification',
        ],
        'references': [
            'IBM Cloud Pak for Data - Text classification: https://www.ibm.com/cloud/learn/text-classification',
            'Word Embeddings with IBM Watson: https://www.ibm.com/cloud/learn/word-embeddings-watson',
            # Add more IBM references as needed
        ],
    },
    # ... (continue with the rest of the NLP syllabus)
]
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if username and password match
        if username in user_data and user_data[username] == password:
            # Redirect to the syllabus page for AI (you can change this based on your logic)
            return redirect(url_for('generate_syllabus', subject='ai'))
        else:
            error = 'Invalid username or password. Please try again.'

    return render_template('login.html', error=error if 'error' in locals() else None)

# Sample route for syllabus
@app.route('/generate_syllabus/<subject>')
def generate_syllabus(subject):
    syllabus_data = {
        'ai': {'subject': 'Artificial Intelligence', 'syllabus': ai_syllabus},
        'ml': {'subject': 'Machine Learning', 'syllabus': ml_syllabus},
        'nlp': {'subject': 'Natural Language Processing', 'syllabus': nlp_syllabus},
    }

    if subject in syllabus_data:
        return render_template('syllabus.html', **syllabus_data[subject])

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
