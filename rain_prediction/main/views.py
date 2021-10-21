from django.shortcuts import render
import json
import pickle


def home(request):
    response = render(request, 'main/home.html')
    if request.method == "POST":
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        data = pickle.load(open('csv_data.pkl', 'rb'))
        date_list = json_data['date'].split('-')
        date_list.reverse()
        X = data.loc[
            data['Date'] == '-'.join(date_list)
        ].loc[
            data['Location'] == json_data['location']
        ]
        response['Rainfall'] = X['RainTomorrow'].values[0].upper()
        return response
    return response
