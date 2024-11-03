# Simulador da Arquitetura de Von Neumann com Pipeline MIPS

## Descrição do Projeto
Este projeto é um simulador de um pipeline MIPS básico na arquitetura de Von Neumann, desenvolvido em Python. A arquitetura de Von Neumann utiliza uma única memória para armazenar dados e instruções, e o pipeline MIPS permite processar múltiplas instruções simultaneamente em diferentes estágios, otimizando a execução.

O objetivo deste projeto é simular o fluxo de instruções através de um pipeline com cinco estágios. Esse pipeline fatiado permite que uma instrução entre no pipeline a cada ciclo de relógio e avance etapa por etapa, enquanto novas instruções continuam a ser adicionadas. Este simulador é especialmente útil para compreender como a CPU gerencia múltiplas instruções ao mesmo tempo e para visualizar o impacto das instruções aritméticas, condicionais e de salto na arquitetura MIPS.

## Funcionalidades
- **Pipeline MIPS de 5 estágios**: Cada instrução passa pelos cinco estágios clássicos do pipeline MIPS: IF, ID, EX, MEM, WB.
- **Suporte a Operações Aritméticas**: ADD, SUB, MULT, DIV.
- **Instruções de Controle de Fluxo**: BEQ (desvio condicional) e JUMP (salto incondicional).
- **Operações de Transferência entre Registradores**: LOAD e STORE, para movimentação de dados entre registradores.
- **Organização Modular do Código**: Dividido em arquivos para CPU, memória, pipeline, simulador principal e funções utilitárias, o que torna o código organizado e de fácil manutenção.

## Estrutura do Projeto
A estrutura do projeto foi cuidadosamente organizada para modularizar cada componente e manter o código limpo e fácil de entender. Aqui está a disposição das pastas e arquivos:

```plaintext
von_neumann_pipeline_simulator/
├── data/
│   ├── Instructions.txt      # Arquivo de instruções
│   └── setRegisters.txt      # Arquivo de valores iniciais dos registradores
├── src/
│   ├── cpu.py                # Classe CPU para operações de instruções
│   ├── memory.py             # Classe Memory para simulação de armazenamento de dados
│   ├── pipeline.py           # Classe Pipeline para gerenciar estágios de execução
│   ├── simulator.py          # Classe Simulator que integra CPU, memória e pipeline
│   └── utils.py              # Funções utilitárias para carregar arquivos
├── README.md                 # Documentação do projeto
└── main.py                   # Script principal para execução do simulador

## Como Funciona o Pipeline MIPS
O pipeline MIPS usado aqui é um modelo de pipeline de cinco estágios. Cada instrução passa pelos seguintes estágios:

- **IF (Instruction Fetch): Carrega a instrução da memória.
- **ID (Instruction Decode): Decodifica a instrução e identifica os registradores.
- **EX (Execute): Executa a operação aritmética ou lógica.
- **MEM (Memory Access): Acessa a memória, se necessário, para operações LOAD e STORE.
- **WB (Write Back): Escreve o resultado da operação no registrador de destino.
Cada estágio é tratado de forma sequencial no simulador, mas os estágios são organizados de forma que várias instruções possam avançar simultaneamente ao longo do pipeline. Isso significa que enquanto uma instrução está no estágio EX, uma nova pode começar em IF.
