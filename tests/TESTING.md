# Commit Info Extractor - Local Testing Guide

## 🧪 테스트 방법

### Python으로 직접 테스트 (Docker 불필요)
```bash
cd /path/to/commit-info-extractor
python3 tests/test_local.py
```

## 🔍 테스트 케이스

### Test 1: 기본 커밋 메시지 추출
- 최근 5개 커밋 메시지 추출
- Pretty 포맷 사용

### Test 2: grep 명령어로 키워드 추출
- 'chore' 키워드 추출
- 정규식 사용

### Test 3: JSON 출력 형식
- 커밋 메시지를 JSON 배열로 출력

### Test 4: CSV 출력 형식
- 커밋 메시지를 CSV 형식으로 출력

### Test 5: 특정 커밋 타입 추출
- 'refactor' 타입 커밋만 추출

## 📝 환경 변수

| 변수 | 설명 | 기본값 |
|------|------|--------|
| INPUT_COMMIT_LIMIT | 추출할 커밋 수 | 10 |
| INPUT_PRETTY | Pretty 포맷 사용 여부 | false |
| INPUT_KEY_VARIABLE | 출력 변수 이름 | ENVIRONMENT |
| INPUT_EXTRACT_COMMAND | 추출 명령어 (grep 등) | - |
| INPUT_FAIL_ON_EMPTY | 빈 결과시 실패 여부 | false |
| INPUT_OUTPUT_FORMAT | 출력 형식 (text/json/csv) | text |

## 🐛 디버깅

문제가 발생하면 다음을 확인:

1. Git 저장소인지 확인: `.git` 디렉토리 존재 여부
2. 커밋 히스토리 확인: `git log`
3. grep 명령어 테스트: `echo "test fix" | grep -oE '\\bfix\\b'`
4. Python 버전 확인: `python3 --version` (3.7 이상 권장)
