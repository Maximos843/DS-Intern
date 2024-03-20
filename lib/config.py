from dataclasses import dataclass


@dataclass
class Variables:
    UNIQUE_CITIES = ['Астрахань', 'Балашиха', 'Барнаул', 'Белгород','Брянск', 'Видное',
                     'Владивосток', 'Владимир', 'Волгоград', 'Волжский', 'Вологда', 'Воронеж',
                     'Долгопрудный', 'Екатеринбург', 'Зеленоград', 'Иваново', 'Ижевск', 'Хабаровск'
                     'Иркутск', 'Казань', 'Калининград', 'Кемерово', 'Киров', 'Котельники', 'Красногорск', 'Краснодар',
                     'Красноярск', 'Липецк', 'Люберцы', 'Магнитогорск', 'Махачкала', 'Москва', 'Мытищи',
                     'Набережные Челны', 'Нижний Новгород', 'Новосибирск', 'Одинцово', 'Омск', 'Оренбург',
                     'Пенза', 'Пермь', 'Подольск', 'Реутов', 'Ростов-на-Дону', 'Рязань', 'Самара',
                     'Санкт-Петербург', 'Саратов', 'Сочи', 'Ставрополь', 'Сургут', 'Тверь', 'Томск', 'Тюмень',
                     'Ульяновск', 'Уфа', 'Химки', 'Чебоксары', 'Челябинск', 'Щёлково', 'Ярославль']

    UNIQUE_TERRITORIES = ['Дальневосточный федеральный округ', 'Приволжский федеральный округ',
                          'Северо-Западный федеральный округ', 'Северо-Кавказский федеральный округ',
                          'Сибирский федеральный округ', 'Уральский федеральный округ',
                          'Центральный федеральный округ', 'Южный федеральный округ']

    UNIQUE_TYPES = ['ATM', 'Amusement Park', 'Art Museum', 'Auto Maintenance', 'Bakery', 'Bank', 'Bar or Pub', 'Billiards',
                    'Bookstore', 'Business Facility', 'Butcher', 'Caucasian Food', 'Chicken Restaurant', 'Childrens Apparel',
                    'Chinese Food', 'Church', 'Cinema', 'City', 'Civic Center', 'Clothing Store', 'Coffee Shop', 'College',
                    'Consumer Electronics Store', 'Convenience Store', 'Creperie', 'Dentist', 'Department Store', 'Diving Center',
                    'East European Food', 'Fitness Center', 'Food and Beverage Shop', 'Furniture Store', 'Government Office',
                    'Grocery', 'Historical Monument', 'Home Improvement Store', 'Hospital', 'Hotel', 'Ice Skating Rink',
                    'Indoor Sports', 'Industrial Zone', 'International Food', 'Italian Food', 'Japanese Food', 'Karaoke', 'Library',
                    'Medical Clinic', 'Mexican Food', 'Night Club', 'Nightlife', 'Office Supplies Store', 'Parking', 'Pastries',
                    'Performing Arts', 'Pet Store', 'Pharmacy', 'Pizza', 'Police Station', 'Post Office', 'Rental Cars', 'Residential Area',
                    'Russian Food', 'School', 'Shopping Center', 'Specialty Store', 'Sporting Goods Store', 'Sports Center', 'Sushi',
                    'Tourist Attraction', 'District', 'Gas Station', 'Live Music', 'Sandwich Shop']

    CATEGORIAL_COLUMNS = ['population_category', 'territory_category', 'city_category', 'type_category']
