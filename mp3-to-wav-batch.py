# Keep this file with MP3's to be converted and output will be available in same directory.

import glob
import os
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor

def speechToText(name):
    base_filename, file_extension = os.path.splitext(name)
    txt_filename = f"{base_filename}.txt"
    src = base_filename+".mp3"
    filename = base_filename+".wav"
	# download ffmpeg from: https://ffmpeg.zeranoe.com/builds/win64/static/
	# Add path to bin in Environment Variables under "path"
    subprocess.call(['ffmpeg', '-i', src, filename])

def main(filenames):
    with ThreadPoolExecutor() as executor:
        executor.map(speechToText, filenames)

if __name__ == "__main__":
    filenames = glob.glob("*.mp3")
    print(filenames)
    start_time = time.time()
    main(filenames)
    duration = time.time() - start_time
    print(f"Converted {len(filenames)} in {duration} seconds")
