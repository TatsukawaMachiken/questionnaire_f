from flask import Flask,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy  # 追加
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import os
from datawrite import filewrite,filemakes,check_yesno


#app.config.from_object('config')
#db = SQLAlchemy(app)

#db.create_all()
#class Employee(app):
#    __tablename__ = 'employee'
#    id = db.Column(db.Integer, primary_key=True)  # システムで使う番号
#    name = db.Column(db.String(255))  # 社員名
#    age = db.Column(db.String(255))  # 年齢
#    hight = db.Column(db.String(255))  # 身長
#    weight = db.Column(db.String(255))  # 体重
#    streng = db.Column(db.String(255))  # 握力
app = Flask(__name__)
"""回答保存用20221018"""
body=[]




"""ページ遷移"""
def getpage_method(title,nextname,question):
    my_dict = {'type':title,'nextpage':nextname,'insert_something1': question}
    return render_template('question.html', my_dict=my_dict)

"""回答保存"""
def getanswer_method(title,number):
    if request.method == "POST":
        answer= request.form['check']
        answer=check_yesno(answer)        
        body.insert(number,['','','',str(number),title,answer])
        """テスト出力"""
        if(number==3):
            print(body)
            filewrite(body)
            return 0
        return 0
    else:
        return getpage_method('エラーが発生しました','/error','404')

    
@app.route('/q1', methods=['GET', 'POST'])
def form_q1():
    age=50
    filemakes('フレイルある人',str(age))
    getanswer_method('バスや電車で1人で外出しますか?',1)
    return getpage_method('ここはq1です','/q2','バスや電車で1人で外出しますか?')

@app.route('/q2', methods=['GET', 'POST'])
def form_q2():
    getanswer_method('日用品の買い物をしていますか?',2)
    return getpage_method('ここはq2です','/q3','日用品の買い物をしていますか?')

@app.route('/q3', methods=['GET', 'POST'])
def form_q3():
    getanswer_method('預貯金の出し入れをしていますか?',3)
    return getpage_method('ここはq3です','/q4','預貯金の出し入れをしていますか?')
@app.route('/q4', methods=['GET', 'POST'])
def form_q4():
    getanswer_method('友人の家を訪ねていますか?',4)
    return getpage_method('ここはq4です','/q5','友人の家を訪ねていますか?')
@app.route('/q5', methods=['GET', 'POST'])
def form_q5():
    return getpage_method('ここはq5です','/q6','家族や友人の相談に乗っていますか？')

@app.route('/q6', methods=['GET', 'POST'])
def form_q6():
    return getpage_method('ここはq6です','/q7','階段を手すりや壁を使わずに昇っていますか？')

@app.route('/q7', methods=['GET', 'POST'])
def form_q7():
    return getpage_method('ここはq7です','/q7','椅子に座った状態から手を付かずに立ち上がれますか？')

@app.route('/')
def index():
        my_dict = {
        'insert_something1': 'RoboWELL（ロボウェル）って?',
        'insert_something2': 'views.pyのinsert_something2部分です。',
         'test_titles': ['質問1', '質問2', '質問3']
        }
        return render_template('index.html', my_dict=my_dict) # 変更

@app.route('/comp', methods=['GET', 'POST'])   
def comp_form():
        my_dict = {
            'type':'ここはcompです','nextpage':'index.html',
            'insert_something1': "回答ありがとうございます。"
            }
        return redirect(url_for('index.html'), my_dict=my_dict)

@app.route('/sampleform-post', methods=['POST'])
def sample_form_temp():
        print('POSTデータ受け取ったので処理します')
        my_dict2 = {'tern_something1':"回答ありがとうございます。"}
        return render_template('sampleform-post.html', my_dict=my_dict2)
        
if __name__ == "__main__":
    app.run(debug=True)

#@app.route('/add_employee', methods=['GET', 'POST'])
#def add_employee():
 #   if request.method == 'GET':
  #      return render_template('add_employee.html')
  #  if request.method == 'POST':
  #      employee = Employee(
  #          name = "kouki" , # 社員名
  #          age = "24"  ,# 年齢
  #          hight = "175" , # 身長
  #          weight = "54" , # 体重
  #          streng = "45"  # 握力
  #      )
  #      db.session.add(employee)
  #      db.session.commit()
  #      return redirect(url_for('index'))








    '''@app.route('/q1', methods=['GET', 'POST'])

@app.route('/q8', methods=['GET', 'POST'])
def q8_form():
    my_dict = {
        'type':'ここはq8です','nextpage':'/q9',
        'insert_something1': '15分位続けて歩いていますか？'
        }
    return render_template('question.html', my_dict=my_dict)
@app.route('/q9', methods=['GET', 'POST'])   
def q9_form():
    my_dict = {
        'type':'ここはq9です','nextpage':'/q10',
        'insert_something1': 'ここ1年間で転んだことはありますか？'
        }
    return render_template('question.html', my_dict=my_dict)
@app.route('/q10', methods=['GET', 'POST'])   
def q10_form():
    my_dict = {
        'type':'ここはq10です','nextpage':'/q11',
        'insert_something1': '転倒に対して不安がありますか？'
        }
    return render_template('question.html', my_dict=my_dict)

@app.route('/q11', methods=['GET', 'POST'])   
def q11_form():
    my_dict = {
        'type':'ここはq11です','nextpage':'/q12',
        'insert_something1': '6ヵ月間で2-3kg体重が減少しましたか？'
        }
    return render_template('question.html', my_dict=my_dict)
@app.route('/q12', methods=['GET', 'POST'])   
def q12_form():
    my_dict = {
        'type':'ここはq12です','nextpage':'/q13',
        'insert_something1': '半年前に比べて硬いものが食べにくくなりましたか？'
        }

 
    return render_template('question.html', my_dict=my_dict)

@app.route('/q13', methods=['GET', 'POST'])   
def q13_form():
    my_dict = {
        'type':'ここはq13です','nextpage':'/q14',
        'insert_something1': 'お茶や汁物でむせることがありますか？'
        }
    return render_template('question.html', my_dict=my_dict)
@app.route('/q14', methods=['GET', 'POST'])   
def q14_form():
    my_dict = {
        'type':'ここはq14です','nextpage':'/q15',
        'insert_something1': '口の渇きが気になりますか？'
        }
    return render_template('question.html', my_dict=my_dict)

@app.route('/q15', methods=['GET', 'POST'])   
def q15_form():
    my_dict = {
        'type':'ここはq15です','nextpage':'/q16',
        'insert_something1': '週に1回以上外出していますか？'
        }
    return render_template('question.html', my_dict=my_dict)
@app.route('/q16', methods=['GET', 'POST'])   
def q16_form():
    my_dict = {
        'type':'ここはq16です','nextpage':'/q17',
        'insert_something1': '昨年と比べて外出の回数が減っていますか？'
        }
    return render_template('question.html', my_dict=my_dict)

@app.route('/q17', methods=['GET', 'POST'])   
def q17_form():
    my_dict = {
        'type':'ここはq17です','nextpage':'/q18',
        'insert_something1': '周りの人から「いつも同じことを聞く」等と言われたり物忘れがあると言われますか？'
        }
    return render_template('question.html', my_dict=my_dict)
@app.route('/q18', methods=['GET', 'POST'])   
def q18_form():
    my_dict = {
        'type':'ここはq18です','nextpage':'/q19',
        'insert_something1': '自分で電話番号を調べて、電話をかけることをしていますか？'
        }
    return render_template('question.html', my_dict=my_dict)
@app.route('/q19', methods=['GET', 'POST'])   
def q19_form():
    my_dict = {
        'type':'ここはq19です','nextpage':'/q20',
        'insert_something1': '今日が何月何日かわからなことがありますか？'
        }
    return render_template('question.html', my_dict=my_dict)

@app.route('/q20', methods=['GET', 'POST'])   
def q20_form():
    my_dict = {
        'type':'ここはq20です','nextpage':'/q21',
        'insert_something1': '毎日の生活に充実感がありませんか？（ここ2週間）'
        }
    return render_template('question.html', my_dict=my_dict)

@app.route('/q21', methods=['GET', 'POST'])   
def q21_form():
    my_dict = {
        'type':'ここはq21です','nextpage':'/q22',
        'insert_something1': 'これまで楽しんでやれたことが楽しめなくなりましたか？（ここ2週間）'
        }
    return render_template('question.html', my_dict=my_dict)
@app.route('/q22', methods=['GET', 'POST'])   
def q22_form():
    my_dict = {
        'type':'ここはq22です','nextpage':'/q23',
        'insert_something1': '以前は楽にできていたことが今ではおっくうに感じられますか？（ここ2週間）'
        }
    return render_template('question.html', my_dict=my_dict)

@app.route('/q23', methods=['GET', 'POST'])   
def q23_form():
    my_dict = {
        'type':'ここはq23です','nextpage':'/q24',
        'insert_something1': '自分が役に立つ人間だと思いますか？（ここ2週間）'
        }
    return render_template('question.html', my_dict=my_dict)

@app.route('/q24', methods=['GET', 'POST'])   
def q24_form():
    my_dict = {
        'type':'ここはq24です','nextpage':'/add_employee',
        'insert_something1': 'わけもなく疲れ多様な感じがしますか？（ここ2週間）'
        }
    return render_template('question.html', my_dict=my_dict)'''



