from kobart_generation import KoBARTCommentGenerator
import easydict
import os.path

class ReviewCommentGenertator:
    def __init__(self, model_path):
        if os.path.isfile(model_path):
            print("model found")
        
        args = easydict.EasyDict({
            'model_path': model_path,
            "max_seq_len": 256
        })

        self.comment_generator = KoBARTCommentGenerator(args)
        

    def generate(self, review, issue):
        return self.comment_generator.print_comment(review,issue)
        

# class ReviewCommentGenertator:
#   __goodByeMessage = 'SOL 센터 1599-8000(평일 09~18시) 또는, 이메일(developer@shinhan.com)로 연락 주시면 안내 드리겠습니다. SOL 이용에 불편함이 없도록 최선을 다하겠습니다. 감사합니다.'

#   @staticmethod
#   def generate(issueId):
#     common_message = ''
#     if issueId == 0:  # 앱 실행
#         return common_message + '[앱 실행 기능] 안녕하세요. 고객님. 앱 실행에 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
#     elif issueId == 1:  # 로그인
#         return common_message + '[로그인 기능] 안녕하세요. 고객님, 로그인에 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
#     elif issueId == 2:  # 회원가입
#         return common_message + '[회원가입 기능] 안녕하세요. 고객님, 회원가입에 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
#     elif issueId == 3:  # 금융 서비스
#         return common_message + '[금융 서비스 기능] 안녕하세요. 고객님, 금융 서비스에 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
#     elif issueId == 4:  # 기타
#         return common_message + '[기타 기능] 안녕하세요, 기타 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
#     elif issueId == 5:  # 엡 외부 기능
#         return common_message + '[앱 외부 기능] 안녕하세요, 앱 외부 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
#     return '[기능 없음] 안녕하세요. 고객님. 문제를 알 수 없습니다.'
    