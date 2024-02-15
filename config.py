def getOrgsFromShortName (name):
    orgs = {
        'vgaps': 'https://sdo.vgaps.ru',
        'adpo': 'https://sdo.adpo-edu.ru',
        'uripkip': 'https://sdo.urgaps.ru',
        'niidpo': 'https://sdo.niidpo.ru',
        'bm': 'https://sdo.mcdo.moscow',
        'ipp': 'https://sdo.ippss.ru',
        'narhsi': 'https://sdo.narhsi.ru',
        'mipk': 'https://sdo2.dpomipk.ru',
        'penta': 'https://sdo.pentaschool.ru'}
    return orgs.get(name)
# print(getOrgsFromShortName('ipp'))
