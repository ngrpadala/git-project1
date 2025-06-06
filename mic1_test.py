import pyaudio

audio = pyaudio.PyAudio()

print("Available Audio Input Devices:")
for i in range(audio.get_device_count()):
    device_info = audio.get_device_info_by_index(i)
    print(f"{i}: {device_info['name']}")

audio.terminate()
