[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 

# Resistor Color Code Decoding Project
This project is a Python implementation of the IEC 60062 standard for resistor color coding. It decodes the colors of a resistor into its resistance value and tolerance.

## Usage
The script accepts a string in the format "<Resistance Value> <Tolerance>" as an input, for example, "100R 5%". The resistance value and tolerance must be separated by a space.

The output is a list of strings that represent the colors of the resistor's bands.

## Dictionary Definitions
The following dictionaries are used in the script:

<pre>
<code>

dic_cor_f = {0: "Preta", 1: "Marrom", 2: "Vermelha", 3: "Laranja", 4: "Amarela", 5: "Verde",
6: "Azul", 7: "Violeta", 8: "Cinza", 9: "Branca"}

dic_cor_mu = {-3: "Rosa", -2: "Prata", -1: "Dourada", 0: "Preta", 1: "Marrom", 2: "Vermelha", 3: "Laranja", 4: "Amarela", 5: "Verde",
6: "Azul", 7: "Violeta", 8: "Cinza", 9: "Branca"}

dic_cor_t = {20: "Nenhuma", 10: "Prata", 5 : "Dourada", 1: "Marrom", 2: "Vermelha", 0.05: "Laranja", 0.02: "Amarela", 0.5: "Verde",
0.25: "Azul", 0.1: "Violeta", 0.01: "Cinza"}

dic_mu = {"m": -3, "-": 0, "K": 3, "M": 6, "G": 9}

</code>
</pre>

These dictionaries map numbers or characters to their corresponding color.

## Function IEC60062
The main function IEC60062 takes in the resistor string and decodes it into the colors of its bands. The function first splits the input string into the resistance value and tolerance. It then processes the resistance value to obtain the corresponding colors using the dictionaries defined above. The tolerance value is also processed and its corresponding color is obtained. 

The final output is a list of strings representing the colors of the resistor's bands.

## Conclusion
This project provides an easy way to decode the colors of a resistor into its resistance value and tolerance. It follows the IEC 60062 standard and uses dictionaries to map numbers and characters to their corresponding colors.


# Projeto de Código de Cores de Resistores
Este projeto é uma implementação de uma função em Python que retorna as cores correspondentes aos valores de resistência, tensão e tolerância de acordo com o padrão IEC 60062.

## Uso
A função IEC60062 recebe como entrada uma string no formato "valor_de_resistência unidade_de_resistência tolerância". 

Exemplo: "1.2M 5%".

A função retorna uma lista de strings, representando as cores dos anéis na resistência.

## Dicionários
O código possui 4 dicionários com valores pré-definidos:

- dic_cor_f: corresponde às cores dos fatores de resistência (1º e 2º anéis).

- dic_cor_mu: corresponde às cores das unidades de resistência (3º anel).

- dic_cor_t: corresponde às cores da tolerância (4º anel).

- dic_mu: corresponde às unidades de resistência.

## Notas
O formato de entrada deve ser seguido rigorosamente para que a função retorne corretamente as cores.
Caso a entrada seja inválida, a função retornará None.
