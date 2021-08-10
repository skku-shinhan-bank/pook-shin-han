from flask import Flask, request, jsonify
from src.lib.review_comment_generator import ReviewCommentGenertator
from src.lib.issue_predictor import IssuePredictor
from flask_cors import CORS
from datetime import datetime

class App:
  def __init__(self):
    issuePredictor = IssuePredictor('model/koelectra_classification_model_v2.pth')

    #Flask 객체 인스턴스 생성
    app = Flask(__name__)

    CORS(app)

    @app.route('/', methods=('GET', ))
    def index_route():
      return 'SKKU Team Shinhan Bank'

    @app.route('/reviews', methods=('POST', ))
    def review_route():
      review = request.json['review']

      issueId, total_issue_info = issuePredictor.predict(review)
      now = datetime.now()
      write_time = now.strftime("%Y/%m/%d %H:%M")

      return jsonify({
        'status': 200,
        'body': {
          'review': review,
          'comment': ReviewCommentGenertator.generate(issueId),
          'total_issue_info': total_issue_info,
          'write_time': write_time,
        }
      })
    self.app = app
  
  def run(self, host, port, debug):
    self.app.run(host=host, port=port, debug= debug)
