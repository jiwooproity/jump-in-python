## Django란?

파이썬으로 개발된 오픈 소스 웹 애플리케이션 프레임워크이다.

웹 애플리케이션을 빠르게 개발하고 유지 보수하기 쉽도록 설계되었고,

데이터베이스 모델링, URL 라우팅, 템플릿 엔진, 폼 처리, 보안, 사용자 인증 및 권한 부여와 다양한 기능을 제공한다.

## Django의 아키텍처

Django는 MVC 아키텍처 패턴에서 영감을 받아 MVT 아키텍처를 사용하도록 설계되었다.

기존 Model, View, Controller와 동일한 의미로 Model View Template으로 이루어져 있다.

![image](https://github.com/jiwooproity/jump-in-python/assets/58384366/52dd453c-cb06-4e93-a351-9d90d28e91b9)


## MVT ( Model, View, Controller )

`Model` 은 서버에서의 데이터베이스 작업이라고 생각하면 된다고 한다.

`View` 는 브라우저 상에서 사용자에게 보여지는 페이지를 의미합니다.

`Controller` 는 `Model` 에다가 일을 시키는 작업을 진행한다.

사용자는 뷰를 통해 컨트롤러를 실행하고 `Model` 에 필요한 작업을 요청한다.

## MVC와 MVT의 차이점

차이점은 이름이 다르다는 점 말고는 의미가 동일한 형태의 아키텍처이다.

`Model → Model`

`View → Template`

`Controller → View`

위와 같이 의미 매칭이 가능하다.

## Django 환경 구성하기

```jsx
pip install django
```

django를 사용하기 위해선 파이썬의 pip 패키지 매니저를 통해 django를 설치해야 한다.

```jsx
1. django-admin startproject mysite // mysite라는 이름을 가진 프로젝트 폴더 생성
"or"
2. django-admin startproject config . // 현재 폴더에 프로젝트 설정 파일을 구성
```

django-admin으로 설치된 django-admin.py를 실행하여 django 프로젝트를 구성한다.

프로젝트를 바로 생성하고 싶다면 1번 커맨드, 설정 파일만 현재 폴더에 구성하고 싶다면 2번을 선택한다.

```jsx
python3 manage.py makemigrations
// -> model의 변경사항에 따라 새로운 migration파일을 생성
python3 manage.py migrate
// -> 생성된 migration 파일을 DB에 적용

--
python3 manage.py runserver // 기본 포트 8000
```
