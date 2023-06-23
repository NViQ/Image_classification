import torch
from torchvision import models, transforms

# Загрузка предобученной модели
model = models.resnet50(pretrained=True)
model.eval()

# Преобразование изображения перед подачей на вход модели
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Ф-я классификации изображения
def classify_image(image):
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)
    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')
    with torch.no_grad():
        output = model(input_batch)
    _, predicted_idx = torch.max(output, 1)

    with open('imagenet_classes.txt', 'r') as f:
        labels = f.readlines()
    class_name = labels[predicted_idx.item()].strip().split(": ")[1]

    return class_name
