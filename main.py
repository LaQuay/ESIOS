import json

from ESIOS.ESIOS import get_minimum_consecutives
from ESIOS.ESIOS_API import ESIOS_API

with open('config.json') as config_file:
    data = json.load(config_file)
    TOKEN = data["api"]["token"]

mESIOS = ESIOS_API(TOKEN)

pvp_array = mESIOS.get_pvpc_data(decimals=5)

min_pvpc_array = get_minimum_consecutives(pvp_array, type="PCB", n_consecutives=3)
for pvpc in min_pvpc_array:
    print(pvpc)
