import os
import requests
import pdfplumber

# Lista de URLs dos arquivos PDF
urls = [
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/guia-para-analise-de-atos-de-concentracao-horizontal.pdf",
    "http://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/Guide-for-Horizontal-Merger-Review.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/gun-jumping-versao-final.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/guideline-gun-jumping-september.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/guia-compliance-versao-oficial.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/compliance-guidelines-final-version.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/guia-tcc-atualizado-11-09-17.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/guidelines_tcc-1.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/Guia-do-Programa-de-Leniencia-do-Cade_Vers%C3%A3o_Atualizada.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/guidelines-cades-antitrust-leniency-program-2020.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/guia-remedios.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/Guide-Antitrust-Remedies.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/guia-de-combate-a-carteis-em-licitacao-versao-final-1.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/guide-for-fighting-cartels-in-procurements_version_01-10.pdf",
    "https://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/Guia-recomendacoes-probatorias-para-proposta-de-acordo-de-leniencia-com-o-Cade.pdf",
    "http://cdn.cade.gov.br/Portal/centrais-de-conteudo/publicacoes/guias-do-cade/Guide-Parameters-for-submitting-evidence-in-leniency-applications-Atualizado.pdf"
]

def download_pdf(url):
    """Baixa um arquivo PDF da URL fornecida."""
    response = requests.get(url)
    if response.status_code == 200:
        # Obtém o nome do arquivo do último segmento da URL
        filename = url.split('/')[-1]
        # Salva o arquivo PDF
        with open(filename, 'wb') as f:
            f.write(response.content)
        return filename
    else:
        print(f"Erro ao baixar o arquivo: {url}")
        return None

def convert_pdf_to_text(pdf_path):
    """Converte um arquivo PDF em um arquivo de texto com o mesmo nome base."""
    text_output = pdf_path.replace('.pdf', '.txt')
    all_text = ''
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                all_text += page.extract_text() or ''
        with open(text_output, 'w', encoding='utf-8') as f:
            f.write(all_text)
    except Exception as e:
        print(f"Erro ao processar o arquivo: {pdf_path}, {e}")

def main():
    for url in urls:
        pdf_file = download_pdf(url)
        if pdf_file:
            convert_pdf_to_text(pdf_file)
            os.remove(pdf_file)  # Remove o arquivo PDF após a conversão

if __name__ == '__main__':
    main()