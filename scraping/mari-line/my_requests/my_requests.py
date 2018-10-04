from requests import get
from requests.exceptions import RequestException
from contextlib import closing


def simple_get(url):
    cookies = '_ga=GA1.2.1677934236.1538197248; _gid=GA1.2.1339815130.1538197248; _ym_uid=1538197248411002508; _ym_d=1538197248; BX_USER_ID=5c324d358a7aa102bedc644a65fd1abd; _ym_isad=1; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; BITRIX_SM_LOGIN=valyagur%40yandex.ru; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; BITRIX_SM_UIDL=valyagur%40yandex.ru; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; _ym_visorc_29068165=w; PHPSESSID=a64cf8424dcac82a84e7ef8fbf982c9f; BITRIX_SM_UIDH=117aaf85205746022c32761021da51f0; BITRIX_SM_UIDL=valyagur%40yandex.ru; BITRIX_SM_UIDH=117aaf85205746022c32761021da51f0'
    headers = {'Cookie': cookies}
    try:
        with closing(get(url, stream=True, headers=headers)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)
