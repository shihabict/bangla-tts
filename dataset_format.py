# from TTS.tts.datasets import load_tts_samples
#
#
# # custom formatter implementation
# def formatter(root_path, manifest_file, **kwargs):  # pylint: disable=unused-argument
#     """Assumes each line as ```<filename>|<transcription>```
#     """
#     txt_file = os.path.join(root_path, manifest_file)
#     items = []
#     speaker_name = "my_speaker"
#     with open(txt_file, "r", encoding="utf-8") as ttf:
#         for line in ttf:
#             cols = line.split("|")
#             wav_file = os.path.join(root_path, "wavs", cols[0])
#             text = cols[1]
#             items.append({"text":text, "audio_file":wav_file, "speaker_name":speaker_name, "root_path": root_path})
#     return items
#
# # load training samples
# train_samples, eval_samples = load_tts_samples(dataset_config, eval_split=True, formatter=formatter)
import os
from pathlib import Path
import shutil
import tqdm

target_dir = 'my_dataset/wavs'

os.makedirs(target_dir,exist_ok=True)


def convert_to_wav(input_audio_path, output_dir):

    command = f'ffmpeg -i "{input_audio_path}" -acodec pcm_s16le -ar {22050} -ac 1 -y -nostats -loglevel 0 "{output_dir}"'
    os.system(command)
    # return output_path


def format_tts_data(root_dir):
    wav_files = list(Path(root_dir).rglob('*.wav'))
    for wav_file in tqdm.tqdm(wav_files):
        wav_file = str(wav_file)

        text_file = wav_file.split('.')[0] + '.txt'
        with open(text_file) as text_file:
            text = text_file.read()
            text = text.replace('\n', ' ').strip(' ')

        if len(text) > 1:
            base_name = Path(wav_file).stem+'.wav'
            output_path = os.path.join(target_dir,base_name)
            convert_to_wav(wav_file, output_path)
            # target_wav = Path(wav_file).stem + '.wav'
            with open('my_dataset/metadata.txt', 'a') as file:
                file.write(f"{base_name}|{text}")
                file.write('\n')
        else:
            print(target_dir)


root_dir = '/home/shihab/Projects/experiment/retranscription/talkshow_testset1'
format_tts_data(root_dir)
