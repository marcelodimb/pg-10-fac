import calendar
import time

from django.http import HttpResponse
from django.shortcuts import render

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

from .forms import FACForm


def index(request):
    if request.method == 'POST':
        form = FACForm(request.POST)

        if form.is_valid():
            response = generate_pdf(form)
            return response
    else:
        form = FACForm()

    context = {
        'form': form
    }

    return render(request, 'fac/index.html', context)


def generate_pdf(form):
    filename = 'report-%s.pdf' % (calendar.timegm(time.gmtime()))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s"' % (filename)

    pdf = canvas.Canvas(response)

    pdf.setTitle('FORMULÁRIO DE ANÁLISE CONTÁBIL - Anexo VIII')

    pdf.drawInlineImage('fac/static/fac/img/brasao-estado-rio-de-janeiro-thumbnail.jpg', 275, 763)

    pdf.setFont('Helvetica-Bold', 10)
    pdf.drawCentredString(300, 751, 'Procuradoria Trabalhista - PG-10')
    pdf.drawCentredString(300, 736, 'FORMULÁRIO DE ANÁLISE CONTÁBIL - Anexo VIII')

    pdf.rect(48, 30, 522, 692, stroke=1, fill=0)

    pdf.setFont('Helvetica-Bold', 8)
    pdf.drawString(50, 710, 'Para: Assessoria de Cálculos e Perícias Contábeis - ACPC')
    pdf.drawString(50, 696, 'PROCESSO ADM N.º ' + form.cleaned_data['num_processo_adm'])
    pdf.drawString(50, 683, 'Analisar: cálculos de fls. ' + form.cleaned_data['calculos_fls_pa'])
    pdf.drawString(195, 683, 'do PA ou fls. ' + form.cleaned_data['calculos_fls_judicial'])
    pdf.drawString(310, 683, 'do Judicial')
    pdf.drawString(382, 683, ('(   X   )' if form.cleaned_data['processo_eletronico'] is True else '(        )') + ' Processo eletrônico.')
    pdf.drawString(50, 669, 'Prazo máximo para devolução: ' + form.cleaned_data['prazo_maximo_devolucao'].strftime("%d/%m/%Y"))

    pdf.setFont('Helvetica', 8)
    pdf.drawString(50, 655, 'Em: ' + form.cleaned_data['data_preenchimento'].strftime("%d/%m/%Y"))
    pdf.drawString(237, 655, 'Assinatura e carimbo do Solicitante:')
    pdf.setLineWidth(inch * 0.005)
    pdf.line(367, 655, 530, 655)

    pdf.setFont('Helvetica-Bold', 8)
    pdf.drawString(50, 633, '1) Composição do principal a apurar:')
    pdf.setFont('Helvetica', 8)

    pdf.rect(48, 618, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 621, ('X' if form.cleaned_data['comp_princ_ap_salario_devido'] is True else ''))
    pdf.drawString(89, 621, 'Salário Devido')

    pdf.rect(48, 606, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 609, ('X' if form.cleaned_data['comp_princ_ap_diferenca_salarial'] is True else ''))
    pdf.drawString(89, 609, 'Diferença Salarial')

    pdf.rect(48, 594, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 597, ('X' if form.cleaned_data['comp_princ_ap_reflexo_salarial'] is True else ''))
    pdf.drawString(89, 597, 'Reflexo Salarial')

    pdf.rect(48, 582, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 585, ('X' if form.cleaned_data['comp_princ_ap_horas_extras'] is True else ''))
    pdf.drawString(89, 585, 'Horas Extras')

    pdf.rect(48, 570, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 573, ('X' if form.cleaned_data['comp_princ_ap_horas_noturnas'] is True else ''))
    pdf.drawString(89, 573, 'Horas Noturnas')

    pdf.rect(48, 558, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 561, ('X' if form.cleaned_data['comp_princ_ap_adicionais_ins_per'] is True else ''))
    pdf.drawString(89, 561, 'Adicionais( Insalub./Pericul.)')

    pdf.rect(48, 546, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 549, ('X' if form.cleaned_data['comp_princ_ap_fgts'] is True else ''))
    pdf.drawString(89, 549, 'FGTS')

    pdf.rect(48, 534, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 537, ('X' if form.cleaned_data['comp_princ_ap_multa_40_perc_fgts'] is True else ''))
    pdf.drawString(89, 537, 'Multa de 40% do FGTS')

    pdf.rect(207, 618, 40, 12, stroke=1, fill=0)
    pdf.drawString(225, 621, ('X' if form.cleaned_data['comp_princ_ap_dec_terc_salario'] is True else ''))
    pdf.drawString(248, 621, '13º Salário')

    pdf.rect(207, 606, 40, 12, stroke=1, fill=0)
    pdf.drawString(225, 609, ('X' if form.cleaned_data['comp_princ_ap_ferias_1_3'] is True else ''))
    pdf.drawString(248, 609, 'Férias + 1/3')

    pdf.rect(207, 594, 40, 12, stroke=1, fill=0)
    pdf.drawString(225, 597, ('X' if form.cleaned_data['comp_princ_ap_aviso_previo'] is True else ''))
    pdf.drawString(248, 597, 'Aviso Prévio')

    pdf.rect(207, 582, 40, 12, stroke=1, fill=0)
    pdf.drawString(225, 585, ('X' if form.cleaned_data['comp_princ_ap_multa_art_477_clt'] is True else ''))
    pdf.drawString(248, 585, 'Multa Art. 477 CLT')

    pdf.rect(207, 570, 40, 12, stroke=1, fill=0)
    pdf.drawString(225, 573, ('X' if form.cleaned_data['comp_princ_ap_multa_art_467_clt'] is True else ''))
    pdf.drawString(248, 573, 'Multa Art. 467 CLT')

    pdf.rect(207, 558, 40, 12, stroke=1, fill=0)
    pdf.drawString(225, 561, ('X' if form.cleaned_data['comp_princ_ap_vale_transporte'] is True else ''))
    pdf.drawString(248, 561, 'Vale Transporte')

    pdf.rect(207, 546, 40, 12, stroke=1, fill=0)
    pdf.drawString(225, 549, ('X' if form.cleaned_data['comp_princ_ap_vale_refeicão'] is True else ''))
    pdf.drawString(248, 549, 'Vale Refeição')

    pdf.rect(207, 534, 40, 12, stroke=1, fill=0)
    pdf.drawString(225, 537, ('X' if form.cleaned_data['comp_princ_ap_licencas_mat_pat_outras'] is True else ''))
    pdf.drawString(248, 537, 'Licenças ( Mater./Patern/Outras)')

    pdf.rect(379, 618, 40, 12, stroke=1, fill=0)
    pdf.drawString(397, 621, ('X' if form.cleaned_data['comp_princ_ap_adicional_proj_especial'] is True else ''))
    pdf.drawString(420, 621, 'Adicional Proj. Especial')

    pdf.rect(379, 606, 40, 12, stroke=1, fill=0)
    pdf.drawString(397, 609, ('X' if form.cleaned_data['comp_princ_ap_pcs_2000_2001'] is True else ''))
    pdf.drawString(420, 609, 'PCS 2000/2001 (9,85% e 14,04%)')

    pdf.rect(379, 594, 40, 12, stroke=1, fill=0)
    pdf.drawString(397, 597, ('X' if form.cleaned_data['comp_princ_ap_equiparacao_salarial'] is True else ''))
    pdf.drawString(420, 597, 'Equiparação Salarial')

    pdf.rect(379, 582, 40, 12, stroke=1, fill=0)
    pdf.drawString(397, 585, ('X' if form.cleaned_data['comp_princ_ap_premio_maquinista'] is True else ''))
    pdf.drawString(420, 585, 'Premio Maquinista')

    pdf.rect(379, 570, 40, 12, stroke=1, fill=0)
    pdf.drawString(397, 573, ('X' if form.cleaned_data['comp_princ_ap_passivo_trabalhista'] is True else ''))
    pdf.drawString(420, 573, 'Passivo Trabalhista')

    pdf.rect(379, 558, 40, 12, stroke=1, fill=0)
    pdf.drawString(397, 561, ('X' if form.cleaned_data['comp_princ_ap_pcs_1990'] is True else ''))
    pdf.drawString(420, 561, 'PCS /1990 (antiguidade e merecimento)')

    pdf.rect(379, 546, 40, 12, stroke=1, fill=0)
    pdf.drawString(397, 549, ('X' if form.cleaned_data['comp_princ_ap_outros'] is True else ''))
    pdf.drawString(420, 549, 'Outros:')

    pdf.setFont('Helvetica-Bold', 8)
    pdf.drawString(50, 505, '2) Indicação das fls. contendo as decisões processuais:')
    pdf.setFont('Helvetica', 8)

    pdf.drawString(50, 493, 'Decisões de 1o grau (sentença):')
    pdf.drawString(315, 493, 'Fls. ' + form.cleaned_data['fls_decisoes_1_grau_sentenca'])

    pdf.drawString(50, 480, 'Decisão de 1o grau sobre Embargos:')
    pdf.drawString(315, 480, 'Fls. ' + form.cleaned_data['fls_decisao_1_grau_embargos'])

    pdf.drawString(50, 467, 'Decisões de 2o grau (Acórdãos):')
    pdf.drawString(315, 467, 'Fls. ' + form.cleaned_data['fls_decisoes_2_grau_acordaos'])

    pdf.drawString(50, 454, 'Decisão de 2o grau sobre Embargos:')
    pdf.drawString(315, 454, 'Fls. ' + form.cleaned_data['fls_decisao_2_grau_embargos'])

    pdf.setFont('Helvetica-Bold', 8)
    pdf.drawString(50, 425, '3) Período da execução:')
    pdf.setFont('Helvetica', 8)

    pdf.drawString(50, 410, ('(   X   )' if form.cleaned_data['periodo_execucao'] == "1" else '(        )') + ' O mesmo apurado nos cálculos objeto da análise.')
    pdf.drawString(50, 395, ('(   X   )' if form.cleaned_data['periodo_execucao'] == "2" else '(        )') + ' Data da Primeira parcela Devida:')
    pdf.drawString(50, 380, ('(   X   )' if form.cleaned_data['periodo_execucao'] == "3" else '(        )') + ' Outros:')

    pdf.setFont('Helvetica-Bold', 8)
    pdf.drawString(50, 353, '4) Correção Monetária:')
    pdf.drawString(50, 340, '4.1) Indique o(s) Indexador(es):')
    pdf.setFont('Helvetica', 8)

    pdf.drawString(50, 327, ('(   X   )' if form.cleaned_data['correcao_monetaria_indexadores'] == "1" else '(        )') + ' Índices da caderneta de poupança TR. (Súmula no 381 do TST)')
    pdf.drawString(50, 313, ('(   X   )' if form.cleaned_data['correcao_monetaria_indexadores'] == "2" else '(        )') + ' IPCA-E a partir de 26/03/2015 ( Decisão STF na ADI n.o 4357)')
    pdf.drawString(50, 300, ('(   X   )' if form.cleaned_data['correcao_monetaria_indexadores'] == "3" else '(        )') + ' Outros:')

    pdf.setFont('Helvetica-Bold', 8)
    pdf.drawString(50, 287, '4.2) A partir:')
    pdf.setFont('Helvetica', 8)

    pdf.drawString(50, 274, ('(   X   )' if form.cleaned_data['correcao_monetaria_a_partir'] == "1" else '(        )') + ' Do mês subsequente ao do vencimento')
    pdf.drawString(50, 261, ('(   X   )' if form.cleaned_data['correcao_monetaria_a_partir'] == "2" else '(        )') + ' Do transito em julgado')
    pdf.drawString(288, 274, ('(   X   )' if form.cleaned_data['correcao_monetaria_a_partir'] == "3" else '(        )') + ' Sentença/Acórdão')
    pdf.drawString(288, 261, ('(   X   )' if form.cleaned_data['correcao_monetaria_a_partir'] == "4" else '(        )') + ' Outros:')

    pdf.setFont('Helvetica-Bold', 8)
    pdf.drawString(50, 237, '5) Juros de mora:')
    pdf.drawString(50, 226, '5.1) Porcentagem e/ou Orientação Legal:')
    pdf.setFont('Helvetica', 8)

    pdf.rect(48, 211, 40, 12, stroke=1, fill=0)
    # pdf.drawString(66, 214, ('X' if form.cleaned_data['juros_mora_porcentagem'] == "1") else '')
    pdf.drawString(66, 214, ('X' if form.cleaned_data['juros_mora_porcentagem'] == "1" else ''))
    pdf.drawString(89, 214, '1% a m, capitalizado (Decreto-Lei 2322/87)')

    pdf.rect(48, 199, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 202, ('X' if form.cleaned_data['juros_mora_porcentagem'] == "2" else ''))
    pdf.drawString(89, 202, '1% a m, simples (Lei 8177/91)')

    pdf.rect(48, 187, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 190, ('X' if form.cleaned_data['juros_mora_porcentagem'] == "3" else ''))
    pdf.drawString(89, 190, 'OJ no 7 do TST')

    pdf.rect(48, 175, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 178, ('X' if form.cleaned_data['juros_mora_porcentagem'] == "4" else ''))
    pdf.drawString(89, 178, 'Súmula 304 do TST')

    pdf.rect(48, 163, 40, 12, stroke=1, fill=0)
    pdf.drawString(66, 166, ('X' if form.cleaned_data['juros_mora_porcentagem'] == "5" else ''))
    pdf.drawString(89, 166, 'Art. 100 da CF')

    pdf.setFont('Helvetica-Bold', 8)
    pdf.drawString(50, 149, '5.2) A partir:')
    pdf.setFont('Helvetica', 8)

    pdf.drawString(50, 135, ('(   X   )' if form.cleaned_data['juros_mora_a_partir'] == "1" else '(        )') + ' Do Ajuizamento')
    pdf.drawString(50, 122, ('(   X   )' if form.cleaned_data['juros_mora_a_partir'] == "2" else '(        )') + ' Do transito em julgado')
    pdf.drawString(300, 135, ('(   X   )' if form.cleaned_data['juros_mora_a_partir'] == "3" else '(        )') + ' Sentença/Acórdão')
    pdf.drawString(300, 122, ('(   X   )' if form.cleaned_data['juros_mora_a_partir'] == "4" else '(        )') + ' Outros:')

    pdf.setFont('Helvetica-Bold', 8)
    pdf.drawString(50, 99, '6) Observações ou orientações complementares:')
    pdf.setFont('Helvetica', 8)

    pdf.drawString(50, 84, form.cleaned_data['observacoes_orientacoes_complementares'])

    pdf.showPage()
    pdf.save()

    return response
