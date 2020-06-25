import webbrowser
import folium # 匯入 folium 套件
from geopy.geocoders import Nominatim
from math import radians, cos, sin, asin, sqrt

class Map_Search():

    def __init__(self):
        self.File_Name=".html"
        self.geolocator = Nominatim(user_agent="Test")

    def Create_Fmap(self,list_location=[22.632082,120.299156],zoom_start=15):
        # 建立地圖與設定位置
        self.fmap = folium.Map(location=list_location, zoom_start=zoom_start)


# ----------------------------------------------------------------------------------------------
    '''
    設置Icon Nail
    icon type : 
    驚嘆號 : 'info-sign' 
    顏色 : 'green' 
    雲的 : 'cloud'
    '''
    #
    def Set_Icon(self,list_location,width,height,str='22.632082,120.299156',Icon_Text='六合夜市\n經緯度',icon_color='green'):
        #設定點擊Icon文字
        Icon_Text = Icon_Text+str
        #設置點擊Icon出現的Frame
        iframe = folium.IFrame(Icon_Text, width=width, height=height)
        popup = folium.Popup(iframe, max_width=250)
        #放置地點
        Place = folium.Marker(location=list_location, popup=popup,
                     icon=folium.Icon(icon_color=icon_color))
        #加進地圖
        self.fmap.add_child(Place)


    #設置更多Icon
    def Make_More_Nail(self,location=[22.632082,120.299156],popup='六合夜市',icon_color='green'):
        folium.Marker(
            location=location,
            popup=popup,
            icon=folium.Icon(color=icon_color)
        ).add_to(self.fmap)

    #按下點顯示經緯度
    def Set_Fmap_Get_location(self):
        self.fmap.add_child(folium.LatLngPopup())

    #再按下點產生icon
    def Realtime_Nail(self):
        self.fmap.add_child(folium.ClickForMarker(popup='Waypoint'))

# ----------------------------------------------------------------------------------------------
    #要儲存的Html 檔案名
    def Set_File_Name(self,File_Name):
        self.File_Name=File_Name

    #儲存檔案
    def Save_Map(self,Map_Name):
        self.fmap.save(Map_Name+self.File_Name)
        return Map_Name+".html"

    #開啟檔案
    def Open_Map(self,Map_Name):
        webbrowser.open_new_tab(Map_Name+self.File_Name)
        return Map_Name+".html"

    #儲存並開啟
    def Save_Open(self,Map_Name):
        self.fmap.save(Map_Name+self.File_Name)
        webbrowser.open_new_tab(Map_Name + self.File_Name)

# ----------------------------------------------------------------------------------------------
    #設定要查詢的地點
    def Set_Geocode(self,Geocode_Text="六合夜市"):
        self.location = self.geolocator.geocode(Geocode_Text)
        if(self.location==None):
            self.Log.Debug("Wrong Address")
            return "需要更詳細的地址"
        else:
            return self.location

    #取得地址
    def Get_Address(self):
        print(self.location.address)
        return self.location.address

    #取得經緯度
    def Get_Lat_Lon(self):
        print((self.location.latitude, self.location.longitude))
        return self.location.latitude, self.location.longitude

    #取得原始資料
    def Get_Raw(self):
        print(self.location.raw)
        return self.location.raw

    #印出所有資料
    def Print_All_Detail(self):
        print(self.location.address)
        print((self.location.latitude, self.location.longitude))
        print(self.location.raw)

# ----------------------------------------------------------------------------------------------

    #畫出線段
    def Map_Draw_Line(self,Fill=True,*args):
        '''
        [22.73264868398435, 120.28450012207031],
        [22.72837380478485, 120.28450012207031],
        [22.723307108275556, 120.28604507446288]
        '''
        folium.PolyLine(locations=args,fill=Fill).add_to(self.fmap)

    #畫出多邊形區域
    def Map_Draw_Polygon(self,Fill=True,*args):
        '''
        locations=[
            [22.73264868398435, 120.28450012207031],
            [22.72837380478485, 120.28450012207031],
            [22.723307108275556, 120.28604507446288]
        ]
        '''
        folium.Polygon(locations=args,fill=Fill).add_to(self.fmap)

    #畫出矩形區域
    def Map_Draw_Rectangle(self,Fill=True,*args):
        '''
        [
            [22.727344647244575, 120.27111053466797],
            [22.739219071089853, 120.29419898986816]
        ]
        '''
        folium.Rectangle(locations=args,fill=Fill).add_to(self.fmap)

    #畫出圓形區域
    #採用真實尺寸
    def Map_Draw_Circle(self,Radius=10,Fill=True,*args):
        '''
            [22.73444963475145, 120.28458595275877],
        '''
        folium.Circle(locations=args,radius=Radius,fill=Fill).add_to(self.fmap)

    #畫出圓形標記區域
    #採用地圖尺寸
    def Map_Draw_CircleMaker(self,Radius=10,Fill=True,*args):
        '''
            [22.73444963475145, 120.28458595275877]
        '''
        folium.CircleMarker(locations=args,radius=Radius,fill=Fill).add_to(self.fmap)

# ----------------------------------------------------------------------------------------------
    #用圖片取代區域
    def Map_ImageOverlay(self,ImageUrl= 'https://opendata.cwb.gov.tw/fileapi/opendata/MSC/O-B0028-003.jpg',*args):
        '''
        imageBounds = [
            [18.600625745, 115.976888855],
            [27.79937425, 126.02300114]
        ]
        '''
        ImageBounds = [
            args
        ]
        folium.raster_layers.ImageOverlay(
            ImageUrl,
            ImageBounds,
            opacity=0.4
        ).add_to(self.fmap)

    #用影片取代區域
    def Map_VideoOverlay(self, VideoUrl = 'https://www.mapbox.com/bites/00188/patricia_nasa.webm',*args):
        # videoBounds = [[32, -130], [13, -100]]
        VideoBounds = args
        folium.raster_layers.VideoOverlay(
            VideoUrl,
            VideoBounds
        ).add_to(self.fmap)
        self.myMap.fit_bounds(VideoBounds)

# ----------------------------------------------------------------------------------------------
    #計算2地相差距離
    def Get_Haversine(self,lon1, lat1, lon2, lat2):  # 經度1，緯度1，經度2，緯度2 （十進制度數）
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # 將十進制度數轉化為弧度
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # Haversine公式
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # 地球平均半徑，單位為公里
        return c * r


