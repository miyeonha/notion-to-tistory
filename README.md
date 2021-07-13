![header](https://capsule-render.vercel.app/api?type=rounded&color=auto&height=300&section=header&text=Notion%20to%20Tistory&desc=노션으로%20티스토리%20블로그에%20포스트하기&fontSize=40)


# Overview
- 파이썬 + Flask를 사용해 만든 웹페이지로, 노션에 작성한 페이지를 [티스토리 Open API](https://tistory.github.io/document-tistory-apis/)를 활용하여 티스토리 블로그에 간편하게 포스트합니다. 
- 추후 다른 티스토리 API들도 추가할 예정입니다. 
<br />

# Requirements
- 이 프로젝트는 파이썬3를 기반으로 만들어졌습니다. 웹사이트를 구동하려면 파이썬3가 설치되어 있어야 합니다. 
- [파이썬 공식 홈페이지](https://www.python.org/downloads/)에서 설치할 수 있습니다.
<br />

# How to Use
## 노션 페이지를 Html 파일로 준비하기
### 노션 화면에서 우측 상단에 있는 메뉴 버튼을 클릭합니다. 
![노션 화면에서 우측 상단에 있는 메뉴 버튼을 클릭합니다. ](https://lh3.googleusercontent.com/s0HqYzN5tblk06rJPEOoYEED9q7OvRqFFxyLLCScbDRHLFXzo3pTDcNPi5sz1rjCus3reAXsA1btR2iiL4XogCJ6AEV2vG0xs0MZwZrymsNrUDKlob97SHU6u3n2O_YvqsNSwGPrjxU)

### Export 버튼을 클릭한 후, Export format을 HTML로 선택하고 다운로드합니다.
![]()
- Include Subpages는 Off 상태여야 합니다.
- 일부 블록은 html로 변환 시 티스토리 블로그에서 정상적으로 보이지 않을 수 있습니다. [Limitations > 노션 페이지 작성 시 주의사항]()을 참고해주세요.
- 다운로드된 파일은 zip 파일입니다. 압축 해제하면 HTML 파일이 나옵니다.
<br />

## 티스토리 API 사용을 위한 앱 등록하기
### [티스토리 오픈 API 관리자 페이지 > 앱 등록 화면](https://www.tistory.com/guide/api/manage/register)에 접속합니다. 
![]()

### 앱 정보를 입력한 후 등록 버튼을 클릭합니다.
![]()
{% note %}
Callback이 스크린샷처럼 `http://localhost:5000`으로 설정되어야 합니다.
{% endnote %}




<br />

## 웹페이지 실행하기
1. 이 깃헙 데이터를 관리하기 편한 곳에 저장합니다.
2. 파이썬 실행 환경상에서 notion-to-tistory 폴더로 이동합니다.
3. `tistory_auth.json` 파일을 notion-to-tistory 폴더 바로 아래에 생성합니다. (tistory_serve.py와 동일 위치에 있어야 합니다.)
4. `tistory_auth.json` 파일은 아래와 같은 내용을 담고 있어야 합니다. [티스토리 API 사용을 위한 앱 등록하기]()에서 만들었던 앱 정보에서 앱 ID를 client_id에, 앱 Secret key를 client_secret에 입력합니다. 
```json
tistory_auth.json

{
    "client_id": "",
    "client_secret": "",
    "redirect_uri": "http://localhost:5000"
}
```
<br />

4. `pip install -r requirements.txt`를 입력해서 필요한 패키지들을 설치합니다.
    > virtualenv나, pipenv와 같은 개발 환경을 사용하시는걸 추천합니다.
5. 동일 폴더에서 python3 tistory_serve.py를 입력하면 웹페이지가 실행됩니다. 

## 내 티스토리 블로그 권한 부여하기
1. 화면에 나타난 티스토리 블로그 권한 부여하기 버튼을 클릭합니다. 
2. 티스토리 로그인 화면이 나타나면 글을 업로드할 블로그를 관리하는 계정으로 로그인합니다. 
3. 내 블로그에 접근할 권한을 부여할지 묻는 창이 나타납니다. 
    > 여기서 부여된 권한은 [티스토리 API 사용을 위한 앱 등록하기]()에서 만든 앱에 부여됩니다.
4. 권한을 허가하면 사용할 수 있는 티스토리 API 목록이 나타납니다.
    > 현재는 글 쓰기 API만 사용 가능합니다.
5. 글 쓰기를 진행할 블로그를 선택합니다. 


## 포스트 정보 입력하기
1. [노션 페이지를 Html 파일로 준비하기]()에서 준비했던 html 파일을 업로드합니다. 
2. 글 제목을 입력합니다. 
    > 노션 페이지의 타이틀은 티스토리 블로그 업로드 과정에서 제외되고, 본문만 사용됩니다.
3. 카테고리를 선택합니다. 



# Tips
## 샘플 페이지로 테스트하기

사용중인 티스토리 블로그 스킨에 따라 포스트 내용이 깨져보이는 현상이 있을 수 있습니다. 본격적으로 내가 작성한 노션 페이지를 업로드하기 전에, [notion-to-tistory/Notion/sample.html](./Notion/sample.html) 파일을 사용해서 블로그에 포스트해보길 추천드립니다. 
> 문서가 깨져보인다면, 아래 [문서 스타일 변경]()에 설명된대로 HTML 파일에 적용될 CSS를 조정해주세요.


## 문서 스타일 변경

노션에서 Export한 HTML 파일을 그대로 티스토리 API로 포스트 등록하면 블로그 화면 전체가 깨지는 현상이 발생합니다. 그래서 HTML 파일에서 `body` 부분만 사용하고, 가독성이 높아지도록 CSS를 앞부분에 추가하는 방식으로 HTML을 변환하여 티스토리 블로그에 포스트합니다. 이 단계에서 사용되는 CSS는 [notion-to-tistory/Notion/style.html](./Notion/style.html)에서 보실 수 있습니다. `<head></head>`안의 내용을 편하신대로 수정하여 사용할 수 있습니다. 



# Limitations
## 노션 페이지 작성 시 주의사항

여러 테스트용 노션 페이지를 사용해본 결과, 일부 블록, 그리고 특정한 블록의 배열은 티스토리 블로그에서 예쁘게 보이지 않습니다. 노션에서 글을 작성하기 전에 아래 주의사항을 확인해주세요.

### 이미지는 Upload file이 아니라 Embed Link를 사용해야 합니다. 

### 평행하게 위치된 블록 모음은 한 줄로 바뀌어서 업로드됩니다. 



> 그 외 티스토리 블로그에서 깨져 보이는 현상이 있다면 [Issues](https://github.com/miyeon-ha/notion-to-tistory/issues)에 제보해주세요.

