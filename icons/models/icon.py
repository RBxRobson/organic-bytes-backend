from django.db import models

class Icon(models.Model):
    # Campo para armazenar o link da imagem
    image_url = models.URLField(max_length=500)  
    
    # Campo para descrição do ícone, com limite de 255 caracteres
    alt = models.CharField(max_length=255,blank=True, null=True)  


    def __str__(self):
        # Retorna o alt como a representação da instância do modelo
        return self.alt  
