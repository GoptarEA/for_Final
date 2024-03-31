from flask import Flask, render_template, request
from flask_cors import CORS
import requests


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello_world():  # put application's code here
    response = requests.get('https://olimp.miet.ru/ppo_it_final/date', headers={'X-Auth-Token': 'ppo_9_30003'})
    dates = []
    for elem in response.json()['message']:
        dates.append(elem)
    print(dates)
    return render_template("index.html", days=len(dates), dates=dates)


@app.route('/api/v1.0/show_rooms', methods=['POST', 'GET'])
def show_rooms():
    print(request.form.get("date"))
    date = request.form.get("date").split("-")
    print('https://olimp.miet.ru/ppo_it_final/?day=' + date[0] + '&month=' + date[1] + '&' + date[2] + '')
    response = requests.get('https://olimp.miet.ru/ppo_it_final/?day=' + date[0] + '&month=' + date[1] + '&' + date[2] + '',
                            headers={'X-Auth-Token': 'ppo_9_30003'})
    print(response)
    return {"status": "success"}



if __name__ == '__main__':

    app.run(host="0.0.0.0")
