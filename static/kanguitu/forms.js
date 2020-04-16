
   var vetor_provincia = ["Luanda", "Bengo", "Benguela","Bié","Cabinda","Cunene","Huambo","Huila","Cuando Cubango",
   "Cuanza Norte","Cuanza Sul","Lunda Norte","Lunda Sul","Malanje", "Moxico","Namibe","Uige","Zaire"];
   var mascara_bi = ["999999999LA999", "999999999BO999","999999999BA999","999999999BE999", "999999999CA999", "999999999CE999", "999999999HO999",
   "999999999HA999", "999999999CC999", "999999999CN999", "999999999CS999", "999999999LN999", "999999999LS999", "999999999ME999", "999999999MO999",
   "999999999NA999","999999999UE999", "999999999ZE999"];

$('#id_categoria').click(troca_categoria);
$('#id_provincia').click(validar_provinciaBi);
$('#dificiencia_ajax').click(funcao_especifica_dificiencia);



if($('#id_categoria').val() == "DOCENTE") {
    document.getElementById('cat_docente').style.display = '';
}
if($('#id_categoria').val() == "ESTUDANTE") {
    document.getElementById('cat_estudante').style.display = '';
}
if($('#id_categoria').val() == "EFUNCIONARIO") {
    document.getElementById('cat_funcionario').style.display = '';
}

if ($('#dificiencia_ajax').val() == "Sim") {
    document.getElementById('especifica_dificiencia_id').style.display = '';
}


//mascar de inicalização do bi
$("input.bi_mask").mask("999999999LA999");


// troca a a categoria e abre a outra opção na hora de cadastro
function troca_categoria (){
    if ($('#id_categoria').val() == "DOCENTE") {
         document.getElementById('cat_docente').style.display = '';
         document.getElementById('cat_estudante').style.display = 'none';
         document.getElementById('cat_funcionario').style.display = 'none';
     }
     if ($('#id_categoria').val() == "ESTUDANTE") {
          document.getElementById('cat_estudante').style.display = '';
          document.getElementById('cat_docente').style.display = 'none';
          document.getElementById('cat_funcionario').style.display = 'none';

      }
      if ($('#id_categoria').val() == "FUNCIONARIO") {
           document.getElementById('cat_funcionario').style.display = '';
           document.getElementById('cat_estudante').style.display = 'none';
           document.getElementById('cat_docente').style.display = 'none';
       }

}



//função que vai mostra o campo para especifica a dificiencia
function funcao_especifica_dificiencia (){
    if ($('#dificiencia_ajax').val() == "Sim") {
         document.getElementById('especifica_dificiencia_id').style.display = '';
     }
     if ($('#dificiencia_ajax').val() == "Não") {
         document.getElementById('especifica_dificiencia_id').style.display = 'none';

      }

}


// função vai trazr as disciplina de curso qdo estiver a lançar a nota
$('.ajax_curso_nota').click(function () {

  var nova_escolhas = document.getElementById("id_disciplina");
  if($('.ajax_curso_nota').val() > 0 && $('.ajax_ano_nota').val() > 0 && $('.ajax_semestre_nota').val() > 0){
  $.ajax({
      url: '/secretaria/ajax_cursoID_anoID_retorna_disciplinas/',
      type: 'POST',
      data: JSON.stringify({
         'curso': $('.ajax_curso_nota').val(),
          'ano': $('.ajax_ano_nota').val(),
          'semestre': $('.ajax_semestre_nota').val() }),

      dataType: 'json',
      headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
      },
      success: function (data) {

          while (nova_escolhas.options.length) {
              nova_escolhas.remove(0);
          }
          for (let k = 0; k < data.resposta.length; k++) {
              var resp = data.resposta[k];
              var novos = new Option(resp[1], resp[0]);
              nova_escolhas.options.add(novos)
          }
      },
      error: function () {
          console.log('erro interno')
      }
  });
  }else{

  while (nova_escolhas.options.length) {
      nova_escolhas.remove(0);
       }
 }

});


// quando selecionar o ano, para atribuição da nota
$('.ajax_ano_nota').click(function () {

  var nova_escolhas = document.getElementById("id_disciplina");
  if($('.ajax_curso_nota').val() > 0 && $('.ajax_ano_nota').val() > 0 && $('.ajax_semestre_nota').val() > 0){
  $.ajax({
      url: '/secretaria/ajax_cursoID_anoID_retorna_disciplinas/',
      type: 'POST',
      data: JSON.stringify({
         'curso': $('.ajax_curso_nota').val(),
          'ano': $('.ajax_ano_nota').val(),
          'semestre': $('.ajax_semestre_nota').val() }),

      dataType: 'json',
      headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
      },
      success: function (data) {

          while (nova_escolhas.options.length) {
              nova_escolhas.remove(0);
          }
          for (let k = 0; k < data.resposta.length; k++) {
              var resp = data.resposta[k];
              var novos = new Option(resp[1], resp[0]);
              nova_escolhas.options.add(novos)
          }
      },
      error: function () {
          console.log('erro interno')
      }
  });
   }else{

  while (nova_escolhas.options.length) {
      nova_escolhas.remove(0);
       }
 }

});



// quando selecionar o semestre para atrbuir a nota
$('.ajax_semestre_nota').click(function () {

  var nova_escolhas = document.getElementById("id_disciplina");
  if($('.ajax_curso_nota').val() > 0 && $('.ajax_ano_nota').val() > 0 && $('.ajax_semestre_nota').val() > 0){
  $.ajax({
      url: '/secretaria/ajax_cursoID_anoID_retorna_disciplinas/',
      type: 'POST',
      data: JSON.stringify({
         'curso': $('.ajax_curso_nota').val(),
          'ano': $('.ajax_ano_nota').val(),
          'semestre': $('.ajax_semestre_nota').val() }),

      dataType: 'json',
      headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
      },
      success: function (data) {

          while (nova_escolhas.options.length) {
              nova_escolhas.remove(0);
          }
          for (let k = 0; k < data.resposta.length; k++) {
              var resp = data.resposta[k];
              var novos = new Option(resp[1], resp[0]);
              nova_escolhas.options.add(novos)
          }
      },
      error: function () {
          console.log('erro interno')
      }
  });
 }else{

  while (nova_escolhas.options.length) {
      nova_escolhas.remove(0);
       }
 }

});



// função que seleciona a provincia e atrbui a sigla da provincia no campo de BI

function validar_provinciaBi(){
    for (var i = 0; i < vetor_provincia.length; i++) {
        if ($('#id_provincia').val() == vetor_provincia[i]) {
             $("input.bi_mask").mask(mascara_bi[i]);
              break;
            return true;
        }
    }
    $.ajax({

        url:  '/secretaria/municipio_retorna/',
        type:  'POST',
        data: JSON.stringify({'provincia': $('#id_provincia').val()}),
        dataType:  'json',

        success: function (data) {
            var municipio = document.getElementById("id_municipio");
            while (municipio.options.length) {
                municipio.remove(0);
              }
            for (let k = 0; k < data.dados.length; k++) {
                var lista = new Option(data.dados[k], data.dados[k]);
                municipio.options.add(lista);
            }
        },
        error: function(e){
           console.log(e);
        }
    });
   }



  function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');
// Setup ajax connections safetly

   function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
   }

   $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
