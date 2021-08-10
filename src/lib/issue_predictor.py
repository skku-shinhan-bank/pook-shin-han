from koelectra_classification import KoElectraClassificationPredictor
import os.path

class IssuePredictor:
    def __init__(self, model_path):
        if os.path.isfile(model_path):
            print("model found")
        
        self.predictor = KoElectraClassificationPredictor(
            num_of_classes=7,
            model_path=model_path,
        )

    def predict(self, review):
        probability_per_class_list = self.predictor.predict(
            data_list=[review],
            max_sequence_length=128,
            batch_size=32,
        )

        probability_per_class = probability_per_class_list[0]

        max_probabillity_class = -1
        max_probability = -99999

        for class_id, probability in enumerate(probability_per_class[0]):
            if probability > max_probability:
                max_probability = probability
                max_probabillity_class = class_id

        return max_probabillity_class, probability_per_class[0]