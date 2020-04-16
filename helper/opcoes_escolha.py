
# ficheiro de opçoes de escolha de formulario e modelo

PERIODO_MATRICULA = (
    ('Manhã', 'Manhã'),
    ('Tarde', 'Tarde'),
    ('Noite', 'Noite'),

)

PERIODO_MATRICULA2 = (
    ('', '--------'),
    ('Manhã', 'Manhã'),
    ('Tarde', 'Tarde'),
    ('Noite', 'Noite'),

)



TIPOLOGIA =(
    ('Declarações', 'Declarações'),
    ('Plano de Trabalho', 'Plano de Trabalho'),
    ('Propostas', 'Propostas'),
    ('Relatórios', 'Relatórios'),
    ('Ata de Reunião', 'Ata de Reunião'),
    ('Decreto', 'Decreto'),
    ('Contrato', 'Contrato'),
    ('Ofício', 'Ofício'),
    ('Jornal Cientifico', 'Jornal Cientifico'),
    ('Diversos', 'Diversos'),
)

PARTILHA_ARQUIVO =(
    ('APENAS DOCENTE', 'APENAS DOCENTE'),
    ('APENAS ESTUDANTE', 'APENAS ESTUDANTE'),
    ('TODOS', 'TODOS'),
    ('NÃO', 'NÃO'),
)


CATEGORIA_UTILIZADOR =(
    ('estudante', 'estudante'),
    ('gestor', 'Gestor'),
    ('gerente', 'Gerente'),
    ('admin', 'Admin'),

)



INDIVIAL_GRUPO = (
    ('INDIVIDUAL', 'INDIVIDUAL'),
    ('GRUPO', 'GRUPO'),
    ('INDIVIDUAL/GRUPO', 'INDIVIDUAL / GRUPO')
)

GENERO = (
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
)

ESTADO_CIVIL = (
    ('Solteiro (a)', 'solteiro (a)'),
    ('Casado (a)', 'casado (a)'),
    ('Divorciado (a)', 'Divorciado (a)'),
)

DIFICIENCIA = (
    ('', ''),
    ('Sim', 'Sim'),
    ('Não', 'Não'),
)



MOTIVO_RECLAMACAO = (
    ('Falta Nota', 'Falta Nota'),
    ('Nota Não Lançada', 'Nota Não Lançada'),
    ('Propina', 'Propina'),
    ('Prova Não Realizada', 'Prova Não Realizada'),
    ('Acedio Sexual', 'Acedio Sexual'),
    ('Curropção', 'Curropção'),
)

MESES=('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')




PROVINCIA = (
    ('Luanda', 'Luanda'),
    ('Bengo', 'Bengo'),
    ('Benguela', 'Benguela'),
    ('Bié', 'Bié'),
    ('Cabinda', 'Cabinda'),
    ('Cunene', 'Cunene'),
    ('Huambo', 'Huambo'),
    ('Huila', 'Huila'),
    ('Cuando Cubango', 'Cuando Cubango'),
    ('Cuanza Norte', 'Cuanza Norte'),
    ('Cuanza Sul', 'Cuanza Sul'),
    ('Lunda Norte', 'Lunda Norte'),
    ('Lunda Sul', 'Lunda Sul'),
    ('Malanje', 'Malanje'),
    ('Moxico', 'Moxico'),
    ('Namibe', 'Namibe'),
    ('Uige', 'Uige'),
    ('Zaire', 'Zaire'),
)


CATEGORIA = (
    ('ESTUDANTE', 'ESTUDANTE'),
    ('DOCENTE', 'DOCENTE'),
    ('FUNCIONARIO', 'FUNCIONARIO'),

)

NIVEL_DOCENTE = (
    ('Licenciado', 'Licenciado'),
    ('Mestre', 'Mestre'),
    ('Doutor', 'Doutor'),
)

NIVEL_FUNCIONARIO = (
    ('12ª Classe', '12ª Classe'),
    ('13ª Classe', '13ª Classe'),
    ('Têcnico Medio', 'Têcnico Médio'),
    ('Licenciado', 'Licenciado'),
    ('Mestre', 'Mestre'),
    ('Doutor', 'Doutor'),
)


BENGO = ['Ambriz', 'Bula Atumba', 'Dande', 'Dembos', 'Nambuangongo', 'Pango Aluquém']
BENGUELA = ['Balombo', 'Baía Farta', 'Benguela', 'Bocoio', 'Caimbambo', 'Catumbela', 'Chongorói', 'Cubal', 'Ganda', 'Lobito']
BIE = ['Andulo', 'Camacupa, ''Catabola', 'Chinguar', 'Chitembo', 'Cuemba', 'Cunhinga', 'Kuito', 'Nharea']
CABINDA  =['Belize', 'Buco-Zau', 'Cabinda', 'Cacongo']
CUANDO_CUBANGO = ['Calai', 'Cuangar', 'Cuchi', 'Cuito Cuanavale', 'Dirico', 'Longa', 'Mavinga', 'Menongue', 'Nancova', 'Rivungo']
CUNENE = ['Cahama', 'Cuanhama', 'Curoca', 'Cuvelai', 'Namacunde', 'Ombadja']
HUAMBO = ['Bailundo', 'Catchiungo', 'Caála', 'Ekunha', 'Huambo', 'Londuimbale', 'Longonjo', 'Mungo', 'Tchicala-Tcholoanga', 'Tchindjenje', 'Ucuma']
HUILA = ['Caconda', 'Cacula', 'Caluquembe', 'Chiange', 'Chibia', 'Chicomba', 'Chipindo', 'Cuvango', 'Humpata', 'Jamba', 'Lubango', 'Matala', 'Quilengues', 'Quipungo']
CUANZA_NORTE = ['Ambaca', 'Banga', 'Bolongongo', 'Cambambe', 'Cazengo', 'Golungo Alto', 'Gonguembo', 'Lucala', 'Quiculungo', 'Samba Caju']
CUANZA_SUL = ['Amboim', 'Cassongue', 'Cela', 'Conda', 'Ebo', 'Libolo', 'Mussende', 'Porto Amboim', 'Quibala', 'Quilenda', 'Seles', 'Sumbe']
LUANDA = ['Belas', 'Cacuaco', 'Cazenga', 'Ícolo e Bengo', 'Luanda', 'Quiçama', 'Viana']
LUNDA_NORTE = ['Cambulo', 'Capenda-Camulemba', 'Caungula', 'Chitato', 'Cuango', 'Cuílo', 'Lubalo', 'Lucapa', 'Xá-Muteba']
LUNDA_SUL = ['Cacolo', 'Dala', 'Muconda', 'Saurimo']
MALANJE = ['Cacuso', 'Calandula', 'Cambundi-Catembo', 'Cangandala', 'Caombo', 'Cuaba Nzogo', 'Cunda-Dia-Baze', 'Luquembo', 'Malanje', 'Marimba', 'Massango', 'Mucari', 'Quela', 'Quirima']
MOXICO = ['Alto Zambeze', 'Bundas', 'Camanongue', 'Léua', 'Luau', 'Luacano', 'Luchazes', 'Luena', 'Lumeje', 'Moxico']
NAMIBE = ['Bibala', 'Camucuio', 'Moçâmedes', 'Tômbua', 'Virei']
UIGE = ['Alto Cauale', 'Ambuíla', 'Bembe', 'Buengas', 'Bungo', 'Damba', 'Macocola', 'Milunga', 'Mucaba', 'Negage', 'Puri', 'Quimbele', 'Quitexe', 'Sanza Pombo', 'Songo', 'Uíge', 'Zombo']
ZAIRE = ['Cuimba', 'MBanza Kongo', 'Noqui', 'NZeto', 'Soyo', 'Tomboco']
