# -*- coding: utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup

class Mask_Map_Load():

    def __init__(self):
        try:
            self.Url='https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json'
            rs = requests.session()
            res = rs.get(self.Url)
            if res.status_code == 200:
                self.Soup= BeautifulSoup(res.text, 'lxml')
                self.Total=''
        except Exception as Errr :
            raise Errr

    def Reload_Json(self):
        try:
            self.Url='https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json'
            rs = requests.session()
            res = rs.get(self.Url)
            if res.status_code == 200:
                self.Soup= BeautifulSoup(res.text, 'lxml')
                self.Total=''
                self.Output_Json()
        except Exception as Errr :
            raise Errr

    def Output_Json(self,File_Name='Map_Info.txt'):
        with open(File_Name,'w',encoding='utf-8') as Map_Info:
            Map_Info.write(self.Soup.text)

    def Read_Json(self,File_Name='Map_Info.txt'):
        self.Total=''
        with open(File_Name,'r',encoding='utf-8') as Map_Info:
            self.Total+=Map_Info.read()

    def Json_Load(self):
        Data=json.loads(self.Total)
        return Data