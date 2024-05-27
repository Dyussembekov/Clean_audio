from pydub import AudioSegment
import noisereduce as nr
import numpy as np

audio = AudioSegment.from_file(r"C:\Users\User\Desktop\Sound\audio.wav")

# Преобразование аудио в массив numpy
samples = np.array(audio.get_array_of_samples())

# Определение частоты дискретизации
frame_rate = audio.frame_rate

reduced_noise = nr.reduce_noise(y=samples, sr=frame_rate)

# Преобразование массива обратно в аудио
clean_audio = AudioSegment(
    reduced_noise.tobytes(), 
    frame_rate=frame_rate,
    sample_width=audio.sample_width, 
    channels=audio.channels
)

# Сохранение очищенного аудио
clean_audio.export("cleaned_audio.wav", format="wav")