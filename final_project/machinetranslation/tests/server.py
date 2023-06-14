from machinetranslation import translator 
from flask import Flask
app = Flask("MY Translation Website")
@app.route('/')
@app.route("index.html")
@app.route("/englishToFrench")
def entofr(en_text):
    fr_text = translator.englishtofrench(en_text)
    print(fr_text)
    return fr_text
@app.route("/frenchToEnglish")
def frtoen(fr_text):
    en_text = translator.englishtofrench(fr_text)
    print (en_text)
    return en_text    
if __name__ == "__main__" :
    app.run(debug=True)
