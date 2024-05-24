## Informações 

Endpoint para lidar com métodos relacionados ao gerenciamento de usuários.

![BadgeCount](https://img.shields.io/badge/Rota-/-purple) 
![BadgeCount](https://img.shields.io/badge/Metódos-REST-blue)

## Propriedades 
Os atributos de um usuário são:

```json
{
    "id": "integer",
    "cpf": "string",
    "email": "string",
    "name": "string",
    "lname": "string",
    "username": "string",
    "password": "string",
    "status": "enum ['active', 'inactive', 'banned']",
    "role": "enum ['admin', 'user']"
}
```

<hr>

### GET /users
Retorna todos os usuários do sistema.

* **Parâmetros da URL**  
  None
* **Parâmetros do Body**  
  None
* **Headers**  
  Content-Type: application/json  
  Authorization: Bearer `<OAuth Token>`
* **Resposta de Sucesso:**  
  * **Código HTTP:** 200  
  * **Content:**  
    ```json
    {
      "users": 
        [
          {"<user_object>"},
          {"<user_object>"},
          {"<user_object>"}
        ]
    }
    ```

### GET /users/{id}
Retorna o usuário especificado.

* **Parâmetros de URL**  
  *Required:* `id=[integer]`
* **Parâmetros de Body**  
  None
* **Headers**  
  Content-Type: application/json  
  Authorization: Bearer `<OAuth Token>`
* **Resposta de Sucesso:**  
  * **Código HTTP:** 200  
  * **Content:**  
    ```json
    {
        "<user_object>"
    }
    ```
* **Resposta de Erro:**  
  * **Código HTTP:** 404  
  * **Content:** 
    ```json
    { 
        "error" : "Usuário inexistente"
    }
    ```
  * **Código HTTP:** 401  
  * **Content:** 
    ```json
    {
        "error" : "Você não está autorizado a fazer essa solicitação."
    }
    ```

### POST /users
Cria um novo usuário.

* **Parâmetros da URL**  
  None
* **Parâmetros do Body**  
  *Required:* `cpf=[string]`  
  *Required:* `email=[string]`  
  *Required:* `name=[string]`  
  *Required:* `lname=[string]`  
  *Required:* `username=[string]`  
  *Required:* `password=[string]`  
  *Required:* `status=[enum ['active', 'inactive', 'banned']]`  
  *Required:* `role=[enum ['admin', 'user']]`
* **Headers**  
  Content-Type: application/json  
  Authorization: Bearer `<OAuth Token>`
* **Resposta de Sucesso:**  
  * **Código HTTP:** 201  
  * **Content:**  
    ```json
    {
        "message": "Usuário criado com sucesso."
    }
    ```
* **Resposta de Erro:**  
  * **Código HTTP:** 400  
  * **Content:** 
    ```json
    { 
        "error" : "Erro ao criar usuário."
    }
    ```
  * **Código HTTP:** 401  
  * **Content:** 
    ```json
    {
        "error" : "Você não está autorizado a fazer essa solicitação."
    }
    ```

### PUT /users/{id}
Atualiza um usuário existente.

* **Parâmetros da URL**  
  *Required:* `id=[integer]`
* **Parâmetros do Body**  
  *Required:* `cpf=[string]`  
  *Required:* `email=[string]`  
  *Required:* `name=[string]`  
  *Required:* `lname=[string]`  
  *Required:* `username=[string]`  
  *Required:* `password=[string]`  
  *Required:* `status=[enum ['active', 'inactive', 'banned']]`  
  *Required:* `role=[enum ['admin', 'user']]`
* **Headers**  
  Content-Type: application/json  
  Authorization: Bearer `<OAuth Token>`
* **Resposta de Sucesso:**  
  * **Código HTTP:** 200  
  * **Content:**  
    ```json
    {
        "message": "Usuário atualizado com sucesso."
    }
    ```
* **Resposta de Erro:**  
  * **Código HTTP:** 400  
  * **Content:** 
    ```json
    { 
        "error" : "Erro ao atualizar usuário."
    }
    ```
  * **Código HTTP:** 401  
  * **Content:** 
    ```json
    {
        "error" : "Você não está autorizado a fazer essa solicitação."
    }
    ```
  * **Código HTTP:** 404
  * **Content:**  
    ```json
    { 
        "error" : "Usuário inexistente."
    }
    ```

### PATCH /users/{id}
Atualiza um ou mais atributos de um usuário existente.

* **Parâmetros da URL**  
  *Required:* `id=[integer]`
* **Parâmetros do Body**  
  *Optional:* `cpf=[string]`  
  *Optional:* `email=[string]`  
  *Optional:* `name=[string]`  
  *Optional:* `lname=[string]`  
  *Optional:* `username=[string]`  
  *Optional:* `password=[string]`  
  *Optional:* `status=[enum ['active', 'inactive', 'banned']]`  
  *Optional:* `role=[enum ['admin', 'user']]`
* **Headers**  
  Content-Type: application/json  
  Authorization: Bearer `<OAuth Token>`
* **Resposta de Sucesso:**  
  * **Código HTTP:** 200  
  * **Content:**  
    ```json
    {
        "message": "Usuário atualizado com sucesso."
    }
    ```
* **Resposta de Erro:**  
  * **Código HTTP:** 400  
  * **Content:** 
    ```json
    { 
        "error" : "Erro ao atualizar usuário."
    }
    ```
  * **Código HTTP:** 401  
  * **Content:** 
    ```json
    {
        "error" : "Você não está autorizado a fazer essa solicitação."
    }
    ```
  * **Código HTTP:** 404
  * **Content:**  
    ```json
    { 
        "error" : "Usuário inexistente."
    }
    ```

### DELETE /users/{id}
Deleta um usuário existente.

* **Parâmetros da URL**  
  *Required:* `id=[integer]`
* **Parâmetros do Body**  
  None
* **Headers**  
  Content-Type: application/json  
  Authorization: Bearer `<OAuth Token>`
* **Resposta de Sucesso:**  
  **Código HTTP:** 200  
  **Content:**  
    ```json
    {
        "message": "Usuário deletado com sucesso."
    }
    ```
* **Resposta de Erro:**  
  * **Código HTTP:** 400  
  * **Content:** 
    ```json
    { 
        "error" : "Erro ao deletar usuário."
    }
    ```
  * **Código HTTP:** 401  
  * **Content:** 
    ```json
    {
        "error" : "Você não está autorizado a fazer essa solicitação."
    }
    ```
  * **Código HTTP:** 404
  * **Content:**  
    ```json
    { 
        "error" : "Usuário inexistente."
    }
    ```

<hr>

## Exemplo de Objeto de Usuário
```json
{
    "id": 1,
    "cpf": "123.456.789-00",
    "email": "johndoe@gmail.com",
    "name": "John",
    "lname": "Doe",
    "username": "johndoe",
    "password": "password",
    "status": "active",
    "role": "user"
}
```

