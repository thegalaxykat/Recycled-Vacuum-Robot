from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3('/home/pi/Katstone/sounds/R2D2.mp3')
play (sound)