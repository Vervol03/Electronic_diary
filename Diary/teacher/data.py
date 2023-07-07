CLASS_CHOICES = (
    ('1-A', '1-A'), ('1-B', '1-B'),
    ('2-A', '2-A'), ('2-B', '2-B'),
    ('3-A', '3-A'), ('3-B', '3-B'),
    ('4-A', '4-A'), ('4-B', '4-B'),
    ('5-A', '5-A'), ('5-B', '5-B'),
    ('6-A', '6-A'), ('6-B', '6-B'),
    ('7-A', '7-A'), ('7-B', '7-B'),
    ('8-A', '8-A'), ('8-B', '8-B'),
    ('9-A', '9-A'), ('9-B', '9-B'),
    ('10-A', '10-A'), ('10-B', '10-B'),
    ('11-A', '11-A'), ('11-B', '11-B'),
)

PREDMET_CHOICES = (
    ('Алгебра', 'Алгебра'),
    ('Англійська мова', 'Англійська мова'),
    ('Астрономія', 'Астрономія'),
    ('Біологія', 'Біологія'),
    ('Біологія і екологія', 'Біологія і екологія'),
    ('Географія', 'Географія'),
    ('Геометрія', 'Геометрія'),
    ('Громадянська освіти', 'Громадянська освіти'),
    ('Зарубіжна література', 'Зарубіжна література'),
    ('Інформатика', 'Інформатика'),
    ('Історія', 'Історія'),
    ('Історія України', 'Історія України'),
    ('Математика', 'Математика'),
    ('Мистецтво', 'Мистецтво'),
    ('Музика', 'Музика'),
    ('Основи здоров’я', 'Основи здоров’я'),
    ('Правознавство', 'Правознавство'),
    ('Природа', 'Природа'),
    ('Технології', 'Технології'),
    ('Українська література', 'Українська література'),
    ('Українська мова', 'Українська мова'),
    ('Фізика', 'Фізика'),
    ('Фізична культура', 'Фізична культура'),
    ('Хімія', 'Хімія'),
    ('Я досліджую світ', 'Я досліджую світ')
)

post = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12')
)

clas_id = {}
login_id = {}
login = {}

predmet_all = ['Алгебра', 'Англійська мова', 'Астрономія', 'Біологія', 'Біологія і екологія', 'Географія', 'Геометрія',
               'Громадянська освіти', 'Зарубіжна література', 'Інформатика', 'Історія', 'Історія України', 'Математика',
               'Мистецтво', 'Музика', 'Основи здоров’я', 'Правознавство', 'Природа', 'Технології',
               'Українська література', 'Українська мова', 'Фізика', 'Фізична культура', 'Хімія', 'Я досліджую світ']

all_class = {
    '1': ['Англійська мова', 'Математика', 'Мистецтво', 'Музика', 'Технології', 'Українська мова', 'Фізична культура',
          'Я досліджую світ'],
    '10': ['Англійська мова', 'Астрономія', 'Біологія і екологія', 'Географія', 'Громадянська освіта',
           'Зарубіжна література', 'Інформатика', 'Історія', 'Історія України', 'Математика', 'Мистецтво', 'Технології',
           'Українська література', 'Українська мова', 'Фізика', 'Фізична культура', 'Хімія']
}