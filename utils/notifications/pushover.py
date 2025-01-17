import logging

import requests

logging.getLogger("requests").setLevel(logging.WARNING)
log = logging.getLogger("pushover")


class Pushover:
    NAME = "Pushover"

    def __init__(self, app_token, user_token, priority=0):
        self.app_token = app_token
        self.user_token = user_token
        self.priority = priority
        log.info("Initialized Pushover notification agent")

    def send(self, **kwargs):
        if not self.app_token or not self.user_token:
            log.error("You must specify an app_token and user_token when initializing this class")
            return False

        # send notification
        try:
            payload = {
                'token': self.app_token,
                'user': self.user_token,
                'priority': self.priority,
                'message': kwargs['message'],
            }
            resp = requests.post('https://api.pushover.net/1/messages.json', data=payload, timeout=30)
            return resp.status_code == 200

        except Exception:
            log.exception("Error sending notification to %r", self.user_token)
        return False
