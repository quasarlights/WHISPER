
import whisper

video= "I will find YouI will Kill You Taken Movie best scene ever  liam neeson.mp4"

model = whisper.load_model("base")
result = model.transcribe(video, fp16=False)
print(result["text"])


