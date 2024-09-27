from django.db import models

class Hero(models.Model):
    # Campo para armazenar o link da imagem
    image_url = models.URLField(max_length=500)  
    
    # Campo para o título, com limite de 255 caracteres
    title = models.CharField(max_length=255)  
    
    # Campo opcional para o subtítulo
    subtitle = models.CharField(max_length=255, blank=True, null=True) 
    
    # Campo opcional para a descrição
    description = models.TextField(blank=True, null=True)  
    
    # Palavra ou frase em destaque
    highlighted_text = models.CharField(max_length=255, blank=True, null=True)  

    def __str__(self):
        # Retorna o título como a representação da instância do modelo
        return self.title  
