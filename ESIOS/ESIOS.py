import sys


class PVPC(object):
    def __init__(self, day, hour, pcb, cym):
        """ Initialize a PVPC object.

        Parameters:
        day - str - The day of the PVPC [DD/MM/YYYY]
        hour - str - The hour of this item [HH:MM]
        pcb - float - The €/kWh of the default fare Peninsula, Canarias, Baleares [0,10895]
        cym - float - The €/kWh of the default fare Ceuta, Melilla [0,10895]
        """

        self.day = day
        self.hour = hour
        self.pcb = pcb
        self.cym = cym

    def __str__(self):
        return f"{self.day} | {self.hour} | {self.pcb} | {self.cym}"


def get_minimum_consecutives(a_PVPC, type, n_consecutives):
    """ Returns the lowest n_consecutive elements in the aPVPC desired type.

    Parameters:
    a_PVPC - PVPC - Array of PVPC elements
    type - str - PCB or CYM
    n_consecutive - int - Desired minimum consecutive elements

    Return:
    Array of PVPC elements.
    """

    if not a_PVPC:
        raise Exception("Error: aPCPC should not be empty")

    if n_consecutives > len(a_PVPC) or n_consecutives < 1:
        raise Exception("Error: 0 < n <= len(aPCPC)")

    if not (type == "PCB" or type == "CYM"):
        raise Exception("Error: type should be PCB or CYM")

    min_accumulated = 0
    min_accumulated_array = []
    min_total = sys.maxsize
    min_total_array = []

    for j in range(len(a_PVPC)):
        for i, value in enumerate(a_PVPC):
            if type == "PCB":
                min_accumulated += value.pcb
            elif type == "CYM":
                min_accumulated += value.cym
            min_accumulated_array.append(value)

            if (i + 1) % n_consecutives == 0:
                if min_accumulated < min_total:
                    min_total = min_accumulated
                    min_total_array = min_accumulated_array
                min_accumulated = 0
                min_accumulated_array = []
        a_PVPC.pop(0)

    return min_total_array
