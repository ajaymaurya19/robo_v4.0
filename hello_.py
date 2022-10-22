from gtts import gTTS
tts = gTTS('Good Morning')
tts.save('good.mp3')
tts = gTTS('I am a Robo from Rizvi College of Engineering.')
tts.save('college.mp3')
tts = gTTS("Hello")
tts.save('hello.mp3')
tts = gTTS("President sir and director Madam.")
tts.save('introd.mp3')
tts = gTTS("we wish you both happy birthday and happy founder's day.")
tts.save('birth.mp3')

