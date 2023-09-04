import random
from datetime import datetime
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re
# from core import summ as SUM
# from core import q_ans as QAns
# from core import ask_q as AskQ

from .init_system import *
from model.student import * 

BOT_NAME = "Course AI"

## Models
model = SentenceTransformer('HooshvareLab/bert-base-parsbert-uncased')

## Globals
state = "CONVERSATION_GREETING"
asked_question = ''
previous_questions_embeddings = []
student = initialize_system()
in_action_exam = None

greeting = [
    "سلام! من اینجام تا توی درسات بهت کمک کنم.",
    "سلام دوست درسخون من! بیا شروع کنیم.",
    "درود! خوشحالم قراره با هم درس بخونیم.",
    "سلام و درود! میتونی توی درس خوندنت روی من حساب کنی.",
    "سلام دوست خوب من! برای درس خوندنت پیش خوب کسی اومدی",
]
    

course = [
   "دوست داری توی چه درسی بهت کمک کنم؟",
   "امروز میخوای چه درسی رو با هم کار کنیم؟",
   "تو فقط به من اسم درس بگو، بقیش با من!",
   "چه درسی رو میخوای با هم کار کنیم؟",
   "کدوم درس رو دوست داری با هم بخونیم؟",
   
]

grade = [
    "کدوم سال رو میخوای؟",
    "چه پایه‌ای؟",
    "چه مقطعی رو با هم کار کنیم؟",
    "کدوم مقطع رو میخوای با هم کار کنیم؟",
    "چه پایه‌ای رو دوست داری با هم کار کنیم؟",
   
]


feature = [
   "دوست داری کدوم یکی از کارای زیر رو برات بکنم؟",
   "خب چه کاری دوست داری بکنیم؟",
   "کدوم یکی از کارای زیر رو دوست داری انجام بدیم؟",
   "میخوای چه کاری برات انجام بدم؟",
   "چجوری میتونم کمکت کنم؟"
]

summerization = [
    "متنی که میخوای برات خلاصه کنم رو بنویس.",
    "متنت رو بفرست تا برات خلاصه‌اش کنم.",
    "چه متنی رو میخوای برات خلاصه‌ کنم؟",
    "متن بده، خلاصشه‌اش رو تحویل بگیر.",
    "متنی که میخوای برات خلاصه‌اش کنم رو بفرست."
]

asking_question = [
    "از چه بخشی از کتاب میخوای ازت سوال بپرسم؟",
    "کدوم فصل رو میخوای با هم کار کنیم؟",
    "چه فصلی رو؟",
    "از کدوم مبحث کتاب میخوای ازت سوال بپرسم؟",
    "تو فقط شماره فصل بگو!"
]

question_answering = [
    "سوالات رو بپرس.",
    "Ask your question :)",
    "جانم، سوالت رو بپرس.",
    "Try me, I won't disappoint you ;)",
    "سوالت رو برام بنویس."
]

finish_exam = [
    "خسته نباشی! دوست داری الان چیکار کنیم؟"
]

analysis_planning_offer = [
    "دیگه چیکار کنیم؟"
]

wait_for_studying = [
    "الان برو مطالعه کن. پایان زمان مطالعه دوباره میبینمت!"
]

goodbye = [
    "خداحافظ! امیدوارم تونسته باشم کمکت کنم.",
    "به امید دیدار، بعدا باز هم با درس میخونیم."
]

not_available_feature = [
    "هنوز این قابلیت رو نداریم. ببخشید :)",
    "شرمنده، هنوز نمیتونم این کار رو بکنم.",
    "هنوز نمیتونم کاری که میخوای رو انجام بدم، ولی به زودی یاد میگیرم.",
    "متاسفانه هنوز این قابلیت رو نداریم. شرمنده",
    "با عرض پوزش چنین قابلیتی رو نداریم فعلا. "
]

def shuffle_lst(lst):
    random.shuffle(lst)
    return 0


def find_k_most_relevant(query_similarity_vector, boostan_poems, k):
    results = []
    for i in range(k):
        max_value = max(query_similarity_vector)
        max_index = query_similarity_vector.index(max_value)
        results.append(boostan_poems[max_index])
        query_similarity_vector[max_index] = -1
    return results


def random_generator(current_questions, previous_questions_embeddings):
    future_question = random.choice(current_questions)
    previous_questions_embeddings.append(model.encode(future_question))
    return previous_questions_embeddings, future_question


RANDOMNESS_PARAM = 0.5
def embedding_generator(model, previous_questions_embeddings, current_questions):
    i = 1
    s = 0
    average_embedding = np.zeros(768, dtype='float32')
    print(len(previous_questions_embeddings))
    for q in previous_questions_embeddings: 
        # print(np.shape(previous_questions_embeddings[0]), np.shape(average_embedding))
        average_embedding += (previous_questions_embeddings[0] * i)
        s += i
        i += 1
    average_embedding /= s
    # print(average_embedding)
    current_questions_embeddings = []
    for q in current_questions:
        current_questions_embeddings.append(model.encode(q))
    
    if random.uniform(0, 1) <= RANDOMNESS_PARAM:
        future_question = random.choice(current_questions)
        previous_questions_embeddings.append(model.encode(future_question))
        return previous_questions_embeddings, future_question
    else:
        query_similarity_vector = cosine_similarity(
        [average_embedding],
        current_questions_embeddings
        )
        query_similarity_vector = list(query_similarity_vector[0])
        future_question = find_k_most_relevant(query_similarity_vector, current_questions, 1)[0]
        previous_questions_embeddings.append(model.encode(future_question))
        return previous_questions_embeddings, future_question


def feature_selection(feature):
    summerization = ["برام خلاصه کن"]
    question_answering = ["به سوالام جواب بده"]
    asking_question = ["ازم سوال بپرس"]
    taking_exam = ["میخوام آزمون بدم."]
    if feature in summerization:
        return "SUMMERIZATION"
    elif feature in asking_question:
        return "ASKING_QUESTION"
    elif feature in question_answering:
        return "QUESTION_ANSWERING"
    elif feature in taking_exam:
        return "EXAM"
    else:
        return "NOT_AVAILABLE"


def back_detection(message):
    back_pool = ["برگردیم عقب"]
    if message in back_pool:
        return "BACK"
    return "NO"

def get_next_page():
    global state
    # get page name from state, first word before _
    page = state.split("_")[0].lower()
    return page

def information_retrieval_module(message):
    global state, asked_question, previous_questions_embeddings

    if state.startswith("CONVERSATION"):
        res, buttons = handle_conversation_page(message)
    elif state.startswith("EXAM"):
        res, buttons = handle_exam_page(message)
    elif state.startswith("ANALYSIS"):
        res, buttons = handle_analysis_page(message)
    elif state.startswith("PLANNING"):
        res, buttons = handle_planning_page(message)
    elif state.startswith("REVIEW"):
        res, buttons = handle_review_page(message)
    page = get_next_page(state)
    return page, res, buttons
 
 
def handle_conversation_page(message):
    global state, previous_questions_embeddings, in_action_exam, student

    ## GREETING 
    if state == "CONVERSATION_GREETING": 
        previous_questions_embeddings, future_question = random_generator(greeting, previous_questions_embeddings)
        state = "CONVERSATION_COURSE"
        return future_question, ["سلام", "درود"]

    ## COURSE
    elif state == "CONVERSATION_COURSE": 
        previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, course)
        state = "CONVERSATION_GRADE"
        return future_question, ["ریاضی", "زیست شناسی"]
    
    ## GRADE
    elif state == "CONVERSATION_GRADE": 
        previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, grade)
        state = "CONVERSATION_FEATURE"
        return future_question, ["دهم", "یازدهم", "دوازدهم"]

    # FEATURE
    elif state == "CONVERSATION_FEATURE": 
        previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, feature)
        state = "CONVERSATION_FEATURE_SELECTION"
        return future_question, ["میخوام آزمون بدم."] #"به سوالام جواب بده", "برام خلاصه کن", "ازم سوال بپرس"

    ## FEATURE SELECTION
    elif state == "CONVERSATION_FEATURE_SELECTION": 
        f = feature_selection(message)

        if f == "EXAM":
            exam = generate_exam()
            in_action_exam = exam
            qo_list = exam.get_question_options_list()
            start_time = datetime.now()
            start_time = start_time.strftime("%B %d, %Y")
            exam_time_minute = 1*exam.question_count()
            response = {
                "title": "آزمون",
                "start_time": start_time,
                "duration": exam_time_minute,
                "qo_list": qo_list
            }

            state = "EXAM_TAKING_EXAM"
            return response, []

    elif state == "CONVERSATION_FINISH_EXAM" or state == "CONVERSATION_ANALYSIS_PLANNING_OFFER":
        if message == "آزمون رو تحلیل کنیم.":
            last_taken_exam = student.taken_exams[-1]
            overall_stats, sections, percentages, strong_sections, weak_sections = last_taken_exam.analize_exam()
            exam_sammary = "آزمون خوبی بود. نقاط قوت و ضعفت رو در ادامه بهت میگم."
            response = {overall_stats=overall_stats,
                        sections=sections,
                        percentages=percentages,
                        strong_sections=strong_sections,
                        weak_sections=weak_sections,
                        exam_sammary=exam_sammary}

            state = "ANALYSIS_CHARTS"
            return future_question, [] 
        elif message == "پاسخ‌برگ رو ببینیم.":
            last_taken_exam = student.taken_exams[-1]
            qo_list = last_taken_exam.get_question_options_list()
            response = {"qo_list": qo_list}

            state = "ANALYSIS_ANSWER_SHEET"
        elif message == "بهم مشاوره بده.":
            ## TODO
            response = {}

            state = "PLANNING_SHOW_PLAN"

    elif state == "CONVERSATION_WAIT_FOR_STUDYING":
        ## TODO
        response = {}

        state = "REVIEW_ANSWERING_QUESTIONS"
        

    # elif state == "CONVERSATION_FEATURE_SELECTION": 
    #     f = feature_selection(message)
    #     print("back back", f, message)
    #     if f == "SUMMERIZATION":
    #         previous_questions_embeddings, future_question = embedding_generato
    # r(model, previous_questions_embeddings, summerization)
    #         return future_question, "SUMMERIZATION", ["یه متن از کتاب", "برگردیم عقب"], previous_questions_embeddings
    #     elif f == "ASKING_QUESTION":
    #         previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, asking_question)
    #         return future_question, "ASKING_QUESTION", ["فصل اول", "برگردیم عقب"], previous_questions_embeddings
    #     elif f == "QUESTION_ANSWERING":
    #         previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, question_answering)
    #         return future_question, "QUESTION_ANSWERING", ["اطلاعات وراثتی کجا ذخیره میشه", "برگردیم عقب"], previous_questions_embeddings
    #     else:
    #         previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, feature)
    #         return future_question, "END", ["دوباره امتحان کنیم"], previous_questions_embeddings

    #  ## ASKING QUESTION
    # elif state == "ASKING_QUESTION": 
    #     if back_detection(message) == "BACK":
    #         previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, feature)
    #         return future_question, "FEATURE_SELECTION",  ["به سوالام جواب بده", "برام خلاصه کن", "ازم سوال بپرس"], previous_questions_embeddings
    #     print(asked_question)
    #     question = AskQ.ask_question(1)
    #     asked_question = question
    #     print(asked_question)
    #     return question, "ASKING_QUESTION_ANSWER", [], previous_questions_embeddings


    # ## SUMMERIZATION
    # elif state == "SUMMERIZATION": 
    #     if back_detection(message) == "BACK":
    #         previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, feature)
    #         return future_question, "FEATURE_SELECTION",  ["به سوالام جواب بده", "برام خلاصه کن", "ازم سوال بپرس"], previous_questions_embeddings
    #     text_summ = SUM.summerize_text(message)
    #     return text_summ[0]["generated_text"].replace("<n>", ""), "SUMMERIZATION", ["یه متن از کتاب", "برگردیم عقب"], previous_questions_embeddings

    # ## ASKING QUESTION
    # elif state == "ASKING_QUESTION_ANSWER": 
    #     res, real_answer = AskQ.check_answer(asked_question, message)
    #     return res + " به عبارتی " + real_answer, "ASKING_QUESTION", ["فصل اول", "برگردیم عقب"], previous_questions_embeddings

    
    # ## QUESTION ANSWERING
    # elif state == "QUESTION_ANSWERING": 
    #     if back_detection(message) == "BACK":
    #         print("back back")
    #         previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, feature)
    #         return future_question, "FEATURE_SELECTION",  ["به سوالام جواب بده", "برام خلاصه کن", "ازم سوال بپرس"], previous_questions_embeddings
    #     answer = QAns.answer_question(message)
    #     return answer, "QUESTION_ANSWERING", ["اطلاعات وراثتی کجا ذخیره میشه", "برگردیم عقب"], previous_questions_embeddings
        
    # # THANK USER
    # elif state == "END":
    #     return "امیدوارم تونسته باشم کمکت کنم.", "END2", ["خوب بود", "جالب نبود"], previous_questions_embeddings
    

def handle_exam_page(message):
    global state, student, in_action_exam

    if state == "EXAM_TAKING_EXAM": 
        previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, finish_exam)
        state = "CONVERSATION_FINISH_EXAM"
        
        taken_exam = TakenExam(student=student, exam=in_action_exam, 
                answers=[x["selectedAnswer"] for x in message], passed_time = None)
        student.taken_exams.append(take_exam)
        return future_question, ["آزمون رو تحلیل کنیم.","پاسخ‌برگ رو ببینیم.","برام برنامه‌ریزی کن."]

def handle_analysis_page(message):
    if state == "ANALYSIS_CHARTS" or state == "ANALYSIS_ANSWER_SHEET":
        previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, analysis_planning_offer)
        state = "CONVERSATION_ANALYSIS_PLANNING_OFFER"
            
        return future_question, ["آزمون رو تحلیل کنیم.","پاسخ‌برگ رو ببینیم.","برام برنامه‌ریزی کن."]


def handle_planning_page(message):
    if state == "PLANNING_SHOW_PLAN":
        previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, wait_for_studying)
        state = "CONVERSATION_WAIT_FOR_STUDYING"
            
        return future_question, ["من برگشتم، بریم سراغ مرور."]


def handle_review_page(message):
    if state == "REVIEW_ANSWERING_QUESTIONS":
        if message == "خروج":
            previous_questions_embeddings, future_question = embedding_generator(model, previous_questions_embeddings, wait_for_studying)
            state = "CONVERSATION_GOODBYE"
                
            return future_question, ["شروع دوباره!"]
        elif message == "":
            ## TODO
            pass
