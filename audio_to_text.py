from pydub import AudioSegment
from pydub.utils import make_chunks
import os
import speech_recognition as sr
from tkinter.filedialog import *
from pydub.silence import split_on_silence

r = sr.Recognizer()

def transcribe_audio(path):
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        text=r.recognize_google(audio_listened)
    return text
    
def get_large_audio_transcription_on_silence(path):
    sound = AudioSegment.from_file(path)
    chunks = split_on_silence(sound, min_silence_len = 500, silence_thresh = sound.dBFS-14, keep_silence=500,)

    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        try:
            text = transcribe_audio(chunk_filename)
        except sr.UnknownValueError as e:
            print("Error:", str(e))
        else:
            text = f"{text.capitalize()}. "
            #print(chunk_filename, ":", text)
            whole_text += text
    # return the text for all chunks detected
    return whole_text


txt = open("audio_text3.txt","w+")
txt.write(get_large_audio_transcription_on_silence('sample.wav'))



    