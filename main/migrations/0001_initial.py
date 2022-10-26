# Generated by Django 4.1.2 on 2022-10-26 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('ano_lancamento', models.IntegerField()),
                ('valor_locacao', models.FloatField()),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrega', models.DateField()),
                ('data_locacao', models.DateField()),
                ('valor', models.IntegerField()),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
                ('Filme', models.ManyToManyField(to='main.filme')),
            ],
        ),
    ]