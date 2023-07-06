# PyFinance
Sistema de gestão de despesas em uma república de estudantes.

# Concepção
Docente: Flavius Gorgônio
Discente: Alec Can Yalcin

Projeto desenvolvido para avaliação da terceira unidade da matéria DCT1101 no CERES-UFRN.

## Bibliotecas e Ferramentas Utilizadas
1. Virtual Enviroment
- Ferramenta disponibilizada pelo próprio Python, serve para o desenvolvimento interno, faciliza na integração e manipulação de bibliotecas.
2. Bibliotecas Instaladas: TinyDB
- Utilizado para guardar as informações em JSON como um banco de dados em dicionário. Caso utilize o código, não se esqueça de rodar:
> pip install tinydb
3. Bibliotecas Nativas: Os, Webbrouser e Platform
- Somente utilizado para formatação geral do sistema.

# Módulos
O Projeto conta com três módulos: Usuários, Repúblicas e Despesas. Esses módulos atuam em conjunto para a construção da utilidade da ferramenta.
Cada Módulo atua dependentemente do outro. Sendo o nível de Hierarquia: Usuários > Repúblicas > Despesas. 

## Usuários
Os usuários são o módulo que identifica os usuários do programa e os divide entre Estudantes e Proprietários. Estudante é aquele que busca a República, estando apto
a procurar por elas e ter acesso indefinido. Já o Proprietário é dono de uma república e serve somente de referência para a criação e manutenção de uma mesma república. 

Eles possuem algumas propriedades:
> ### Propriedades de Users
> - ```name: String```
> - ```password: String```
> - ```tel: String```
> - ```is_staff: Boolean```
> - ```has_republic: Boolean (False)```
> - ```republic: String (none)```
> - ```bank: Float (0.0)```

Também possuindo algumas funções.
> ### Funções de Users
> - ```login(name: String, password: String)```
>   - ```Retorna "user" como um dicionário.```
> - ```register(name: String, password: String, tel: String, is_staff: Boolean)```
>   - ```Retorna a função login(user).```
> - ```printUser(user: Dictionary)```
>   - ```Não tem retorno. Executa um print que retorna todas as informações do usuário formatadas```
> - ```newName(user: Dictionary, _name: String)```
>   - ```Retorna o dicionário user. Altera o valor do nome do usuário no banco de dados local.```
> - ```newPassword(user: Dictionary, _password: String)```
>   - ```Retorna o dicionário user. Altera o valor da senha do usuário no banco de dados local.```
> - ```newTel(user: Dictionary, _tel: String)```
>   - ```Retorna o dicionário user. Altera o valor do telefone do usuário no banco de dados local.```
> - ```addBank(user: Dictionary, _bank: Float)```
>   - ```Retorna o dicionário user. Adiciona valores float para o valor banco do usuário.```
> - ```userOptions(user: Dictionary)```
>   - ```Retorna int options e dicionário user. Retorna um valor de escolha do usuário.```

## Repúblicas

## Despesas
