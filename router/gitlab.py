from flask import make_response
from rancher import rancher
from rancher import deploy
from rancher import service
from flask import request

def attach(app):
    @app.route('/webhook/gitlab/<projectId>/<serviceId>', methods=['POST'])
    def gitlab(projectId, serviceId):
        config = app.i_config
        if not (request.headers.get("X-Gitlab-Token") == config.GITLAB_PASS):
            resp = make_response("Auth Token Error", 401)
            return resp
        if request.get_json()["object_attributes"]["status"] != "success":
            # GitLab is not success
            return make_response("skip", 204)
        rancher_service = service.Service(
            projectId, serviceId
        )
        rancher_instance = rancher.Rancher(
            config.RANCHER_HOST, config.RANCHER_ACCESS_KEY, config.RANCHER_SCRECT_KEY
        )
        deploy.DeployThread(
            rancher_instance, rancher_service, config, request.get_json()
        ).start()

        return "Deploy theading started"
