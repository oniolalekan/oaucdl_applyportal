from django.apps import AppConfig


class CusersConfig(AppConfig):
    name = 'cusers'

    def ready(self):
        import cusers.signals


    

