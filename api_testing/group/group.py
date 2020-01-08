""" director account specific methods """

from api_request.request import *
from config import *

class Groups():
    projectAccData = {}

    def __init__(self, director_url, api_key, api_password):
        # configobj = Config(director_url, api_key, api_password)
        # self.base_url = configobj.GROUPS_URL
        base_url = director_url + "/v3"
        GROUPS_URL = f"{base_url}/groups"
        self.base_url = GROUPS_URL
        # Data request object initialize
        requestobj = Data(api_key, api_password) 
        self.request = requestobj  
      
    def setProjectAccountDataIfExists(self):
        groupsList = self.request.get(self.base_url)
        account = "ProjectAccount"
        for dict in groupsList:
            if account == dict["name"]:
                print(dict["name"])
                Groups.projectAccData = dict
                return True
        print("Project Account does not exist")
        return False
        
    def getProjectAccountID(self):
        if self.setProjectAccountDataIfExists():
            return self.projectAccData['id']
        else:
            return None