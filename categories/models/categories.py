from django.db import models

class Category(models.Model):
    # Campo para armazenar o link da imagem
    image_url = models.URLField(max_length=500)  
    
    # Campo para descrição da categoria, com limite de 255 caracteres
    alt = models.CharField(max_length=255) 
    
    # Campo para nome da categoria, com limite de 255 caracteres
    name = models.CharField(max_length=255)


    def __str__(self):
        # Retorna o alt como a representação da instância do modelo
        return self.alt  