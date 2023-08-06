# Wagtail CKEditor plugin

This is a [Wagtail](https://wagtail.io/) plugin, which allows [CKEditor](http://ckeditor.com/) to be used as an internal editor
instead of hallo.js or draftail.

## Requirments

Wagtail 2+
Django 3+

## How to install

Include `wagtail_ckeditor` in your `INSTALLED_APPS`.

Ensure that you have this entry in your `settings.py` file.

    WAGTAILADMIN_RICH_TEXT_EDITORS = {
        'default': {
            'WIDGET': 'wagtail_ckeditor.widgets.CKEditor'
        }
    }

There are several options you can add to your `settings.py` file.

```
WAGTAIL_CKEDITOR_CONFIG = {
    "language": "ru",
}
```

Inspired by:

---

Richard Mitchell (<https://github.com/isotoma/wagtailtinymce.git>)
mastnym (<https://github.com/mastnym/wagtail-ckeditor>)
