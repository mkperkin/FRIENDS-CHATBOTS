from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re


e_regex1 = re.compile("(.*?)Opening Credits(.*?)\n", flags=re.IGNORECASE)
e_regex2 = re.compile("(.*?)Commericial Break(.*?)\n", flags=re.IGNORECASE)
e_regex3 = re.compile("(.*?)Closing Credits(.*?)\n", flags=re.IGNORECASE)
e_regex4 = re.compile("(\s)*End(\s)*\n", flags=re.IGNORECASE)
e_regex5 = re.compile("(.*?)Opening titles(.*?)\n", flags=re.IGNORECASE)


english = [e_regex1, e_regex2, e_regex3, e_regex4, e_regex5]




e_regex1s = re.compile("(.*?)CREDITOS DEL PRINCIPIO(.*?)\n", flags=re.IGNORECASE)
e_regex2s = re.compile("(.*?)CORTE PUBLICITARIO(.*?)\n", flags=re.IGNORECASE)
e_regex3s = re.compile("(.*?)CREDITOS DEL FINAL(.*?)\n", flags=re.IGNORECASE)
e_regex4s = re.compile("(\s)*FIN(\s)*\n", flags=re.IGNORECASE)
e_regex5s = re.compile("(.*?)PAUSA COMERCIAL(.*?)\n", flags=re.IGNORECASE)
e_regex6s = re.compile("(.*?)TITULOS DE APERTURA(.*?)\n", flags=re.IGNORECASE)
e_regex7s = re.compile("(.*?)CREDITOS FINALES(.*?)\n", flags=re.IGNORECASE)
e_regex8s = re.compile("(.*?)CREDITOS INICIALES(.*?)\n", flags=re.IGNORECASE)
e_regex9s = re.compile("(.*?)CORTE COMERCIAL(.*?)\n", flags=re.IGNORECASE)


spanish = [e_regex1s, e_regex2s, e_regex3s, e_regex4s,
          e_regex5s, e_regex6s, e_regex7s, e_regex8s, e_regex9s]
