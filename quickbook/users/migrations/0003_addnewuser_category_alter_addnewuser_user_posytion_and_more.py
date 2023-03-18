# Generated by Django 4.1.7 on 2023-03-13 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_posytion_remove_addnewuser_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addnewuser',
            name='category',
            field=models.CharField(choices=[('F', 'Fryzjerka'), ('R', 'Recepcjonistka'), ('S', 'Superviser')], default='S', max_length=20),
        ),
        migrations.AlterField(
            model_name='addnewuser',
            name='user_posytion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Posytion',
        ),
    ]