import csv
import webbrowser
import time
import pyautogui

with open("C:/Users/Brandt/Documents/query_results.csv") as file:
    reader = csv.DictReader(file)

    count = 0
    for row in reader:
        if int(row['Date'][len(row['Date'])-4:]) < 1987 or int(row['Date'][len(row['Date'])-4:]) % 5 != 0:
            continue

        webbrowser.open(row['href'], new=0, autoraise=True)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'w')
        count += 1
