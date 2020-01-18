# This class holds all the interface to communicate to the ESIOS API.

import requests

from ESIOS.ESIOS import PVPC

URL_BASE = "https://api.esios.ree.es"
URL_GET_ALL_ARCHIVES = f"{URL_BASE}/archives_json"
URL_GET_PVPC_CURVE = f"{URL_BASE}/archives/70/download_json?locale=es"


class ESIOS_API(object):
    dateformat = '%Y-%m-%dT%H:%M:%S'

    def __init__(self, token):
        """ Initialize the ESIOS class

        Parameters:
        token - str - Your personal token to access the SIOS API
        """

        if token is None:
            raise Exception("Token variable should not be empty")
        self.token = token

    def __default_headers__(self):
        """Prepares the python-requests headers"""

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json; application/vnd.esios-api-v1+json",
            "Authorization": f"Token token=\"{self.token}\""
        }

        return headers

    def get_pvpc_data(self):
        response = requests.get(url=URL_GET_PVPC_CURVE, headers=self.__default_headers__())

        aPVPC = []
        for element in response.json()["PVPC"]:
            pvpc = PVPC(element['Dia'], element['Hora'],
                        round(float(element['GEN'].replace(",", ".")) / 1000, 5),
                        round(float(element['NOC'].replace(",", ".")) / 1000, 5),
                        round(float(element['VHC'].replace(",", ".")) / 1000, 5))
            aPVPC.append(pvpc)

        return aPVPC
