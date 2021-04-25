from environs import Env
import dotenv

dotenv.load_dotenv()
env = Env()
env.read_env()

BOT_TOKEN = '1647230704:AAGwt33avCK-zUuyRaePyDJi1vl1EIwZxhc'
ADMINS = env.list("ADMINS")
IP = env.str("ip")
YANDEX_API_TOKEN_GEOCODER = env.str('YANDEX_API_TOKEN_GEOCODER')
YANDEX_API_TOKEN_ORGANIZATIONS = env.str('YANDEX_API_TOKEN_ORGANIZATIONS')
YANDEX_LINK_GEOCODER = 'https://geocode-maps.yandex.ru/1.x/'
YANDEX_LINK_ORGANIZATIONS = 'https://search-maps.yandex.ru/v1/'
