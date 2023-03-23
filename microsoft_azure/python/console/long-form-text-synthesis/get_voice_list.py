import azure.cognitiveservices.speech as speechsdk

# config
speech_config = speechsdk.SpeechConfig(subscription='f687802b8dbc49d58661816c360e8d43', region="eastus")

# Create your client
client = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Request the list of available voices
voices_result = client.get_voices_async().get()

# iterate through the list of voices
for v in voices_result.voices:
    if v.locale == 'en-US':
        print(v.gender, v.short_name, v.locale)



        # en-US-JennyNeural
        # en-US-JennyNeural