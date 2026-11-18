# Modelo: **Petição**

Você pode instanciar uma petição, utilizada em métodos em que a mesma é necessária:

```python
from intimai.modelos.peticao import Peticao

peticao = Peticao(
    'caminho/da/peticao',
    32,          # Tipo do documento. Opcional (depende do tribunal)
    'descricao'  # Opcional
)
```

[Voltar para o README](../../README.md#intimaai--sdk-v3-python)
