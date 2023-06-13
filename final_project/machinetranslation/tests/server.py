import machinetranslation
import flask

@app.route('/')
@app.route('/index.html')
@app.route('/englishtofrench')
def entofr(en_text)
fr_text = machinetranslation.translator.englishtofrench(en_text)
return fr_text 

@app.route('/frenchtoenglish')
def frtoen(fr_text)
en_text = machinetranslation.translator.frenchtoenglish(fr_text)
return en_text