from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

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

def find_k_most_relevant(query_similarity_vector, pool, k):
    results = []
    for i in range(k):
        max_value = max(query_similarity_vector)
        max_index = query_similarity_vector.index(max_value)
        results.append(pool[max_index])
        query_similarity_vector[max_index] = -1
    return results

def embedding_generator(model, question, question_pool):
    question_embedding = model.encode(question)

    question_pool_embeddings = []
    for q in question_pool:
        question_pool_embeddings.append(model.encode(q))

    query_similarity_vector = cosine_similarity([question_embedding], question_pool_embeddings)
    query_similarity_vector = list(query_similarity_vector[0])
    print(max(query_similarity_vector))
    if max(query_similarity_vector) < 0.6:
        return "IDK"
    most_similar_question = find_k_most_relevant(query_similarity_vector, question_pool, 1)[0]
    return most_similar_question

bert_model = SentenceTransformer('HooshvareLab/bert-base-parsbert-uncased')

def answer_question(question):
  most_similar_question = embedding_generator(bert_model, question, question_pool)
  if most_similar_question == "IDK":
    return "این سوالت رو بلد نیستم."
  return answer_pool[most_similar_question]