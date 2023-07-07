from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=15, unique=True, verbose_name='Логін учня')),
                ('clas', models.CharField(choices=[('1-A', '1-A'), ('1-B', '1-B'), ('2-A', '2-A'), ('2-B', '2-B'), ('3-A', '3-A'), ('3-B', '3-B'), ('4-A', '4-A'), ('4-B', '4-B'), ('5-A', '5-A'), ('5-B', '5-B'), ('6-A', '6-A'), ('6-B', '6-B'), ('7-A', '7-A'), ('7-B', '7-B'), ('8-A', '8-A'), ('8-B', '8-B'), ('9-A', '9-A'), ('9-B', '9-B'), ('10-A', '10-A'), ('10-B', '10-B'), ('11-A', '11-A'), ('11-B', '11-B')], max_length=4, verbose_name='Клас')),
                ('last_name', models.CharField(max_length=15, verbose_name="Ім'я учня")),
                ('first_name', models.CharField(max_length=15, verbose_name='Прізвище учня')),
                ('image', models.ImageField(upload_to='D:\\Working\\Praktic\\Project\\Diary\\student\\static\\student\\img', verbose_name='Аватарка учня')),
            ],
            options={
                'verbose_name': 'Учень',
                'verbose_name_plural': 'Учні',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=15, unique=True, verbose_name='Логін вчителя')),
                ('last_name', models.CharField(max_length=15, verbose_name="Ім'я вчителя")),
                ('first_name', models.CharField(max_length=15, verbose_name='Прізвище вчителя')),
                ('predmet', models.CharField(choices=[('Алгебра', 'Алгебра'), ('Англійська мова', 'Англійська мова'), ('Астрономія', 'Астрономія'), ('Біологія', 'Біологія'), ('Біологія і екологія', 'Біологія і екологія'), ('Географія', 'Географія'), ('Геометрія', 'Геометрія'), ('Громадянська освіти', 'Громадянська освіти'), ('Зарубіжна література', 'Зарубіжна література'), ('Інформатика', 'Інформатика'), ('Історія', 'Історія'), ('Історія України', 'Історія України'), ('Математика', 'Математика'), ('Мистецтво', 'Мистецтво'), ('Музика', 'Музика'), ('Основи здоров’я', 'Основи здоров’я'), ('Правознавство', 'Правознавство'), ('Природа', 'Природа'), ('Технології', 'Технології'), ('Українська література', 'Українська література'), ('Українська мова', 'Українська мова'), ('Фізика', 'Фізика'), ('Фізична культура', 'Фізична культура'), ('Хімія', 'Хімія'), ('Я досліджую світ', 'Я досліджую світ')], max_length=255, verbose_name='Предмети')),
                ('image', models.ImageField(upload_to='D:\\Working\\Praktic\\Project\\Diary\\teacher\\static\\teacher\\img', verbose_name='Аватарка вчителя')),
            ],
            options={
                'verbose_name': 'Вчитель',
                'verbose_name_plural': 'Вчителі',
            },
        ),
    ]
