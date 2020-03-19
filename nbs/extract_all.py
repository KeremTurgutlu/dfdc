from tqdm import tqdm
from dfdc.core.download_unzip import *
from dfdc.face_detection.download_detect_crop_save import *

for part in tqdm((download_parts[18:])): download_detect_crop_save(part)