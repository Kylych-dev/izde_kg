# Бунгало (Bungalow) - это стиль жилья, одноэтажный дом или коттедж,
# Дуплексы обычно предлагают возможность размещения двух семей или жилых помещений в одном здании


# Одноэтажный Двухэтажный Трехэтажный + 
STOREY = (
    ('Bungalow', 'Bungalow'),
    ('Duplex', 'Duplex'),
    ('One Storeys', 'One Storeys'),
    ('Two Storeys', 'Two Storeys'),
    ('Three Storeys', 'Three Storeys'),
    ('Four Storeys', 'Four Storeys'),
    ('Five Storeys', 'Five Storeys')
)

# мебeлированная
FURNISHED = (
    ('yes', 'yes'),
    ('no', 'no'),
    ('somewhat', 'somewhat'),
)

# новое имущество или новостройка
NEW_PROPERTY = (
    ('yes', 'yes'),
    ('no', 'no'),
)

# место для парковки
PARKING_SPACE = (
    ('yes', 'yes'),
    ('no', 'no'),
)

# спальня
BEDROOM = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)

# продолжительность или срок
DURATION = (
    ('1 month', '1 month'),
    ('3 months', '3 months'),
    ('6 months', '6 months'),
    ('Year', 'Year'),
    ('2 Years', '2 Years'),
    ('3 Years', '3 Years'),
)

# ванная комната
BATHROOM = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)

# цель или назначение
PURPOSE = (
    ('Residential', 'Residential'),
    ('Office', 'Office'),
    ('Business', 'Business'),
    ('Other', 'Other'),
)

# выбор гендера
GENDER_CHOICES = (
    ('no', 'no'),
    (1, 'male'),
    (2, 'female'),
<<<<<<< HEAD
    (3, 'other')
)


'''type_property = (
        'office',
        'house',
    )
type_operations = (
        'sell',
        'rent'
    )'''
=======
)

REGION_CHOICES = (
    ('no', 'no'),
    ('CHUI', 'CHUI'),
    ('DJALAL-ABAD', 'DJALAL-ABAD'),
    ('OSH', 'OSH'),
    ('NARYN', 'NARYN'),
    ('TALAS', 'TALAS'),
    ('ISSYK-KUL', 'ISSYK-KUL'),
)

DEAL= (
    ('rent', 'Rent'),
    ('sale', 'Sale'),
    ('term', 'Term'),
)

CURRENCY = (
        ('no', 'no'),
        ('ru', 'RU'),
        ('us', 'US'),
        ('som', 'SOM'),
        ('EU', 'EU'),
)

STYLE = (
    ('104', '104'),
    ('105', '105'),
    ('Сталинка', 'Сталинка'),
    ('Хрущевка', 'Хрущевка'),

)
# Описать все серии квартир и стилей, например хрущевка 
# сталинка элитка и тд, посмотреть все варианты можно в лалафо
>>>>>>> 6eeb663169c96a41a3a81064e704a2c60a065635
