from datetime import datetime
import requests
import sqlite3

conn = sqlite3.connect('StoreProfile.db')
cursor = conn.cursor()


def get_results():

    Apps = []
    total = 0
    AppApps = ""
    today = datetime.today().strftime('%d-%m-%Y')

    cursor.execute(
        '''SELECT APP, ENTERTAINMENT FROM StoringData WHERE DATE_OPEN = ?''', (today,))
    results = cursor.fetchall()

    for i in results:
        total = total + i[1]
        Apps.append(i[0])

    Apps.remove('Admin')

    cursor.execute('''SELECT MAXEnt FROM StoringData WHERE id = ?''', (1,))
    MAXENT = cursor.fetchone()

    for ele in Apps:
        AppApps += "\n" + ele + "\n"

    if total > MAXENT[0]:
        return f"Your child has exceeded the maximum number of Entertainment Apps allowed for today by {MAXENT[0] - total}. Here is a list of Apps that have been accessed Today: \n {AppApps}"
    else:
        return f"Your child has not exceeded the number of Entertainment Apps allowed for today. Here is a list of Apps that have been accessed: \n {AppApps}"


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox311cf2d405ec43c39e1b32fa07943120/messages",
        auth=("api", "050db543434ed59b0fc3c67121a8faaf-48c092ba-ee0cc0e6"),
        data={"from": "Excited User <mailgun@sandbox311cf2d405ec43c39e1b32fa07943120>",
              "to": ["bar@example.com",     "arjavatripathi5@gmail.com"],
              "subject": "Todays Summary!",
              "text": get_results()})


send_simple_message()
