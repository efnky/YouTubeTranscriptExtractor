
# Python code to convert video to audio
import moviepy.editor as mp
from tkinter.filedialog import *
 
clip=askopenfilename()

# Insert Local Video File Path 
clip = mp.VideoFileClip(clip)
 
# Insert Local Audio File Path
clip.audio.write_audiofile('baba.mp3')
print("Completed!!")