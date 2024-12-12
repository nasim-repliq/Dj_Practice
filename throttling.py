# Throttling

'''The default throttling policy may be set globally, using the DEFAULT_THROTTLE_CLASSES and DEFAULT_THROTTLE_RATES settings. For examples.'''

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/days',
        'user': '1000/days'
    }
}


# AnonRateThrottle
''' IP address generate a unique key for user
restrict the rate of requests from unknown source'''
# DEFAULT_THROTTLE_RATES['anon']


# UserRateThrottle
''' User ID a unique key for user'''
# DEFAULT_THROTTLE_RATES['user']


# ScopedRateThrottle
'''Restrict access to specific parts of the API. throttle_scope property. user id or ip address'''



# Setting up throttling in GLOBAL

# settings
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES':{
        'anon': '2/day',
        'user': '5/hour',
    }
}

#views
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]




## Specific Throttle?

#throttling:
from rest_framework.throttling import UserRateThrottle

class JackRateThrottle(UserRateThrottle):
    scope = 'jack'

# settings
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES':{
        'anon': '2/day',
        'user': '5/hour',
        'jack': '3/minute'
    }
}

# views
throttle_class = [AnonRateThrottle, JackRateThrottle]

