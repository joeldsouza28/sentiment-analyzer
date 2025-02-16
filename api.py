from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import os
app = FastAPI()


model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment"

templates = Jinja2Templates(directory="html")
save_directory = "./saved_model"

if os.path.isdir(save_directory):
    model = AutoModelForSequenceClassification.from_pretrained(save_directory)
    tokenizer = AutoTokenizer.from_pretrained(save_directory)
else:
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model.save_pretrained(save_directory)
    tokenizer.save_pretrained(save_directory)

sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("input.html", {"request": request, "message": "Hello, FastAPI!"})


@app.get("/getResult")
async def get_resul(req: Request):
    text = req.query_params.get("text")
    result = sentiment_pipeline(text)

    return {
        "result": result[0]["label"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)