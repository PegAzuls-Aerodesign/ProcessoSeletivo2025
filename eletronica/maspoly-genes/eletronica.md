# Nivelamento em Eletrônica

## Objetivo

> Descreva aqui o objetivo desta etapa do processo seletivo.
## Atividades

### Questão 1

> Explique por que é importante observar a polaridade de componentes como LED, capacitores eletrolíticos e baterias em um circuito. O que pode acontecer se a polaridade for invertida?

**O que esperamos como resposta:**

> Os componentes eletrônicos costumam ter polaridades bem definidas e só funcionam corretamente quando instalados na posição adequada. Caso sejam conectados de forma incorreta, o equipamento pode apresentar problemas temporários de funcionamento, sofrer danos físicos permanentes em outras partes do circuito e, em situações mais graves, até gerar riscos de segurança, como a possibilidade de incêndio.
---

### Questão 2

> Um LED é alimentado por uma fonte de 9 V através de um resistor de 330 Ω.
 a) Qual é a corrente que circula pelo resistor?
 b) Se o LED cair a tensão de 2 V, qual será a tensão no resistor e a corrente real?\
(Use V = R·I)

**O que esperamos como resposta:**

> a)   V = R * I => 9= 330 * I => I = 9/330 => I = 27mA

> b)  finalV = 9V - 2V = 7V =>
      V = R * I => 7 = 330 * I => I = 7/330 => I = 21,2 mA

---
### Questão 3

>  Explique em suas palavras a diferença entre um circuito puramente analógico e um circuito com microcontrolador (Arduino).
Dê um exemplo de cada tipo.

**O que esperamos como resposta:**

> Circuito analógico: Opera apenas com componentes eletrônicos como resistores, capacitores e transistores, sem exigir nenhum tipo de programação. 
>-Exemplo: um controle de volume feito com um potenciômetro.

>Circuito com Arduino: Baseia-se em um microcontrolador programável, capaz de interpretar informações de sensores e reagir a elas. 
>-Exemplo: identificar a presença de um obstáculo e desviar automaticamente.

---
### Questão 4

>  Explique o que é um divisor de tensão e como ele funciona. Dê um exemplo prático de onde um divisor de tensão pode ser utilizado em um circuito eletrônico.
**O que esperamos como resposta:**

> Um divisor de tensão é um circuito composto por dois resistores ligados em série, no qual a tensão de saída corresponde a uma parte da tensão de entrada. Essa fração é determinada pela proporção entre os valores dos resistores.
Exemplo prático: ao utilizar dois resistores iguais de 1 kΩ, é possível reduzir uma entrada de 9 V para aproximadamente 4,5 V, permitindo alimentar um sensor que não suporta tensões acima de 5 V.

---
### Questão 5

> No código abaixo, explique o que acontecerá com o LED conectado ao pino 9?
> ```cpp
> void setup() {
>   pinMode(9, OUTPUT);
> 
> void loop() {
>   analogWrite(9, 128);
> }
> ```
 
**O que esperamos como resposta:**
> O comando analogWrite(9, 128) produz um sinal PWM (modulação por largura de pulso) com ciclo ativo de 50%, já que o valor 128 representa a metade do limite máximo (255). Dessa forma, o LED não alcança seu brilho total, permanecendo iluminado em torno de metade da intensidade máxima — como se estivesse quase aceso.
---
### Questão 6
> Um motor DC de 5 V precisa de 0,3 A para funcionar. Você só tem uma fonte de 9 V. Qual deve ser a resistência em série para limitar a corrente a 0,3 A?
**O que esperamos como resposta:**
> Vr​ = 9−5 = 4V
R = Vr/I ​​= 4/0,3 ​≈ 13,3Ω
Resposta: 13Ω
---
### Questão 7
> Um resistor ôhmico, quando submetido a uma ddp de 40 V, é atravessado por uma corrente elétrica de intensidade 20 A. Quando a corrente que o atravessa for igual a 4 A, a ddp, em volts, nos seus terminais, será:
> a) 8 V\
> b) 12 V\
> c) 16 V\
> d) 20 V\
> e) 30 V\
> Justifique sua resposta.
**O que esperamos como resposta:**
> R = V/I ​= 40/20 ​= 2Ω

com 4A:
V = R⋅I = 2 ⋅ 4 = 8V
Resposta: a) 8V
---
### Questão 8
>Faça um circuito no TinkerCad que simule um sinal de trânsito.\
Use um Arduino Uno e faça as seguintes conexões:\
> * LED Verde no pino 8 (com resistor 220 Ω para GND). Tempo de espera 5000 ms
> * LED Amarelo no pino 9 (com resistor 220 Ω para GND). Tempo de espera 2000 ms
> * LED Vermelho no pino 10 (com resistor 220 Ω para GND). Tempo de espera 6000 ms\
Para simular o tempo de espera use a função delay(), ela já espera receber o tempo em ms como parâmetro, as demais funções necessárias são as que foram mostrado em aula
**O que esperamos como resposta:**
> Mande o Link do circuito.
https://www.tinkercad.com/things/eCDRBSrrGCZ/editel?returnTo=%2Fdashboard&sharecode=sJymnKryxtteawaOVNwh_DeFPt-xWbDCT3Nf_NPlgIY