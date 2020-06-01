from Map_Search import Map_Search
from Mask_Map_Load import Mask_Map_Load
from Time_difference import Time_difference
from Mask_Search import Mask_Search

class Mask_Map_Core():

    def __init__(self):
        try:
            self.Map_Search=Map_Search()
            self.Mask_Map_Load=Mask_Map_Load()
            self.Time_difference=Time_difference()
            self.Mask_Search=Mask_Search()
        except Exception as Errr:
            raise Errr