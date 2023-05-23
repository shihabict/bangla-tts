import os


def convert_to_wav(self, input_audio_path, output_dir):
    input_file_name_with_ext = os.path.basename(input_audio_path)
    input_file_name_wo_ext = "".join(input_file_name_with_ext.split(".")[:-1])
    output_path = os.path.join(output_dir, input_file_name_wo_ext + ".wav")

    command = f'ffmpeg -i "{input_audio_path}" -acodec pcm_s16le -ar {22050} -ac 1 -y -nostats -loglevel 0 "{input_audio_path}"'
    os.system(command)
    return output_path

