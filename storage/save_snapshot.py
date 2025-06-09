import cv2
import os
import time
import pandas as pd
from utils.config import SNAPSHOT_DIR, LOG_CSV

def save_frame(frame):
    if not os.path.exists(SNAPSHOT_DIR):
        os.makedirs(SNAPSHOT_DIR)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}.jpg"
    path = os.path.join(SNAPSHOT_DIR, filename)
    cv2.imwrite(path, frame)

    df = pd.DataFrame([[timestamp, filename]], columns=["timestamp", "filename"])
    if os.path.exists(LOG_CSV):
        df.to_csv(LOG_CSV, mode='a', header=False, index=False)
    else:
        df.to_csv(LOG_CSV, index=False)

    return path
