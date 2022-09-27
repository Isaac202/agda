$(function(){
    $(document).ready(function() {
        $('#cpf').mask('000.000.000-00', { reverse: true });
        $('.telefone').mask('(00) 0 0000-0000');
        var SPMaskBehavior = function(val) {
                return val.replace(/\D/g, '').length === 11 ? '(00) 0 0000-0000' : '(00) 0000-00009';
            },
            spOptions = {
                onKeyPress: function(val, e, field, options) {
                    field.mask(SPMaskBehavior.apply({}, arguments), options);
                }
            };
    
        $('#telefone').mask(SPMaskBehavior, spOptions);
        $('#inputTelefone').mask(SPMaskBehavior, spOptions);
    
    })
    
})




function verificaForcaSenha() 
{
	var numeros = /([0-9])/;
	var alfabeto = /([a-zA-Z])/;
	var chEspeciais = /([~,!,@,#,$,%,^,&,*,-,_,+,=,?,>,<])/;

	if($('.password').val().length<8) 
	{
		$('.password-status').html("<span style='color:red'>Senha fraca, insira no mínimo 8 caracteres</span>");
	} else {  	
		if($('.password').val().match(numeros) && $('.password').val().match(alfabeto) && $('.password').val().match(chEspeciais))
		{            
			$('.password-status').html("<span style='color:green'><b>Senha forte</b></span>");
		} else {
			$('.password-status').html("<span style='color:orange'>Senha média, insira um caracter especial</span>");
		}
	}
}

// function validarSenhas()
// {
//     if ($("#password").val() !== $("#password2").val()){
//         console.log($("#password").val(),$("#password2").val())
//         $('.password-status-senha2').html("<span style='color:red'>Senha diferente da primeira</span>");
//     }
// }



$(function(){
    $(".cadastrar_cliente").submit(function(e){
        e.preventDefault()
        var form = $(this)
        $.ajax({
            beforeSend:function(){
                $(".loader").fadeIn()
            },
            url:"cadastrar_cliente",
            method:"POST",
            dataType:"json",
            data:form.serialize()
        }).done(function(data){
            console.log(data.tipo_status)
            
            if (data.sucesso){
                $(".loader").fadeOut()
                window.location.href ='/login'
            }
            if (data.tipo_status){
                console.log(data)
                alert(data.Mensagem)
                $(".loader").fadeOut()
                
            }
        })
        
    })

    // $("form_login").submit(function(e){
    //     e.preventDefault()
    //     var form = $(this)
    //     $.ajax({
    //         beforeSend:function(){
    //             $(".loader").fadeIn()
    //         },
    //         url:"entrar",
    //         method:"POST",
    //         dataType:"json",
    //         data:form.serialize()
    //     }).done(function(data){
    //         if (data.sucesso){
    //             $(".loader").fadeOut()
    //             window.location.href ='/'
    //         }
    //     })
    // })
})


$(document).ready(function(){
          
    $('.date').mask('00/00/0000');
    $('.time').mask('00:00:00');
    $('.date_time').mask('00/00/0000 00:00:00');
    $('.cep').mask('00000-000');
    $('.phone').mask('0000-0000');
    $('.cod').mask('0000');
    $('#telefone').mask('(00) 0000-0000');
    $('.phone_us').mask('(000) 000-0000');
    $('.mixed').mask('AAA 000-S0S');
    $('.cpf').mask('000.000.000-00', {reverse: true});
    $('.cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('#numero_cartao').mask('0000 0000 0000 0000', {reverse: true});
    $('.money2').mask("#.##0,00", {reverse: true});
    $('.ip_address').mask('0ZZ.0ZZ.0ZZ.0ZZ', {
      translation: {
        'Z': {
          pattern: /[0-9]/, optional: true
        }
      }
    });
    $('.ip_address').mask('099.099.099.099');
    $('.percent').mask('##0,00%', {reverse: true});
    $('.clear-if-not-match').mask("00/00/0000", {clearIfNotMatch: true});
    $('.placeholder').mask("00/00/0000", {placeholder: "__/__/____"});
    $('.fallback').mask("00r00r0000", {
        translation: {
          'r': {
            pattern: /[\/]/,
            fallback: '/'
          },
          placeholder: "__/__/____"
        }
      });
    $('.selectonfocus').mask("00/00/0000", {selectOnFocus: true});
  });


  $(".pix_label").click(()=>{
    $(".pix_label").addClass("botoes_metodos_ativo")
    $(".cartao_label").removeClass("botoes_metodos_ativo")
    $(".metodo_cartao").css("display","none")
    $(".forma_pix").css("display","flex")
  })

  $(".cartao_label").click(()=>{
    $(".metodo_cartao").removeClass("none")
    $(".cartao_label").addClass("botoes_metodos_ativo")
    $(".pix_label").removeClass("botoes_metodos_ativo")
    $(".forma_pix").css("display","none")
    $(".metodo_cartao").css("display","flex")
  })