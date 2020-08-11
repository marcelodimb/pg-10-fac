(function($) {
    'use strict';

    $(document).ready(function() {
        var datepicker_config = {
            showOn: "button",
            buttonImage: "/static/fac/img/calendar-icon.png",
            buttonImageOnly: true,
            dateFormat: 'dd/mm/yy',
            changeMonth: true,
            changeYear: true,
            dayNames: ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'],
            dayNamesMin: ['D','S','T','Q','Q','S','S','D'],
            dayNamesShort: ['Dom','Seg','Ter','Qua','Qui','Sex','Sáb','Dom'],
            monthNames: ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
            monthNamesShort: ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
        }

        $( "#id_prazo_maximo_devolucao").datepicker(datepicker_config);

        $('[data-type=checkbox-outros]').on('click', function(){
            var elem_outros_id = ('#' + $(this)[0].id).replace('checkbox_', '');

            if ($(this).is(":checked")){
                $(elem_outros_id).show();
            } else if ($(this).is(":not(:checked)")){
                $(elem_outros_id).hide();
            }
        });
    });
})(django.jQuery);
