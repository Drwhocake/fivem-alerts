from win10toast import ToastNotifier
import threading
import time

queue = []

def alert (title, message):
	#add the alert to the queue
	queue.append([title, message])
	# check if there is already a thread running
	if threading.active_count() == 1:
		# if there is not a thread running then start one to run through alerts in the queue
		threading.Thread(target=runAlerts).start()
	else:
		# if there is a thread running then do nothing
		pass

def runAlerts():
	# loop through the queue and display each alert
	for alert in queue:
		toaster = ToastNotifier()
		toaster.show_toast(alert[0], alert[1], icon_path=None, duration=5, threaded=True)
		# remove the alert from the queue
		queue.remove(alert)
		# wait for the alert to finish
		while toaster.notification_active(): time.sleep(0.1)

	#check if there are any more alerts in the queue
	if len(queue) > 0:
		# if there are more alerts in the queue then run through them again
		runAlerts()
	else:
		# if there are no more alerts in the queue then do nothing
		pass


