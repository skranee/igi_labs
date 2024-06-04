from app.models_app.aboutModel import About


class AboutService:
    @staticmethod
    def get_info():
        return About.objects.all().first()
