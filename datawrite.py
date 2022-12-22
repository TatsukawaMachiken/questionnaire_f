import csv
import datetime

question=[]
def fileread():

    file = open('quesset.csv', 'r')
    data = csv.reader(file)
    for row in data:
        for col in row:
            question.append(col)  
    file.close()
    print(question)
    return question



def filewrite_name(name_set,body):
    dt_now = datetime.datetime.now()
    """回答日時、名前、年齢"""
    day = str(dt_now.year)+'/'+str(dt_now.month)+'/'+str(dt_now.day)+'/'+str(dt_now.hour)+'/'+str(dt_now.minute)
    #question[:0] = ['回答日時','名前','性別','年齢','身長','体重']
    body[:0]=name_set
    body.insert(0, str(day))
    file= open('data.csv', 'a',newline="")
    writer = csv.writer(file)
    #writer.writerow(question)
    writer.writerow(body)
    body.clear()
    #question.clear()
    file.close()
    body=[]
    return 0

"""def filewrite_data(:

    with open('data.csv', 'a',newline="") as f:
         writer = csv.writer(f)
         writer.writerows(header2)
         writer.writerows(body)
    f.close()
    return 0"""

"""htmlからのPOSTデータの「0」「1」を対応するワードに変換"""
def check_yesno(answer):
    if(int (answer)==0):
     answer = 'はい'
    elif(int (answer)==1):
     answer = 'いいえ'
    else: answer = 'エラー'
    return answer 