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

# Ideias e Módulos

O sistema contra com três módulos: Autenticação(Authentication), Despesas(Finances),Receita(Receipt) e Republica(republics). O Principal objetivo do sistema é facilitar o pagamento das despesas, assim facilitando a vida do usuário. Contudo, um dos módulos adicionais serve para facilitar outros estudantes a encontarem despesas nas quais eles podem participar da renda e/ou tenham uma boa localização para eles.

## Authentication

Se refere aos usuários da república de estudante, os próprios moradores. Com funções para adicionar e retirar esses mesmos estudantes, curso, matrícula...

Existem alguns tipos de autenticação especiais: A do proprietário e dos estudantes.

1. A do proprietário
serve somente para ele ter controle sobre a república, cobrar as despesas e receber o dinheiro da receitas essenciais dos estudantes. Aquelas que o proprietário pode registrar como fixas.

2. A do estudante
Serve para os estudantes terem ideia das finanças, além das fixas, e registrá-las para que todos os outros estudantes tenham ideia do que se está acontecendo.

## Finances

Se refere as próprias despesas, nome, custo, tempo de vencimento, receita disponível suficiente.

Existem dois tipos de finanças para a república: Finanças Fixas e Variáveis.

1. Fixas
refere-se a finanças que sempre deverão estar em dia para a continuidade dos estudantes dentro daquela república acessando os serviços: Água e Energia são exemplos

2. Variáveis
refere-se a finanças que surgem de necessidades dos estudantes e que não necessariamente precisam ser cobradas em um determinado tempo. Tais como gás, confortos, alimentação entre outros.

## Receipt

Se refere e receita da república, provinda dos próprios estudantes ou de um meio externo. Essa receita pode ser diretamente retirada das contas dos estudantes ou adicionadas por meio de doações externas.

## Republics

Se refere as repúblicas dos estudantes. Afim de fiscalizar e prezar pela manutenção do sistema, diferentes república poderão utilizar-se do sistema.

As repúblicas informam se há vagas para aquela república se um estudante quiser entrar nela. Também informa dos custos a se pagar para participar ativamente daquela república.

## API Rest

O sistema utilizará de APIs para guardar as informações disponíveis e também para gravá-las.