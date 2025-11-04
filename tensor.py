import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="best_float32.tflite")
interpreter.allocate_tensors()
print(interpreter.get_output_details())

