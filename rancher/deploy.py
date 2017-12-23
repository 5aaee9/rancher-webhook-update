import threading
import rancher
import time

class DeployThread(threading.Thread):
    def __init__(self, rancher, service):
        self.rancher = rancher
        self.service = service
        super(DeployThread, self).__init__()
    
    def run(self):
        self.rancher.upgradeService(self.service)
        while True:
            if self.rancher.getServiceState(self.service) != rancher.rancher.STATE_UPGRADED:
                time.sleep(1)
            else:
                self.rancher.finishServiceUpgrade(self.service)
                break