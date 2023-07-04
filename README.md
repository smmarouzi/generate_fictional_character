# StoryCraft test

## Instructions to setup the project:
`git clone https://github.com/thelucidproject/biomir.git`

`cd biomir`

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

download deeplabv3_xception_tf_dim_ordering_tf_kernels.h5 from https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5 and add it to models/remove_background directory

download inswapper_a28.onnx from https://drive.google.com/file/d/1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF/view and add it to models/face_swapper directory

`python main.py`

## About running main.py
- you might need to press a key to close opened image windows
- please enter a number whenever it is asked in terminal
    - a number between 1 to 13 to choose different customs
    - a number between 1 to 4 to choose different backgrounds
- to run chat, an Openai API key is needed, please enter it whenever it is asked
