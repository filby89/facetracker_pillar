from ultralytics import YOLO


class FaceTracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)


    def track(self, frame, verbose=False, persist=True):
        results = self.model.track(source=frame, line_width=2, verbose=verbose, persist=persist, save=True)
        return results
    
