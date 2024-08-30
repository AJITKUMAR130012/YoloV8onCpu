import os
import time
print("Ajit")
st=time.time()
model_path="traffic_best_n.onnx"
output_path="out"
cmd=["deepsparse.yolov8.annotate", "--source", "1.mp4", "--model_filepath", str(model_path), "--save_dir", output_path]
cmd = ' '.join(cmd)
os.system(cmd)
ed=time.time()
print(ed-st)


    