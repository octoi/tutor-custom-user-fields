from django.utils.translation import gettext_lazy as _

# Add custom fields to USER_PROFILE_EXTENDED_FIELDS
USER_PROFILE_EXTENDED_FIELDS = [
    "address",
    "place",
    "pincode"
]

# Define the fields in REGISTRATION_EXTRA_FIELDS
REGISTRATION_EXTRA_FIELDS = {
    "address": {
        "required": False,
        "label": _("Address"),
        "placeholder": _("Enter your address"),
        "name": "address",
        "exposed": True
    },
    "place": {
        "required": False,
        "label": _("Place"),
        "placeholder": _("Enter your city/town"),
        "name": "place",
        "exposed": True
    },
    "pincode": {
        "required": False,
        "label": _("Pincode"),
        "placeholder": _("Enter your pincode"),
        "name": "pincode",
        "exposed": True
    }
}

# Update ACCOUNT_SETTINGS_EXTRA_FIELDS to show fields in account settings
ACCOUNT_SETTINGS_EXTRA_FIELDS = {
    "address": {
        "label": _("Address"),
        "field_type": "text",
        "required": False
    },
    "place": {
        "label": _("Place"),
        "field_type": "text",
        "required": False
    },
    "pincode": {
        "label": _("Pincode"),
        "field_type": "text",
        "required": False
    }
}

# API Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

# Update the UserProfile serializer
ACCOUNT_VISIBILITY_CONFIGURATION['custom_fields'] = {
    'admin': ['address', 'place', 'pincode'],
    'staff': ['address', 'place', 'pincode'],
    'self': ['address', 'place', 'pincode'],
}

REGISTRATION_API_EXTRA_FIELDS = REGISTRATION_EXTRA_FIELDS
