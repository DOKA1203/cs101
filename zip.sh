#!/bin/bash

STUDENT_ID="12263723"
NAME="JEESEUNGHYEON"

if [ -z "$1" ]; then
    echo "사용법: $0 <week번호>"
    echo "예시: $0 9"
    exit 1
fi

WEEK="week$1"

if [ ! -d "$WEEK" ]; then
    echo "오류: '$WEEK' 폴더가 존재하지 않습니다."
    exit 1
fi

PY_FILES=("$WEEK"/*.py)
if [ ! -e "${PY_FILES[0]}" ]; then
    echo "오류: '$WEEK' 폴더에 파이썬 파일이 없습니다."
    exit 1
fi

TMPDIR=$(mktemp -d)
ZIP_NAME="${WEEK}_${STUDENT_ID}_${NAME}.zip"

for src in "$WEEK"/*.py; do
    base=$(basename "$src" .py)
    cp "$src" "$TMPDIR/${base}_${STUDENT_ID}_${NAME}.py"
done

(cd "$TMPDIR" && zip -j "$OLDPWD/$ZIP_NAME" ./*.py)

rm -rf "$TMPDIR"

echo "생성 완료: $ZIP_NAME"
