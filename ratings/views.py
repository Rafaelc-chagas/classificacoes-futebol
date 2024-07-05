from django.views.generic import View
from django.shortcuts import render
import requests
from datetime import datetime

URL = 'https://v3.football.api-sports.io/standings'
API_KEY = ''


def get_ratings(league_id, season):
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': API_KEY,
    }
    params = {
        'league': league_id,
        'season': season,
    }
    response = requests.get(URL, headers=headers, params=params)
    return response.json()


class RatingView(View):
    template_name = 'ratings.html'
    leagues = [
        {'id': '39', 'name': 'Premier League'},
        {'id': '140', 'name': 'La Liga'},
        {'id': '135', 'name': 'Serie A'},
        {'id': '78', 'name': 'Bundesliga'},
        {'id': '61', 'name': 'Ligue 1'},
        {'id': '71', 'name': 'Campeonato Brasileiro'},
    ]

    def get(self, request):
        current_year = datetime.now().year
        years = [str(year) for year in range(current_year, current_year - 5, -1)]
        context = {'leagues': self.leagues, 'years': years}
        return render(request, self.template_name, context)

    def post(self, request):
        league_id = request.POST.get('league')
        season = request.POST.get('season')
        ratings = get_ratings(league_id, season)
        current_year = datetime.now().year
        years = [str(year) for year in range(current_year, current_year - 5, -1)]
        context = {
            'ratings': ratings,
            'leagues': self.leagues,
            'season': season,
            'years': years,
        }
        return render(request, self.template_name, context)
