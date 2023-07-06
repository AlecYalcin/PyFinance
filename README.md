# PyFinance
Sistema de gestão de despesas em uma república de estudantes

# Concepção
Docente: Flavius Gorgônio
Discente: Alec Can Yalcin

Projeto desenvolvido para avaliação da terceira unidade da matéria DCT1101 no CERES-UFRN.

## Bibliotecas e Ferramentas Utilizadas
1. Virtual Enviroment
Ferramenta disponibilizada pelo próprio Python, serve para o desenvolvimento interno, faciliza na integração e manipulação de bibliotecas.
2. TinyDB
Utilizado para guardar as informações em JSON como um banco de dados em dicionário.
3. Os, Webbrouser e Platform
Somente utilizado para formatação geral do sistema.

# Ideias e Módulos

O sistema contra com três módulos: Autenticação(Authentication), Despesas(Finances) e Republica(republics). O Principal objetivo do sistema é facilitar o pagamento das despesas, assim facilitando a vida do usuário. Contudo, um dos módulos adicionais serve para facilitar outros estudantes a encontarem despesas nas quais eles podem participar da renda e/ou tenham uma boa localização para eles.

## Authentication

Se refere aos usuários da república de estudante, os próprios moradores. Com funções para adicionar e retirar esses mesmos estudantes, curso, matrícula...

Existem alguns tipos de autenticação especiais: A do proprietário e dos estudantes.

1. A do proprietário
serve somente para ele ter controle sobre a república, cobrar as despesas e receber o dinheiro da receitas essenciais dos estudantes. Aquelas que o proprietário pode registrar como fixas.

2. A do estudante
Serve para os estudantes terem ideia das finanças, além das fixas, e registrá-las para que todos os outros estudantes tenham ideia do que se está acontecendo.

## Finances

Se refere as próprias despesas, nome, custo, receita disponível suficiente.

## Republics

Se refere as repúblicas dos estudantes. Afim de fiscalizar e prezar pela manutenção do sistema, diferentes república poderão utilizar-se do sistema.

As repúblicas informam se há vagas para aquela república se um estudante quiser entrar nela. Também informa dos custos a se pagar para participar ativamente daquela república.