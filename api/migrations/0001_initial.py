from django.db import migrations
from api.user.models import userModel


class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user = userModel(name = 'helal',
                         email = 'shohag.2896@gmail.com',
                         is_staff = True,
                         is_superuser = True,
                         phone = '01681123137',
                         gender = 'male')
        user.set_password('Shohag147')
        user.save()

    dependencies = [
     
    ]    
    
    operations = [
        migrations.RunPython(seed_data),
    ]