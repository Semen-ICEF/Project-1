class ColorizeMixin:
    """Changes colour of the text output """

    def __repr__(self):
        """
        :return: setting the text colour to custom
        """
        return f'\033[1;{Advert.color_code};40m'

class Advert(ColorizeMixin):
    color_code = 32

    def __init__(self, mapping: dict):
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += "_"
            if isinstance(value, dict):
                value = Advert(value)
            self.__dict__[key] = value

        if 'price' not in self.__dict__:
            self.price = 0
        elif self.__dict__['price'] < 0:
            raise ValueError('must be >= 0')


    def __getattr__(self, name):
        if hasattr(self.__dict__, name):
            return getattr(self.__dict__, name)
        else:
            return Advert.create(self.__dict__[name])

    @classmethod
    def create(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.create(item) for item in obj]
        else:
            return obj

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            raise ValueError('must be >= 0')
        elif key == 'price':
            self.__dict__['price'] = value

    @property
    def class_(self):
        """Property for 'class'"""
        return self.__dict__['class_']

    def __repr__(self):
        return f'{super().__repr__()} {self.title} | {self.price} ₽'

if __name__ == "__main__":
    import keyword
    import json
    from collections import abc

    # Test 1. General
    lesson_str = """{
                        "title": "python", "price": 1,
                        "location": {
                        "address": "город Москва, Лесная, 7",
                        "metro_stations": ["Белорусская"]
                        }
                    }"""

    lesson_ad = Advert(json.loads(lesson_str))
    print(lesson_ad.location.address)    # город Москва, Лесная, 7
    print(lesson_ad.price)               # 1

    # Test 2. Non-assigned price
    lesson_str_ = """{"title": "python"}"""
    lesson_ = json.loads(lesson_str_)
    lesson_ad_ = Advert(lesson_)
    print(lesson_ad_.price)              # 0

    # Test 3. Negative price
    # lesson_str__ = """{"title": "python", "price": -1}"""
    # lesson__ = json.loads(lesson_str__)
    # lesson_ad__ = Advert(lesson__)
    # print(lesson_ad__.price)           # ValueError: must be >= 0

    # Test 4. Metro stations
    metro_str = """{
                "title": "iPhone X",
                "price": 100,
                "location": {
                "address": "город Самара, улица Мориса Тореза, 50",
                "metro_stations": ["Спортивная", "Гагаринская"]
                }
            }"""
    metro = json.loads(metro_str)
    metro_ad = Advert(metro)
    print(metro_ad.location.metro_stations)

    # Test 5. Class and
    corgi_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {"address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"}}"""
    corgi_dict = json.loads(corgi_str)
    corgi = Advert(corgi_dict)
    print(corgi.class_)                  # dogs
    print(corgi)                         # Вельш-корги | 1000 ₽ (green colour)
