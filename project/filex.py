import yaml,json
from yaml.loader import SafeLoader
import configparser
import os
class filex(object):
    def __init__(self):
        '''constructor for this class'''
        pass
    
    def __repr__(self):
        return "We have functions yaml , confRead,JSON"
        
    def yaml(self,filename):
        '''function to read YAML'''
        try:
            with open(file_name) as f:
                self.data = yaml.load(f, Loader=SafeLoader)
                print(self.data)
            '''writing a data to flatfile'''
            file = open('yamlDict.txt', 'wt')
            file.write(str(self.data))
            file.close()
            
        except Exception as e:
            print("Exception on yaml: ".format(e))
            
    
    def confRead(self,file):
        '''function to read config files'''
        try:
            config_object = ConfigParser()
            config_object.read(file)
            temp={}
            for i in range(len(config_object.sections())):
                key=config_object.sections()[i]
                userinfo=config_object[str(key)]
                temp_d={}
                for n,j in userinfo.items():
                    temp_d[n]=j
                temp[key]=temp_d 
                
            self.confVal=temp
            print(temp)
            '''writing a data to flatfile'''
            file = open('confFile.txt', 'wt')
            file.write(str(self.confVal))
            file.close()
    
        except Exception as e:
            print("Exception on confRead: ".format(e))
            
            
    def jsonread(self,filename):
        '''function to read read JSON'''
        try:
            with open(filename) as f:
                self.data = json.load(f)
                print(self.data)
            '''writing a data to flatfile'''
            file = open('jsonDict.txt', 'wt')
            file.write(str(self.data))
            file.close()
            
        except Exception as e:
            print("Exception on JSON: ".format(e))
            