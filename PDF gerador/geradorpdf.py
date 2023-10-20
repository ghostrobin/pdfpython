print("GERADOR DE ORÇAMENTOS em PDF")

#coletando dados do usuário

projeto = input("Digite a descrição do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")

#Realizando calculo

valor_total = int(horas_previstas)* int(valor_hora)

print(valor_total)

print("Documento gerado com sucesso")

#dados para gerar o PDF

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font('Arial')
pdf.image("template.png", x=0, y=0, w=210, h=297)


pdf.text (115, 145, projeto)
pdf.text (115,160, horas_previstas)
pdf.text (115, 175, valor_hora)
pdf.text (115, 190, prazo)
pdf.text (115, 205, str(valor_total))

pdf.output("Orçamento.pdf")


