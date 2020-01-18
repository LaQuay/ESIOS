class PVPC(object):
    def __init__(self, day, hour, gen, noc, vhc):
        """ Initialize a PVPC object.

        Parameters:
        day - str - The day of the PVPC [DD/MM/YYYY]
        hour - str - The hour of this item [HH:MM]
        gen - float - The €/kWh of the default fare (no DH) [0,10895]
        noc - float - The €/kWh of the DHA fare (2-period) [0,10895]
        vhc - float - The €/kWh of the DHS fare (3-period) [0,10895]
        """

        self.day = day
        self.hour = hour
        self.gen = gen
        self.noc = noc
        self.vhc = vhc

    def __str__(self):
        return f"{self.day} | {self.hour} | {self.gen} | {self.noc} | {self.vhc}"


def get_minimum_consecutives(a_PVPC, type, n):
    """ Returns the lowest n consecutive elements in the aPVPC desired type.

    Parameters:
    a_PVPC - PVPC - Array of PVPC elements
    type - str - GEN, NOC or VHC
    n - int - Desired minimum consecutive elements

    Return:
    Array of PVPC elements.
    """

    if not a_PVPC:
        raise Exception("Error: aPCPC should not be empty")

    if n > len(a_PVPC) or n < 1:
        raise Exception("Error: 0 < n <= len(aPCPC)")

    if not (type == "GEN" or type == "NOC" or type == "VHC"):
        raise Exception("Error: type should be GEN or NOC or VHC")

    minAccumulated = 0
    aMinAccumulated = []
    minTotal = 1000
    aMinTotal = []

    for j in range(len(a_PVPC)):
        for i, value in enumerate(a_PVPC):
            if type == "GEN":
                minAccumulated += value.gen
            elif type == "NOC":
                minAccumulated += value.noc
            elif type == "VHC":
                minAccumulated += value.vhc
            aMinAccumulated.append(value)

            if (i + 1) % n == 0:
                if minAccumulated < minTotal:
                    minTotal = minAccumulated
                    aMinTotal = aMinAccumulated
                minAccumulated = 0
                aMinAccumulated = []
        a_PVPC.pop(0)

    return aMinTotal
