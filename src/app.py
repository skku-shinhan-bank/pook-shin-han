from flask import Flask, request, jsonify
from src.lib.review_comment_generator import ReviewCommentGenertator
from src.lib.issue_predictor import IssuePredictor
from flask_cors import CORS
from datetime import datetime

class App:
  def __init__(self):
    issue_predictor = IssuePredictor('model/koelectra_classification_model_v2.pth')
    comment_generator = ReviewCommentGenertator('model/kobart_generator_model_v1.pth')

    #Flask 객체 인스턴스 생성
    app = Flask(__name__)

    CORS(app)

    @app.route('/', methods=('GET', ))
    def index_route():
      return 'SKKU Team Shinhan Bank'

    @app.route('/reviews', methods=('POST', ))
    def review_route():
      review = request.json['review']

      issue_id, total_issue_info = issue_predictor.predict(review)
      now = datetime.now()
      write_time = now.strftime("%Y/%m/%d %H:%M")

      return jsonify({
        'status': 200,
        'body': {
          'review': review,
          'comment': comment_generator.generate(review, issue_id),
          'total_issue_info': total_issue_info,
          'write_time': write_time,
          'issue_id': issue_id,
        }
      })
    self.app = app
  
  def run(self, host, port, debug):
    self.app.run(host=host, port=port, debug= debug)
