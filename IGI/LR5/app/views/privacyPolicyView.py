from django.views import View
from django.shortcuts import render
from app.services.outerApiService import OuterApiService


class PrivacyPolicy(View):
    @staticmethod
    def get(request):
        dog_image = OuterApiService.random_dog_image()
        random_activity = OuterApiService.random_activity()
        return render(request, 'privacy-policy.html',
                      {'role': request.session['role'], 'activity': random_activity, 'dog_image': dog_image})
