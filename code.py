import time
from plyer import notification
times= float(input("Enter time interval for notification in seconds: "))
titles = input("enter title of notification: ")
text = input("Enter your text want to show on notification: ")

for i in range (0,5):
  time.sleep (times)
  notification.notify (title = (titles), message = (text), timeout =3)
