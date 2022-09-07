from flask import Flask, render_template, request, redirect
import pandas as pd


# flask라는 Class에서 __init__ 함수에 self를 제외한 매개변수 1개
# __name__ : 자기 자신의 파일 이름
app = Flask(__name__)

#api생성하기

#127.0.0.1:5000 : 본인 컴퓨터 주소를 말함
#5000이라는 숫자는 port 번호
#port: 
# 127.0.0.1 = localhost

## localhost : 5000/
@app.route("/")   #@app.route() -> localhost:5000/ 요청이 있는 경우에 바로 아래 있는 함수를 실행
#함수 실행
def index():
    return render_template("index.html")

#get 형식에서 데이터는 url에 실어서 보낸다
#request -> 유저가 서버에게 보내는 데이터를 dict 형태로 출력
#유저가 보낸 데이터 중에 url에 있는 데이터는 : request.args : dict형태

@app.route("/second")
def second():
    _id = request.args.get("ID")
    _pass = request.args.get("password")
    # id 값과 password 값
    # id는 test password는 1234
    # 위 조건이 만족해야만 second.html 리턴
    # 위 조건이 거짓이면 "로그인 실패" 리턴
    #print(request)77

    # if _id == "test" and _pass == "1234" :
        
    #     return render_template("second.html")
    # else:
    #     #return("로그인 실패")
    #     return redirect("/") #안에는 주소를 적는 형태
    return render_template("second.html")

#localhost:5000/third post 형식으로 요청 시
#post 
@app.route("/third/", methods=["post"])
def third():
    _title = request.form["title"]   #id 값이 title로 넘어가고
    _content = request.form["content"]  #pw 값이 content로 받아서 쓴 것 --> second page에서 이걸로 받음
    print(_title, _content)
    return render_template("third.html", content=_content, title=_title)

@app.route("/dashboard")
def dashboard():
    print("dashboard")
    df = pd.read_csv("../data/corona.csv")
    #칼럼 이름 변경
    df.columns = ["인덱스", "등록일시", "사망자", "확진자", "게시글번호", "기준일", "기준시간", "수정일시", "누적의심자", "누적확진률"]
    #등록일시 기준으로 오름차순 정렬
    df.sort_values("등록일시", inplace = True)
    #일일 확진자, 일일 사망자 라는 파생변수 생성
    df["일일확진자"] = df["확진자"] - df["확진자"].shift()
    df["일일사망자"] = df["사망자"].diff()
    data = df.head(30)
    cnt = len(data)
    _decide_data = data["일일확진자"].tolist()
    _date_list = data["등록일시"].tolist()
    _death_data = data["일일사망자"].tolist()

    return render_template("dashboard.html", cnt = cnt, date_list = _date_list, decide_data = _decide_data, death_data= _death_data)

    #flask라는 Class 안에 있는 run()이라는 함수 호출
app.run()