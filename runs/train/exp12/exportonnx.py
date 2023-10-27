import onnx
from onnx import shape_inference
path = "E:/yolov5-6.0/runs/train/exp12/weights/best.onnx" #the path of your onnx model
onnx.save(onnx.shape_inference.infer_shapes(onnx.load(path)), path)
