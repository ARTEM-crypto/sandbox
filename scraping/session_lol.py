from requests import Session

def lot_ajax(lot_id, referer):
    if not type(lot_id) == str:
        lot_id = str(lot_id)

    session = Session()
    session.head('https://24-ok.ru')

    response = session.post(
        url='https://24-ok.ru/function_po.php',
        data={
            'cmd': 'get_lot_card',
            'lot_id': lot_id,
            'isCompare': '0',
            'isLink': '0'
        },
        headers={
            'Origin': 'https://24-ok.ru/',
            'Referer': referer,
            'Cookie': '_ga=GA1.2.285990363.1535687046; _ym_uid=153568704617632385; _ym_d=1535687046; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; phpbb3_sp39_u=210110; phpbb3_sp39_k=43fa42cf9dcc7f72; phpbb3_sp39_sid=35260d3427d2b937b53e307046feda3a; _gid=GA1.2.1612249477.1535863955; _ym_isad=1'
        }
    )
    return response.text

def get_item_list(catalog_id, start=None):
    if start:
        start = '&start=' + str(start)
    url = f"https://24-ok.ru/catalog_new.php?catalog_id={str(catalog_id)}{start}&ajax=1&_pjax=%23pjax-container"
    referer = f"https://24-ok.ru/catalog_new.php?catalog_id={str(catalog_id)}{start}"

    session = Session()
    session.head('https://24-ok.ru')

    response = session.get(
        url=url,
        headers={
            'Origin': 'https://24-ok.ru/',
            'Referer': referer,
            'Cookie': '_ga=GA1.2.285990363.1535687046; _ym_uid=153568704617632385; _ym_d=1535687046; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; phpbb3_sp39_u=210110; phpbb3_sp39_k=43fa42cf9dcc7f72; phpbb3_sp39_sid=35260d3427d2b937b53e307046feda3a; _gid=GA1.2.1612249477.1535863955; _ym_isad=1'
        }
    )
    return response.text


if __name__ == "__main__":
    referer = 'https://24-ok.ru/catalog_new.php?catalog_id=2637994'
    lot_id = '327848248'

    lot_ajax(lot_id, referer)
