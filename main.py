import json

from ESIOS.ESIOS import get_minimum_consecutives
from ESIOS.ESIOS_API import ESIOS_API

with open('config.json') as config_file:
    data = json.load(config_file)
    TOKEN = data["api"]["token"]

mESIOS = ESIOS_API(TOKEN)

aPVPC = mESIOS.get_pvpc_data()

aMinPVPC = get_minimum_consecutives(aPVPC, "GEN", 3)
for pvpc in aMinPVPC:
    print(pvpc)