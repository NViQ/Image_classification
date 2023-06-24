from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from .utils import classify_image

#Ф-я обработки запроса для загрузки файла изображения
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            if file:
                img = Image.open(file).convert('RGB')
                width, height = img.size
                class_name = classify_image(img)
                return render(request, 'result.html', {'width': width, 'height': height, 'class_name': class_name})
            else:
                error_message = "file not selected"
                return render(request, 'upload.html', {'error_message': error_message})
        else:
            error_message = "file not selected"
            return render(request, 'upload.html', {'error_message': error_message})
    return render(request, 'upload.html')

def upload_another_image(request):
    return redirect('upload_file')

