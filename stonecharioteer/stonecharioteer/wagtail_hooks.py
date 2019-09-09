from wagtail.core import hooks


@hooks.register('insert_global_admin_css')
def import_fontawesome_stylesheet():
    elem = '<link rel="stylesheet" href="{}/static/vendor/fontawesome-free-5.10.2-web/css/fontawesome.min.css">'.format(
        settings.STATIC_URL
    )
    return format_html(elem)
