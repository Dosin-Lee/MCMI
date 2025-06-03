# 예제 사용 방법

이 폴더에는 Python 버전의 MCMI 알고리즘을 실행해 볼 수 있는 작은 데이터와 스크립트가 들어 있습니다.

## 파일 구성

- `input/test.vcf` : Beagle로 보간된 예시 VCF 파일
- `input/phenotype.tsv` : VCF와 일치하는 형질 정보
- `run_example.py` : 데이터를 불러와 `mcmi`를 실행하는 스크립트
- `output/results.txt` : 스크립트 실행 결과가 저장되는 파일

## 실행 방법

저장소 루트에서 Python 의존성 설치 후 스크립트를 실행합니다.

```bash
pip install numpy scikit-learn
cd example
python3 run_example.py
```

실행이 끝나면 선택된 feature 인덱스가 `output/results.txt`에 기록됩니다.

