import logging
from datetime import datetime
import json

logging.basicConfig(filename="audit.log", level=logging.INFO)

def log_event(action, cid):
    event = {
            "action": action,
            "cid": cid,
            "timestamp": datetime.utcnow().isoformat()
            }
    with open("audit_log.json", "a") as log:
        log.write(json.dumps(event) + "\n")


