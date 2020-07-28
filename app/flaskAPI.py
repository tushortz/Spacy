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

@app.route('/ner')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/ner/<rawtext>')
def getNER(rawtext):
    doc = nlp(rawtext)
    d = []
    for ent in doc.ents:
        d.append((ent.label_, ent.text))
        df = pd.DataFrame(d, columns=('named entity', 'output'))
        GPE_named_entity = df.loc[df['named entity'] == 'GPE']['output']

    return GPE_named_entity.to_json(orient='split')

if __name__ == '__main__':
    app.run(debug=True)
