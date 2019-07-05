
   var vetor_provincia = ["Luanda", "Bengo", "Benguela","Bié","Cabinda","Cunene","Huambo","Huila","Cuando Cubango",
   "Cuanza Norte","Cuanza Sul","Lunda Norte","Lunda Sul","Malanje", "Moxico","Namibe","Uige","Zaire"];
   var mascara_bi = ["999999999LA999", "999999999BO999","999999999BA999","999999999BE999", "999999999CA999", "999999999CE999", "999999999HO999",
   "999999999HA999", "999999999CC999", "999999999CN999", "999999999CS999", "999999999LN999", "999999999LS999", "999999999ME999", "999999999MO999",
   "999999999NA999","999999999UE999", "999999999ZE999"];

$('#id_categoria').click(troca_categoria);
$('#id_provincia').click(validar_provinciaBi);

if($('#id_categoria').val() == "DOCENTE") {
    document.getElementById('cat_docente').style.display = '';
}
if($('#id_categoria').val() == "ESTUDANTE") {
    document.getElementById('cat_estudante').style.display = '';
}
if($('#id_categoria').val() == "EFUNCIONARIO") {
    document.getElementById('cat_funcionario').style.display = '';
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
