from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS(교차-출처 리소스 공유) 설정 
origins = [
    "http://127.0.0.1:5173",
]

'''
# allow_origin_regex 설정
regex = [
    "http://.*\\.example\\.org",
]
'''

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # 교차-출처 요청을 보낼 수 있는 출처의 리스트
                                # 모든 출처 허용을 위해 ['*'] 사용 가능
    # allow_origin_regex=regex  # 교차-출처 요청을 보낼 수 있는 출처를 정규표현식 문자열로 나타냄
                                # allow_origins 와 allow_origins_regex 중 하나만 사용해야 함
    allow_methods=["*"],        # 교차-출처 요청을 허용하는 HTTP 메소드의 리스트. 
                                # 기본값은 ['GET']
                                # ['*'] 을 통해 모든 표준 메소드들 허용 가능
    allow_headers=["*"],        # 교차-출처를 지원하는 HTTP 요청 헤더의 리스트. 
                                # 기본값은 []
                                # ['*'] 을 통해 모든 헤더들을 허용 가능
                                # Accept, Accept-Language, Content-Language 그리고 Content-Type 헤더는 CORS 요청시 언제나 허용
    allow_credentials=True,     # 교차-출처 요청시 쿠키 지원 여부 설정
                                # 기본값은 Fasle
                                # 해당 항목을 허용할 경우 allow_origins 는 ['*'] 로 설정 불가 -> 출처를 반드시 특정해야 함
    # max_age=3600              # 브라우저가 CORS 응답을 캐시에 저장하는 최대 시간을 초 단위로 설정
                                # 기본값은 600
)

from domain.user import user_router

app.include_router(user_router.router, tags=["User"])