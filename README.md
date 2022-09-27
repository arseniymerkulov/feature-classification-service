# Feature classification service

Service extracts features from images and stores it in feature dataset for classification purposes.

### Dependencies
- python 3.9
- tensorflow 2.10.0
- tensorflow-hub 0.12.0
- flask 2.2.2
- numpy 1.23.3
- opencv-python 4.6.0.66
- requests 2.28.1

### Deploy
1. Execute ```run flask``` in project directory
2. For running scripts that represent service functionality, execute ```python tests/*.py```

### Feature extractor 
Model is taken from tensorflow hub, url is set in the settings. For now, model is efficient-net-lite0, output dimension is 1280.

### Feature classification 
Suppose we are given an input vector V that we want to classify. For every feature vector U from dataset:
1. Calculates difference (U-V)
2. Calculates squared euclidean norm of the difference

Label with minimal norm is chosen as response.