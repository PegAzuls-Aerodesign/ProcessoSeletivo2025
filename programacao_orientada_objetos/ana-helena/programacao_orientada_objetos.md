# Nivelamento em Programação Orientada a Objetos

## Objetivo

> Ao fim dessa etapa, é esperado do candidato ter noções básicas de programação orientada a objetos, suas principais características e boas práticas relacionadas, bem como modelar problemas da vida real no âmbito computacional

## Questões conceituais

### Questão 1

> Explique o que é Programação Orientada a Objetos destacando quais as motivações que fizeram ela surgir, bem como suas principais diferenças em relação à programação estruturada

**O que esperamos como resposta:**

>  É um paradigma da programação, que se organiza em torno de objetos, entidades que combinam atributos e métodos, assim, representando conceitos do mundo real, surgiu para lidar com a complexidade que o desenvolvimento de software estava tomando, busca maior modularidade, reutilização de códigos e facilidade de manutenção, as principais diferenças entre Programação Orientada a Objetos (POO) e Programação Estruturada (PE), enquanto POO organiza o código em torno de objetos que possuem atributos e métodos, a PE foca em executar em sequências de tarefas, usando estruturas de controle, como sequência, seleção e iteração.

---

### Questão 2

> Explique o que é um objeto em POO, quais são suas principais caracteristicas? No que ele se difere do conceito de classe? Cite Exemplos de classes e objetos

**O que esperamos como resposta:**

> Um objeto é um módulo concreto de um "Conceito do mundo real", possuí atributos e métodos, é uma instância da classe, essa sendo o molde que define as características e comportamentos comuns a um tipo de objeto. Um exemplo de Classe: 

--> Classe 
class Aeronave:
    def __init__(self, nome, tipo, capacidade_passageiros):
        self.nome = nome
        self.tipo = tipo
        self.capacidade_passageiros = capacidade_passageiros
        self.voando = False

--> Objeto
boeing = Aeronave("Boeing 747", "Jato Comercial", 416)

---

### Questão 3 

> Leia a descrição de cada solução de software abaixo. Para cada uma, identifique qual dos quatro pilares da Programação Orientada a Objetos **(Abstração, Encapsulamento, Herança ou Polimorfismo)** está sendo mais bem demonstrado.

#### Cenários:

**1. Sistema de Recursos Humanos**

> Para modelar os diferentes cargos em uma empresa, foi criada uma classe base `Funcionario` que contém atributos e métodos comuns a todos, como `nome`, `matricula` e o método `calcular_salario()`. Em seguida, foram criadas as classes `Gerente` e `Desenvolvedor`, que são baseadas na classe `Funcionario`, **reaproveitando todo o seu código** e apenas adicionando funcionalidades específicas, como o método `aprovar_ferias()` para o Gerente e `codificar()` para o Desenvolvedor. A relação aqui é que todo `Gerente` **É UM** `Funcionario`.
>
> **Pilar associado:** Herança

**2. Módulo de Pagamentos**

> Em um sistema de e-commerce, foi criada uma única função chamada `processar_pagamento`. Essa função é capaz de receber uma lista de objetos de **tipos diferentes**, como `PagamentoBoleto`, `PagamentoCartao` e `PagamentoPix`. A função simplesmente itera sobre a lista e chama o **mesmo método** `.confirmar_pagamento()` em cada objeto. Cada tipo de pagamento executa a confirmação de sua **própria maneira específica**: o boleto verifica a compensação, o cartão contata a operadora e o Pix checa o banco central.
>
> **Pilar associado:** polimorfismo

**3. Controle de uma Smart TV**

> Ao modelar a classe `SmartTV` para um aplicativo de controle remoto, os desenvolvedores decidiram expor apenas os métodos essenciais que um usuário precisa, como `ligar()`, `mudar_canal()` e `aumentar_volume()`. Toda a **complexidade interna** do sistema operacional da TV, o processamento de sinal digital, os circuitos eletrônicos e a comunicação com a internet foi **completamente omitida** da interface da classe. O objetivo era fornecer um modelo simplificado, mostrando apenas o necessário para o **contexto do controle pelo usuário**.
>
> **Pilar associado:** Abstração


**4. Classe de Conta Bancária**

> Para garantir a integridade dos dados, a classe `ContaBancaria` foi projetada de forma que o atributo `_saldo` seja **protegido de acesso direto**. Qualquer tentativa de modificação no saldo de uma conta deve ser feita **exclusivamente através dos métodos públicos** `depositar(valor)` e `sacar(valor)`. Esses métodos contêm regras de negócio importantes, como não permitir depósitos de valores negativos ou saques maiores que o saldo disponível, garantindo que o objeto nunca entre em um estado inválido.
>
> **Pilar associado:** Encapsulamento

**O que esperamos como resposta:**

> Preencher no devido espaço qual pilar associado e, logo abaixo, justificar sua resposta

---

### Questão 4

> Analise as descrições de cada cenário abaixo. Para cada um, identifique se o relacionamento principal entre as classes é de **Herança**, **Composição** ou **Agregação**.

#### Cenários:

**1. Modelagem de uma Universidade**

> Em um sistema acadêmico, uma `Turma` é formada por um conjunto de `Alunos`. Os objetos do tipo `Aluno` são criados de forma independente e podem existir no sistema mesmo sem estarem associados a uma turma. Ao criar uma `Turma`, o sistema **recebe uma lista de objetos `Aluno` já existentes** e os armazena. Se a `Turma` for cancelada e o objeto correspondente destruído, os objetos `Aluno` continuarão existindo no sistema.
>
> **Relacionamento associado:** Agregação

**2. Sistema de uma Editora de Livros**

> Ao modelar um `Livro`, foi definido que todo livro **É UM** `Produto` vendável. A classe `Livro` foi criada com base na classe `Produto`, **reaproveitando automaticamente** atributos como `codigo_de_barras` e `preco`, além de métodos como `calcular_imposto()`. A classe `Livro` então adicionou atributos próprios, como `autor` e `numero_paginas`.
>
> **Relacionamento associado:** Herança
**3. Representação de um Computador**

> No sistema de uma loja de eletrônicos, a classe `Computador` é modelada. Ficou definido que um `Computador` é composto por partes essenciais, como uma `PlacaMae`. O objeto `PlacaMae` é uma **parte intrínseca e exclusiva** do `Computador`. Ele é **criado no exato momento em que o `Computador` é instanciado** e não faz sentido existir no sistema de forma independente. Se o objeto `Computador` for removido do inventário (destruído), o objeto `PlacaMae` associado a ele também deixa de existir.
>
> **Relacionamento associado:** Composição

**O que esperamos como resposta:**

> Preencher no devido espaço qual pilar associado e, logo abaixo, justificar sua resposta

---

## Questões Práticas

### Questão 5 (classes, métodos e atributos)

> Fazer um programa para ler os dados de um funcionário (nome, salário bruto e imposto). Em
seguida, mostrar os dados do funcionário (nome e salário líquido). Em seguida, aumentar o
salário do funcionário com base em uma porcentagem dada (somente o salário bruto é
afetado pela porcentagem) e mostrar novamente os dados do funcionário. Use a classe
projetada abaixo.

<div>
    <p align="center">
        <img src="img/employee.png" height="150" tittle="Employee"> 
    </p>
</div>

**O que esperamos como resposta:**

> Responda tanto a implementação da classe, quanto o utilização da mesma descrita no enunciado em um único arquivo questao5.py

---

### Questão 6 (Herança e polimorfismo)

> Faça um programa para ler os dados de N
produtos (N fornecido pelo usuário). Ao final,
mostrar a etiqueta de preço de cada produto na
mesma ordem em que foram digitados.

> Todo produto possui nome e preço. Produtos
importados possuem uma taxa de alfândega, e
produtos usados possuem data de fabricação.
Estes dados específicos devem ser
acrescentados na etiqueta de preço. Para produtos
importados, a taxa e alfândega deve ser
acrescentada ao preço final do produto.

> O programa deve primeiro, perguntar o numero de produtos que o usuario deseja cadastrar, depois, para cada produto, será perguntado qual tipo de produto será cadastrado (Importado, Usado e Comum) e logo após será solicitado os dados específicos para cada tipo de produto.

> Por fim, após todos os produtos cadastrados, será exibida a etiqueta de cada um

**O que esperamos como resposta:**

> Responda tanto a implementação da classe, quanto o utilização da mesma descrita no enunciado em um único arquivo questao6.py

> Exemplo de execução do programa (Não precisa ser em ingles)

<div>
    <p align="center">
        <img src="img/heranca.png" height="300" tittle="Employee"> 
    </p>
</div>

### Questão 7 (SOLID)

> Nossa equipe de aerodesign, precisa de um sistema flexível para calcular a pontuação final de nossas aeronaves nos relatórios de desempenho. A pontuação é baseada em um conjunto de critérios que podem mudar ou ser expandidos a cada nova competição.

> Seu desafio é criar a primeira versão desta calculadora e, em seguida, provar que seu design é robusto o suficiente para acomodar novas regras sem quebrar o que já existe.

**Objetivo**: Criar um programa que calcula a pontuação final de uma aeronave (soma de todas as pontuações) com base em dois critérios iniciais.

**Requisitos:**

1.  Crie uma classe simples chamada `Aeronave` para armazenar os dados de desempenho.
    * Atributos: `nome` (str), `peso_vazio_kg` (float), `carga_paga_kg` (float).

2.  Crie uma classe chamada `CalculadoraDePontuacao`.
    * Ela deve ter um método `calcular_pontuacao_final(self, aeronave, criterios)` que recebe um objeto `Aeronave` e uma lista de critérios a serem aplicados.
    * Este método deve calcular e retornar a soma dos pontos de todos os critérios aplicados.

3.  **Implemente os dois critérios de pontuação iniciais:**
    * **Critério de Carga Paga:** A pontuação é `carga_paga_kg * 10`.
    * **Critério de Leveza:** A pontuação é calculada pela fórmula `max(0, 100 - (peso_vazio_kg * 5))`. (A aeronave perde 5 pontos para cada kg de peso vazio, a partir de uma base de 100 pontos).
    * Cada um desses critérios pode receber um objeto `Aeronave` para conseguir acessaros atributos e calcular a pontuação

4. Demais classes auxiliares podem ser necessárias para implementação

**O que esperamos como resposta:**

> Aplicação do Open/closed principle em um problema do escopo do projeto.

> Todo código pode estar implementado em uma arquivo questao7.py

> Tal problema é semelhante ao apresentado em `aula/solid/ocp/Exemplo2.py`e pode servir de inspiração.

### Questão 8 (Ponte)

Para representar a geometria de uma ponte treliçada, podemos criar estruturas geométricas básicas a partir de classes.

1. Construa uma classe `Point` que representa um ponto P = (x, y). 
2. Construa uma classe `Line` que represente um segmento de reta, descria por dois pontos finais A=(x_1,y_1) e B=(x_2,y_2).
   1. Os pontos devem ser atributos da classe
   2. O comprimento do segmento deve ser um atributo, estimado através de um método privado
   3. A classe deve implementar um método público que receba outro segmento de reta e retorna o ângulo formado entre estes.

---

Em mecânica, uma treliça é geralmente definida como uma estrutura com dois elementos de força (tração ou compressão) conectados formando unidades triangulares. ([Truss Bridges - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/B9780128044322000086))

3. Construa uma classe `Truss` que represente uma treliça. A classe deve ter como atributos: nome, uma lista de pontos, e uma lista de linhas que conectem os pontos na ordem correta.

<div>
    <p align="center">
        <img src="img/ponte.png" height="200" tittle="Employee"> 
    </p>
</div>


## Material complementar

[Playlist do professor Gadelha](https://www.youtube.com/playlist?list=PLy2F8FMtB4X4MD3ooCHn_XSOOUJAqW8xX)

[Playlist do professor Gustavo Guanabara](https://www.youtube.com/playlist?list=PLHz_AreHm4dkqe2aR0tQK74m8SFe-aGsY)

[POO em python](https://realpython.com/python-classes)

[Os 4 pilares da Programação Orientada a Objetos](https://www.devmedia.com.br/os-4-pilares-da-programacao-orientada-a-objetos/9264)

[Vantagens e desvantagens da Programação Orientada a Objetos](https://www.devmedia.com.br/vantagens-e-desvantagens-da-poo/32655)

[SOLID: guia completo sobre os 5 princípios da POO!](https://blog.betrybe.com/linguagem-de-programacao/solid-cinco-principios-poo)

[O que é SOLID](https://medium.com/desenvolvendo-com-paixao/o-que-é-solid-o-guia-completo-para-você-entender-os-5-princípios-da-poo-2b937b3fc530)

[SOLID fica FÁCIL com Essas Ilustrações](https://www.youtube.com/watch?v=6SfrO3D4dHM)

