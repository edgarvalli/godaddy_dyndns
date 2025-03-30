from time import sleep
from godaddy import GodaddyAPI


while True:
    gclient = GodaddyAPI()
    for task in gclient.config.tasks:
        gclient.update_a_record(task.domain, task.record_name, task.last_public_ip)
    sleep(gclient.config.TIMEOUT)