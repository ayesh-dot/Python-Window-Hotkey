import json
import os
import keyboard
import pygetwindow as gw
import pyautogui

pyautogui.FAILSAFE = True

config_file = "config.json"
default_config = {"target_window": "Chrome Remote Desktop", "hotkey": "tab"}

if not os.path.exists(config_file):
  with open(config_file, "w") as f:
    json.dump(default_config, f, indent=4)

with open(config_file, "r") as f:
    config = json.load(f)

target_window = config.get("target_window", "Chrome Remote Desktop")
hotkey_choice = config.get("hotkey", "tab")


def focus_target():
  matches = gw.getWindowsWithTitle(target_window)
  if matches:
    window = matches[0]
    if window.isMinimized:
      window.restore()
    window.activate()
    screen_width, screen_height = pyautogui.size()
    pyautogui.click(screen_width / 2, screen_height / 2)
    print("Refocused successfully!")
  else:
    print("Target window not found!")


keyboard.add_hotkey(hotkey_choice, focus_target)

print(
    f"Active! Press {hotkey_choice} to focus '{target_window}' (Loaded via"
    " config.json)"
)
keyboard.wait()