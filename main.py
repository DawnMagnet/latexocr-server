from PIL import Image
from pix2tex.cli import LatexOCR
from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
import uvicorn

model = LatexOCR()
app = FastAPI()


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # 接收上传的图片文件
    img = await file.read()
    img = cv2.imdecode(np.frombuffer(img, dtype=np.uint8), cv2.IMREAD_COLOR)
    pil_img = Image.fromarray(img)

    # 在实际应用中，这里会进行图片处理或预测逻辑
    # 但根据你的要求，我们简单地跳过这个步骤

    return model(pil_img)


# 运行服务器
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_config="uvicorn_config.json")
