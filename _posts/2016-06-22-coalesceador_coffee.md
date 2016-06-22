---
layout: post
---

        entrada = 'r.v r_v, j.v j_v, co(i.v) i_v, p.p, k.k as k_k'

        apelido = (div) ->
          if div.length is 3
            div[2]
          else
            div[1]

        print = (msg) ->
          console.log msg

        coalescezar = (aliasado) ->
          aliasado = aliasado.trim()
          if !aliasado.startsWith 'co('
            div = aliasado.split ' '
            if div.length is 1
              aliasado
            else
              "coalesce(#{div[0]}) #{apelido(div)}"
          else
            aliasado

        aliasados = entrada.split(',')
        res = ''
        res+= (coalescezar aliasado) + ', ' for aliasado in aliasados
        print entrada
        print res
