DEBUG = True

SECRET_KEY = '^7jcx7^h#b@%a76lr@a2!7xj#@4@5ayuyan9c$y#(_(8l3)_%t'

INSTALLED_APPS = [
    'kagiso_image',

    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'wagtail.wagtaildocs',
    'wagtail.wagtailembeds',
    'wagtail.wagtailforms',
    'wagtail.wagtailimages',
    'wagtail.wagtailredirects',
    'wagtail.wagtailsearch',
    'wagtail.wagtailsites',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

# ROOT_URLCONF = 'auth_backend.urls'

WSGI_APPLICATION = 'kagiso_image.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'kagiso_image',
        'USER': 'postgres',
        'PASSWORD': 'password',
    }
}

# Project specific settings
##
MIN_IMAGE_WIDTH = 350
MIN_IMAGE_HEIGHT = 350
