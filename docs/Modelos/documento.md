# Modelo: **Documento**

Você pode instanciar um documento, utilizado em métodos em que o mesmo é necessário:

```python
from intimai.modelos.documento import Documento

documento = Documento(
    'caminho/do/documento',
    1,           # Ordem (primeiro, segundo, terceiro...) de processamento/envio
    32,          # Tipo do documento. Opcional (depende do tribunal)
    'descricao'  # Opcional
)
```

[Voltar para o README](../../README.md#intimaai---sdk-v3-python)
