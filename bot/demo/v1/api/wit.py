import requests

def call_wit(msg):
    re = requests.get('https://api.wit.ai/message?v=20211116&q={}'.format(msg),
            headers = {'Authorization': 'Bearer P4EEQRQBI5AHKMC4TEYAONOWD475YU26'})
    jsoned = re.json()
    print(jsoned['intents'][0]['name'])
    if jsoned['intents'][0]['name'] == 'Findcinema':
        reply = (requests.get('http://127.0.0.1:5001/v2/cinema')).json()


    elif jsoned['intents'][0]['name'] == 'cinemaBymovie':
        moviename = (jsoned['entities']['moviename:moviename'][0]['body']).lower()
        para = {'movie name' : moviename}
        reply = (requests.get('http://127.0.0.1:5001/v2/cinema/search', params=para)).json()

    elif jsoned['intents'][0]['name'] == 'Findoffer':
        cinemaname = (jsoned['entities']['cinema:cinema'][0]['body']).lower()
        para = {'cinema name' : cinemaname}
        reply = (requests.get('http://127.0.0.1:5001/v2/cinema/offer', params=para)).json()

    elif jsoned['intents'][0]['name'] == 'Findmovie':
        moviename = (jsoned['entities']['moviename:moviename'][0]['body']).lower()
        cinemaname = (jsoned['entities']['cinema:cinema'][0]['body']).lower()
        para = {'movie name': moviename, 'cinema name' : cinemaname}
        reply = (requests.get('http://127.0.0.1:5003/v2/movie', params=para)).json()

    elif jsoned['intents'][0]['name'] == 'booking':
        moviename = (jsoned['entities']['moviename:moviename'][0]['body']).lower()
        cinemaname = (jsoned['entities']['cinema:cinema'][0]['body']).lower()
        time = (jsoned['entities']['wit$datetime:datetime'][0]['body'])[3:].lower()
        ticket = (jsoned['entities']['numticket:numticket'][0]['body']).lower()
        name = (jsoned['entities']['username:username'][0]['body']).lower()
        para = {'username':name, 'cinema':cinemaname, 'movie name': moviename, 'timeslot':time, 'number of tickets':ticket}
        reply = (requests.get('http://127.0.0.1:5001/v3/booking/book', params=para)).json()

    elif jsoned['intents'][0]['name'] == 'Cancelbooking':
        moviename = (jsoned['entities']['moviename:moviename'][0]['body']).lower()
        cinemaname = (jsoned['entities']['cinema:cinema'][0]['body']).lower()
        time = (jsoned['entities']['wit$datetime:datetime'][0]['body'])[3:].lower()
        name = (jsoned['entities']['username:username'][0]['body']).lower()
        para = {'username': name, 'cinema': cinemaname, 'movie name': moviename, 'timeslot': time}
        reply = (requests.get('http://127.0.0.1:5001/v3/booking/cancel', params=para)).json()

    else:
        reply = 'sorry, I cant understand what you said ...'

    return reply