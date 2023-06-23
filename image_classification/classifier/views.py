from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from .utils import classify_image

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        img = Image.open(file).convert('RGB')
        width, height = img.size
        class_name = classify_image(img)
        return render(request, 'result.html', {'width': width, 'height': height, 'class_name': class_name})
    return render(request, 'upload.html')

def upload_another_image(request):
    return redirect('upload_file')
