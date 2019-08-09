# Github 사용하기

## Github에 Push / Pull

1. 만약 master로 push한 기록이 있다면 pull 받아오기 (자신의 브랜치에서)

```
git checkout [Branch Name]
git pull origin master
```

2. 자신의 브랜치에서 작업

3. 자신의 브랜치에 Push

```
git push origin [Branch Name]
```

4. master에서 자신의 브랜치 Merge

```
git checkout master
git pull origin [Branch Name]
git push origin master
```

> origin은 원격 저장소를 의미

---

## 파이썬 라이브러리를 설치한 경우

requirements.txt 파일에 설치한 라이브러리를 모두 저장

> 라이브러리를 설치한 경우에는 필수적으로 해줘야 함.

```
pip freeze > requirements.txt
```

requirements.txt 파일에 명시되어있는 라이브러리를 깔 때

> 특정 라이브러리가 없다는 오류가 뜰 때 필수적으로 해줘야 함.

```
pip install -r requirements.txt
```
