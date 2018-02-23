# -*- coding:utf-8 -*-
import os
class MakeDir(object):
    def mkdir(self,path):
    
        path=path.strip()
        path=path.rstrip("/")
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path) 
            
            return True
        else:
            
            return False
 

