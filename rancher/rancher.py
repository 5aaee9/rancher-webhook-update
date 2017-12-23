import requests
import service
import json

_JSON_API_HEADER = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

STATE_UPGRADTING = "upgrading"
STATE_UPGRADED = "upgraded"

class Rancher(object):
    """
    Rancher manager API

    Attributes:
        host: The host of rancher, like https://docker.indexyz.me
        access_key: The access_key of rancher, can get from admin panel
        screct_key: The screct_key of rancher, can get from admin panel
    """
    def __init__(self, host, access_key, screct_key):
        """Init this class"""
        self.host = host
        self.access_key = access_key
        self.screct_key = screct_key
    
    def getEndpoint(self):
        """Get API endpoint"""
        if not (self.host.startswith("http://") or self.host.startswith("https://")):
            self.host = "https://" + self.host
        
        if self.host.endswith("/"):
            return self.host + "v2-beta"
        else:
            return self.host + "/v2-beta"

    def getAuth(self):
        """Get auth pair"""
        return (self.access_key, self.screct_key)

    def getServicePoint(self, service):
        return "{}/projects/{}/services/{}/".format(
            self.getEndpoint(), service.project_id, service.service_id
        )

    def updateService(self, service):
        return requests.post("{}?action=update".format(self.getServicePoint(service)), 
            headers=_JSON_API_HEADER, data=r"{}", auth=self.getAuth()
        ).json()

    def upgradeService(self, service):
        update_infomation = self.updateService(service)["upgrade"]

        return requests.post("{}?action=upgrade".format(self.getServicePoint(service)),
            headers=_JSON_API_HEADER, data=json.dumps(update_infomation), auth=self.getAuth()
        ).json()

    def getInfomaction(self, service):
        return requests.get("{}".format(self.getServicePoint(service)), 
            headers=_JSON_API_HEADER, auth=self.getAuth()
        ).json()

    def getServiceState(self, service):
        return self.getInfomaction(service)["state"]
    
    def finishServiceUpgrade(self, service):
        return requests.post("{}?action=finishupgrade".format(self.getServicePoint(service)),
            headers=_JSON_API_HEADER, auth=self.getAuth()
        ).json()
