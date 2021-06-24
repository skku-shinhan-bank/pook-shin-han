from flask import Flask
from src.lib.review_comment_generator import ReviewCommentGenertator

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/', methods=('GET', ))
def index():
  return 'SKKU Team Shinhan Bank'

@app.route('/reviews', methods=('POST', ))
def review():
  return ReviewCommentGenertator.generate(0)
