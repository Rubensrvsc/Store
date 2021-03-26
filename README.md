
# Store API

Construção de uma API de loja de roupas.
Para que os donos de lojas de roupas pudessem ter um maior controle de estoque do seu estabelecimento se faz necessário a construção de sistemas
que possam ajudar no gerenciamento dos produtos de sua loja.

Em virtude do que foi citado construí essa API com o objetivo de proporcionar um melhor conhecimento dos produtos que estão no estoque da loja

Para a contrução dessa API usei as seguintes tecnologias

```
Python3
Pip3
SQLITE3
Django
Django Rest Framework
```

### Esse projeto pode ser encontrado neste [link](https://api-django-store.herokuapp.com/)

### Cloning this project

```
git clone https://github.com/Rubensrvsc/api-django-store.git
```

### Running project

```
python3 manage.py runserver
```

### Running tests

```
python3 manage.py test
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


### Descrição dos EndPoints

#### /producttypes [POST]

| Parâmetro | Tipo | 
|---|---|
| `name_product_type` | String |

+ Request (application/json)

    + Body

            {
                "name_product_type": "Camisa",
            }

+ Response 201 Created (application/json)

#### /producttypes [GET]

+ Response 200 OK (application/json)

  + Body

        [
          {
            "name_product_type": "Camisa"
          },
          {
            "name_product_type": "Calça"
          },
          {
            "name_product_type": "Camisa Regata"
          }
        ]

#### /size [GET]

+ Response 200 OK(application/json)

    + Body

            [
                {
                    "id": 1,
                    "size": "P"
                },
                {
                     "id": 2,
                    "size": "PP"
                },
                {
                     "id": 3,
                    "size": "M"
                }
            ]

#### /size [POST]

| Parâmetro | Tipo | 
|---|---|
| `size` | String |

+ Request (application/json)

   + Body

            {
                "size": "GG",
            } 
  + Response 201 Created (application/json)

#### /createcategory [POST]

| Parâmetro | Tipo | 
|---|---|
| `name_product_category` | String |

+ Request (application/json)

   + Body

            {
                "name_product_category": "Adolescente",
            } 
            
 + Response 201 Created (application/json)

#### /productcategories [GET]

+ Response 200 OK(application/json)

    + Body

            [
            {
            "id": 1,
            "name_product_category": "Infantil",
            "product": [
                {
                    "name_product": "Camisa 2",
                    "color": "Vermelha",
                    "price": 10.0
                },
                {
                    "name_product": "camisa com mangas",
                    "color": "azul",
                    "price": 78.9
                }
            ]
            },
            {
            "id": 2,
            "name_product_category": "Adolescente",
            "product": [
                {
                    "name_product": "Camisa Regata Nike",
                    "color": "Azul",
                    "price": 30.7
                },
                {
                    "name_product": "Camisa Neon Nike",
                    "color": "Neon",
                    "price": 48.99
                },
                {
                    "name_product": "Camisa Real Madrid",
                    "color": "branca",
                    "price": 450.0
                }
            ]
            }
            ]

#### /products [GET]

+ Response 200 OK(application/json)

    + Body

            [
                {
                    "name_product": "Camisa Umbro",
                    "color": "Branca",
                    "price": 78.9,
                    "product_category": "Adulto",
                    "product_size": "M",
                    "product_type": "Camisa"
                },
                {
                    "name_product": "Camisa Regata Nike",
                    "color": "Azul",
                    "price": 30.7,
                    "product_category": "Adolescente",
                    "product_size": "G",
                    "product_type": "Camisa Regata"
                },
                {
                    "name_product": "Regata Adidas",
                    "color": "Branca",
                    "price": 50.0,
                    "product_category": "Adulto",
                    "product_size": "G",
                    "product_type": "Camisa Regata"
                }
            ]

#### /create_product [POST]

| Parâmetro | Tipo | 
|---|---|
| `name_product_category` | String |
| `color` | String |
| `price` | Int|
| `product_category` | Int|
| `product_size` | Int |
| `product_type` | Int |

+ Request (application/json)

   + Body

            {
                "name_product": "Adolescente",
                "color": "Azul",
                "price": 50,
                "product_category": 2
                "product_size": 4
                "product_type": 2
            } 

#### /updateproduct/<1> [PUT]

| Parâmetro | Tipo | 
|---|---|
| `name_product_category` | String |
| `color` | String |
| `price` | Int 

+ Request (application/json) 

   + Body

            {
                "name_product": "Adolescente",
                "color": "Azul",
                "price": 50
            } 
  + Response 200 OK(application/json)

#### /searchproduct/?name_product=Camisa [GET]

+ Response 200 OK(application/json)

    + Body

            [
                {
                    "name_product": "Camisa Umbre",
                    "color": "Branca",
                    "price": 78.9,
                    "product_category": "Adulto",
                    "product_size": "M",
                    "product_type": "Camisa"
                },
                {
                     "name_product": "Camisa Regata Nike",
                    "color": "Azul",
                    "price": 30.7,
                    "product_category": "Adolescente",
                    "product_size": "G",
                    "product_type": "Camisa Regata"
                },
                {
                    "name_product": "Camisa 2",
                    "color": "Vermelha",
                    "price": 10.0,
                    "product_category": "Infantil",
                    "product_size": "P",
                    "product_type": "Camisa"
                }
            ]

#### /searchpriceproduct/20/200 [GET]


+ Response 200 OK(application/json)

    + Body

            
            [
                  {
                     "name_product": "Camisa Umbre",
                     "color": "Branca",
                    "price": 78.9,
                    "product_size__size": "M",
                    "product_category__name_product_category": "Adulto",
                    "product_type__name_product_type": "Camisa"
                },
                {
                    "name_product": "Camisa Regata Nike",
                    "color": "Azul",
                    "price": 30.7,
                    "product_size__size": "G",
                    "product_category__name_product_category": "Adolescente",
                    "product_type__name_product_type": "Camisa Regata"
                },
                {
                    "name_product": "Regata Adidas",
                    "color": "Branca",
                    "price": 50.0,
                    "product_size__size": "G",
                    "product_category__name_product_category": "Adulto",
                    "product_type__name_product_type": "Camisa Regata"
                },
                {
                    "name_product": "Camisa Neon Nike",
                    "color": "Neon",
                    "price": 48.99,
                    "product_size__size": "G",
                    "product_category__name_product_category": "Adolescente",
                    "product_type__name_product_type": "Camisa Regata"
                },
                {
                    "name_product": "camisa com mangas",
                    "color": "azul",
                    "price": 78.9,
                    "product_size__size": "P",
                    "product_category__name_product_category": "Infantil",
                    "product_type__name_product_type": "Camisa"
                }
            ]


Feito por Rubens Carvalho

[Linkedin](https://www.linkedin.com/in/rubens-carvalho-892584120/)


EMAIL: rubens.rvsc@gmail.com

