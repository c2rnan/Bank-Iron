<h1 align="center">🏦 Banco Iron - Sistema Bancário em Python</h1>

<p align="center">
Sistema bancário desenvolvido em Python com foco em lógica de programação,
estrutura de dados e organização modular.
</p>

<br>

<h2>📌 Sobre o Projeto</h2>

<p>
O <b>Banco Iron</b> é uma aplicação executada no terminal que simula operações
bancárias essenciais. O projeto foi desenvolvido com o objetivo de fortalecer
fundamentos em programação, aplicando regras de negócio reais em um ambiente controlado.
</p>

<p>
A aplicação permite criar contas, realizar movimentações financeiras e acompanhar
o histórico de transações, utilizando <b>dicionários aninhados</b> como estrutura
principal de armazenamento.
</p>

<br>

<h2>🚀 Funcionalidades</h2>

<ul>
<li><b>Criação de Conta:</b> Geração automática de número de conta e cadastro de titular.</li>
<li><b>Depósito:</b> Atualização de saldo com validação de valor positivo.</li>
<li><b>Saque:</b> Validação de saldo suficiente antes da retirada.</li>
<li><b>Consulta de Saldo:</b> Exibição formatada com duas casas decimais.</li>
<li><b>Histórico de Movimentações:</b> Registro completo de depósitos e saques.</li>
<li><b>Menu Interativo:</b> Controle de fluxo contínuo até encerramento do sistema.</li>
</ul>

<br>

<h2>🧠 Estrutura de Dados</h2>

<p>As contas são armazenadas em um dicionário principal chamado <b>banco</b>:</p>

<pre>
{
    numero_conta: {
        "Titular": "Nome do Cliente",
        "Saldo": 0.00,
        "Historico": []
    }
}
</pre>

<p>
Essa estrutura permite acesso direto por número de conta e atualização dinâmica
das informações financeiras.
</p>

<br>

<h2>⚙️ Regras de Negócio Implementadas</h2>

<ul>
<li>Não permite depósito com valor menor ou igual a zero.</li>
<li>Não permite saque com valor menor ou igual a zero.</li>
<li>Impede saque superior ao saldo disponível.</li>
<li>Valida existência da conta antes de qualquer operação.</li>
<li>Registra todas as movimentações no histórico.</li>
</ul>

<br>

<h2>🛠️ Tecnologias Utilizadas</h2>

<ul>
<li><b>Python 3</b></li>
<li>Estruturas de dados (dicionários)</li>
<li>Funções</li>
<li>Estruturas condicionais</li>
<li>Laços de repetição</li>
<li>F-strings para formatação monetária</li>
</ul>

<br>

<h2>🎯 Objetivo do Projeto</h2>

<p>
Consolidar conhecimentos em lógica de programação e simular a construção
de um sistema funcional aplicando princípios fundamentais de desenvolvimento back-end.
</p>

<br>

<h2>👨‍💻 Autor</h2>

<p>
<b>Caio Renan</b><br>
Desenvolvedor em formação com foco em back-end e estruturação de sistemas.
</p>
