import pathlib
import pandas as pd
import re
import numpy as np
import spacy
nlp = spacy.load("en_core_web_sm")
root = pathlib.Path(__file__).parent
pd.set_option("display.max_columns",None)
df = pd.read_csv(str(root).replace("\\","/")+"/dataset.csv")
df.drop(columns=["vote_average","vote_count","status","revenue","runtime","adult","original_language","budget","homepage","original_title","tagline","production_countries"],inplace=True)
df.dropna(inplace=True)
df["overview"] = df["overview"].apply(lambda x : str(x).split())
df["genres"] = df["genres"].apply(lambda x : str(x).split(", ")).apply(lambda x: [i.replace(" ","") for i in x])
df["production_companies"] = df["production_companies"].apply(lambda x : str(x).split(", ")).apply(lambda x: [i.replace(" ","") for i in x])
df["spoken_languages"] = df["spoken_languages"].apply(lambda x : str(x).split(", ")).apply(lambda x: [i.replace(" ","") for i in x])
df["keywords"] = df["keywords"].apply(lambda x : str(x).split(", "))
df["tags"] = df["overview"]+df["genres"]+df["keywords"]+df["production_companies"]+df["spoken_languages"]
df["tags"] = df["tags"].apply(lambda x: " ".join(x))
data = df.loc[:,["title","release_date","tags","imdb_id","poster_path"]]
data["tags"] = data["tags"].apply(lambda x: " ".join([token.lemma_ for token in nlp(x)]))
data.to_csv(str(root).replace("\\","/")+"/dataset2.csv")
print(data["tags"])
