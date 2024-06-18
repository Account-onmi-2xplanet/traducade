# Projeto TraduCADE

## Descrição
O Projeto TraduCADE é focado na tradução de documentos legais e oficiais do CADE (Conselho Administrativo de Defesa Econômica do Brasil), com o objetivo de gerar versões precisas e referendadas em inglês. Utilizamos tecnologias de Processamento de Linguagem Natural (PLN), especificamente o modelo T5 da Google, para automatizar o processo inicial de tradução.

## Motivação
A necessidade de traduções precisas e consistentes em contextos legais é crítica. Por isso, optamos por usar o modelo de PLN T5, que é altamente eficaz para tarefas de tradução devido à sua capacidade de entender e processar nuances linguísticas complexas.

## Dados Ostensivos
Todos os documentos utilizados neste projeto são ostensivos, ou seja, de domínio público e não confidenciais. Isso garante que não há restrições de direitos autorais ou de confidencialidade envolvidos no uso, compartilhamento ou processamento desses documentos. [Fonte dos dados](https://www.gov.br/cade/pt-br/centrais-de-conteudo/publicacoes-institucionais/guias-do-cade)

## Escolha do Modelo: T5 e T5-Base
O modelo T5 (Text-to-Text Transfer Transformer) foi escolhido por sua versatilidade e eficácia em tarefas de tradução text-to-text. Optamos pela variante T5-Base devido ao seu equilíbrio entre desempenho e uso eficiente de recursos computacionais, permitindo a tradução de documentos de forma rápida e com um alto nível de precisão.

### Funcionalidades do T5-Base
- **Capacidade de Tradução**: Converte textos de uma língua para outra com alta fidelidade.
- **Ajuste Fino**: Permite ajustes específicos para lidar com a linguagem técnica e legal dos documentos do CADE.
- **Eficiência**: Oferece uma boa performance em máquinas com recursos moderados.

## Processo

### Passo 1: Preparação dos Documentos
Os documentos são inicialmente baixados e convertidos para texto utilizando o script Python localizado em [bulk_pdf_to_txt.py](/bulk_pdf_to_txt.py). Este script automatiza o download e a extração de texto de arquivos PDF disponíveis nos sites oficiais. Usando as bibliotecas requests e pdfplumber, o script  eficientemente transforma os documentos PDF em formatos de texto puro, preparando-os para a próxima fase de curadoria manual.

Este primeiro passo é crucial para garantir que os dados estejam prontos e acessíveis para revisões detalhadas e ajustes de precisão nos textos.

### Passo 2: Curadoria de Dados e Preparação de Textos

Após a conversão inicial dos documentos PDF para texto, procedemos com uma etapa essencial de curadoria de dados. Nesta fase, revisamos manualmente os textos gerados para assegurar que as versões em português e inglês reflitam de maneira fiel e equilibrada o conteúdo dos documentos originais. Esse cuidado meticuloso garante que ambos os conjuntos de textos estejam alinhados e isentos de discrepâncias ou distorções que possam afetar a fidelidade e a integridade das traduções.

Os textos cuidadosamente tratados são então salvos na pasta txt_files_human_treated, preparando o caminho para a próxima fase de tradução automática. Esta organização facilita a gestão eficiente dos dados e otimiza o fluxo de trabalho subsequente de tradução e revisão.

### Passo 3: Tradução Automática
Utilizamos o modelo T5-Base para traduzir o texto do português para o inglês. Esta tradução serve como uma primeira versão, que é depois refinada.

### Passo 4: Ajuste Humano
Após a tradução automática, iniciamos a fase de ajuste humano. Esta etapa é crucial para assegurar que as versões em texto nos idiomas português e inglês sejam equivalentes em termos de precisão e estilo. Durante o ajuste, revisores bilingues comparam as versões e fazem correções manuais para garantir que o texto traduzido seja fiel ao original em todos os aspectos técnicos e legais.

### Passo 4: Revisão Final
A versão final do documento é revisada e certificada por um especialista para garantir sua conformidade e adequação ao uso oficial e público.

## Como Contribuir

Para contribuir para este projeto, siga estas etapas:

1. **Fork** este repositório.
2. **Clone** o repositório forkado para sua máquina local.
3. **Crie uma branch** para suas alterações.
4. **Faça suas alterações** e commit suas contribuições.
5. **Push** suas alterações para sua fork.
6. Crie um **Pull Request** para propor suas alterações no repositório original.

Agradecemos suas contribuições para aperfeiçoar este projeto!

## Licença
Este projeto está licenciado sob a Licença MIT, que é amplamente utilizada para projetos de código aberto. Esta licença permite reutilização, modificação e distribuição para fins não comerciais e comerciais, desde que o crédito apropriado seja dado ao autor original. 
