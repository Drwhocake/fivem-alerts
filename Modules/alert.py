from win10toast import ToastNotifier

def test ():
	toaster = ToastNotifier()
	toaster.show_toast("Hello World!!!",
	                   "Python is 10 seconds awsm!",
	                   icon_path="custom.ico",
	                   duration=10)

	toaster.show_toast("Example two",
	                   "This notification is in it's own thread!",
	                   icon_path=None,
	                   duration=5,
	                   threaded=True)
	# Wait for threaded notification to finish
	while toaster.notification_active(): time.sleep(0.1)


def alert (title, message):
	toaster = ToastNotifier()
	toaster.show_toast(title, message, icon_path=None, duration=4, threaded=True)
