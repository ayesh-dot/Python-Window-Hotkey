# Python-Window-Hotkey
Lightweight python tool for window switching hotkeys.


# QuickFocus Utility

A lightning-fast, ultra-lightweight Python automation utility designed to fix focus-loss and mouse-lock issues for remote desktop sessions and background application windows.

## Why QuickFocus?
Unlike heavy macro software or resource-hungry background tools, QuickFocus is built to be completely invisible to your system performance:
* **Negligible Resource Footprint:** Runs on a pure Python event listener loop with virtually zero CPU usage while idling in the background.
* **Minimal Memory Usage:** Consumes only a tiny fraction of RAM (typically just standard base Python interpreter overhead).
* **Zero Bloat:** No heavy graphical user interfaces, no background analytics, and no unnecessary dependencies—just pure, direct OS-level window management.

## Features
* **Instant Refocusing:** Press a single hotkey to bring your target window to the foreground and center-click to lock your controls back in.
* **Configurable:** Easily adjust your target window title and hotkey via a clean `config.json` file without touching the core source code.
* **Safety First:** Built with `pyautogui` fail-safes so you always retain full manual control.

## Prerequisites

Make sure you have Python installed, then install the required lightweight dependencies:

```bash
pip install keyboard pygetwindow pyautogui
```

## Configuration

The first time you run the script, it will automatically generate a `config.json` file. You can customize your target application and hotkey at any time:

```json
{
  "target_window": "Chrome Remote Desktop",
  "hotkey": "tab"
}
```

## Usage

Run the script from your terminal (note: administrator/root privileges are required for global hotkey monitoring):

```bash
python main.py
```
