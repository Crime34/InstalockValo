import pyautogui
import time
import threading

class Automator:
    def __init__(self):
        # Fail-safe: Drag mouse to corner to abort
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.01 # Minimal pause for speed, but safe enough

    def click_at(self, x, y):
        """Moves to x,y and clicks immediately."""
        pyautogui.click(x, y)

    def lock_in(self, agent_coords, lock_coords):
        """
        Performs the instalock sequence:
        1. Click Agent
        2. Click Lock Button
        """
        if not agent_coords or not lock_coords:
            # print("Missing coordinates!")
            return False

        # Execute as fast as possible
        # We use a separate thread usually to avoid UI freezing, 
        # but pyautogui is blocking anyway.
        # This function should be called from a worker thread if called from GUI.
        
        # Click Agent
        pyautogui.click(agent_coords['x'], agent_coords['y'])
        
        # Slight delay might be needed by the game to register selection
        # But for 'instalock' we try 0 delay first.
        # If it fails, we can add time.sleep(0.01)
        
        # Click Lock
        pyautogui.click(lock_coords['x'], lock_coords['y'])
        
        # Double tap to be sure?
        pyautogui.click(lock_coords['x'], lock_coords['y'])
        
        return True
