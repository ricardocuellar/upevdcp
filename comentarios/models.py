from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_editorjs import EditorJsField
from etps.models import ETP
#Models 
# Create your models here.

class Comentario(models.Model):

    comentario=EditorJsField(editorjs_config={
        "tools":{
            "Image":{
                "config":{
                    "endpoints":{
                        "byFile": '/imageUPload/',
                        "byUrl": '/imageUPload',
                    },
                    "additionalRequestHeaders":[{"Content-Type": 'multipart/form-data'}]
                }
            },
            "Attaches":{
                "config":{
                    "endpoint": '/fileUPload/'
                }
            }
        }
    })

    etp = models.ForeignKey(ETP, on_delete=models.CASCADE)

    evaluador =  models.ForeignKey(User, on_delete=models.CASCADE)  
