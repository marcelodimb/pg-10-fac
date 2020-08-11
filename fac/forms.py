from django import forms
import datetime


class FACForm(forms.Form):
    num_processo_adm = forms.CharField(
        label='PROCESSO ADM N.º',
        max_length=100,
        required=True
    )
    calculos_fls_pa = forms.CharField(
        label='do PA',
        max_length=6,
        required=True
    )
    calculos_fls_judicial = forms.CharField(
        label='do Judicial',
        max_length=6,
        required=True
    )
    processo_eletronico = forms.BooleanField(
        label='Processo Eletrônico',
        required=False
    )
    prazo_maximo_devolucao = forms.DateField(
        label='Prazo máximo para devolução',
        required=True
    )
    data_preenchimento = forms.DateField(
        label='Em',
        initial=datetime.date.today,
        disabled=True
    )
    comp_princ_ap_salario_devido = forms.BooleanField(
        label='Salário Devido',
        required=False
    )
    comp_princ_ap_dec_terc_salario = forms.BooleanField(
        label='13º Salário',
        required=False
    )
    comp_princ_ap_adicional_proj_especial = forms.BooleanField(
        label='Adicional Proj. Especial',
        required=False
    )
    comp_princ_ap_diferenca_salarial = forms.BooleanField(
        label='Diferença Salarial',
        required=False
    )
    comp_princ_ap_ferias_1_3 = forms.BooleanField(
        label='Férias + 1/3',
        required=False
    )
    comp_princ_ap_pcs_2000_2001 = forms.BooleanField(
        label='PCS 2000/2001 (9,85% e 14,04%)',
        required=False
    )
    comp_princ_ap_reflexo_salarial = forms.BooleanField(
        label='Reflexo Salarial',
        required=False
    )
    comp_princ_ap_aviso_previo = forms.BooleanField(
        label='Aviso Prévio',
        required=False
    )
    comp_princ_ap_equiparacao_salarial = forms.BooleanField(
        label='Equiparação Salarial',
        required=False
    )
    comp_princ_ap_horas_extras = forms.BooleanField(
        label='Horas Extras',
        required=False
    )
    comp_princ_ap_multa_art_477_clt = forms.BooleanField(
        label='Multa Art. 477 CLT',
        required=False
    )
    comp_princ_ap_premio_maquinista = forms.BooleanField(
        label='Premio Maquinista',
        required=False
    )
    comp_princ_ap_horas_noturnas = forms.BooleanField(
        label='Horas Noturnas',
        required=False
    )
    comp_princ_ap_multa_art_467_clt = forms.BooleanField(
        label='Multa Art. 467 CLT',
        required=False
    )
    comp_princ_ap_passivo_trabalhista = forms.BooleanField(
        label='Passivo Trabalhista',
        required=False
    )
    comp_princ_ap_adicionais_ins_per = forms.BooleanField(
        label='Adicionais( Insalub./Pericul.)',
        required=False
    )
    comp_princ_ap_vale_transporte = forms.BooleanField(
        label='Vale Transporte',
        required=False
    )
    comp_princ_ap_pcs_1990 = forms.BooleanField(
        label='PCS /1990 (antiguidade e merecimento)',
        required=False
    )
    comp_princ_ap_fgts = forms.BooleanField(
        label='FGTS',
        required=False
    )
    comp_princ_ap_vale_refeicão = forms.BooleanField(
        label='Vale Refeição',
        required=False
    )
    comp_princ_ap_outros = forms.BooleanField(
        label='Outros',
        required=False
    )
    comp_princ_ap_multa_40_perc_fgts = forms.BooleanField(
        label='Multa de 40% do FGTS',
        required=False
    )
    comp_princ_ap_licencas_mat_pat_outras = forms.BooleanField(
        label='Licenças ( Mater./Patern/Outras)',
        required=False
    )
    fls_decisoes_1_grau_sentenca = forms.CharField(
        label='Decisões de 1º grau (sentença)',
        max_length=6,
        required=False
    )
    fls_decisao_1_grau_embargos = forms.CharField(
        label='Decisão de 1º grau sobre Embargos',
        max_length=6,
        required=False
    )
    fls_decisoes_2_grau_acordaos = forms.CharField(
        label='Decisões de 2º grau (Acórdãos)',
        max_length=6,
        required=False
    )
    fls_decisao_2_grau_embargos = forms.CharField(
        label='Decisão de 2º grau sobre Embargos',
        max_length=6,
        required=False
    )
    per_exec_mesmo_apurado_calculos = forms.BooleanField(
        label='O mesmo apurado nos cálculos objeto da análise',
        required=False
    )
    """
    per_exec_data_primeira_parc = forms.DateField(
        label='Data da Primeira parcela Devida',
        required=False
    )
    per_exec_data_ultima_parc = forms.DateField(
        label='Data da Última parcela Devida',
        required=False
    )
    per_exec_outros = forms.CharField(
        label='Outros',
        max_length=100,
        required=False
    )
    indexadores_indice_cp = forms.BooleanField(
        label='Indices da caderneta de poupança TR. (Súmula no 381 do TST)',
        required=False
    )
    indexadores_ipca = forms.BooleanField(
        label='IPCA-E a partir de 26/03/2015 ( Decisão STF na ADI n.o 4357)',
        required=False
    )
    indexadores_outros = forms.CharField(
        label='Outros',
        max_length=100,
        required=False
    )
    indexadores_a_partir_mes_sub_venc = forms.BooleanField(
        label='Do mês subsequente ao do vencimento',
        required=False
    )
    indexadores_a_partir_trans_julg = forms.DateField(
        label='Do transito em julgado',
        required=False
    )
    indexadores_a_partir_set_acord = forms.DateField(
        label='Sentença/Acórdão',
        required=False
    )
    indexadores_a_partir_outros = forms.CharField(
        label='Outros',
        max_length=100,
        required=False
    )
    """
    CHOICES_PERIODO_EXECUCAO = [
        ('1', 'O mesmo apurado nos cálculos objeto da análise.'),
        ('2', 'Data da Primeira parcela Devida:'),
        ('3', 'Outros')
    ]

    periodo_execucao = forms.ChoiceField(
        label='',
        choices=CHOICES_PERIODO_EXECUCAO, widget=forms.RadioSelect,
        required=False
    )

    CHOICES_CORRECAO_MONETARIA_INDEXADORES = [
        ('1', 'Índices da caderneta de poupança TR. (Súmula no 381 do TST)'),
        ('2', 'IPCA-E a partir de 26/03/2015 ( Decisão STF na ADI n.o 4357)'),
        ('3', 'Outros')
    ]

    correcao_monetaria_indexadores = forms.ChoiceField(
        label='',
        choices=CHOICES_CORRECAO_MONETARIA_INDEXADORES, widget=forms.RadioSelect,
        required=False
    )

    CHOICES_CORRECAO_MONETARIA_A_PARTIR = [
        ('1', 'Do mês subsequente ao do vencimento'),
        ('2', 'Do transito em julgado'),
        ('3', 'Sentença/Acórdão'),
        ('4', 'Outros')
    ]

    correcao_monetaria_a_partir = forms.ChoiceField(
        label='',
        choices=CHOICES_CORRECAO_MONETARIA_A_PARTIR, widget=forms.RadioSelect,
        required=False
    )

    CHOICES_JUROS_MORA_PORCENTAGEM = [
        ('1', '1% a m, capitalizado (Decreto-Lei 2322/87)'),
        ('2', '1% a m, simples (Lei 8177/91)'),
        ('3', 'OJ no 7 do TST'),
        ('4', 'Súmula 304 do TST'),
        ('5', 'Art. 100 da CF')
    ]

    juros_mora_porcentagem = forms.ChoiceField(
        label='',
        choices=CHOICES_JUROS_MORA_PORCENTAGEM, widget=forms.RadioSelect,
        required=False
    )

    CHOICES_JUROS_MORA_A_PARTIR = [
        ('1', 'Do Ajuizamento'),
        ('2', 'Do transito em julgado'),
        ('3', 'Sentença/Acórdão'),
        ('4', 'Outros')
    ]

    juros_mora_a_partir = forms.ChoiceField(
        label='',
        choices=CHOICES_JUROS_MORA_A_PARTIR, widget=forms.RadioSelect,
        required=False
    )
    """
    juros_mora_a_partir_ajuizamento = forms.DateField(
        label='Do Ajuizamento',
        required=False
    )
    juros_mora_a_partir_trans_julg = forms.DateField(
        label='Do transito em julgado',
        required=False
    )
    juros_mora_a_partir_sent_acord = forms.DateField(
        label='Sentença/Acórdão',
        required=False
    )
    juros_mora_a_partir_outros = forms.CharField(
        label='Outros',
        max_length=100,
        required=False
    )
    """
    observacoes_orientacoes_complementares = forms.CharField(
        label='',
        max_length=255,
        widget=forms.Textarea(),
        required=False
    )
