# python:3.9의 이미지로 부터
FROM python:3.9
# 제작자 및 author 기입
LABEL maintainer="ajtwlswjddnv1102@gmail.com"

# 해당 디렉토리에 있는 모든 하위항목들을 '/app/server`로 복사한다
COPY . /app/server

# image의 directory로 이동하고
WORKDIR /app/server

# 필요한 의존성 file들 설치
RUN pip install -r requirements.txt

RUN export FLASK_ENV=production

# 환경 설정 세팅
# RUN python setup.py install

# For KoBERT
RUN pip install --no-cache-dir torch
RUN pip install gluonnlp pandas tqdm sentencepiece transformers mxnet
RUN pip install ./KoBERT

# container가 구동되면 실행
ENTRYPOINT ["python", "run.py", "False", "0.0.0.0", "5000"]