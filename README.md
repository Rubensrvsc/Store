
# Store API

Construção de uma API de loja de roupas.
Para que os donos de lojas de roupas pudessem ter um maior controle de estoque do seu estabelecimento se faz necessário a construção de sistemas
que possam ajudar o empresário dono da loja.

Em virtude do que foi citado construí essa API com o objetivo de proporcionar um melhor conhecimento dos produtos que estão no estoque da loja

Para a contrução dessa API usei as seguintes tecnologias

```
Python3
Pip3
SQLITE3
Django
Django Rest Framework
```

Abaixo pode ser vistos os endpoints com uma breve descrição

### EndPoints

| Method |EndPoint | Description |
|---|---|---|
| GET | `http://localhost:8000/products` | Lista todos os produtos |
| POST | `http://localhost:8000/create_product` | Cria um produto |
| PUT | `http://localhost:8000/updateproduct/<id>` | Edita um produto pelo id |
| GET | `http://localhost:8000/products/<int:id>` | Permite ver apenas um produto |
| GET | `http://localhost:8000/searchproduct/?name_product=<nome_produto>` | Filtra produtos por um nome enviado |
| GET | `http://localhost:8000/searchpriceproduct/<preço_um>/<preço_dois>` | Traz uma lista de produtos que está entre dois preços |
| POST | `http://localhost:8000/createcategory` | Cria uma categoria de produtos |
| GET | `http://localhost:8000/productcategories` | Lista todas as categorias de produtos |
| POST | `http://localhost:8000/size` | Cria um tipo de tamanho de roupa |
| GET | `http://localhost:8000/size` | Lista todos os tamanhos de roupas |
| POST | `http://localhost:8000/producttypes` | Cria um tipo de produto |
| GET | `http://localhost:8000/producttypes` | Lista todos os tipos de produtos |

