import threading
import rancher
import time

class DeployThread(threading.Thread):
    def __init__(self, rancher, service):
        self.rancher = rancher
        self.service = service
        super(DeployThread, self).__init__()
    
    def run(self):
        while self.rancher.getServiceState(self.service) != rancher.rancher.STATE_ACTIVE:
            print "Some task is deploying, sleeping."
            time.sleep(1)

        self.rancher.upgradeService(self.service)
        while self.rancher.getServiceState(self.service) != rancher.rancher.STATE_UPGRADED:
            time.sleep(1)
            print "Cheacking status error, sleeping."
            
        self.rancher.finishServiceUpgrade(self.service)
        print "Finished deploy, theading down!"