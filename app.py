from flask import Flask,request,render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello,World!'
@app.route('/hello') 
def hellohtml(): 
    return render_template("hello.html") 
@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET': 
        # args_dict = request.args.to_dict() 
        # # print(args_dict) 
        num = request.args["num"] 
        name = request.args.get("name") 
        return "GET으로 전달된 데이터({}, {})".format(num, name) 
    else: 
        num = request.form["num"] 
        name = request.form["name"] 
        return "POST로 전달된 데이터({}, {})".format(num, name) 
@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/result',methods=['POST'])
def result():
    id = 'abc'
    pw = '1234'
    formid =request.form["fid"]
    formpw = request.form["fpw"] 

    if(id == formid):
        if(pw == formpw):
            return "아이디와 비번이 맞습니다."
    return "아이디와 비번이 맞지 않습니다."

@app.route('/daum')
def daum():
    return redirect("https://www.daum.net/")
@app.route('/naver')
def naver():
    return redirect("https://www.naver.com/")
@app.route('/move/naver')
def moveNaver():
    return redirect(url_for('naver'))
@app.route('/move/daum')
def moveDaum():
    return redirect(url_for('daum'))
if __name__ == '__main__': 
    app.run(debug=True)