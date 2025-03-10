import urllib.parse

BASE_URL = 'https://qa-scooter.praktikum-services.ru'
MAIN_URL = urllib.parse.urljoin(BASE_URL, '/')
ORDER_PAGE = urllib.parse.urljoin(BASE_URL, 'order')
TRACK_URL = urllib.parse.urljoin(BASE_URL, 'track')

DZEN_URL = 'https://dzen.ru/'
DZEN_REDIRECT_URL = 'https://dzen.ru/?yredirect=true'
