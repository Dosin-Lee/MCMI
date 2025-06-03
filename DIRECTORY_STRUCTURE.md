# 디렉터리 구조

```
MCMI/
├── cv10class.py              # 10폴드 분류 모듈
├── entropy.py                # 엔트로피 계산
├── joint_entropy.py          # 결합 엔트로피 계산
├── mcmi.py                   # MCMI 특징 선택 알고리즘
├── mutual_information.py     # 상호 정보량 계산
├── Feature Selection Package.zip
├── GBMCNA.mat                # 예제 데이터
├── Lung_CNA.mat              # 예제 데이터
├── example/
│   ├── input/                # 예제 입력 파일
│   │   ├── test.vcf          # Beagle로 보간된 VCF
│   │   └── phenotype.tsv     # 형질 정보
│   ├── output/               # 예제 결과
│   │   └── results.txt       # 실행 후 생성되는 파일
│   ├── run_example.py        # 예제 실행 스크립트
│   └── README.md             # 예제 설명
└── README.md
```

`example` 폴더에서 `run_example.py`를 실행하면 `output/results.txt`가 생성됩니다.

