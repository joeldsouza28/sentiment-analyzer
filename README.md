# SENTIMENT ANALYSIS

## summary
This project is a simple multilingual sentiment analysis project that predicts the sentiment of a given sentence. It provides three outcomes depending on the sentence i.e. positive, negative and neutral. In order to perform sentiment analysis the model that is used is [cardiffnlp/twitter-xlm-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment). The project is built using fastapi for serving responses, transformers for loading the model, and basic html and css for input and fetching results. The project has been dockerized and can be run on any platform

## tech :hammer_and_pick:
```
fastapi==0.115.8
transformers==4.48.3
```

## how to run
```
python3 -m pip install -r requirements.txt
python3 api.py
```

## how to run dockerized app
```
docker build -t sentiment-analyzer .
docker run -p 8000:8000 sentiment-analyzer
```