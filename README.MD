Simulador da Arquitetura de Von Neumann com Pipeline MIPS
Descrição do Projeto
Este projeto é um simulador da Arquitetura de Von Neumann com um pipeline MIPS básico, desenvolvido em Python. A arquitetura de Von Neumann, que usa uma única memória compartilhada para dados e instruções, é fundamental para os sistemas computacionais modernos. Esse simulador é uma ferramenta educacional que permite observar como instruções são carregadas, decodificadas, executadas e como os resultados são armazenados.

Funcionalidades
Execução em Pipeline: Cada instrução passa pelos cinco estágios clássicos de um pipeline MIPS: IF, ID, EX, MEM, WB.
Operações Básicas: Suporta operações aritméticas (ADD, SUB, MULT, DIV), operações de carregamento e armazenamento (LOAD, STORE), e instruções de controle de fluxo (BEQ, JUMP).
Interface Modular: A arquitetura do código é dividida em módulos, facilitando a manutenção e expansão.
Estrutura do Projeto
plaintext
Copiar código
von_neumann_pipeline_simulator/
├── data/
│   ├── Instructions.txt      # Arquivo de instruções
│   └── setRegisters.txt      # Arquivo de valores iniciais dos registradores
├── src/
│   ├── cpu.py                # Classe CPU com operações de instruções
│   ├── memory.py             # Classe Memory para armazenamento de dados
│   ├── pipeline.py           # Classe Pipeline para gerenciar estágios de execução
│   ├── simulator.py          # Classe Simulator que integra CPU, memória e pipeline
│   └── utils.py              # Funções utilitárias para carregar arquivos
├── README.md                 # Documentação do projeto
└── main.py                   # Script principal para execução do simulador
data/: Contém os arquivos com as instruções e os valores iniciais dos registradores.
src/: Contém o código-fonte organizado por módulos, cada um responsável por uma parte específica do simulador.
main.py: O ponto de entrada do simulador.
Como Funciona
Arquivos de Entrada
Instructions.txt: Contém as instruções a serem executadas pelo simulador, uma por linha, no formato:

mathematica
Copiar código
OPERAÇÃO, REGISTRADOR_DESTINO, REGISTRADOR_1, REGISTRADOR_2
Exemplo:
plaintext
Copiar código
ADD, 1, 2, 3
SUB, 4, 1, 3
STORE, 3, 2, 0
LOAD, 0, 2, 0
BEQ, 7, 3, 4
JUMP, 8, 0, 0
setRegisters.txt: Define os valores iniciais dos registradores no formato:

Copiar código
REGISTRADOR, VALOR
Exemplo:
plaintext
Copiar código
2,10
3,5
4,7
Esses arquivos devem estar na pasta data/ para que o simulador possa acessá-los.

Pipeline MIPS
O pipeline MIPS implementado neste simulador segue os cinco estágios clássicos:

IF (Instruction Fetch): Carrega a instrução da memória.
ID (Instruction Decode): Decodifica a instrução e prepara os registradores.
EX (Execute): Executa a operação aritmética ou lógica.
MEM (Memory Access): Acessa a memória para operações LOAD e STORE.
WB (Write Back): Escreve o resultado no registrador de destino.
Cada instrução passa por esses estágios, permitindo a execução paralela de instruções em diferentes estágios do pipeline.

Instruções para Execução
Clonar o Repositório

Clone o repositório para o seu ambiente local:

bash
Copiar código
git clone https://github.com/seu-usuario/von_neumann_pipeline_simulator.git
cd von_neumann_pipeline_simulator
Instalação dos Requisitos

Não há dependências externas para este projeto, apenas Python 3.8+.

Configuração dos Arquivos de Entrada

Certifique-se de que os arquivos Instructions.txt e setRegisters.txt estão na pasta data/. Esses arquivos contêm as instruções a serem executadas e os valores iniciais dos registradores, respectivamente.

Executar o Simulador

Execute o script principal:

bash
Copiar código
python3 main.py
Exemplo de Saída
Durante a execução, o simulador exibirá o estado dos registradores e da memória a cada estágio do pipeline. Aqui está um exemplo de saída esperada:

plaintext
Copiar código
IF: Processing ['ADD', '1', '2', '3']
ID: Decoding ['ADD', '1', '2', '3']
EX: Executing ADD on registers 2 and 3
MEM: Accessing memory if needed for ['ADD', '1', '2', '3']
WB: Writing result to register 1
PC: 1, Registers: {0: 0, 1: 15, 2: 10, 3: 5, ...}
Memory: [0, 0, 0, ...]
Explicação dos Módulos
1. cpu.py
Define a classe CPU, que é responsável por:

Armazenar o valor dos registradores e o contador de programa (PC).
Executar as operações de instruções, como ADD, SUB, LOAD, STORE, etc.
Controlar o fluxo das instruções com operações de salto (BEQ, JUMP).
2. memory.py
A classe Memory simula a memória principal do sistema.

Permite operações de leitura e escrita.
A memória é representada por uma lista de tamanho fixo.
3. pipeline.py
A classe Pipeline gerencia os estágios de execução das instruções:

Stages: Define os cinco estágios do pipeline (IF, ID, EX, MEM, WB).
Queue: Armazena e processa as instruções em uma fila FIFO.
Remove a instrução do pipeline apenas após o estágio WB.
4. utils.py
Funções utilitárias para carregar os arquivos de instruções e registradores iniciais.

load_registers: Carrega valores iniciais dos registradores a partir de setRegisters.txt.
load_instructions: Carrega as instruções a partir de Instructions.txt.
5. simulator.py
A classe Simulator integra CPU, memória e pipeline.

Carrega as instruções e valores iniciais dos registradores.
Processa cada instrução e executa o pipeline.
Exibe o estado final dos registradores e da memória após a execução.
6. main.py
O ponto de entrada do simulador, que inicializa e executa o processo completo:

Carrega arquivos de dados.
Inicializa o simulador.
Executa o pipeline e exibe os resultados.
Possíveis Expansões
Aqui estão algumas ideias para expandir o simulador no futuro:

Instruções Adicionais: Adicionar mais operações aritméticas e lógicas.
Gerenciamento de Memória: Simular cache e diferentes políticas de substituição.
Multithreading: Permitir simulação de múltiplos núcleos, com registradores independentes para cada núcleo.
Visualização Gráfica: Integrar uma interface gráfica para visualizar os estágios do pipeline.
Conclusão
Este simulador é uma ferramenta educacional que permite explorar os fundamentos da Arquitetura de Von Neumann e do pipeline MIPS. Ele mostra como instruções são executadas em um pipeline e permite observar o impacto de diferentes operações sobre o estado dos registradores e da memória.



