from turtle import window_height
from flask import Flask,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy  # 追加
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sklearn import svm, metrics, preprocessing, model_selection
import pickle
from datawrite import filewrite_name,check_yesno,fileread
import socket


app = Flask(__name__)
"""回答保存用20221018"""
body_set=[]
name_set=[]
data_box=[]
analys_data=[]
question=fileread()
j=0
k=0


print("start network")
addr = ("192.168.3.15", 50007)  # 192.168.0.9

print("network setup started")
def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]
"""csvを読み取って次の行を決定する→トップページの「はい」でその行にIDを当てる、IDを渡し続けて配列に突っ込んだらはい押した端末と回答が紐づけられる？"""
def get_fortune(food_list,age):
    print("fortune_start")
    food_meet=0
    food_fish=0
    food_egg=0
    food_soy=0
    food_milk=0
    food_veg=0
    food_sea=0
    food_potato=0
    food_fruit=0
    food_oil=0
    for k in range(len(food_list)):
        if(int(food_list[k])==1):
            food_meet = 1
        if(int(food_list[k])==2):
            food_fish = 1
        if(int(food_list[k])==3):
            food_egg = 1
        if(int(food_list[k])==4):
            food_soy = 1
        if(int(food_list[k])==5):
            food_milk = 1
        if(int(food_list[k])==6):
            food_veg = 1
        if(int(food_list[k])==7):
            food_sea = 1
        if(int(food_list[k])==8):
            food_potato = 1
        if(int(food_list[k])==9):
            food_fruit = 1
        if(int(food_list[k])==10):
            food_oil = 1

    X_test=[[float(age),food_meet,food_fish,food_egg,food_soy,food_milk,food_veg,food_sea,food_potato,food_fruit,food_oil]]
    print(X_test)
    loaded_model = pickle.load(open("model_htn.sav", 'rb'))
    pre=loaded_model.predict(X_test)
    print(pre)
    return pre


"""回答保存"""
def getanswer_method(number):
    print(number)
    if request.method == "POST":
        answer= request.form['check']
        data_box.insert(number,answer)
        answer=check_yesno(answer) 
        print(answer)
        
        body_set.insert(number,str(answer))
        """テスト出力"""
        if(number==3):
            print(body_set)
        return data_box
def change_b(body_set):
     if(body_set=="はい"):
            body_set_int=1
     elif(body_set=="いいえ"):
            body_set_int=0
     print(body_set_int)
     return body_set_int
def change(body_set):
     if(body_set=="いいえ"):
            body_set_int=1
     elif(body_set=="はい"):
            body_set_int=0
     print(body_set_int)
     return body_set_int

def getname_method(name,sex,age,hight,weight):
    if request.method == "POST":     
        name_set=[str(name),str(sex),str(age),str(hight),str(weight)]
        motion_Frailty=0
        nutrition_Frailty=0
        oral_Frailty=0
        etc_Frailty=0
       
        etc_Frailty = etc_Frailty + change(body_set[0])        
        etc_Frailty = etc_Frailty + change(body_set[1])
        etc_Frailty = etc_Frailty + change(body_set[2])
        etc_Frailty = etc_Frailty +  change(body_set[3])
        etc_Frailty = etc_Frailty +  change(body_set[4])
        motion_Frailty = motion_Frailty + change(body_set[5])
        motion_Frailty = motion_Frailty +  change(body_set[6])
        motion_Frailty = motion_Frailty +  change(body_set[7])
        motion_Frailty = motion_Frailty +  change_b(body_set[8])
        motion_Frailty = motion_Frailty +  change_b(body_set[9])
        nutrition_Frailty=nutrition_Frailty+ change_b(body_set[10])
        oral_Frailty=oral_Frailty+change_b(body_set[11])
        oral_Frailty=oral_Frailty+change_b(body_set[12])
        oral_Frailty=oral_Frailty+change_b(body_set[13])
        etc_Frailty = etc_Frailty + change(body_set[14])
        etc_Frailty = etc_Frailty + change_b(body_set[15])
        etc_Frailty = etc_Frailty + change_b(body_set[16])
        etc_Frailty = etc_Frailty + change(body_set[17])
        etc_Frailty = etc_Frailty + change_b(body_set[18])
        
        BMI=int(weight)/(int(hight)/100*int(hight)/100)
        
    

       
        
        
    if (BMI<18.5):
            a=1
    else: 
            a=0
    nutrition_Frailty=nutrition_Frailty+a
    
    if(motion_Frailty>3):
        motion_Frailty_check="運動フレイルの傾向が見られます"
    else:
        motion_Frailty_check="運動フレイルの傾向は見られません"   

    if(nutrition_Frailty>2):
        nutrition_Frailty_check="栄養フレイルの傾向が見られます"
    else:
        nutrition_Frailty_check="栄養フレイルの傾向は見られません"


    if(oral_Frailty>2):
        oral_Frailty_check="口腔フレイルの傾向が見られます"
    else:
        oral_Frailty_check="口腔フレイルの傾向は見られません"
    print(oral_Frailty_check)
       
    if(etc_Frailty+motion_Frailty+nutrition_Frailty+oral_Frailty>10):
        etc_Frailty_check="総合的にフレイルの傾向が見られます"
    else:
        etc_Frailty_check="特出した項目は見られません"
   
    print(motion_Frailty)
    print(nutrition_Frailty)
    print(oral_Frailty)
    print(etc_Frailty_check)
    filewrite_name(name_set,body_set)
    
    return  motion_Frailty_check,nutrition_Frailty_check,oral_Frailty_check,etc_Frailty_check

"""
def get_answer(number):
     if request.method == "POST":
        answer= request.form['check']
        data_box[number]=answer
        return data_box
"""


        


              
@app.route('/q<i>', methods=['GET', 'POST'])
def q_form(i="0"):
        if  (int(i)==0):
            page_contents = {'type':'質問'+ str(i) ,'nextpage':'/q'+ str(int(i)+1) ,
        'insert_something1': question[int(i)-1]}
            return render_template('question.html', page_contents=page_contents)
        elif(int(i)<len(question)):
            page_contents = {'type':'質問'+ str(i) ,'nextpage':'/q'+ str(int(i)+1),'insert_something1': question[int(i)-1]}
            data_box=getanswer_method(int(i)-1)
            return render_template('question.html', page_contents=page_contents)
        elif(int(i) == len(question)):
            data_box=getanswer_method(int(i)-1)
        
            page_contents = {'type':'質問'+ str(i),'nextpage':'personaldata.html','insert_something1':'最後に下の問題に答えてください'}

            return render_template('personaldata.html', page_contents=page_contents)

@app.route('/personaldata.html', methods=['GET', 'POST'])
def p_form():
    name= request.form['name']
    sex=request.form['sex']
    age= request.form['age']
    hight= request.form['hight']
    weight= request.form['weight']
   
    motion_Frailty_check,nutrition_Frailty_check,oral_Frailty_check,etc_Frailty_check= getname_method(name,sex,age,hight,weight)
    BMI=int(weight)/(int(hight)/100*int(hight)/100)
    
    print(BMI)
    if (BMI<18.5):
        tips='やせ型です'
    elif(BMI>30):
         tips='やや肥満ぎみです'
    else:
        tips='健康な体型です'
    BMI="{:.1f}".format(BMI)
    
   

    page_contents = {'nextpage':'result.html','insert_something1': '回答終了です', 'BMI_sets':BMI,'tips':tips,'motion':motion_Frailty_check,'nutrition':nutrition_Frailty_check,'oral':oral_Frailty_check,'etc':etc_Frailty_check}
    return render_template('result.html', page_contents=page_contents)

@app.route('/result-fort',methods=['GET', 'POST'])
def fort_result_form_temp():
    if request.method == "POST":
        sex=request.form['sex']
        age= float(request.form['age'])*0.01
        print("get_data")
        foods = request.form.getlist("food")
        ans=get_fortune(foods,age) 
        if(ans==0):
            tips="苦手な食べ物が似ている方の内、高血圧の方は少ないです。"
            #表現を検討2022/12/14
        
        elif(ans==1):
            tips="苦手な食べ物が似ている方の内、高血圧の方が多いです。食生活に注意しましょう。"    

    page_contents = {'type':'食べ物占い','insert_something1':tips}
    return render_template('result-fort.html', page_contents=page_contents)


@app.route('/result.html', methods=['GET', 'POST'])
def end_form():    
    page_contents = {
        'insert_something1': 'RoboWELL（ロボウェル）って?',
        'insert_something2': 'views.pyのinsert_something2部分です。',
        }
    return render_template('index.html', page_contents=page_contents)

@app.route('/index')
def rool_form():
       
        page_contents = {
        'insert_something1': 'RoboWELL（ロボウェル）って?',
        'insert_something2': 'views.pyのinsert_something2部分です。',
         'test_titles': ['質問1', '質問2', '質問3']
        }
        return render_template('index.html', page_contents=page_contents) # 変更

@app.route('/fort')
def fort_form_temp():
    i=0
    page_contents = {'type':'食べ物占い','insert_something1':'普段あまり食べない食べ物にチェックマークをつけてね'}
    return render_template('fort.html', page_contents=page_contents)




@app.route('/')
def index():
       
        page_contents = {
        'insert_something1': 'RoboWELL（ロボウェル）って?',
        'insert_something2': 'views.pyのinsert_something2部分です。',
         'test_titles': ['質問1', '質問2', '質問3']
        }
        return render_template('index.html', page_contents=page_contents) # 変更

       

@app.route('/sampleform-post')
def sample_form_temp():
    i="1"
    saved_pues=question
    print(question)
    
    page_contents = {'type':'それではアンケートを始めます','insert_something1': saved_pues[int(i)-1]}
    return render_template('sampleform-post.html', page_contents=page_contents)
@app.route('/robowell')
def robo_form():    
    page_contents = {
        'insert_something1': 'RoboWELL（ロボウェル）って?',
        'insert_something2': 'views.pyのinsert_something2部分です。',
        }
    return render_template('robowell.html', page_contents=page_contents)
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)




