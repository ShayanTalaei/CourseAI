from transformers import pipeline
pipe = pipeline("text2text-generation", model="alireza7/PEGASUS-persian-base-PN-summary")

def summerize_text(text):
    return pipe(text)