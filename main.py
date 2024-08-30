import os
import time
print("Ajit")
st=time.time()
model_path="traffic_best_n.onnx"
output_path="out"
cmd=["deepsparse.yolov8.annotate", "--source", "image/2.jpg", "--model_filepath", str(model_path), "--save_dir", output_path]
cmd = ' '.join(cmd)
os.system(cmd)
ed=time.time()
print(ed-st)


    