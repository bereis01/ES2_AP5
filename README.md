# Calculadora Cumulativa [![Tests](https://github.com/bereis01/ES2_AP5/actions/workflows/tests.yml/badge.svg)](https://github.com/bereis01/ES2_AP5/actions/workflows/tests.yml)

Este trabalho prático consiste na **Atividade Prática 5** da disciplina **Engenharia de Software II**. O objetivo consiste em praticar o uso da ferramenta Github Actions no contexto de estudo das práticas de CI/CD e de DevOps em desenvolvimento de software.

Para isso, foi implementado um sistema simples em Python, referente a uma **calculadora cumulativa**. A ideia é que o usuário seja capaz de instanciar a calculadora, invocar funções referentes a operações, para as quais o número a ser operado com o resultado corrente é fornecido, e, ao final, chamar uma função que retorna o resultado da pilha de operações acumulada. Também existe uma funcionalidade simples de reverter a última operação feita e de observar o histórico de resultados.

Além disso, testes para esse código foram elaborados e estão presentes no diretório ```tests/```. Um **workflow** do Github Actions foi configurado para os executar de maneira automática a cada *push* à branch *main*. Essa execução é feita nos sistemas operacionais Linux, MacOS e Windows, e, para cada um, nas versões da linguagem de programação Python de 3.10 a 3.14.
