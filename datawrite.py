import csv
import datetime


def filemakes(name,age):
    dt_now = datetime.datetime.now()
    """回答日時、名前、年齢"""
    day = str(dt_now.year)+'/'+str(dt_now.month)+'/'+str(dt_now.day)+'/'+str(dt_now.hour)+'/'+str(dt_now.minute)
    header = ['回答日時','名前','年齢']
    tag = [day,name,age]
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(tag)
        f.close()
    return 0

def filewrite(body):

    with open('data.csv', 'a') as f:
         header2 = [['','','','問題番号','問題','回答']]
         writer = csv.writer(f)
         writer.writerows(header2)
         writer.writerows(body)
    f.close()
    return 0

"""htmlからのPOSTデータの「0」「1」を対応するワードに変換"""
def check_yesno(answer):
    if(int (answer)==0):
     answer = 'はい'
    elif(int (answer)==1):
     answer = 'いいえ'
    else: answer = 'エラー'
    return answer 