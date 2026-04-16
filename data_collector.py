import cv2
import mss
import numpy as np
import keyboard
import time
import os
import uuid

output_folder = "dataset_raw"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print("Programma avviato!")
print("1. Posiziona la finestra del gioco in alto a sinistra.")
print("2. Premi 'S' per salvare uno screenshot.")
print("3. Premi 'Q' per uscire.")

monitor_area = {"top": 0, "left": 0, "width": 1000, "height": 800}

with mss.mss() as sct:
    while True:
        screenshot = sct.grab(monitor_area)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        
        cv2.imshow("Anteprima - Premi 'S' per salvare", img)
        
        if keyboard.is_pressed('s'):
            filename = f"{output_folder}/{uuid.uuid4()}.jpg"
            cv2.imwrite(filename, img)
            print(f"Salvata: {filename}")
            time.sleep(0.5) 
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
