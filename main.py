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
    response = requests.get(f'https://olimp.miet.ru/ppo_it_final?day={date[0]}&month={date[1]}&year={date[2]}',
                            headers={'X-Auth-Token': 'ppo_9_30003'})
    print(response.json())
    rooms = response.json()["message"]["windows"]["data"]
    windows_for_room = response.json()["message"]["windows_for_flat"]["data"]
    rooms_count = response.json()["message"]["flats_count"]["data"]
    print(windows_for_room)
    print(rooms_count)
    rooms_with_light = []
    k = 0
    room_number = 0
    all_windows = []
    for key in rooms:
        r = rooms[key]
        vsp = []
        for i in range(rooms_count):
            room_number += 1
            print(r)
            left_win = sum(windows_for_room[:i])
            right_win = sum(windows_for_room[:i]) + windows_for_room[i]
            print(left_win, right_win)
            for j in range(left_win, right_win):
                if r[j]:
                    vsp.append([True, room_number])
                else:
                    vsp.append([False, room_number])


            if any(r[j] for j in range(left_win, right_win)):
                k += 1
                rooms_with_light.append(room_number)
        all_windows.append(vsp)
    print(k)
    print(rooms_with_light)
    print("\n\n\n")
    for ind1 in range(len(all_windows)):
        for ind2 in range(len(all_windows[ind1])):
            all_windows[ind1][ind2] = str(all_windows[ind1][ind2][0]) + " " + str(all_windows[ind1][ind2][1])
    for ind1 in range(len(all_windows)):
        all_windows[ind1] = ",".join(all_windows[ind1])



    return {"status": "success",
            "floors_count": len(rooms),
            "k": k,
            "rooms_with_light": " ".join(map(str, rooms_with_light)),
            "rooms_count": rooms_count,
            "window_on_floor": " ".join(map(str, windows_for_room)),
            "all_windows": ";".join(all_windows)
            }



if __name__ == '__main__':

    app.run(host="0.0.0.0")
