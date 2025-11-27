import json
from sentence_transformers import SentenceTransformer, util
def get_response(message):
    # Your logic here
    return "This is a response"

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load data
with open('faq_data.json') as f:
    faq_data = json.load(f)

# Pre-compute embeddings
questions = [item['question'] for item in faq_data]
answers = [item['answer'] for item in faq_data]
question_embeddings = model.encode(questions)

def get_response(user_input):
    user_embedding = model.encode(user_input)
    similarity_scores = util.cos_sim(user_embedding, question_embeddings)[0]
    best_match_idx = similarity_scores.argmax()
    return answers[best_match_idx]

def get_response(message):
    return f"You said: {message}"