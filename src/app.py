from flask import Flask, request, jsonify
from src.lib.review_comment_generator import ReviewCommentGenertator
from src.lib.issue_predictor import IssuePredictor
from flask_cors import CORS

class App:
  def __init__(self):
    issuePredictor = IssuePredictor('model/kobert_issue_classification_test.pt')

    #Flask 객체 인스턴스 생성
    app = Flask(__name__)

    CORS(app)

    @app.route('/', methods=('GET', ))
    def index():
      return 'SKKU Team Shinhan Bank'

    @app.route('/reviews', methods=('POST', ))
    def review():
      review = request.json['review']

      issueClass = issuePredictor.predict(review)

      return jsonify({
        'status': 200,
        'body': {
          'review': review,
          'comment': ReviewCommentGenertator.generate(issueClass),
        }
      })
    self.app = app
  
  def run(self, host, port, debug):
    self.app.run(host=host, port=port, debug= debug)
