import pyaudio
import wave
import threading
import copy

class Sound:
	def __init__(self, path, chunk=1024):
		self.path = path
		self.chunk = chunk

	def _play(self):
		wav = wave.open(self.path, "rb")
		audio = pyaudio.PyAudio()
		stream = audio.open(
			format=audio.get_format_from_width(wav.getsampwidth()),
			channels=wav.getnchannels(),
			rate=wav.getframerate(),
			output=True
		)

		data = wav.readframes(self.chunk)

		while data:
			stream.write(data)
			data = wav.readframes(self.chunk)

		stream.stop_stream()
		stream.close()

	def play(self):
		thread = threading.Thread(target=self._play)
		thread.start()


# wx = Sound("../click.wav")
# wx.play()