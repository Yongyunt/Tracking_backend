from .models import User,Status,Personnel_information,request_position,Criterion
from rest_framework import serializers

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'id',
                   'name'

        ]
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [ 'id',
                   'name'
        ]

class Personnel_informationserializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel_information
        fields = [ 'id',
                'fristname',
                'Lastname',
                'Phone_number',
                'Email',
                'Status',
                'Criterion',
                'Gender',
                'Degree_Certificate',
                'test_date',
                'Startdate',
                'Date_you_can_request_position'
        ]

class request_positionserializer(serializers.ModelSerializer):
    class Meta:
        model = request_position
        fields = [ 'id',
                   'Assessment_date',
                   'NameResearchwork',
                   'Research_base',
                   'Date',
                   'Research_level',
                   'Theresult_of_theoperation',
                   'Criterion',
                   'Status'

        ]

class Criterionserializer(serializers.ModelSerializer):
    class Meta:
        model = Criterion
        fields = [ 'id',
                   'NameResearch',
                   'NameResearchbase',
                   'date',
                   'Research_level',
                   'book'

        ]


