from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import numpy as np

# question_pool = ["پوست از چی ساخته شده؟", "مو از چی ساخته شده؟", "استخوان از چی ساخته شده؟"]

# answer_pool = {
#     "پوست از چی ساخته شده؟": "پوست از بافت اسفنجی ساخته شده",
#     "مو از چی ساخته شده؟": "مو از سلول‌های مرده‌ی بدن تشکیل شده",
#     "استخوان از چی ساخته شده؟": "استخوان از فلان چیز ساخته شده"
#     }

import pandas as pd
data = pd.read_csv("core/qanda.csv")
answer_pool = dict(zip(data.question, data.answer))
question_pool = list(answer_pool.keys())

def find_k_least_relevant(query_similarity_vector, pool, k):
    results = []
    for i in range(k):
        min_value = min(query_similarity_vector)
        min_index = query_similarity_vector.index(min_value)
        results.append(pool[min_index])
        query_similarity_vector[min_index] = -1
    return results


def random_generator(model, previous_questions_embeddings, current_questions):
    future_question = random.choice(current_questions)
    previous_questions_embeddings.append(model.encode(future_question))
    return previous_questions_embeddings, future_question

RANDOMNESS_PARAM = 0
def embedding_generator(model, previous_questions_embeddings, current_questions):
    i = 1
    s = 0
    average_embedding = np.zeros(768, dtype='float32')
    print(len(previous_questions_embeddings))
    for q in previous_questions_embeddings:
        average_embedding += (previous_questions_embeddings[0] * i)
        s += i
        i += 1
    average_embedding /= s

    current_questions_embeddings = []
    for q in current_questions:
        current_questions_embeddings.append(model.encode(q))

    if random.uniform(0, 1) <= RANDOMNESS_PARAM:
        print("rand")
        future_question = random.choice(current_questions)
        previous_questions_embeddings.append(model.encode(future_question))
        return previous_questions_embeddings, future_question
    else:
        print()
        query_similarity_vector = cosine_similarity(
        [average_embedding],
        current_questions_embeddings
        )
        query_similarity_vector = list(query_similarity_vector[0])
        future_question = find_k_most_relevant(query_similarity_vector, current_questions, 1)[0]
        previous_questions_embeddings.append(model.encode(future_question))
        return previous_questions_embeddings, future_question


bert_model = SentenceTransformer('HooshvareLab/bert-base-parsbert-uncased')
def ask_question(number_of_questions):
  previous_questions_embeddings = []
  current_questions = question_pool.copy()
  tobe_asked_questions = []
  previous_questions_embeddings, future_question = random_generator(bert_model, previous_questions_embeddings, current_questions)
  current_questions.remove(future_question)
  tobe_asked_questions.append(future_question)
  for i in range(number_of_questions-1):
    previous_questions_embeddings, future_question = embedding_generator(bert_model, previous_questions_embeddings, current_questions)
    current_questions.remove(future_question)
    tobe_asked_questions.append(future_question)
  return tobe_asked_questions


def check_answer(question, user_answer):
    real_answer = answer_pool[question[0]]
    real_answer_embedding = bert_model.encode(real_answer)
    user_answer_embedding = bert_model.encode(user_answer)
    query_similarity_vector = cosine_similarity([real_answer_embedding], [user_answer_embedding])
    print(query_similarity_vector)
    if query_similarity_vector[0] > 0.65:
      return "آفرین! جوابت درسته.", real_answer
    return "فکر میکنم جوابت اشتباهه :(", real_answer