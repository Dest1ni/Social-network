from django.shortcuts import render
from django.views.generic import TemplateView,View
import requests
class ListServies(TemplateView):
    template_name = 'index.html'

class WeatherView(TemplateView):
    template_name = 'weather.html'
    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        city = request.POST.get("city")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=b8a26bb384d449620973d3b744de7977&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            context["json"] = data
            context["answer"] = "True"
            print(data)
        else:
            print("Ошибка при получении данных.")

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return render(context=self.get_context_data(**kwargs),template_name='weather.html',request=request)
    
class MusicView(TemplateView):
    template_name = 'music.html'
