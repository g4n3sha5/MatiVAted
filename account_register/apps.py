from django.apps import AppConfig


# class AccountRegisterConfig(AppConfig):
#      default_auto_field = 'django.db.models.BigAutoField'
#      name = 'account_register'


class UsersConfig(AppConfig):
    name = 'account_register'
    def ready(self):
        import account_register.signals