# Nivelamento em Programação Orientada a Objetos

## Objetivo

> Ao fim dessa etapa, é esperado do candidato ter noções básicas de programação orientada a objetos, suas principais características e boas práticas relacionadas, bem como modelar problemas da vida real no âmbito computacional

## Questões conceituais

### Questão 1

> Explique o que é Programação Orientada a Objetos destacando quais as motivações que fizeram ela surgir, bem como suas principais diferenças em relação à programação estruturada

**O que esperamos como resposta:**

> Pode responder aqui em baixo

Programação Orientada a Objetos (POO) é um paradigma que modela sistemas como coleções de objetos interagentes, cada um encapsulando dados (atributos) e comportamentos (métodos). Suas principais motivações surgiram para gerenciar a complexidade de sistemas grandes, promovendo reutilização de código, modularidade e modelagem mais próxima do mundo real. Em contraste com a programação estruturada (que organiza código em procedimentos globais aplicados a dados), a POO organiza o código em classes e objetos, onde métodos estão associados aos dados específicos de cada objeto. A programação estruturada tem melhor desempenho em cenários específicos (como sistemas embarcados), mas a POO oferece vantagens como encapsulamento, herança e polimorfismo, facilitando a manutenção e evolução de sistemas complexos.

---

### Questão 2

> Explique o que é um objeto em POO, quais são suas principais caracteristicas? No que ele se difere do conceito de classe? Cite Exemplos de classes e objetos

**O que esperamos como resposta:**

> Pode responder aqui em baixo

Um objeto em POO é uma instância concreta de uma classe, representando uma entidade específica com estado (atributos) e comportamento (métodos). Por exemplo, se "Carro" é uma classe, um objeto pode ser "Fiat UNO 1996" com atributos como cor="Vermelho" e motor="1.4". A classe é o modelo abstrato que define a estrutura e comportamentos comuns, enquanto o objeto é a instância específica criada a partir dessa classe. Diferenças: a classe é a definição genérica, o objeto é a instância com valores concretos.

---

### Questão 3 

> Leia a descrição de cada solução de software abaixo. Para cada uma, identifique qual dos quatro pilares da Programação Orientada a Objetos **(Abstração, Encapsulamento, Herança ou Polimorfismo)** está sendo mais bem demonstrado.

#### Cenários:

**1. Sistema de Recursos Humanos**

> Para modelar os diferentes cargos em uma empresa, foi criada uma classe base `Funcionario` que contém atributos e métodos comuns a todos, como `nome`, `matricula` e o método `calcular_salario()`. Em seguida, foram criadas as classes `Gerente` e `Desenvolvedor`, que são baseadas na classe `Funcionario`, **reaproveitando todo o seu código** e apenas adicionando funcionalidades específicas, como o método `aprovar_ferias()` para o Gerente e `codificar()` para o Desenvolvedor. A relação aqui é que todo `Gerente` **É UM** `Funcionario`.
>
> **Pilar associado:** Herança
    Gerente e Desenvolvedor herdam de Funcionario, reutilizando código e estabelecendo relação "É UM".

**2. Módulo de Pagamentos**

> Em um sistema de e-commerce, foi criada uma única função chamada `processar_pagamento`. Essa função é capaz de receber uma lista de objetos de **tipos diferentes**, como `PagamentoBoleto`, `PagamentoCartao` e `PagamentoPix`. A função simplesmente itera sobre a lista e chama o **mesmo método** `.confirmar_pagamento()` em cada objeto. Cada tipo de pagamento executa a confirmação de sua **própria maneira específica**: o boleto verifica a compensação, o cartão contata a operadora e o Pix checa o banco central.
>
> **Pilar associado:** Polimorfismo
    Diferentes tipos de pagamento implementam o mesmo método .confirmar_pagamento() de forma específica.

**3. Controle de uma Smart TV**

> Ao modelar a classe `SmartTV` para um aplicativo de controle remoto, os desenvolvedores decidiram expor apenas os métodos essenciais que um usuário precisa, como `ligar()`, `mudar_canal()` e `aumentar_volume()`. Toda a **complexidade interna** do sistema operacional da TV, o processamento de sinal digital, os circuitos eletrônicos e a comunicação com a internet foi **completamente omitida** da interface da classe. O objetivo era fornecer um modelo simplificado, mostrando apenas o necessário para o **contexto do controle pelo usuário**.
>
> **Pilar associado:** Encapsulamento
    Expondo apenas métodos essenciais (ligar, mudar_canal) e ocultando detalhes internos complexos.

**4. Classe de Conta Bancária**

> Para garantir a integridade dos dados, a classe `ContaBancaria` foi projetada de forma que o atributo `_saldo` seja **protegido de acesso direto**. Qualquer tentativa de modificação no saldo de uma conta deve ser feita **exclusivamente através dos métodos públicos** `depositar(valor)` e `sacar(valor)`. Esses métodos contêm regras de negócio importantes, como não permitir depósitos de valores negativos ou saques maiores que o saldo disponível, garantindo que o objeto nunca entre em um estado inválido.
>
> **Pilar associado:** Encapsulamento
    Protegendo o saldo com métodos públicos (depositar() e sacar()) para validação.

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
    Alunos existem independentemente da Turma (partes podem existir sem o todo).

**2. Sistema de uma Editora de Livros**

> Ao modelar um `Livro`, foi definido que todo livro **É UM** `Produto` vendável. A classe `Livro` foi criada com base na classe `Produto`, **reaproveitando automaticamente** atributos como `codigo_de_barras` e `preco`, além de métodos como `calcular_imposto()`. A classe `Livro` então adicionou atributos próprios, como `autor` e `numero_paginas`.
>
> **Relacionamento associado:** Herança
    Livro "É UM" Produto (herda atributos e métodos da classe base).

**3. Representação de um Computador**

> No sistema de uma loja de eletrônicos, a classe `Computador` é modelada. Ficou definido que um `Computador` é composto por partes essenciais, como uma `PlacaMae`. O objeto `PlacaMae` é uma **parte intrínseca e exclusiva** do `Computador`. Ele é **criado no exato momento em que o `Computador` é instanciado** e não faz sentido existir no sistema de forma independente. Se o objeto `Computador` for removido do inventário (destruído), o objeto `PlacaMae` associado a ele também deixa de existir.
>
> **Relacionamento associado:** Composição
    PlacaMae é parte intrínseca do Computador, não existe sem ele (destruída junto com o todo).

**O que esperamos como resposta:**

> Preencher no devido espaço qual pilar associado e, logo abaixo, justificar sua resposta
