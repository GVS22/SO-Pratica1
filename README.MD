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
Como Funciona o Pipeline MIPS
O pipeline MIPS usado aqui é um modelo de pipeline de cinco estágios. Cada instrução passa pelos seguintes estágios:

IF (Instruction Fetch): Carrega a instrução da memória.
ID (Instruction Decode): Decodifica a instrução e identifica os registradores.
EX (Execute): Executa a operação aritmética ou lógica.
MEM (Memory Access): Acessa a memória, se necessário, para operações LOAD e STORE.
WB (Write Back): Escreve o resultado da operação no registrador de destino.
Cada estágio é tratado de forma sequencial no simulador, mas os estágios são organizados de forma que várias instruções possam avançar simultaneamente ao longo do pipeline. Isso significa que enquanto uma instrução está no estágio EX, uma nova pode começar em IF.

Como Usar o Simulador
1. Clonar o Repositório
Primeiro, clone o repositório em sua máquina local:

bash
Copiar código
git clone https://github.com/GVS22/SO-Pratica1.git
cd SO-Pratica1
2. Configurar os Arquivos de Entrada
Certifique-se de que a pasta data/ contenha dois arquivos de entrada essenciais:

Instructions.txt: Contém as instruções a serem executadas, uma por linha, no formato:

plaintext
Copiar código
OPERACAO, REGISTRADOR_DESTINO, REGISTRADOR_1, REGISTRADOR_2
Exemplo:

plaintext
Copiar código
ADD, 8, 1, 2
SUB, 9, 8, 3
BEQ, 12, 6, 7
JUMP, 14, 0, 0
setRegisters.txt: Define os valores iniciais dos registradores no formato:

plaintext
Copiar código
REGISTRADOR, VALOR
Exemplo:

plaintext
Copiar código
1,20
2,10
3,5
6,15
7,15
3. Executar o Simulador
Com os arquivos Instructions.txt e setRegisters.txt preparados, execute o simulador:

bash
Copiar código
python3 main.py
O simulador exibirá o estado do pipeline a cada ciclo, mostrando cada estágio (IF, ID, EX, MEM, WB) e o resultado após cada instrução.

Explicação dos Componentes do Código
main.py
O arquivo main.py é o ponto de entrada do programa. Ele instancia a classe Simulator e executa o método run, que processa as instruções através do pipeline. O código carrega os arquivos de entrada e inicia o processo de simulação.

simulator.py
A classe Simulator integra todos os componentes (CPU, Memória, Pipeline) e coordena a execução das instruções. Ele carrega os valores iniciais dos registradores e as instruções de entrada e passa cada instrução pelo pipeline.

Principais Métodos:

__init__: Configura o simulador, inicializando CPU, memória e pipeline.
run: Processa cada instrução no pipeline, exibindo o estado dos registradores e da memória após cada ciclo.
cpu.py
Define a classe CPU, que contém os registradores e implementa a lógica para executar cada instrução (ADD, SUB, MULT, DIV, BEQ, JUMP, LOAD, STORE). Este componente simula o núcleo de processamento.

Principais Métodos:

execute_instruction: Executa a instrução específica, modificando o registrador de destino com base na operação.
__str__: Retorna uma string com o estado dos registradores, útil para depuração.
memory.py
A classe Memory simula a memória principal. Ela armazena dados em um vetor e permite operações de leitura e escrita em posições de memória específicas. Atualmente, as operações LOAD e STORE são configuradas para operar entre registradores e não utilizam a memória principal.

Principais Métodos:

read: Lê o valor de uma posição de memória.
write: Escreve um valor em uma posição de memória.
__str__: Exibe um estado parcial da memória para facilitar a depuração.
pipeline.py
O pipeline gerencia os estágios de execução de cada instrução. Ele contém cinco estágios (IF, ID, EX, MEM, WB) e uma fila de instruções (instruction_queue). A cada ciclo, uma instrução avança para o próximo estágio, até que todas as instruções completem o pipeline.

Principais Métodos:

add_instruction: Adiciona uma nova instrução ao pipeline.
process_pipeline: Simula o avanço de instruções pelos cinco estágios do pipeline, processando a execução no estágio MEM.
utils.py
O arquivo utils.py contém funções auxiliares para carregar as instruções (Instructions.txt) e os valores iniciais dos registradores (setRegisters.txt) a partir dos arquivos.

Principais Funções:

load_registers: Lê e retorna um dicionário com os valores iniciais dos registradores.
load_instructions: Lê e retorna uma lista com as instruções a serem executadas.
Como o Pipeline é Simulado
Para simular o pipeline, o código executa cada estágio sequencialmente para cada instrução, mas organiza as instruções de forma que várias delas possam avançar no pipeline a cada ciclo.

Fila de Instruções: O pipeline usa uma fila (instruction_queue) onde as instruções aguardam para avançar nos estágios.
Processamento por Estágio: Cada instrução passa pelos estágios IF, ID, EX, MEM, e WB. Enquanto uma instrução avança para o próximo estágio, outra pode iniciar o pipeline, simulando o processamento paralelo.
Finalização: Quando uma instrução completa o estágio WB, ela é removida da fila, simulando a finalização de sua execução.
