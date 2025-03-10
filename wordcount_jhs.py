from collections import Counter
from konlpy.tag import Komoran

# 분석할 텍스트
text = """
시스코와 엔비디아가 기업의 AI 구현을 지원하기 위한 양사 간의 협업을 확대한다. 시스코의 실리콘 원(Silicon One) 기술과 엔비디아의 이더넷 네트워킹 플랫폼을 결합해 기업 데이터센터 전반에 걸쳐 AI 워크로드를 지원할 계획이다.
시스코의 부사장 겸 최고 제품 책임자인 지투 파텔은 블로그 포스트를 통해 “지금까지 AI에 대한 업계의 대화는 대부분 칩, 컴퓨팅 성능, LLM에 집중됐다. 그러나 기업이 AI 워크로드를 도입하면서, 데이터센터와 클라우드 내부, 그 사이에서 컴퓨팅 자원과 데이터를 연결하는 문제는 AI 혁신의 다음 단계가 될 것이다. 이런 의미에서 네트워크는 기업에서 AI를 성공적으로 확장하는 데 핵심이 될 것”이라고 강조했다.
양사는 시스코의 실리콘 원 기술과 엔비디아의 슈퍼NIC를 결합해 엔비디아 스펙트럼-X 이더넷 네트워킹 플랫폼에 통합할 계획이다.
시스코 실리콘 원 프로세서는 높은 네트워크 대역폭과 성능을 지원하는 전용 프로세서로, 단일 칩셋에서 라우팅 또는 스위칭용으로 맞춤화할 수 있어 네트워크 기능마다 서로 다른 프로세서 아키텍처가 필요하지 않다. 실리콘 원 시스템의 핵심은 향상된 이더넷 기능(향상된 흐름 제어, 혼잡 인식 및 회피 기능 등)을 지원하는 것이다.
참고로, 시스코는 최근 복잡한 데이터 처리 작업을 분산하고 AI 및 대규모 워크로드 처리를 위한 스위치를 구현하기 위해 AMD의 내장형 프로그래머블 DPU(Data Processing Unit)을 포함한 실리콘 원 칩을 기반으로 새로운 데이터센터 스위치 제품군을 공개했다.
슈퍼NIC는 이더넷 기반 클라우드에서 하이퍼스케일 AI 워크로드를 가속화하는 엔비디아의 새로운 네트워크 가속기이다. 엔비디아에 따르면, 슈퍼NIC는 GPU 대 GPU 통신을 위한 고속 네트워크 연결 기능을 갖추고 있으며, 컨버지드 이더넷(RoCE) 기술을 통해 RDMA(Remote Direct Memory Access)를 사용해 400Gb/s에 달하는 속도를 제공한다. 엔비디아 스펙트럼-X(Spectrum-X)는 AI 워크로드를 가속화하기 위한 엔비디아의 포괄적인 이더넷 네트워킹 플랫폼이다.
파텔은 “시스코는 엔비디아 스펙트럼 프로세서와 시스코 OS 소프트웨어를 결합한 시스템을 구축해 기업이 데이터센터에서 시스코 네트워킹과 엔비디아 기술을 동시에 표준화할 수 있도록 할 것”이라며, ”기업이 공통의 넥서스 소프트웨어 스택(NX-OS 및 넥서스 대시보드) 하에서 백엔드 연결에 특화된 엔비디아 스펙트럼 프로세서 또는 시스코 실리콘 원을 활용하면, 흥미롭고 새로운 수준의 상호 운용성을 가능해질 것”이라고 설명했다.
또한 시스코와 엔비디아는 혼잡 관리 및 부하 분산과 같은 공통 과제를 해결하기 위해 양사 포트폴리오를 아우르는 기술에도 투자해 기업이 AI 배포를 가속화할 수 있도록 지원할 것이라고 말했다.
양사는 또한 시스코 실리콘 원, 하이퍼패브릭, 넥서스, UCS 컴퓨트, 옵틱스 및 기타 시스코 기술을 이용해 엔비디아 스펙트럼-X 기반의 엔비디아 클라우드 파트너(NCP) 및 엔터프라이즈 레퍼런스 아키텍처를 만들고 검증하기 위해 협력할 것이라고 말했다.
이번 발표는 시스코와 엔비디아가 기존의 협력관계를 확대한 것이다. 양사는 데이터센터와 엣지에서 AI와 데이터 집약적 워크로드를 지원하기 위해 협력해 왔는데, 이미 시스코 UCS X-시리즈와 UCS X-시리즈 다이렉트를 포함한 시스코의 UCS 랙과 블레이드 서버에 엔비디아의 텐서 코어 GPU를 탑재했다. 통합 솔루션에는 프로덕션에 바로 사용할 수 있는 AI를 위한 사전 훈련된 모델과 개발 도구를 갖춘 엔비디아 AI 엔터프라이즈 소프트웨어가 포함되어 있다.
이달 초, 시스코는 엔터프라이즈 데이터센터 환경을 위한 UCS C845A M8 랙 서버를 출하했다고 밝혔다. 8U 랙 서버는 엔비디아의 HGX 플랫폼을 기반으로 구축됐었으며, LLM 훈련, 모델 미세 조정, 대규모 모델 추론, RAG 등의 AI 작업에 필요한 가속 컴퓨팅 기능을 제공한다.
또한 고객이 필요에 따라 데이터센터나 엣지 환경에 연결할 수 있는 사전 구성, 검증, 최적화된 인프라 패키지인 AI 팟(AI Pod)도 공동 개발하고 있다. AI 팟은 시스코의 검증된 설계 원칙을 기반으로 하며, 엔비디아 AI 엔터프라이즈가 포함되어 있다.
시스코는 시스코 넥서스 하이퍼패브릭 AI 클러스터라고 불리는 턴키 AI 패키지도 제공한다. 400G 및 800G 이더넷 패브릭을 지원하는 스파인 앤 리프 구현을 위한 시스코 6000 시리즈 스위치 형태의 통합 네트워킹 패키지이다. 이 패키지에는 블루필드-3 DPU와 슈퍼NIC를 갖춘 엔비디아 GPU, AI 팟 구축을 위한 레퍼런스 디자인, 통합 스토리지, 데이터베이스, AI 워크로드를 위해 구축된 데이터 기반 기능 엔진을 위한 광범위한 데이터 플랫폼이 포함되어 있다.
"""

# Komoran 라이브러리를 사용하여 명사 추출
komoran = Komoran()
nouns = komoran.nouns(text)

# 추출된 명사들을 공백으로 결합하여 문자열 생성
nouns_text = " ".join(nouns)

# 명사의 빈도를 계산하여 Counter 객체 생성
word_counts = Counter(nouns)


def 글자수추출기(text):
    """
    텍스트에서 명사를 추출하고, 각 명사의 출현 빈도를 계산하여 출력하는 함수
    """
    # Komoran 라이브러리를 사용하여 명사 추출
    komoran = Komoran()
    nouns = komoran.nouns(text)
    
    # 명사의 빈도를 저장할 딕셔너리 초기화
    count_dict = {}
    
    # 추출된 명사 리스트를 순회하며 빈도 계산
    for n in nouns:
        if n not in count_dict.keys():
            count_dict[n] = 1
        else:
            count_dict[n] += 1
    
    # 빈도 기준으로 명사 딕셔너리 정렬
    sort_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
    
    # 결과 출력
    print(sort_dict)

# 비교 출력
print(word_counts)
글자수추출기(text)
