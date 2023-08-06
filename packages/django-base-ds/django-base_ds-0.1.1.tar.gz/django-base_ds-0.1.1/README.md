django-base_ds
==========

django-base_ds is a Django app to use for demiansoft. 

Quick start
------------

1. Add "base" to your INSTALLED_APPS setting like this
```python
INSTALLED_APPS = [
    ...
    'base',
]
```

2. 코드를 넣고자 하는 위치에 다음을 추가 한다.
```html
{% load base_tags %}

{% make_seo %}
{% make_favicons %}
<!-- 폰트 링크를 인자로 전달한다 -->
{% make_fonts font_link %}
{% make_vendor_css %}
{% make_vendor_js %}
{% make_analytics %}

```

* context example
```python
components = [
    ...,
    ['analytics', True, None, None],
]
context = {
    "theme": "mentor_ds",
    "seo": {
        "company_name": "MyEnglish",
        "url": "myenglishkr.com",
        "small_title": "1:1 Speaking Practice",
        "desc": "강남구 서초동 교대 반포 법조타운 위치 내인생치과의 홈페이지, 삼성서울병원 구강외과 전문의 진료",
        "keywords": "내인생치과, 반포대로치과, 교대교정치과, 반포치과, 서초치과, 서초동치과, 교대역치과 "
    },
    'analytics': {
        'google_id': "G-351NZ2S4F9",
        'naver_id': "feadf9e1b55868"
    },
    "font_link": "https://fonts.googleapis.com/css2?family=Gugi&family=Jua&family=Nanum+Pen+Script&family=Noto+Sans+KR:wght@100;300;400;500;700;900&family=Noto+Serif+KR:wght@200;300;400;500;600;700;900&display=swap"
}
```

* 템플릿을 추가할 때는 base_tags.py에 make_up_vendor_css(), make_up_vendor_js() 함수에 추가한다. 
