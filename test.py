from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/View')
def View():
    db = sqlite3.connect("Project.db")
    db.row_factory = sqlite3.Row
    Best_Tourspot = db.execute(
        'select T_name, count(*) as NumberOfTraveler from Registration group by T_name order by NumberOfTraveler DESC'
        ).fetchall()
    Best_output=''
    
    for Best_recommend in Best_Tourspot:
        Best_output = '총 이용자 수' + '<br>' +'가장 많은 사람이 여행한 장소는 ' + Best_recommend['T_name'] + ' 입니다' +'<br>''<br>'


    db.close()

    return Best_output
    

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)