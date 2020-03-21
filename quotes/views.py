from django.shortcuts import render
import requests
import json

def home(request):

	if request.method == 'POST':
		ticker = request.POST['tickerSearch']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_37cb8dfc7f334848be40742284eef319")
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})
	else:
		return render(request, 'home.html', {'ticker': "Enter a ticker Symbol"})


def settings(request):
	return render(request, 'settings.html', {})
