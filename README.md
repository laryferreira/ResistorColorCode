[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 

# Projeto APC - 05/02/2023 - 1º semestre
Projeto final na disciplina Algoritimos e Programação de Computadores da Universidade de Brasília.

## Finalidade:

Esse código atribui uma função chamada IEC60062 que recebe um argumento de string chamado "resistência" e retorna uma lista de strings que representam os códigos de cores para esse valor de resistência de acordo com o padrão IEC 60062.

A função primeiro divide a string de entrada em duas partes: "FM" e "T". "FM" representa o valor da resistência e "T" representa a tolerância. A função então usa dicionários (dic_cor_f, dic_cor_mu e dic_cor_t) para mapear o valor de resistência e tolerância para seus códigos de cores correspondentes.

A função então calcula o valor da resistência multiplicando o valor da resistência (F) pela potência apropriada de 10 (M) determinada pelo dicionário dic_mu.

Finalmente, a função usa os dicionários para procurar os códigos de cores para cada parte do valor de resistência (F, M e T) e os adiciona a uma lista de códigos de cores. Em seguida, ele retorna essa lista como a saída da função.

## Casos de teste:
Para usar a função IEC60062, basta importá-la do repositório e chamá-la com uma string no formato FMT. Por exemplo:
<pre>
<code>
from IEC60062 import IEC60062

print(IEC60062('1- 10')) = ['Marrom', 'Preta', 'Dourada', 'Prata']
print(IEC60062('2.70M 0.01')) = ['Vermelha', 'Violeta', 'Preta', 'Amarela', 'Cinza']
print(IEC60062('13m 0.02')) = ['Marrom', 'Laranja', 'Rosa', 'Amarela']
</code>
</pre>

<img src="https://suntsu.com/wp-content/uploads/2021/10/Resistor-Code-Chart.png"/>

## Usage:

This repository contains a Python function called IEC60062 that takes a string representing the value of a resistor in FMT format and returns a list of colors that can be used to print the value of the resistor according to the IEC 60062 standard.

The FMT format consists of three parts:

F: A real number with up to 2 places of precision, representing the resistance value. Always will have a blank space between F and M. <br>
M: The multiple of the ohm measurement unit, such as m (milli-ohms), (for 1 ohm), K (kilo-ohms), M (mega-ohms), G (Giga-ohms). <br>
T: The tolerance value in percentage. <br>
The IEC60062 function uses the first 2 or 3 colors to represent the resistance value, the next color to define the order of magnitude, and the last color to define the resistance tolerance percentage. It is guaranteed that the smallest possible value for a resistance is 10m ohm

## Test cases:
To use the IEC60062 function, just import it from the repository and call it with a string in FMT format. For example:
<pre>
<code>
from IEC60062 import IEC60062

print(IEC60062('1- 10')) = ['Brown', 'Black', 'Gold', 'Silver']
print(IEC60062('2.70M 0.01')) = ['Red', 'Violet', 'Black', 'Yellow', 'Grey']
print(IEC60062('13m 0.02')) = ['Brown', 'Orange', 'Pink', 'Yellow']
</code>
</pre>

