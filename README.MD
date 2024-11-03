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

 

## 2. Configurar os Arquivos de Entrada
Certifique-se de que a pasta `data/` contenha dois arquivos de entrada essenciais:

- **Instructions.txt**: Contém as instruções a serem executadas, uma por linha, no formato:

    ```
    OPERACAO, REGISTRADOR_DESTINO, REGISTRADOR_1, REGISTRADOR_2
    ```

    **Exemplo:**

    ```
    ADD, 8, 1, 2
    SUB, 9, 8, 3
    BEQ, 12, 6, 7
    JUMP, 14, 0, 0
    ```

- **setRegisters.txt**: Define os valores iniciais dos registradores no formato:

    ```
    REGISTRADOR, VALOR
    ```

    **Exemplo:**

    ```
    1,20
    2,10
    3,5
    6,15
    7,15
    ```

## 3. Executar o Simulador
Com os arquivos `Instructions.txt` e `setRegisters.txt` preparados, execute o simulador:

```bash
python3 main.py
