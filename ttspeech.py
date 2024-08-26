from TTS.api import TTS

# TTS with on the fly voice conversion
api = TTS("tts_models/en/ljspeech/tacotron2-DDC")
api.tts_with_vc_to_file(
    "This. is. test. API",
    speaker_wav="target/trainer_voice.mp3",
    file_path="output6.mp3"
)