# candy-box-problem

## Muito obrigado pela visita!

Este repositório é destinado a todos que possuem o interesse de aprender um 
pouco mais sobre como utilizar ferramentas de otimização matemática para tornar
suas vidas muito mais simplex. Nele você tem acesso aos slides usados para a 
apresentação, assim como o código do exemplo apresentado. 

A pasta [quadratic_formulation](quadratic_formulation) contém a formulação 
quadratica para o problema (formulação apresentada na palestra). Entretanto, 
para resolver esse problema se faz necessário a instalação de um solver com 
capacidade de resolver um problema quadrático. Tarefa que pode ser um tanto 
difícil e tediosa. Caso você tenha interesse, recomenda-se a instalação do 
[Bonmin](https://www.coin-or.org/Bonmin/).

Já a pasta [linear_formulation](linear_formulation) contém a formulação linear 
do mesmo problema. Apesar de, em alguns casos, apresentar um comportamento um 
pouco diferente da formulação quadrática, o modelo linear pode ser resolvido 
com solvers menos complexos, como o [glpk](https://www.gnu.org/software/glpk/),
que já vem instalado juntamente com algumas distribuições do linux.

Para os mais interessados, propõe-se os seguintes desafios:

0. Como seria a formulação matemática do problema de divisão de bombons se 
existissem 3 crianças? Como seria a formulação no Pyomo?

0. Como seria a formulação matemática do problema se existissem um número 
qualquer n de crianças? Como seria a formulação no Pyomo?

0. Como seria a formulação matemática do problema se cada criança pudesse dar
um valor de "gostosura" diferente pra cada bombom? Como seria a formulação no 
Pyomo?

