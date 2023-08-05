django-gallery_ds
==========

django-gallery_ds is a Django app to use for demiansoft. 

Quick start
------------

1. Add "gallery" to your INSTALLED_APPS setting like this
```python
INSTALLED_APPS = [
    ...
    'gallery',
]
```

2. 코드를 넣고자 하는 위치에 다음을 추가 한다.
```html
{% load gallery_tags %}
{% make_gallery %}
```

* context example
```python
context = {
    "theme": "mentor_ds",
    "gallery": {
            "title": "Gallery",
            "desc": "Photos from Our Clinic",
        }
}
```

* static - img/gallery/ 폴더내에 동일한 크기(800x600, 세로사진은 안됨)의 jpg 파일을 인식하여 보여줌
* 지원 템플릿 - bethany_ds, medilab_ds