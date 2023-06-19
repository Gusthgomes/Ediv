from django.db.models import TextChoices

class BudgetStatus(TextChoices):
    SOLICITADO = 'OS', 'Orçamento Solicitado'
    EM_ANALISE = 'EA', 'Em análise'
    REALIZADO = 'R', R'Realizado'
    CANCELADO = 'C', 'Cancelado'
    FECHADO = 'F', 'Fechado'
    
class ServiceTags(TextChoices):
    MOTION = 'M', 'Motion designer'
    EDICAO_IMAGEM = 'EI', 'Edição de imagem'
    EDIÇÂO_VIDEO = 'EV', 'Edição de video'