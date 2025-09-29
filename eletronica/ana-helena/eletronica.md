# Nivelamento em Eletrônica

## Objetivo

> Descreva aqui o objetivo desta etapa do processo seletivo.

## Atividades

### Questão 1

> Explique por que é importante observar a polaridade de componentes como LED, capacitores eletrolíticos e baterias em um circuito. O que pode acontecer se a polaridade for invertida?


**O que esperamos como resposta:**

> Os componentes eletrônicos normalmente tem as suas polaridades bem definidas e funcionam apenas quando são posicionados no lugar correto. Caso os componentes forem colocados de maneira errada, esses aparelhos podem sofrer alguns danos, tanto de funcionamento (prejudicando o funcionamento momentaneamente), sofrer danos fisicos do maquinário que esse componente está contido (danos irreversíveis como perda de demais componentes), além de tudo, o perigo correlacionado com esse uso errôneo, como com a possibilidade de incêndio. 
---

### Questão 2

> Um LED é alimentado por uma fonte de 9 V através de um resistor de 330 Ω.
 a) Qual é a corrente que circula pelo resistor?
 b) Se o LED cair a tensão de 2 V, qual será a tensão no resistor e a corrente real?\
(Use V = R·I)
 
     Vled = 2V (LED vermelho)
    Vfinal = 9V - 2V = 7V
     V = R * I --> 7= 330 * I --> I = 7/330--> I = 21,2 mA
    

**O que esperamos como resposta:**

> a)   V = R * I --> 9= 330 * I --> I = 9/330--> I = 27mA

  b)   Vled = 2V (LED vermelho)       Vfinal = 9V - 2V = 7V
      V = R * I --> 7= 330 * I --> I = 7/330--> I = 21,2 mA

---
### Questão 3

>  Explique em suas palavras a diferença entre um circuito puramente analógico e um circuito com microcontrolador (Arduino).
Dê um exemplo de cada tipo.

**O que esperamos como resposta:**

> Circuito analógico: Funciona apenas com componentes como resistores, capacitores e transistores, sem necessidade de programação. Ex.: um controle de volume usando potenciômetro.

Circuito com Arduino: Utiliza um microcontrolador programável, que pode tomar decisões a partir de sensores. Ex.: Dectar um obstáculo e desviar dele

---
### Questão 4

>  Explique o que é um divisor de tensão e como ele funciona. Dê um exemplo prático de onde um divisor de tensão pode ser utilizado em um circuito eletrônico.

**O que esperamos como resposta:**

> Um divisor de tensão é um circuito formado por dois resistores em série, onde a tensão de saída é uma fração da tensão de entrada. Ele funciona pela divisão proporcional da tensão de acordo com os valores dos resistores.

Exemplo prático: reduzir 9 V para ~4,5 V usando dois resistores iguais de 1 kΩ, para alimentar um sensor que não pode receber tensão maior que 5 V.

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

> O comando analogWrite(9, 128) gera um sinal PWM (modulação por largura de pulso) com 50% de ciclo ativo (pois 128 é metade do valor máximo 255). Assim, o LED ficará aceso com metade do brilho máximo, como se estivesse “meio aceso”.

---
### Questão 6
> Um motor DC de 5 V precisa de 0,3 A para funcionar. Você só tem uma fonte de 9 V. Qual deve ser a resistência em série para limitar a corrente a 0,3 A?

**O que esperamos como resposta:**

> Vr​ = 9−5 = 4V
R = Vr/I ​​= 4/0,3 ​≈ 13,3Ω

Resposta: Aproximadamente 13Ω
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

Agora com 4A:
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

https://www.tinkercad.com/things/biejkl9j1dQ/editel?returnTo=%2Fdashboard&sharecode=yb_iDMobcl_Ckg-yzb8aiGDZZAN9WiPsO2HkACDSLig
