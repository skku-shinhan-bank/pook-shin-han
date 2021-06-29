from flask import Flask, request, jsonify
from src.lib.review_comment_generator import ReviewCommentGenertator
from src.lib.issue_predictor import IssuePredictor

issuePredictor = IssuePredictor()

#Flask 객체 인스턴스 생성
app = Flask(__name__)


@app.route('/', methods=('GET', ))
def index():
  return 'SKKU Team Shinhan Bank'

@app.route('/reviews', methods=('POST', ))
def review():
  review = request.json['review']

  issueClass = issuePredictor.predict(review)

  return jsonify({
    'review': review,
    'comment': ReviewCommentGenertator.generate(issueClass),
  })
