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
### 노션 화면에서 우측 상단에 있는 메뉴 버튼을 클릭합니다. 
![노션 페이지 Export 하기](https://lh3.googleusercontent.com/s0HqYzN5tblk06rJPEOoYEED9q7OvRqFFxyLLCScbDRHLFXzo3pTDcNPi5sz1rjCus3reAXsA1btR2iiL4XogCJ6AEV2vG0xs0MZwZrymsNrUDKlob97SHU6u3n2O_YvqsNSwGPrjxU)
<br />

### Export 버튼을 클릭한 후, Export format을 HTML로 선택하고 다운로드합니다.
![노션 페이지 Export 설정](https://lh3.googleusercontent.com/OLgMaw8J9KpdmjepBlD-h5AXsH_fJpdGPtGqVaPwO4VXvMbJF_xGCCQ8ZTDZppRmp496ysUGkfpeFPkclPM1ddTTECb_0B592lSiYFIyZ_hZwbpuYUxgyhck6yw-lHZ12aDWItNkq_U)
- Include Subpages는 Off 상태여야 합니다.
- 일부 블록은 html로 변환 시 티스토리 블로그에서 정상적으로 보이지 않을 수 있습니다. [Limitations > 노션 페이지 작성 시 주의사항](https://github.com/miyeon-ha/notion-to-tistory#%EB%85%B8%EC%85%98-%ED%8E%98%EC%9D%B4%EC%A7%80-%EC%9E%91%EC%84%B1-%EC%8B%9C-%EC%A0%9C%ED%95%9C%EC%82%AC%ED%95%AD)을 참고해주세요.
- 다운로드될 파일은 zip 파일입니다. 압축 해제하면 HTML 파일이 나옵니다.
<br />

## 티스토리 API 사용을 위한 앱 등록하기
### [티스토리 오픈 API 관리자 페이지 > 앱 등록 화면](https://www.tistory.com/guide/api/manage/register)에 접속합니다. 
![앱 등록 화면](https://lh3.googleusercontent.com/vswGd7rc39u8Tev_oNt3qFl4_W7cPP9s0mfZPcKSRz2XKeX99QrYTZhyPy1kXvttXXqp0rDjNvevxLywE5Z63khHZcMUhe6DBoPASfTD8m2oNDrJ3py4901B7VpSxwbYfMvWW5bMdhk)
<br />

### 앱 정보를 입력한 후 등록 버튼을 클릭합니다.
![앱 정보 등록 화면](https://lh3.googleusercontent.com/QQkj3LrN1EzedJ68nEsEQ0snLSAQnl3sCmoTKzFZh0v1vWuddN2sdqDRQL-5STaLQnz1LkvnZAG8jHYq1d16gdFlD7dLsm4PZRL_b0malONx5J78UTE4PzE7_OGift2ih6qiPc70qrY)
- 초록색 상자로 표시된 부분은 스크린샷과 동일하게 설정해주세요. 나머지 정보는 적당한 값으로 입력하면 됩니다. 
<br />

## 웹페이지 실행하기
### 이 저장소를 관리하기 편한 곳에 저장합니다.
- git clone 명령어를 사용하거나, Github 화면상에서 Code > Download Zip 버튼을 사용합니다. 
```
git clone https://github.com/miyeon-ha/notion-to-tistory.git
```
<br />

### 다운로드한 notion-to-tistory 폴더에 tistory_auth.json 파일을 생성합니다. 
![폴더 해제하고 auth 파일 생성](https://lh3.googleusercontent.com/cApcWn76TZNkBY023Vp1-xxc9vTYarOKrgIC6sbfJX28XgXNpNnI9RavIiA7XQSKbDUpVWQwH6eyXw9Cggm9g33S6zgcZr3f9iN6-LlVvuxUIfQ_NDL0YFG2LNvoczOkEUOBuHg2iEU)
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
![앱 설정 화면 진입](https://lh3.googleusercontent.com/hvtbFZ1Aq4hofQ8uCY5ZAQMbY5wpLzmlGnYnAg0w2e4RD7SPnYSFzVvhWLXBdey9yc1YB10v07dhh47RiAPoTJks41mnokdxvmFH0lLUerxqn6q2gKoyFqL59FXnFZWbJIWbD2XpAjA)
![앱 아이디와 Secret key 위치](https://lh3.googleusercontent.com/Gg24-MI0IDTqOzs2ZVCSqBRkI2CHKCMKtbdrXDTyd6rsS4ud3wBkwonsBtGuNL_IB4gszDSTv-pIiJdUOCcSZUjNaMC0hilR1JRG3vvraiLhJAYO0nMTgotB6CwlB8LiucyXwSCnWHQ)
<br />

### `pip install -r requirements.txt`를 입력해서 필요한 패키지들을 설치합니다.
> virtualenv나, pipenv와 같은 개발 환경을 사용하시는걸 추천합니다.
<br />

### 동일 폴더에서 python3 tistory_serve.py를 입력하면 웹페이지가 실행됩니다. 
![Flask web server 실행](https://lh3.googleusercontent.com/4YNmMjRu58i7WF-qwj4Y0sICzJcGaD9lzF5jOxlOcoDWXlByiHAVFBI9NnQwrHWjLZTvntAwDf3-gVJWnuWfd65-BfBB08_yXJ5riOzZbpoOKvol2HSbPwyk_AIVxUguAd4RtYrb_aA)
- flask 웹 서버 실행 후, [http://localhost:5000](http://localhost:5000)에 접속합니다.
<br />

## 내 티스토리 블로그 권한 부여하기
### 화면에 나타난 티스토리 블로그 권한 부여하기 버튼을 클릭합니다. 
![내 블로그 접근 권한 부여하기](https://lh3.googleusercontent.com/pc7zf63nF_1gbpoeq-I1EAsJjnI2bySpvoaH8bwwu9i1Hrz2yRGGzitAT5uw7TTWmKbj4HKj64wyg9eV0lFCagBzEr3yW4qEXRRU1pCdaKqpSQTsdNuRjdlqYx0SkUWo7CGr58RfOkw)
<br />

### 티스토리 로그인 화면이 나타나면 티스토리 계정으로 로그인한 후, 허가하기 버튼을 클릭합니다.
![티스토리 계정으로 로그인하기](https://lh3.googleusercontent.com/Izeol2ZFs4hkfFMMaXDlhjC9B2dNu-wBMXGrwWkyg8OaB-bu-sdWbyO6EjP1CmG4Ep311sKq3EY1Jr28eBRdJV6FBWrpYoEtUJg_wsGZdTD-RPDq2h2W7m5aDOH2-Xcm6RNGAk4KsYY)
<br />

### 권한을 허가하면 사용할 수 있는 티스토리 API 목록이 나타납니다.
![티스토리 API 목록이 나타난 화면](https://lh3.googleusercontent.com/xSaWyZvm0ULA8pbM2LW6Q-X5ENJi8s6jpnukQERIDMhf5U_KxDAbdMIHci4dH5LtQldcnd-W21rliA9s165H4I8otUoi-f1m4udaY32f7cRfiFtIybXq3ghHJWwiL2dQBhLWgqy0EVQ)
> 현재는 글 쓰기 API만 사용 가능합니다.
<br />

## 포스트 정보 입력하기
### 글 쓰기를 진행할 블로그를 선택합니다.
![블로그 선택하기](https://lh3.googleusercontent.com/L7NcB8XAmwj2PqzK06_DZKadXtH-K6kSdvoI-qQ-xzhjo9sKU95eqsHISuwi-fQuxfV2Lwmt6b45mpPCOAL__DYHD4qcQizPL63wza9LjUN9VQzYJkUzT9NUtbQ6j3OZrZUQcfERt7g)
<br />

### 업로드할 글의 정보를 입력합니다.
![글 쓰기 정보 입력하기](https://lh3.googleusercontent.com/0_9ZbvUl1_xKFMTj31H-pY9_MyDUIP0ZbtXlaeo0S9kXmw_OwtoIcz_Wkcp3EgwjYs7fudpB3Ns8ecfIMVVo_RE5jzy0WtfZldejyZ92tKzn_zWgoB8RkwuJKPLx-s_3zxIAKceTq1A)
- 글 내용 : 찾아보기 버튼 클릭 후, [노션 페이지를 Html 파일로 준비하기]()에서 준비했던 html 파일을 업로드합니다. 
- 글 제목 : 블로그에 올라갈 글 제목을 입력해주세요. 노션 페이지의 제목은 HTML 파일로 변환하는 과정에서 삭제됩니다. 
- 카테고리 : 글 쓰기 화면으로 넘어갈 때, 선택된 블로그에 생성된 카테고리 목록을 불러옵니다. 글을 등록할 카테고리를 선택해주세요. 
- 태그 : 비어 있으면 태그 없이 글을 등록합니다. 태그를 여러개 추가하려면 콤마로 구분해 입력해주세요. 
- 글 공개 여부 : `비밀번호 입력시 공개`를 선택하면 비밀번호 입력창이 나타납니다.

<br />
__글 쓰기에 필요한 정보를 모두 입력한 경우의 예시 : __
![](https://lh3.googleusercontent.com/_4wmJXLel_4M_Fx57hCek6EHnBLmSuDy-qydPQAWt5GQMXuB2NvMwV-cl4iXBc_FhEiJzZn9_Q-5sKHPj-nkbjn8MLNgtNX2wseW0YUQwhRnurzk9oBRW-ltVQB76xgqTgi5j-YCfGs)
<br />

### 글 쓰기 실행 버튼을 클릭합니다. 
![글 쓰기 완료](https://lh3.googleusercontent.com/rDS3ReIR_VqizmkGwrtt7IuMSJvDse48se8u58Q-z9dVFjD_ZuwAGF5GLJUa9n3UKddJiVN3MFNBGUEIwEl8AIz9eAX8s_wDPc3EgkHHzXJSXufHyqWR1sNfbk5dFxO1414IbXQo_Ws)
- 글 쓰기가 정상적으로 완료됐다면 화면 아래 쪽에 업로드된 블로그 글 링크가 나타납니다. 
- 이 상태에서 새로 고침을 하지 않고 새 정보를 입력한 후 다시 `글 쓰기 실행` 버튼을 클릭하면 연속해서 블로그 글을 업로드할 수 있습니다. 

<br />
<br />

# Tips
## 샘플 페이지로 테스트하기
사용중인 티스토리 블로그 스킨에 따라 블로그 스킨의 HTML/CSS와 충돌하면서 포스트 내용이 깨져보이는 현상이 있을 수 있습니다. 본격적으로 내가 작성한 노션 페이지를 업로드하기 전에, [notion-to-tistory/Notion/sample.html](./Notion/sample.html) 파일을 사용해서 블로그에 포스트해보길 추천드립니다. 
> 문서가 깨져보인다면, 아래 [문서 스타일 변경]()에 설명된대로 HTML 파일에 적용될 CSS를 조정해주세요.
<br />

## 문서 스타일 변경
노션에서 Export한 HTML 파일을 그대로 티스토리 API로 포스트 등록하면 블로그 화면 전체가 깨지는 현상이 발생합니다. 그래서 HTML 파일에서 `body` 부분만 사용하고, 가독성이 높아지도록 CSS를 앞부분에 추가하는 방식으로 HTML을 변환하여 티스토리 블로그에 포스트합니다. 이 단계에서 사용되는 CSS는 [notion-to-tistory/Notion/style.html](./Notion/style.html)에서 보실 수 있습니다. `<head></head>`안의 내용을 편하신대로 수정하여 사용할 수 있습니다. 

<br />
<br />

# Limitations
여러 테스트용 노션 페이지를 사용해본 결과, 일부 블록, 그리고 특정한 블록의 배열은 티스토리 블로그에서 예쁘게 보이지 않습니다. 노션에서 글을 작성하기 전에 아래 제한사항을 확인해주세요.
<br />

## 이미지는 Upload file이 아니라 Embed Link를 사용해야 합니다. 
HTML 형식의 데이터를 텍스트화해서 티스토리 블로그에 업로드하는 방식이기 때문에 이미지를 파일로 업로드하기 어렵습니다. 노션 페이지 작성 단계부터 이미지를 Embed Link를 사용하면 이미지가 노션에서 사용된 url을 그대로 티스토리 블로그에서도 사용합니다. 
<br />

## 평행하게 위치된 블록 모음은 한 줄로 바뀌어서 업로드됩니다. 
![평행한 블록이 노션에 표시된 상태](https://lh3.googleusercontent.com/RJ_ngPx8J59SQDuvxC0f66bKxpcUC2XbK3elf0NfQQfcFjn7bUggxVFe5aVpXfWmMrGJwLePcFEY7mg4LrjbKQJc1dvciQH72hZ2xAqvOOXkzvOQdzzFmvqR5ApoEt0ujFUknxxFicA)
- 노션에서 블록을 평행하게 배치한 상태에서 HTML 변환 후, 티스토리 블로그에 업로드하면 좌우 폭이 줄어든 블록이 세로로 나열된 형태로 업로드됩니다. 
<br />

![평행한 블록이 티스토리 블로그에 표시된 상태](https://lh3.googleusercontent.com/Hb7dkgjZq1V2xksIohU4UkYGWtGSFhrPo7rsj7k3DBO0Qy0RXPAFVE8ijx_66VtA0RVeLvRyP9qbLZZd9XmIerXh8uh6G6XoiB2-aWTH5ueMS17WrfBTARO8bogOze8nyec9bd6CEyE)
<br />

> 그 외 티스토리 블로그에서 깨져 보이는 현상이 있다면 [Issues](https://github.com/miyeon-ha/notion-to-tistory/issues)에 제보해주세요.

