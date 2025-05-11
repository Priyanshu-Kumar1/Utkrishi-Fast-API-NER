from typing import Union
#get modules for spaCy NER transformer model in output_transformer_128
import spacy

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def read_item(text: str):
    return {"text": text}


#use the spaCy NER transformer model in output_transformer_128 on the input text from the url 
@app.get("/ner")
def read_item(text: str):
    nlp = spacy.load("output_transformer_128/model-best")
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append({"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_})
    return {"entities": entities}

#test url:- /ner?text=Your text here
