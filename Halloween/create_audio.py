from gtts import gTTS
import playsound

intro = ['Hello, would you like some candy?']

final = ['Have a SPOOKTACULAR Halloween!','May your candy last you at least til Christmas!','Hope your Halloween is full of more treats than tricks!','Have a boooo-tiful Halloween!',
        'Happy Halloween to the cutest pumpkin in the patch.','Happy Halloween and enjoy that sugar rush tonight!']

for i in range(len(intro)):
    msg = intro[i]
    tts = gTTS(text=msg, lang='en')
    path = './audio_files/intro/' + str(i) + '.mp3'
    tts.save(path)
    playsound.playsound(path, True)

for i in range(len(final)):
    msg = final[i]
    tts = gTTS(text=msg, lang='en')
    path = './audio_files/final_greetings/' + str(i) + '.mp3'
    tts.save(path)
    playsound.playsound(path, True)