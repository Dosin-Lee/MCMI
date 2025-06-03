# MCMI 특징 선택 알고리즘

이 저장소는 Maximum Conditional Mutual Information(MCMI) 방법을 이용한 특징 선택 코드를 제공합니다. MATLAB 버전과 Python 버전이 포함되어 있으며, 예제 데이터와 실행 스크립트도 제공합니다.

## 시작하기

### 필요 환경
- 원본 구현을 위한 MATLAB
- Python 3
- `numpy`, `scikit-learn` 패키지

### 주요 파일
- `mcmi.m` : MATLAB 구현
- `mcmi.py` : Python 구현
- `Feature Selection Package` 디렉터리: MATLAB에서 필요한 함수 모음
  - `load_fspackage.m`
  - `Entropy.m` / `entropy.py`
  - `JointEntropy.m` / `joint_entropy.py`
  - `MutualInformation.m` / `mutual_information.py`
- 샘플 데이터
  - `GBMCNA.mat`
  - `Lung_CNA.mat`

## 사용 방법

1. 저장소 클론
   ```bash
   git clone https://github.com/yourusername/mcmi-feature-selection.git
   cd mcmi-feature-selection
   ```
2. MATLAB 패키지 로드
   ```matlab
   run('Feature Selection Package/load_fspackage.m')
   ```
3. MCMI 실행
   - MATLAB: `run('mcmi.m')`
   - Python: `python mcmi.py`

## 예제

`example` 폴더에는 Beagle로 보간된 작은 VCF 파일과 형질 정보가 들어 있습니다. 아래와 같이 실행하면 선택된 feature 인덱스가 `output/results.txt`에 저장됩니다.

```bash
pip install numpy scikit-learn
cd example
python3 run_example.py
```

## 함수 설명
- `entropy.py`: 엔트로피 계산
- `joint_entropy.py`: 결합 엔트로피 계산
- `mutual_information.py`: 상호 정보량 계산

추가 내용은 각 스크립트의 주석을 참고하세요.

---

저장소 관리자: Hongtao Shi  
문의: sht@qau.edu.cn

