# Бунгало (Bungalow) - это стиль жилья, одноэтажный дом или коттедж,
# Дуплексы обычно предлагают возможность размещения двух семей или жилых помещений в одном здании


# Одноэтажный Двухэтажный Трехэтажный
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
    (1, 'male'),
    (2, 'female'),
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