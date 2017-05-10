from .models import Serie

def copiar_treino_series(origem, destino):
    print(origem.pk, destino.pk)
    for serie in Serie.objects.filter(treino_id=origem.pk):
        serie.pk = None
        serie.treino_id = destino.pk
        serie.save()
