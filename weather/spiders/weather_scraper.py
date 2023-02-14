import scrapy
from datetime import date, timedelta


class PogodaSpider(scrapy.Spider):
    name = 'pogoda'
    allowed_domains = ['pogoda1.ru']
    cities = ['astana', 'almaty', 'aktyubinsk-aktobe', 'atyrau',
              'semipalatinsk', 'ust-kamenogorsk', 'taraz', 'uralsk-4',
              'zhezkazgan', 'karaganda-2', 'kostanay', 'kyzylorda',
              'aktau-2', 'pavlodar-5', 'petropavlovsk-6', 'shymkent-2',
              'turkestan-2', 'taldykorgan', 'kapchagay', 'kokshetau'
              ]
    start_urls = [f'https://pogoda1.ru/{j}/' + i.strftime('%d-%m-%Y') for j in cities for i in 
                  [date(2018,2,1)+timedelta(days=x) for x in range((date(2023,2,13)-date(2018,2,1)).days)]
                  ]

    def parse(self, response):
        
        city_names = {
            'kostanay': 'Kostanay',
            'karaganda-2': 'karaganda',
            'shymkent-2': 'Shymkent',
            'taraz': 'Taraz',
            'uralsk-4': 'Oral',
            'astana': 'Astana',
            'kyzylorda': 'Kyzylorda',
            'aktau-2': 'Aktau',
            'zhezkazgan': 'Jezkazgan',
            'ust-kamenogorsk': 'Oskemen',
            'semipalatinsk': 'Semey',
            'aktyubinsk-aktobe': 'Aktobe',
            'petropavlovsk-6': 'Petropavl',
            'almaty': 'Almaty',
            'pavlodar-5': 'Pavlodar',
            'atyrau': 'Atyrau',
            'turkestan-2': 'Turkestan',
            'taldykorgan': 'Taldykorgan',
            'kapchagay': 'Konayev',
            'kokshetau': 'Kokshetau',
            }
        
        date = response.url.split('/')[-2].split('-')
        city = response.url.split('/')[-3]
        main = response.css('div.cell-forecast-main span::Text').getall()
        temp = response.css('div.cell-forecast-temp::Text').getall()
        press = response.css('div.cell-forecast-press::Text').getall()
        hum = response.css('div.cell-forecast-hum::Text').getall()
        yield {
            'city': city_names[city],
            'date': date[0],
            'month': date[1],
            'year': date[2],
            'weather_night': main[0],
            'weather_morning': main[1],
            'weather_day': main[2],
            'weather_evening': main[3],
            'temp_night': temp[0],
            'temp_morning': temp[1],
            'temp_day': temp[2],
            'temp_evening': temp[3],
            'press_night': press[0],
            'press_morning': press[1],
            'press_day': press[2],
            'press_evening': press[3],
            'hum_night': hum[0],
            'hum_morning': hum[1],
            'hum_day': hum[2],
            'hum_evening': hum[3],
            }
