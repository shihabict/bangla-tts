# from TTS.api import TTS
#
# # List available 🐸TTS models and choose the first one
# model_name = TTS.list_models()[0]
# # print(0)
# # Init TTS
# tts = TTS(model_name)
# # Run TTS
# # ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
# # Text to speech with a numpy output
# wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
# # Text to speech to a file
# tts.tts_to_file(text="Hello world!", speaker=tts.speakers[0], language=tts.languages[0], file_path="output.wav")

import glob, os
# output_path = "output_path"
# ckpts = sorted([f for f in glob.glob(output_path+"/*/*.pth")])
# configs = sorted([f for f in glob.glob(output_path+"/*/*.json")])
# print(0)
test_ckpt = 'output_path/run-May-13-2023_03+59PM-0000000/speakers.pth'
test_config = 'output_path/run-May-13-2023_03+59PM-0000000/config.json'
os.system(f'tts --text "পানিস্মেন্ট এনাউন্স করেছে ওকে ভাই" \
      --model_path {test_ckpt} \
      --config_path {test_config} \
      --out_path out.wav')