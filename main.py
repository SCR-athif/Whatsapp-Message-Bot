import time
import pyautogui

# Read numbers from text file
with open(r"C:\Users\mohammed.athif\Desktop\numbers.txt", "r") as file:
    numbers = [line.strip() for line in file if line.strip()]

# Message to send (already copied to clipboard before running)
# If you want, we can also auto-copy it per number
# message = "Hello from Python!"
time.sleep(5)	
for number in numbers:
    # Step 1: Open new chat (Ctrl + N)
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(0.8)

    # Step 2: Type the phone number
    pyautogui.write(number)
    time.sleep(0.8)

    # Step 3: Tab twice to reach 'Next' / confirm
    pyautogui.press('tab', presses=2, interval=0.5)
    time.sleep(0.8)

    # Step 4: Press Enter to open chat
    pyautogui.press('enter')
    time.sleep(1)

    # Step 5: Paste the message (Ctrl + V)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    # Step 6: Press Enter to send
    pyautogui.press('enter')

    # Step 7: Wait 2 seconds before next number
    time.sleep(2)
