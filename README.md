
# Criptografia AES em Python

Este é um simples script em Python para demonstrar a criptografia e descriptografia usando o algoritmo AES (Advanced Encryption Standard). O código utiliza a biblioteca `Crypto` para operações criptográficas.

## Como Funciona

1. **Importação de Bibliotecas:**
   - As bibliotecas necessárias para a implementação do AES são importadas, incluindo `AES` para a cifra, `Padding` para o preenchimento de dados, e `get_random_bytes` para gerar bytes aleatórios.

2. **Funções de Criptografia e Descriptografia:**
   - Duas funções principais, `encrypt_AES` e `decrypt_AES`, são definidas para realizar as operações de cifra e decifra, respectivamente. A cifra é realizada em modo CBC (Cipher Block Chaining), e é utilizado preenchimento para garantir que os dados tenham o tamanho necessário.

3. **Função Principal - `main`:**
   - O usuário é solicitado a inserir uma palavra-chave que será utilizada como chave de criptografia. O código verifica se a chave tem um comprimento adequado (entre 2 e 32 bytes) e realiza o preenchimento conforme necessário.

   - Uma mensagem de exemplo (`data`) é definida e, em seguida, é criptografada usando a chave fornecida. A descriptografia é realizada em seguida, e os dados originais são exibidos junto com os dados criptografados.

4. **Execução:**
   - O código é executado quando o script é chamado como
