from fpdf import FPDF

projeto = input("Informe a descrição do projeto: ")
horasEstimadas= int(input("Digite a quantidade de horas que estima-se para este projeto ? "))
valorHora=float(input("Informe o valor da hora trabalhada R$: "))
prazo=int(input("Qual o prazo de entrega ? "))

valorTotal= horasEstimadas*valorHora
pdf= FPDF()


pdf.add_page()
pdf.set_font("Arial")
pdf.image("template.png", x=0, y=0)
pdf.text(115,145, projeto)
pdf.text(115,160, horasEstimadas)
pdf.text(115,190, prazo)
pdf.text(115,205, str(valorTotal))
pdf.output("Orçamento.pdf")

print("ORÇAMENTO GERADO COM SUCESSO ! ")