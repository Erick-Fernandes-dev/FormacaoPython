## Python
___
### Strings

``.capitalize()`` - no inicio coloca um caractere em maiusculo
``.lower()`` - pega todos os caracters e transforma em minusculo
``.strip()``  - tira espaços desnecessarios
substring
find
startswith
endswith

___

### lista

``lista.pop()`` - remmove no final
``lista.append("")`` - adiciona no final
``min(lista)`` - vai pegar o menor valor de dentro de uma lista
``max(lista)`` - vai pegra o maior valor de dentro de uma lista
``len(lista)`` - vai mostrar o tamanho da lista

``.count()`` - Um jeito fácil de contar o número de ocorrências de um determinado elemento em uma lista
``.index("")`` - Retorna o índice da primeira ocorrência de um determinado elemento em uma lista

**OBS!**

Lista são mutávei
Tuple não são mutáveis

___

### Tuple

**Tuple dentro de Lista**
```python

p1 = ("Erick", 22)
p2 = ("Jose", 12)
p3 = ("Junior", 30)

lista_pessoas = [p1, p2, p3]

```

### set

```python
colecao = {11122233344, 22233344455, 33344455566}


colecao.add(44455566677) #vai adicionar pois não existe ainda
colecao.add(11122233344) #nao vai adicionar pois este CPF já existe!
```
**set não possui um índice**

**Resumindo**

Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que não existem elementos duplicados dentro do set.

### Dictionary

```python
instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
```

Nesse par, temos no lado esquerdo a chave e no lado direito o valor. Isso é importante pois usamos a chave para recuperar um valor e assim resolvemos nosso problema:

### Arquivos

**leitura**

```python
arquivo = open('pessoas.txt', 'r')
linha = arquivo.readline()
print(linha)
```

**Escrita**

```python
arquivo = open('pessoas.txt', 'w')
arquivo.write("Alguma coisa")
```

**Adicionar**

```python
arquivo = open('pessoas.txt', 'a')
```

**Fechar**

```python
arquivo = open('pessoas.txt', 'r')
linha = arquivo.readline()

arquivo.close()
```

```python
logo = open('palavras.txt', 'r')
data = logo.read()
logo.close()

# Agora imagine que dê algum problema na hora da leitura quando chamarmos a função read(). Será que mesmo com erro o arquivo será fechado?

# Se for algum erro grave, o programa pode parar a execução sem ter fechado o arquivo! Isso seria muito ruim ...

#=============================================

# Para evitar esse tipo de situação, o Python criou uma sintaxe especial para abertura de arquivo. Veja só:

with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)

# Repare que o with usa a função open. Repare também que não fechamos o arquivo. Isso não é mais necessário pois o Python vai cuidar disso e, mesmo com erro, garantirá o fechamento do arquivo! 
```