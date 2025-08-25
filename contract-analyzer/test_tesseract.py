import pytesseract
from PIL import Image

# Criar uma imagem simples de teste
img = Image.new("RGB", (200, 60), color=(255, 255, 255))

# Escrever algo na imagem
from PIL import ImageDraw
draw = ImageDraw.Draw(img)
draw.text((10, 10), "Teste OCR", fill=(0, 0, 0))

# Rodar OCR
text = pytesseract.image_to_string(img, lang="por")
print("Texto reconhecido:", text)
