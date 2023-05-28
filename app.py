from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.lngkyzb.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name': name_receive,
           'comment': comment_receive }
    db.fan.insert_one(doc)
   
    return jsonify({'msg': '저장 완료!'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comments = list(db.fan.find({},{'_id':False}))
    return jsonify({'result': all_comments})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
