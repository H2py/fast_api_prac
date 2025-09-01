import whisperx
from whisperx.utils import get_writer

import torch
import os

whisper_model = "large-v3" 
device = "cuda" if torch.cuda.is_available() else "cpu"
subtitle_format = "srt"

model = whisperx.load_model(whisper_model, device=device)
file_paths = [
    os.path.realpath(os.path.join("test", file))
    for file in os.listdir("test")
]

for file in file_paths:
    result = model.transcribe(file)
    subtitle_writer = get_writer(subtitle_format, ".")
    subtitle_writer(result, file, {"max_line_width": None, "max_line_count": None, "highlight_words": False}, )

