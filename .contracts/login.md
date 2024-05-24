## Informações 

Endpoint para lidar com métodos relacionados ao login.

![BadgeCount](https://img.shields.io/badge/Rota-auth-purple) 
![BadgeCount](https://img.shields.io/badge/Metódos-POST-blue)

<hr>

### POST /auth/login
Realiza a tentativa de login de um usuário.

* **Parâmetros da URL**  
  None
* **Parâmetros do Body**  
  *Required:* `username=[string]`  
  *Required:* `password=[string]`
* **Headers**  
  Content-Type: application/json
  * **Resposta de Sucesso:**
  * **Código HTTP:** 200
  * **Content:**  
    ```json
    {
      "token":
        {
          "access_token": "<OAuth Token>",
            "token_type": "Bearer",
            "expires_in": "integer"
        }
    }
    ```
* **Resposta de Erro:**
  * **Código HTTP:** 400
  * **Content:**  
    ```json
    {
      "error": "Nome de usuário ou senha inválidos."
    }
    ```
    
### POST /auth/logout
Realiza o logout do usuário.

* **Parâmetros da URL**  
  None
* **Parâmetros do Body**  
  None
* **Headers**  
  Content-Type: application/json  
  Authorization Bearer `<OAuth Token>`
* **Resposta de Sucesso:**  
  * **Código HTTP:** 200  
  * **Content:**  
    ```json
    {
      "message": "Logout realizado com sucesso."
    }
    ```
* **Resposta de Erro:**
  * **Código HTTP:** 401
  * **Content:**  
    ```json
    {
      "error": "Token inválido."
    }
    ```
  * **Código HTTP:** 404
  * **Content:**  
    ```json
    {
      "error": "Token inexistente."
    }
    ```