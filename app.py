from flask import Flask,request,render_template, redirect, url_for
import game,json,dbdb

app = Flask(__name__)

@app.route('/')
def index():
    return '메인페이지'

@app.route('/hello/')
def hello():
    return 'Hello,World!'

@app.route('/form') 
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
        with open("static/save.txt","w", encoding='utf-8') as f: 
            f.write("%s,%s" % (num, name))
        return "POST로 전달된 데이터({}, {})".format(num, name) 

@app.route('/getinfo') 
def getinfo(): # 파일 입력 
    with open("static/save.txt", "r", encoding='utf-8') as file: 
        student = file.read().split(',')  # 쉽표로 잘라서 student 에 배열로 저장 
    return '번호 : {}, 이름 : {}'.format(student[0], student[1])

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

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_charact(name)
    return render_template('gamestart.html', data=character)

@app.route('/input/<int:num>')
def input_num(num):
    if num ==1:
        with open("static/save.txt", "r", encoding='utf-8') as f: 
            data = f.read() 
            character = json.loads(data) 
            print(character['items'])
        return "{}이 {} 아이템을 사용해서 이겼다.".format(character["name"],character["items"][0])
    elif num ==2:
        return "도망가다!"
    elif num ==3:
        return "3번친구"
    else :
        return "아앗, 없어요"

@app.route('/gamestart')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f: 
        data = f.read() 
        character = json.loads(data) 
        print(character['items'])
    return "{}이 {} 아이템을 사용해서 이겼다.".format(character["name"],character["items"][0])

@app.route('/stage2')
def stage2():
    with open("static/save.txt", "r", encoding='utf-8') as f: 
        data = f.read() 
        character = json.loads(data) 
    return render_template('view.html', items=character['items'])
    
@app.route('/senddata') 
def senddata(): 
    name = 'world' 
    return render_template('senddata.html', data=name)

@app.route('/goout') 
def myimage(): 
    return render_template("myimage.html")

@app.errorhandler(404) 
def page_not_found(error): 
    return "페이지가 없습니다. URL를 확인 하세요", 404

if __name__ == '__main__': 
    app.run(debug=True)