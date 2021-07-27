![header](https://capsule-render.vercel.app/api?type=rounded&color=auto&height=300&section=header&text=Notion%20to%20Tistory&desc=노션으로%20티스토리%20블로그에%20포스트하기&fontSize=40)

# Overview
- 파이썬 + Flask를 사용해 만든 웹페이지로, 노션에 작성한 페이지를 [티스토리 Open API](https://tistory.github.io/document-tistory-apis/)를 활용하여 티스토리 블로그에 간편하게 포스트합니다. 
- 추후 다른 티스토리 API들도 추가할 예정입니다. 
<br />

## Contents
- [Requirements](https://github.com/miyeon-ha/notion-to-tistory#Requirements)
- [How to Use](https://github.com/miyeon-ha/notion-to-tistory#How-to-Use)
    - [노션 페이지를 Html 파일로 준비하기](https://github.com/miyeon-ha/notion-to-tistory#%EB%85%B8%EC%85%98-%ED%8E%98%EC%9D%B4%EC%A7%80%EB%A5%BC-html-%ED%8C%8C%EC%9D%BC%EB%A1%9C-%EC%A4%80%EB%B9%84%ED%95%98%EA%B8%B0)
    - [티스토리 API 사용을 위한 앱 등록하기](https://github.com/miyeon-ha/notion-to-tistory#%ED%8B%B0%EC%8A%A4%ED%86%A0%EB%A6%AC-api-%EC%82%AC%EC%9A%A9%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%95%B1-%EB%93%B1%EB%A1%9D%ED%95%98%EA%B8%B0)
    - [웹페이지 실행하기](https://github.com/miyeon-ha/notion-to-tistory#%EC%9B%B9%ED%8E%98%EC%9D%B4%EC%A7%80-%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0)
    - [내 티스토리 블로그 권한 부여하기](https://github.com/miyeon-ha/notion-to-tistory#%EB%82%B4-%ED%8B%B0%EC%8A%A4%ED%86%A0%EB%A6%AC-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EA%B6%8C%ED%95%9C-%EB%B6%80%EC%97%AC%ED%95%98%EA%B8%B0)
    - [포스트 정보 입력하기](https://github.com/miyeon-ha/notion-to-tistory#%ED%8F%AC%EC%8A%A4%ED%8A%B8-%EC%A0%95%EB%B3%B4-%EC%9E%85%EB%A0%A5%ED%95%98%EA%B8%B0)
- [Tips](https://github.com/miyeon-ha/notion-to-tistory#Tips)
- [Limitations](https://github.com/miyeon-ha/notion-to-tistory#Limitations)
<br />
<br />

# Requirements
- 이 프로젝트는 파이썬3를 기반으로 만들어졌습니다. 웹사이트를 구동하려면 파이썬3가 설치되어 있어야 합니다. 
- [파이썬 공식 홈페이지](https://www.python.org/downloads/)에서 설치할 수 있습니다.
<br />
<br />

# How to Use
## 노션 페이지를 Html 파일로 준비하기
### 1. 노션 화면에서 우측 상단에 있는 메뉴 버튼을 클릭합니다. 
![노션 페이지 Export 하기](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Notion_1.png)
<br />

### 2. Export 버튼을 클릭한 후, Export format을 HTML로 선택하고 다운로드합니다.
![노션 페이지 Export 설정](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Notion_2.png)
- Include Subpages는 Off 상태여야 합니다.
- 일부 블록은 html로 변환 시 티스토리 블로그에서 정상적으로 보이지 않을 수 있습니다. [Limitations > 노션 페이지 작성 시 주의사항](https://github.com/miyeon-ha/notion-to-tistory#%EB%85%B8%EC%85%98-%ED%8E%98%EC%9D%B4%EC%A7%80-%EC%9E%91%EC%84%B1-%EC%8B%9C-%EC%A0%9C%ED%95%9C%EC%82%AC%ED%95%AD)을 참고해주세요.
- 다운로드될 파일은 zip 파일입니다. 압축 해제하면 HTML 파일이 나옵니다.
<br />

## 티스토리 API 사용을 위한 앱 등록하기
### 1. [티스토리 오픈 API 관리자 페이지 > 앱 등록 화면](https://www.tistory.com/guide/api/manage/register)에 접속합니다. 
![앱 등록 화면](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Tistory_1.png)
<br />

### 2. 앱 정보를 입력한 후 등록 버튼을 클릭합니다.
![앱 정보 등록 화면](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Tistory_2.png)
- 초록색 상자로 표시된 부분은 스크린샷과 동일하게 설정해주세요. 나머지 정보는 적당한 값으로 입력하면 됩니다. 
<br />

## 웹페이지 실행하기
### 1. 이 저장소를 관리하기 편한 곳에 저장합니다.
- git clone 명령어를 사용하거나, Github 화면상에서 Code > Download Zip 버튼을 사용합니다. 
```
git clone https://github.com/miyeon-ha/notion-to-tistory.git
```
<br />

### 2. 다운로드한 notion-to-tistory 폴더에 tistory_auth.json 파일을 생성합니다. 
![폴더 해제하고 auth 파일 생성](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Web_1.png)
<br />

- __tistory_auth.json은 아래와 같은 형식이어야 합니다.__
```json
{
    "client_id": "내가 만든 앱 설정 화면에 있는 App ID",
    "client_secret": "내가 만든 앱 설정 화면에 있는 Secret Key",
    "redirect_uri": "http://localhost:5000"
}
```
<br />

- client_id와 client_secret은 [티스토리 오픈 API 앱 관리](https://www.tistory.com/guide/api/manage/register) 화면에서 찾을 수 있습니다.
<br />

![앱 설정 화면 진입](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Web_2.png)

![앱 아이디와 Secret key 위치](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Web_3.png)

<br />

### 3. 동일 폴더에서 python3 tistory_serve.py를 입력하면 웹페이지가 실행됩니다. 
![Flask web server 실행](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Web_4.png)
- 실행 전에 아래 패키지가 설치되어 있어야 합니다. 
    - [Flask](https://pypi.org/project/Flask/)
    - [Flask-Caching](https://pypi.org/project/Flask-Caching/)
    - [requests](https://pypi.org/project/requests/)
- flask 웹 서버 실행 후, [http://localhost:5000](http://localhost:5000)에 접속합니다.
<br />

## 내 티스토리 블로그 권한 부여하기
### 화면에 나타난 티스토리 블로그 권한 부여하기 버튼을 클릭합니다. 
![내 블로그 접근 권한 부여하기](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Web_5.png)
<br />

### 티스토리 로그인 화면이 나타나면 티스토리 계정으로 로그인한 후, 허가하기 버튼을 클릭합니다.
![티스토리 계정으로 로그인하기](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Web_6.png)
<br />

### 권한을 허가하면 사용할 수 있는 티스토리 API 목록이 나타납니다.
![티스토리 API 목록이 나타난 화면](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Web_7.png)
> 현재는 글 쓰기 API만 사용 가능합니다.
<br />

## 포스트 정보 입력하기
### 글 쓰기를 진행할 블로그를 선택합니다.
![블로그 선택하기](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Web_8.png)
<br />

### 업로드할 글의 정보를 입력합니다.
![글 쓰기 정보 입력하기](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Web_9.png)
- 글 내용 : 찾아보기 버튼 클릭 후, [노션 페이지를 Html 파일로 준비하기](https://github.com/miyeon-ha/notion-to-tistory#%EB%85%B8%EC%85%98-%ED%8E%98%EC%9D%B4%EC%A7%80%EB%A5%BC-html-%ED%8C%8C%EC%9D%BC%EB%A1%9C-%EC%A4%80%EB%B9%84%ED%95%98%EA%B8%B0)에서 준비했던 html 파일을 업로드합니다. 
- 글 제목 : 블로그에 올라갈 글 제목을 입력해주세요. 노션 페이지의 제목은 HTML 파일로 변환하는 과정에서 삭제됩니다. 
- 카테고리 : 글 쓰기 화면으로 넘어갈 때, 선택된 블로그에 생성된 카테고리 목록을 불러옵니다. 글을 등록할 카테고리를 선택해주세요. 
- 태그 : 비어 있으면 태그 없이 글을 등록합니다. 태그를 여러개 추가하려면 콤마로 구분해 입력해주세요. 
- 글 공개 여부 : `비밀번호 입력시 공개`를 선택하면 비밀번호 입력창이 나타납니다.
<br />

### 글 쓰기 실행 버튼을 클릭합니다. 
![글 쓰기 실행 버튼 클릭](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Web_10.png)
- 글 쓰기가 정상적으로 완료됐다면 화면 아래 쪽에 업로드된 블로그 글 링크가 나타납니다. 
- 이 상태에서 새로 고침을 하지 않고 새 정보를 입력한 후 다시 `글 쓰기 실행` 버튼을 클릭하면 연속해서 블로그 글을 업로드할 수 있습니다. 
![글 쓰기 완료](https://shelling22.dothome.co.kr/img/notion-to-tistory/Howto_Web_11.png)
<br />
<br />

## 티스토리 블로그 CSS 편집하기

티스토리 블로그 관리 페이지 > 스킨 편집 > CSS에서 [tistory_blog.css](./static/css/tistory_blog.css)에 있는 CSS 내용을 붙여넣기해주세요.  

> 블로그에 포스트하는 시점에서 CSS가 미리 적용된 상태로 업로드할 수 있지만, 글을 한 번이라도 수정하게 되면 업로드 시점에 적용된 CSS는 사라지고 티스토리 블로그 스킨에서 사용하는 CSS만 적용됩니다. 노션 글을 그대로 업로드했을 때 UI가 깔끔하게 보이지 않는 것을 수정하려면 블로그 스킨 CSS에 적용하는 편이 안정적입니다.


# Limitations
여러 테스트용 노션 페이지를 사용해본 결과, 일부 블록, 그리고 특정한 블록의 배열은 티스토리 블로그에서 예쁘게 보이지 않습니다. 노션에서 글을 작성하기 전에 아래 제한사항을 확인해주세요.
<br />

## 이미지는 Upload file이 아니라 Embed Link를 사용해야 합니다. 
HTML 형식의 데이터를 텍스트화해서 티스토리 블로그에 업로드하는 방식이기 때문에 이미지를 파일로 업로드하기 어렵습니다. 노션 페이지 작성 단계부터 이미지를 Embed Link를 사용하면 이미지가 노션에서 사용된 url을 그대로 티스토리 블로그에서도 사용합니다. 
<br />

## 평행하게 위치된 블록 모음은 한 줄로 바뀌어서 업로드됩니다. 
![평행한 블록이 노션에 표시된 상태](https://shelling22.dothome.co.kr/img/notion-to-tistory/Limit_01.png)
- 노션에서 블록을 평행하게 배치한 상태에서 HTML 변환 후, 티스토리 블로그에 업로드하면 좌우 폭이 줄어든 블록이 세로로 나열된 형태로 업로드됩니다. 
<br />

![평행한 블록이 티스토리 블로그에 표시된 상태](https://shelling22.dothome.co.kr/img/notion-to-tistory/Limit_02.png)
<br />

> 그 외 티스토리 블로그에서 깨져 보이는 현상이 있다면 [Issues](https://github.com/miyeon-ha/notion-to-tistory/issues)에 제보해주세요.

