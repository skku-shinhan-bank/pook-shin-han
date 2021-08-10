class ReviewCommentGenertator:
  __goodByeMessage = 'SOL 센터 1599-8000(평일 09~18시) 또는, 이메일(developer@shinhan.com)로 연락 주시면 안내 드리겠습니다. SOL 이용에 불편함이 없도록 최선을 다하겠습니다. 감사합니다.'

  @staticmethod
  def generate(issueId):
    common_message = 'issue id: {}\n\n'.format(issueId)
    if issueId == 0:  #불편
        return common_message + '안녕하세요. 고객님. 앱 실행 환경에 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 1:  #오류
        return common_message + '안녕하세요. 고객님, 앱 사용 환경에 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 2:  #문의
        return common_message + '안녕하세요. 고객님, 앱 내 서비스에 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 3:  #불만
        return common_message + '안녕하세요. 고객님, 앱 ui ux 에 문제가 있으신가요??' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 4:  #칭찬
        return common_message + '안녕하세요, 기타 문제 인가요??' + ReviewCommentGenertator.__goodByeMessage
    return ''
    