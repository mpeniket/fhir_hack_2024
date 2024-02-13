import json
transcription = """Hello, could I confirm your full name and date of birth please?
Martha Coles Jones, 13th of the 9th, 98.
Lovely to meet you. What's brought you in today?
I'm feeling quite sad lately. It's February, it's still quite dark, quite early, I think, really affected by the seasons.
And yeah, I just wanted to see if you could help me.
Okay, we'll do our best to get to the bottom of that. How are your energy levels?
Quite low. I'm quite tired all the time. I've not got much energy to do things.
Okay, I'm really sorry to say that.
Have you had any thoughts of self-harm or suicide?
No.
No, I haven't. Some days are quite hard. I feel quite low, but I don't think I've reached that point yet.
Do you feel safe at home where you are? Do you feel anyone?
Yes, I do feel safe. Yes, I do.
And now just a few yes or no questions. Any headaches?
Yes. Tell me more about that.
Yes, I have headaches probably two or three times a week.
I went to the opticians, they said it could be the screen time.
Oh, okay. Why are you on your laptop a lot? What'd you do?
I have a desk job after that's my job.
We're nine to five.
That's great. Thank you for coming in.
I'll point you to some talking therapies and we can look into prescribing some medications that might help."""

# {  "resourceType": "Patient",  "name": [    {      "use": "official",      "family": "Coles Jones",      "given": [        "Martha"      ]    }  ],  "birthDate": "1998-09-13",  "communication": [    {      "language": {        "coding": [          {            "system": "http://terminology.hl7.org/CodeSystem/languages",            "code": "en-US",            "display": "English"          }        ]      }    }  ]}
res = json.dumps(
{
    "resourceType": "ProcedureRequest",
    "status": "draft",
    "intent": "order",
    "subject": {
        "reference": "Patient/1234"
    },
    "code": {
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "433932003",
                "display": "Consultation"
            }
        ]
    },
    "performer": {
        "reference": "Practitioner/5678"
    },
    "reasonCode": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "127305003",
                    "display": "Depressive disorder, single episode, mild"
                }
            ]
        }
    ],
    "supportingInfo": [
        {
            "category": {
                "coding": [
                    {
                        "system": "http://hl7.org/fhir/ValueSet/clinical-findings",
                        "code": "1100",
                        "display": "Symptoms"
                    }
                ]
            },
            "code": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "25064002",
                        "display": "Sad mood"
                    }
                ]
            },
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "162864005",
                        "display": "Depressed mood"
                    }
                ]
            }
        },
        {
            "category": {
                "coding": [
                    {
                        "system": "http://hl7.org/fhir/ValueSet/clinical-findings",
                        "code": "1000",
                        "display": "Medical conditions"
                    }
                ]
            },
            "code": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "37847002",
                        "display": "Headache"
                    }
                ]
            },
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "25064002",
                        "display": "Sad mood"
                    }
                ]
            }
        },
        {
            "category": {
                "coding": [
                    {
                        "system": "http://hl7.org/fhir/ValueSet/clinical-findings",
                        "code": "1100",
                        "display": "Symptoms"
                    }
                ]
            },
            "code": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "255581003",
                        "display": "Fatigue"
                    }
                ]
            },
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "162864005",
                        "display": "Depressed mood"
                    }
                ]
            }
        }
    ],
    "note": [
        {
            "text": "Prescribe talking therapies and medications"
        }
    ]
}
)