from charm_shin_han.kobert_classifier import KoBERTClassifier
from charm_shin_han.kobert_dataset import KoBERTDataset
import torch
from KoBERT.kobert.pytorch_kobert import get_pytorch_kobert_model
from tqdm import tqdm_notebook
from kobert.utils import get_tokenizer
import gluonnlp as nlp

class IssuePredictor:
  def __init__(self, model_path):
    print('1. Get KoBERT model')
    device = torch.device('cpu')
    bert_model, vocab = get_pytorch_kobert_model()
    model = KoBERTClassifier(bert_model, dr_rate=0.5, num_classes=5)
    print('2. Load KoBERT Classifier Model')
    check_point = torch.load(model_path, map_location=device)
    model.load_state_dict(check_point)
    model.eval()

    print('3. Get Tokenizer')
    tokenizer = nlp.data.BERTSPTokenizer(get_tokenizer(), vocab, lower=False)

    self.tokenizer = tokenizer
    self.device = device
    self.model = model
    pass

  def predict(self, review):
    max_len = 64
    num_workers = 1 # thread 수  인듯
    batch_size = 1

    unseen_test = [[review,10]]
    test_set = KoBERTDataset(unseen_test, 0, 1, self.tokenizer, max_len, True, False)
    test_input = torch.utils.data.DataLoader(test_set, batch_size = batch_size, num_workers=num_workers)

    result = None

    for batch_id, (token_ids, valid_length,segment_ids, label) in enumerate(test_input):
      token_ids = token_ids.long().to(self.device)
      segment_ids = segment_ids.long().to(self.device)
      result = self.model(token_ids, valid_length, segment_ids)

    largest = -999999
    issueId = -1
    total_issue_info = []

    for issueIndex, val in enumerate(result[0]):
      value = val.item()
      if largest < val:
        largest = val
        issueId = issueIndex
      total_issue_info.append((issueIndex, value))

    return (issueId, total_issue_info)