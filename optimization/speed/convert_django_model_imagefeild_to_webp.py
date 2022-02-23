from io import BytesIO
import requests
from PIL import Image

from django.core.files.uploadedfile import InMemoryUploadedFile

from config.settings.production import MEDIA_URL 
from curioed.core.models import Team


def convert_to_webp(obj):
    response = requests.get(MEDIA_URL + obj.avatar.name)
    image = Image.open(BytesIO(response.content))
    output = BytesIO()
    image.save(
        output,
        format="WEBP",
        quality=70
    )
    output.seek(0)
    obj.avatar = InMemoryUploadedFile(output, 'ImageField', "%s.webp" % obj.avatar.name.split('.')[0], 'image/webp',
                                        len(output.getbuffer()), None)
    obj.save()

ms = Team.objects.all()
for m in ms: 
    convert_to_webp(m)
    print(m)