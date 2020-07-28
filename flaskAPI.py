from flask import Flask, url_for
import pandas as pd
import spacy
from spacy import displacy
import en_core_web_sm

nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<rawtext>')
def getNER(rawtext):
    choice = "geopolitical"
    results = "boh"
    doc = nlp(rawtext)
    d = []
    for ent in doc.ents:
        d.append((ent.label_, ent.text))
        df = pd.DataFrame(d, columns=('named entity', 'output'))
        ORG_named_entity = df.loc[df['named entity'] == 'ORG']['output']
        PERSON_named_entity = df.loc[df['named entity'] == 'PERSON']['output']
        GPE_named_entity = df.loc[df['named entity'] == 'GPE']['output']
        MONEY_named_entity = df.loc[df['named entity'] == 'MONEY']['output']

    return GPE_named_entity.to_json(orient='split')
    #return rawtext

if __name__ == '__main__':
    app.run(debug=True)
