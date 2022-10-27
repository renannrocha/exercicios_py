# exercicio 003 - Dissecando uma variável

dado = input('digite algo ')
print (f'{dado} é numerico : {dado.isnumeric()}')
print (f'{dado} é uma letra : {dado.isalpha()}')
print (f'{dado} é alfanumerico : {dado.isalnum()}')
print (f'{dado} esta só com letras maiusculas :{dado.isupper()}')
print (f'{dado} esta só com letras minusculas :{dado.islower()}')
print (f'{dado} é um titulo :{dado.istitle()}')
print (f'{dado} é um espaço :{dado.isspace()}')
print (f'{dado} é um digito :{dado.isdigit()}')
print (f'{dado} é um numero decimal :{dado.isdecimal()}')
print (f'{dado} é um identificador :{dado.isidentifier()}')
