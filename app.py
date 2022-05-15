from fastapi import FastAPI
import uvicorn
import pickle
from models import Semantics
from sklearn.metrics.pairwise import cosine_similarity

app=FastAPI()
model = pickle.load(open("pickle_model.pickle","rb"))

@app.get("/{name}")
def hello(name):
    return {"Hello {} and welcome to this API".format(name)}


@app.get("/")
def greet():
    return {"hello world"}

@app.post("/predict")
def predict(req:Semantics):
    sen1=req.sce1
    sen2=req.sce2
    sentence=[]
    sentence.append(sen1)
    sentence.append(sen2)

    sentence_vecs=model.encode(sentence)
    a=cosine_similarity(
        [sentence_vecs[0]],
        [sentence_vecs[1]]
    )

    return{"similarity":"{}".format(int(0.5+a[0][0]))}

if __name__ == "__main__":
    uvicorn.run(app)