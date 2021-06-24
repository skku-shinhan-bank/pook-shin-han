class ReviewCommentGenertator:
  __goodByeMessage = 'SOL 센터 1599-8000(평일 09~18시) 또는, 이메일(developer@shinhan.com)로 연락 주시면 안내 드리겠습니다. SOL 이용에 불편함이 없도록 최선을 다하겠습니다. 감사합니다.'

  @staticmethod
  def generate(issueId):
    if issueId == 0:  #불편
        return '안녕하세요. 고객님, 이용에 불편을 드리게 되어 죄송합니다. 만약 진행에 어려움이 있으실 경우, ' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 1:  #오류
        return '안녕하세요. 고객님, 우선 앱 회원가입과 로그인 진행이 원활하지 않아 서비스 이용에 불편 드리게 되어 죄송합니다. 고객님 문제를 바로 해결해 드리고 싶지만, 조금 더 자세한 정보가 필요합니다. ' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 2:  #문의
        return '안녕하세요. 신한은행 SOL입니다. 먼저 쏠을 이용해주셔서 감사합니다. 소중한 의견 진심으로 감사드리며, SOL 페이 위젯은 고객님의 의견을 적극 반영하여 조속히 편리한 서비스로 찾아뵙도록 하겠습니다. 만약 진행에 어려움이 있으실 경우, ' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 3:  #불만
        return '안녕하세요. 고객님, 신한은행 SOL입니다. 고객님, 소중한 시간을 내어 저희 신한SOL을 사용해 주셨는데, 불편을 드려 진심으로 사과 드립니다. 고객님께 항상 최고의 서비스를 제공하려 노력하고 있지만, 아직 고객님 마음에 들기에는 많이 부족한 것 같습니다. 번거로우시겠지만 어떤 부분이 불편하셨는지 조금 더 상세하게 말씀을 해주시면, 고객님이 만족할 수 있는 편리한 금융서비스를 제공할 수 있도록 발전 하겠습니다. 고객님께 불편을 드려 다시 한 번 진심으로 죄송합니다. 항상 고객님께 안전하고 편리한 금융서비스를 제공하기 위해 최선을 다하는 SOL이 되겠습니다. 만약 진행에 어려움이 있으실 경우, ' + ReviewCommentGenertator.__goodByeMessage
    elif issueId == 4:  #칭찬
        return '안녕하세요, 신한은행 SOL입니다. 고객님의 좋은 소식을 함께 듣고 함께 행복할 수 있어서 너무 좋습니다. 앞으로도 이렇게 좋은 일만 고객님께 있으셨으면 좋겠습니다. 앞으로도 좋은 일만 가득하길 바랍니다. 감사합니다.'
    return ''