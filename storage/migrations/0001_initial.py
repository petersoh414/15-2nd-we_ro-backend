# Generated by Django 3.1.4 on 2021-01-08 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.character')),
            ],
            options={
                'db_table': 'mylists',
            },
        ),
        migrations.CreateModel(
            name='StorageMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.character')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.music')),
            ],
            options={
                'db_table': 'storage_musics',
            },
        ),
        migrations.CreateModel(
            name='StorageArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.character')),
            ],
            options={
                'db_table': 'storage_artists',
            },
        ),
        migrations.CreateModel(
            name='StorageAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.character')),
            ],
            options={
                'db_table': 'storage_albums',
            },
        ),
        migrations.CreateModel(
            name='MylistMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.music')),
                ('mylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.mylist')),
            ],
            options={
                'db_table': 'mylist_musics',
            },
        ),
        migrations.AddField(
            model_name='mylist',
            name='music',
            field=models.ManyToManyField(through='storage.MylistMusic', to='music.Music'),
        ),
    ]
