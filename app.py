from flask import Flask, render_template, request, redirect

app = Flask(__name__) 

@app.route("/") # / ← 슬래시는 메인페이지 
def main():     
    return render_template('메인페이지.html') 

@app.route("/", methods=["POST"])
def predict_img():

    # 파이썬 코드 작성 가능!

    return "작업을 모두 수행했습니다!"

@app.route("/naver") # localhost:5002/naver
def redirect_ex(): 
    return redirect("https://www.naver.com")

app.run(host="0.0.0.0", port=5002) # localhost:5002 로 접속 가능