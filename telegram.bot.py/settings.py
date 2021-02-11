db_url = 'sqlite:///db.sqlite'

ref_pay_perc_1lvl=0.05  #столько получит от 1 уровная рефералов за оплату
ref_pay_perc_2lvl=0.01  #столько получит от 2 уровная рефералов за оплату
ref_view_pay_1lvl=0.10  #столько получит от 1 уровная рефералов за подписку
ref_view_pay_2lvl=0.05  #столько получит от 2 уровная рефералов за подписку
new_ref_cost=0.10       #автоначисление за нового реферала.в копейках.
user_view_perc=0.54     #столько получит пользователь за вступление(проценты от стоимости установленной заказчиком)
min_out_pay=10          #минимальная сумма для вывода
min_post_cost=0.38      #минимальная стоимость 1 подписчика
user_post_perc=0.53     #процент от цены просмотра  
user_timewait_sec=6     #время просмотра поста
min_view_cost=0.037     #минимальная стоимость 1 просмотра


number = +79237907104        # qiwi phone here
qiwi_token = 'cf83896137f674f880357450851779ec' # qiwi token here

ya_number = 400000000000000  # yandex wallet here (hard to enable)
ya_token = '0'

telegram_token='1635434649:AAEWjq8EWukLbiag688dG0dO8HglJxWY0EI'      # bot token here

uah_to_rub = 2.71
usd_to_rub = 75.79
eur_to_rub = 91.13

admins = [ibragimov159]  # admin ids here
bans = []

tutorial_url = 'https'

WEBHOOK_HOST = '193.109.79.59' # Server IP here
WEBHOOK_PORT = 5984            # Server port here
WEBHOOK_LISTEN = '127.0.0.1'   # Internal IP for routeds

WEBHOOK_SSL_CERT = '/keys/webhook_cert.key'
WEBHOOK_SSL_PRIV = '/keys/webhook_pkey.pem'


WEBHOOK_URL_BASE = "https://{}:443".format(WEBHOOK_HOST)
WEBHOOK_URL_PATH = "/ppbot/{}/".format(telegram_token)

out_comment = ""
