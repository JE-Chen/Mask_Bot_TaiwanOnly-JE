import ast
from Models.Mask_Map_Load import Mask_Map_Load
from Models.Map_Search import Map_Search
from Models.Time_difference import Time_difference


class Mask_Search():

    def __init__(self):
        self.Map_Search=Map_Search()
        self.Mask_Map=Mask_Map_Load()
        self.Mask_Map.Reload_Json()
        self.Mask_Map.Read_Json()
        self.Data= self.Mask_Map.Json_Load()
        self.Mask_Data={}
        self.Time_Upgrade=Time_difference()
        self.Time_Upgrade.Do_Time_Job(self.ReLoad)
        self.Map=False


    def Map_Open(self,Map):
        self.Map=Map
        if(Map==True):
            self.Map_Search.Create_Fmap()

    def ReLoad(self):
        self.Mask_Map.Reload_Json()
        self.Mask_Map.Read_Json()
        self.Data= self.Mask_Map.Json_Load()
        self.Mask_Data={}

    def Get_Data(self):
        Map_Info = open('test.txt', 'w+', encoding='utf-8')
        print(len(self.Data['features']))
        for i in range(len(self.Data['features'])):
            Total = ''
            print(self.Data['features'][i]['properties'])
            print('''----------------------------------------------------------------------------------------''')
            print(self.Data['features'][i]['geometry'])
            print('''----------------------------------------------------------------------------------------''')
            print(self.Data['features'][i]['geometry']['coordinates'])
            Total += '名稱: '+str(self.Data['features'][i]['properties']['name']).encode('utf-8').decode('utf-8')+'\n'
            print('''----------------------------------------------------------------------------------------''')
            Total += '電話: '+str(self.Data['features'][i]['properties']['phone']).encode('utf-8').decode('utf-8')+'\n'
            Total += '地址: '+str(self.Data['features'][i]['properties']['address']).encode('utf-8').decode('utf-8')+'\n'
            Total += '成人口罩剩餘量: '+str(self.Data['features'][i]['properties']['mask_adult']).encode('utf-8').decode('utf-8')+'\n'
            Total += '兒童口罩剩餘量: '+str(self.Data['features'][i]['properties']['mask_child']).encode('utf-8').decode('utf-8')+'\n'
            Total += '更新時間: '+str(self.Data['features'][i]['properties']['updated']).encode('utf-8').decode('utf-8')+'\n'
            Total+='經緯度: '+str(self.Data['features'][i]['geometry']['coordinates']).encode('utf-8').decode('utf-8')+'\n'
            self.Mask_Data.update({Total:self.Data['features'][i]['geometry']['coordinates']})
            Map_Info.write(str(self.Data['features'][i])+'\n')
        Map_Info.close()


    '''
    22.632269，120.299803 六合夜市
    
    25.040227, 121.512134 總統府
    '''
    def Get_Position(self,X=121.512134,Y=25.040227):
        for key in self.Mask_Data:
            Now_KM=format(self.Map_Search.Get_Haversine(X,Y,self.Mask_Data.get(key)[0],self.Mask_Data.get(key)[1]),'.5f')
            Now_KM=float(Now_KM)
            self.Mask_Data[key]=Now_KM


    def Return_Nearby(self,X=121.512134,Y=25.040227):
        Return_List=[]
        self.Mask_Map.Read_Json()
        self.Get_Data()
        self.Get_Position(X,Y)
        print('''----------------------------------------------------------------------------------------''')
        Mask_Data = {k: v for k, v in sorted(self.Mask_Data.items(), key=lambda item: item[1])}
        print(Mask_Data)
        print('''----------------------------------------------------------------------------------------''')
        counter=0
        for key in Mask_Data:
            if(counter==10):
                break
            print(key)
            if(self.Map==True):
                Location=(key.split()[-2:])
                Location[0],Location[1]=Location[1],Location[0]
                GG=(Location[0]+Location[1]).replace(',','').replace('[',',').replace(']','')
                GG='['+GG+']'
                Nail=ast.literal_eval(GG)
                self.Map_Search.Make_More_Nail(location=Nail,popup='藥局')
            Return_List.append(key)
            counter+=1
        self.Mask_Data={}
        if (self.Map == True):
            self.Map_Search.Save_Open('Test')
        return Return_List


