from django.shortcuts import redirect, render
import pyautogui
import time

def showform(request):
    return render(request, 'Automation/form.html')

def automate(request):
    buttondata = True
    rounds = 0
    times = int(request.POST.get("rounds",""))
    while rounds<times:
        if request.POST:
            timedata = int((request.POST.get("time", "")))
            time.sleep(timedata)
            pyautogui.typewrite((request.POST.get("text", "")))
            pyautogui.press('enter')
            rounds+=1

    return render(request, 'Automation/working.html')