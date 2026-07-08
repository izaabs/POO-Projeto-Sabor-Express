# 🍽️ Sistema de Gerenciamento de Restaurantes (POO em Python)

Projeto desenvolvido durante um curso da **Alura** com o objetivo de praticar os principais conceitos de **Programação Orientada a Objetos (POO)** em Python.

O sistema permite cadastrar restaurantes, alterar seu status, receber avaliações de clientes e calcular automaticamente a média das notas.

---

## 📚 Conceitos praticados

Durante o desenvolvimento deste projeto foram aplicados diversos conceitos fundamentais de POO, como:

- Classes e Objetos
- Métodos
- Construtores (`__init__`)
- Encapsulamento
- Atributos privados (`_atributo`)
- Métodos especiais (`__str__`)
- Métodos de classe (`@classmethod`)
- Propriedades (`@property`)
- Associação entre classes
- Listas de objetos
- Organização do projeto em módulos

---

## 📁 Estrutura do Projeto

```text
projeto/
│
├── app.py
│
└── modelos/
    ├── restaurante.py
    └── avaliacao.py
```

### Arquivos

### `app.py`

Arquivo principal responsável por:

- Criar restaurantes;
- Adicionar avaliações;
- Executar o programa;
- Exibir todos os restaurantes cadastrados.

### `restaurante.py`

Contém a classe `Restaurante`, responsável por:

- Cadastro dos restaurantes;
- Controle de status (ativo/inativo);
- Armazenamento das avaliações;
- Cálculo da média das notas;
- Listagem dos restaurantes cadastrados.

### `avaliacao.py`

Contém a classe `Avaliacao`, responsável por armazenar:

- Nome do cliente;
- Nota atribuída ao restaurante.

---

## ⚙️ Funcionalidades

- ✅ Cadastro de restaurantes
- ✅ Definição da categoria
- ✅ Controle de status (ativo/inativo)
- ✅ Recebimento de avaliações
- ✅ Validação das notas (1 a 5)
- ✅ Cálculo automático da média das avaliações
- ✅ Listagem de todos os restaurantes

---

## 💻 Exemplo de utilização

```python
from modelos.restaurante import Restaurante

restaurante = Restaurante("JJ Food", "Fast Food")

restaurante.alterar_status()

restaurante.receber_avaliacao("Iza", 5)
restaurante.receber_avaliacao("Maria", 4)

Restaurante.listar_restaurantes()
```

---

## 🧠 Conceitos de POO utilizados

### Encapsulamento

Os atributos internos da classe utilizam o prefixo `_`, indicando que devem ser acessados apenas pelos métodos da própria classe.

Exemplo:

```python
self._nome
self._categoria
self._ativo
self._avaliacao
```

---

### Properties

Foram utilizadas propriedades para disponibilizar informações calculadas sem que o usuário precise chamar métodos diretamente.

Exemplo:

```python
@property
def ativo(self):
    ...
```

e

```python
@property
def media_avaliacoes(self):
    ...
```

Assim é possível utilizar:

```python
restaurante.ativo
restaurante.media_avaliacoes
```

---

### Método de Classe

O método

```python
@classmethod
listar_restaurantes()
```

pertence à classe e permite listar todos os restaurantes cadastrados utilizando a lista compartilhada:

```python
Restaurante.restaurantes
```

---

### Associação entre Classes

Cada objeto `Restaurante` possui uma lista de objetos `Avaliacao`.

```python
Restaurante
    ├── Avaliação
    ├── Avaliação
    └── Avaliação
```

Essa relação demonstra um exemplo de associação entre classes.

---

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

Execute:

```bash
python app.py
```

---

## 📌 Melhorias futuras

Algumas melhorias que podem ser implementadas:

- Interface gráfica
- Menu interativo no terminal
- Persistência de dados em arquivos
- Banco de dados SQLite
- Busca de restaurantes por nome
- Exclusão e edição de restaurantes
- Listagem das avaliações de cada restaurante

---

## 🎓 Aprendizados

Este projeto foi desenvolvido como parte dos estudos em **Programação Orientada a Objetos com Python**, permitindo praticar conceitos essenciais como encapsulamento, propriedades, métodos de classe, associação entre objetos e organização do código em módulos.

---

## 👩‍💻 Autora

**Izabelli Ribeiro**

---

> Projeto desenvolvido para fins de estudo durante um curso de **Python e Programação Orientada a Objetos** da **Alura**.
