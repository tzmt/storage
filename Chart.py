import ctypes as ct
import ctypes.wintypes as cw

class Chart: 
    def __init__(self, inLocation, inMonth, inDay, inYear, inHour, inMinute):

        self.datetime = None
        self.timezone = None
        self.obliquity = None
        self.lst = None
        self.svp = None

        self.location = {
            "Longitude" : (),
            "Latitude" : ()
            }

        self.planet_dictionary = {
            # The order of the doubles is:
            # Ecliptical longitude, celestial latitude, distance, 
            # Speed in long, speed in lat, speed in dist
            "Sun" : (ct.c_double * 6)(),
            "Moon" : (ct.c_double * 6)(),
            "Mercury" : (ct.c_double * 6)(),
            "Venus" : (ct.c_double * 6)(),
            "Mars" : (ct.c_double * 6)(),
            "Jupiter" : (ct.c_double * 6)(),
            "Saturn" : (ct.c_double * 6)(),
            "Uranus" : (ct.c_double * 6)(),
            "Neptune" : (ct.c_double * 6)(),
            "Pluto" : (ct.c_double * 6)()
        }
        self.mundane_positions = {
            # House placement, decimal longitude (out of 360*)
            "Sun" : [ct.c_double(), ct.c_double()],
            "Moon" : [ct.c_double(), ct.c_double()],
            "Mercury" : [ct.c_double(), ct.c_double()],
            "Venus" : [ct.c_double(), ct.c_double()],
            "Mars" : [ct.c_double(), ct.c_double()],
            "Jupiter" : [ct.c_double(), ct.c_double()],
            "Saturn" : [ct.c_double(), ct.c_double()],
            "Uranus" : [ct.c_double(), ct.c_double()],
            "Neptune" : [ct.c_double(), ct.c_double()],
            "Pluto" : [ct.c_double(), ct.c_double()],
            }

        self.right_ascension_positions = {
            # House placement? decimal longitude (out of 360*)
            "Sun" : [ct.c_double(), ct.c_double()],
            "Moon" : [ct.c_double(), ct.c_double()],
            "Mercury" : [ct.c_double(), ct.c_double()],
            "Venus" : [ct.c_double(), ct.c_double()],
            "Mars" : [ct.c_double(), ct.c_double()],
            "Jupiter" : [ct.c_double(), ct.c_double()],
            "Saturn" : [ct.c_double(), ct.c_double()],
            "Uranus" : [ct.c_double(), ct.c_double()],
            "Neptune" : [ct.c_double(), ct.c_double()],
            "Pluto" : [ct.c_double(), ct.c_double()],
            }

        self.cusps = {
            "1" : (ct.c_double)(),
            "2" : (ct.c_double)(),
            "3" : (ct.c_double)(),
            "4" : (ct.c_double)(),
            "5" : (ct.c_double)(),
            "6" : (ct.c_double)(),
            "7" : (ct.c_double)(),
            "8" : (ct.c_double)(),
            "9" : (ct.c_double)(),
            "10" : (ct.c_double)(),
            "11" : (ct.c_double)(),
            "12" : (ct.c_double)(),
            }

        self.angles = {
            "Asc" : (ct.c_double)(),
            "MC" : (ct.c_double)(),
            "Dsc" : (ct.c_double)(),
            "IC" : (ct.c_double)(),
            "Eq Asc" : (ct.c_double)(),
            "Eq Dsc" : (ct.c_double)(),
            "EP (Ecliptical)" : (ct.c_double)(),
            "Zen" : (ct.c_double)(),
            "WP (Ecliptical)" : (ct.c_double)(),
            "Ndr" : (ct.c_double)(),
            }

        # To be one of Natal, SSR, SLR, DSLR
        self.type = "Natal"

    def formatData():
        
