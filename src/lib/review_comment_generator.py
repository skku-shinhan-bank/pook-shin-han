class ReviewCommentGenertator:
  __goodByeMessage = 'SOL 센터 1599-8000(평일 09~18시) 또는, 이메일(developer@shinhan.com)로 연락 주시면 안내 드리겠습니다. SOL 이용에 불편함이 없도록 최선을 다하겠습니다. 감사합니다.'

  @staticmethod
  def generate(issueId):
    common_message = 'issue id: {}\n\n'.format(issueId)
    if issueId == 0:  # 앱 실행
        return common_message + '안녕하세요. 고객님. 앱 실행에 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 1:  # 회원가입
        return common_message + '안녕하세요. 고객님, 로그인에 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 2:  # 금융 서비스
        return common_message + '안녕하세요. 고객님, 금융 서비스에 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 3:  # 기타
        return common_message + '안녕하세요. 고객님, 기타 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 4:  # 앱 외부
        return common_message + '안녕하세요, 앱 외부 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
    return '안녕하세요. 고객님. 문제를 알 수 없습니다.'
    