import streamlit as st
import pandas as pd


q = []

st.titlte('Барои синфи 9. Саволнома оид ба муайян кардани шавқу рағбат Супордани тест')

st.subheader('Аз 15 саволи зерин кадомаш ба шумо маъқул аст')

q1  = st.radio(
     "",
     ('Ҳал намудани масъалаҳои мураккаби математикӣ.', 'Тайёр кардани маҳлулҳо, омехтани реактивҳо.', 'Омўзиши хусусиятҳои ҷараёнҳои физиологӣ, дар организмҳои гуногун.', 'Ҷамъ овардани намудҳои гуногуни маъданҳо (минералҳо).',  'Сохтани (ширеш кардани) модели самолётҳо, ҳавопаймоҳо', 'Иҷро кардани кор бо истифода аз асбобҳои ченкунӣ ва санҷишӣ.', 'Мутолиа намудани асарҳои классикони адабиёти ҷаҳон.', 'Мутолиа кардани асарҳо дар бораи фаъолияти кормандони умури дохила, мубориза бо вайронкунандагони қонун.', 'Шинос шудан ба таърих ва ҳунарҳои халқии Тоҷикистон.', 'Мутолиа кардани китобҳо дар бораи кори омўзгорон.', 'Мутолиа кардани китобу, маҷаллаҳои тиббӣ ва дар бораи фаъолияти духтурон.', 'Тозаю озода нигоҳ  доштани манзил.', 'Мутолиа кардани адабиёти ҳарбӣ.', ' Шунидани мусиқии  классикӣ.', '  Мутолиа кардани китобҳо дар бораи рассомҳо.'))
if q1 == 'Ҳал кардани  масъалаҳои математикӣ ва ҳисобҳои мураккаби математикӣ.':
    q.append('1')
if q1 == 'Тайёр кардани маҳлулҳо, омехтани реактивҳо.':
    q.append('2')
if q1 == 'Омўзиши хусусиятҳои ҷараёнҳои физиологӣ, дар организмҳои гуногун.':
    q.append('3')
if q1 == 'Ҷамъ овардани намудҳои гуногуни маъданҳо (минералҳо).':
    q.append('4')
if q1 == 'Сохтани (ширеш кардани) модели самолётҳо, ҳавопаймоҳо.':
    q.append('5')
if q1 == 'Иҷро кардани кор бо истифода аз асбобҳои ченкунӣ ва санҷишӣ.':
    q.append('6')
if q1 == 'Мутолиа намудани асарҳои классикони адабиёти ҷаҳон.':
    q.append('7')
if q1 == 'Мутолиа кардани асарҳо дар бораи фаъолияти кормандони умури дохила, мубориза бо вайронкунандагони қонун.':
    q.append('8')
if q1 == 'Шинос шудан ба таърих ва ҳунарҳои халқии Тоҷикистон.':
    q.append('9')
if q1 == 'Мутолиа кардани китобҳо дар бораи кори омўзгорон.':
    q.append('10')
if q1 == 'Мутолиа кардани китобу, маҷаллаҳои тиббӣ ва дар бораи фаъолияти духтурон.':
    q.append('11')
if q1 == 'Тозаю озода нигоҳ  доштани манзил.':
    q.append('12')
if q1 == 'Мутолиа кардани адабиёти ҳарбӣ.':
    q.append('13')
if q1 == 'Шунидани мусиқии  классикӣ.':
    q.append('14')
if q1 == ' Мутолиа кардани китобҳо дар бораи рассомҳо.':
    q.append('15')


q2 = st.radio(
     'Аз 15 саволи зерин кадомаш ба шумо маъқул аст',
     ('Дарсҳои математика.', 'Ҳал кардани масъалаҳои химиявӣ.', 'Омўзиши сохти анатомии ҳайвонот.', 'Хондан дар бораи давлатҳои гуногун, иқтисодиёт ва сохти давлатдории онҳо.',  'Хондани маҷаллаҳои техникӣ.', 'Хондани мақолаҳо ва маҷаллаҳои илмӣ-оммавӣ роҷеъ ба дастовардҳо дар соҳаи радиотехника.', 'Таҳлил кардан, муқоиса намудан ва баҳо додан ба асарҳои бадеӣ.',  'Шиносоӣ бо қонунҳо, фармонҳо, оинномаҳо, дастурамалҳои гуногун.', 'Омўхтани таърихи шаҳр, ноҳияе, ки дар он истиқомат доред.', 'Ёрӣ додан ба рафиқони дар таҳсил қафомонда, фаҳмондани масъалаҳои душворфаҳм.', 'Омўзиши дарсҳои анатомия ва физиологияи одам.',  'Ҳамеша бо одамон кор кардан ва хастагиро ҳис накардан.', 'Шиносоӣ бо техникаи ҳарбӣ.', 'Мусиқии ҳозиразамонро гўш кардан.', 'Ба музейҳо ва намоишгоҳҳои бадеӣ ташриф овардан.'))

if q2 == 'Дарсҳои математика.':
    q.append('16')
if q2 == 'Ҳал кардани масъалаҳои химиявӣ.':
    q.append('17')
if q2 == 'Омўзиши сохти анатомии ҳайвонот':
    q.append('18')
if q2 == 'Хондан дар бораи давлатҳои гуногун, иқтисодиёт ва сохти давлатдории онҳо.':
    q.append('19')
if q2 == 'Хондани маҷаллаҳои техникӣ':
    q.append('20')
if q2 == 'Хондани мақолаҳо ва маҷаллаҳои илмӣ-оммавӣ роҷеъ ба дастовардҳо дар соҳаи радиотехника.':
    q.append('21')
if q2 == 'Таҳлил кардан, муқоиса намудан ва баҳо додан ба асарҳои бадеӣ.':
    q.append('22')
if q2 == 'Шиносоӣ бо қонунҳо, фармонҳо, оинномаҳо, дастурамалҳои гуногун.':
    q.append('23')
if q2 == 'Омўхтани таърихи шаҳр, ноҳияе, ки дар он истиқомат доред.':
    q.append('24')
if q2 == 'Ёрӣ додан ба рафиқони дар таҳсил қафомонда, фаҳмондани масъалаҳои душворфаҳм.':
    q.append('25')
if q2 == 'Омўзиши дарсҳои анатомия ва физиологияи одам.':
    q.append('26')
if q2 == 'Ҳамеша бо одамон кор кардан ва хастагиро ҳис накардан.':
    q.append('27')
if q2 == 'Шиносоӣ бо техникаи ҳарбӣ.':
    q.append('28')
if q2 == 'Мусиқии ҳозиразамонро гўш кардан.':
    q.append('29')
if q2 == 'Ба музейҳо ва намоишгоҳҳои бадеӣ ташриф овардан.':
    q.append('30')


q3 = st.radio(
     'Аз 15 саволи зерин кадомаш ба шумо маъқул аст',
     ('Дар маҳфили математикӣ иштирок кардан, дар мактаби метематики хондан', 'Дарсҳои химия.', 'Хондани китобҳо дар бораи олами наботот ва ҳайвонот.', 'Бо ҳамроҳии геологҳо ба экспедитсия рафтан.', 'Шиносоӣ бо дастовардҳои техникаи ҳозиразамон (тамошо кардан ва шунидани барномаҳои телерадио, ба намоишгоҳҳои техникӣ рафтан).', 'Дар маҳфили техникию  компютерӣ  шуғл варзидан.', 'Хондани мақолаҳои адабӣ – техникӣ.', 'Омўхтани сохти сиёсӣ ва тағйиротҳои иҷтимоии дигар давлатҳо.', 'Хондани китобҳо дар мавзўъҳои таърихӣ.', 'Таҳлил кардани рафтору кирдори худ, рафтор бо одамон ҳангоми муносибат бо одамон.', 'Шиносоӣ бо комёбиҳои соҳаи тиб.', 'Тайёр намудани озуқаворӣ ҳангоми сайёҳатҳо.', 'Дарсҳои тарбияи ҷисмонӣ.', 'Дар мактаби мусиқӣ шуғл варзидан.', 'Дар маҳфили рассомон шуғл варзидан.' ))

if q3 == 'Дар маҳфили математикӣ иштирок кардан, дар мактаби метематики хондан.':
    q.append('31')
if q3 == 'Дарсҳои химия.':
    q.append('32')
if q3 == 'Хондани китобҳо дар бораи олами наботот ва ҳайвонот.':
    q.append('33')
if q3 == 'Бо ҳамроҳии геологҳо ба экспедитсия рафтан.':
    q.append('34')
if q3 == 'Шиносоӣ бо дастовардҳои техникаи ҳозиразамон (тамошо кардан ва шунидани барномаҳои телерадио, ба намоишгоҳҳои техникӣ рафтан).':
    q.append('35')
if q3 == 'Дар маҳфили техникию  компютерӣ  шуғл варзидан.':
    q.append('36')
if q3 == 'Хондани мақолаҳои адабӣ – техникӣ.':
    q.append('37')
if q3 == 'Омўхтани сохти сиёсӣ ва тағйиротҳои иҷтимоии дигар давлатҳо.':
    q.append('38')
if q3 == 'Хондани китобҳо дар мавзўъҳои таърихӣ.':
    q.append('39')
if q3 == 'Таҳлил кардани рафтору кирдори худ, рафтор бо одамон ҳангоми муносибат бо одамон.':
    q.append('40')
if q3 == 'Шиносоӣ бо комёбиҳои соҳаи тиб.':
    q.append('41')
if q3 == 'Тайёр намудани озуқаворӣ ҳангоми сайёҳатҳо.':
    q.append('42')
if q3 == 'Дарсҳои тарбияи ҷисмонӣ.':
    q.append('43')
if q3 == 'Дар мактаби мусиқӣ шуғл варзидан.':
    q.append('44')
if q3 == 'Дар маҳфили рассомон шуғл варзидан.':
    q.append('45')


q4 = st.radio(
    'Аз 15 саволи зерин кадомаш ба шумо маъқул аст', (
        'Ҳал кардани масъалаҳои математикӣ.',
        'Гузаронидани таҷрибаҳои химиявӣ.',
        'Дарсҳои ботаника, зоология, анатомия.',
        'Маълумот гирифтан дар бораи ҷойҳои нави кор оид ба коркарди канданиҳои фоиданок.',
        'Сарфаҳм рафтан дар нақшаҳо  ва таҳрирҳои техникӣ.',
        'Таъмир кардани асбобҳои барқии (электрикии) рўзгор.',
        'Худро дар навиштани ҳикояву шеър санҷидан.',
        'Гузаронидани ахбори сиёсӣ дар синф.',
        'Тамошои филмҳо дар бораи воқеаҳои таърихии мамлакатҳои гуногун. ',
        'Тайёр кардани маърўза, хабар ва бо онҳо дар назди хурдсолон баромад кардан.',
        'Ғамхорӣ кардан нисбат ба беморон ва ба онҳо ёрӣ расонидан.',
        'Кўмак кардан ба рафиқ дар мағоза ҳангоми интихоби либосе, ки ба ў нисбатан зебанда аст.',
        'Ширкат варзидан дар бозию саёҳатҳои ҳарбӣ.',
        'Дар саҳна шеър хондан, суруд хондан, баромад кардан.',
        'Ороиш додани рўзномаҳои деворӣ, намоишгоҳҳо.'
    )
)

if q4 == 'Ҳал кардани масъалаҳои математикӣ.':
    q.append('46')
if q4 == 'Гузаронидани таҷрибаҳои химиявӣ.':
    q.append('47')
if q4 == 'Дарсҳои ботаника, зоология, анатомия.':
    q.append('48')
if q4 == 'Маълумот гирифтан дар бораи ҷойҳои нави кор оид ба коркарди канданиҳои фоиданок.':
    q.append('49')
if q4 == 'Сарфаҳм рафтан дар нақшаҳо  ва таҳрирҳои техникӣ.':
    q.append('50')
if q4 == 'Таъмир кардани асбобҳои барқии (электрикии) рўзгор.':
    q.append('51')
if q4 == 'Худро дар навиштани ҳикояву шеър санҷидан.':
    q.append('52')
if q4 == 'Гузаронидани ахбори сиёсӣ дар синф.':
    q.append('53')
if q4 == 'Тамошои филмҳо дар бораи воқеаҳои таърихии мамлакатҳои гуногун.':
    q.append('54')
if q4 == 'Тайёр кардани маърўза, хабар ва бо онҳо дар назди хурдсолон баромад кардан.':
    q.append('55')
if q4 == 'Ғамхорӣ кардан нисбат ба беморон ва ба онҳо ёрӣ расонидан.':
    q.append('56')
if q4 == 'Кўмак кардан ба рафиқ дар мағоза ҳангоми интихоби либосе, ки ба ў нисбатан зебанда аст.':
    q.append('57')
if q4 == 'Ширкат варзидан дар бозию саёҳатҳои ҳарбӣ.':
    q.append('58')
if q4 == 'Дар саҳна шеър хондан, суруд хондан, баромад кардан.':
    q.append('59')
if q4 == 'Ороиш додани рўзномаҳои деворӣ, намоишгоҳҳо.':
    q.append('60')



q5 = st.radio(
    'Аз 15 саволи зерин кадомаш ба шумо маъқул аст',(
        'Ҳалли масъалахои геометрӣ.',
        'Мустақилона ҳосил намудани формулаҳои реаксияҳои кимиёвӣ.',
        'Бо микроскоп омўхтани бофтаҳои зинда, мушоҳида кардани ҳаракатҳои хурдтарини зарраҳо.',
        'Дарсҳои география.',
        'Васл ва таъмир кардани механизмҳои гуногун (велосипед, мошини дарздўзӣ ва ғайра).',
        'Васл ва таъмир кардани асбобҳои   техникию  компютерӣ.',
        'Омўзиши пайдоиши калимаву ибораҳо.',
        'Баромад намудан бо маърўзаҳо, хабарҳо дар назди шумораи зиёди одамон.',
        'Шинос шудан бо маданияти қадима аз рўи кофтуковҳои археологӣ (бостоншиносӣ).',
        'Дар синфҳои поёнӣ сардастаи ахтарон  шуда кор кардан.',
        'Расонидани ёрии аввалин ба маҷрўҳон.',
        'Расонидани хизматҳои гуногуни маишӣ ба мардум.',
        'Машғулият дар бахши дастони моҳир.',
        'Навохтани асбобҳои мусиқӣ.',
        'Бо қалам, фломастер ва  рангҳо расм кашидан.'
    )
)


if q5 == 'Ҳалли масъалахои геометрӣ.':
    q.append('61')
if q5 == 'Мустақилона ҳосил намудани формулаҳои реаксияҳои кимиёвӣ':
    q.append('62')
if q5 == 'Бо микроскоп омўхтани бофтаҳои зинда, мушоҳида кардани ҳаракатҳои хурдтарини зарраҳо.':
    q.append('63')
if q5 == 'Дарсҳои география.':
    q.append('64')
if q5 == 'Васл ва таъмир кардани механизмҳои гуногун (велосипед, мошини дарздўзӣ ва ғайра).':
    q.append('65')
if q5 == 'Васл ва таъмир кардани асбобҳои   техникию  компютерӣ.':
    q.append('66')
if q5 == 'Омўзиши пайдоиши калимаву ибораҳо.':
    q.append('67')
if q5 == 'Баромад намудан бо маърўзаҳо, хабарҳо дар назди шумораи зиёди одамон.':
    q.append('68')
if q5 == 'Шинос шудан бо маданияти қадима аз рўи кофтуковҳои археологӣ (бостоншиносӣ).':
    q.append('69')
if q5 == 'Дар синфҳои поёнӣ сардастаи ахтарон  шуда кор кардан.':
    q.append('70')
if q5 == 'Расонидани ёрии аввалин ба маҷрўҳон.':
    q.append('71')
if q5 == 'Расонидани хизматҳои гуногуни маишӣ ба мардум.':
    q.append('72')
if q5 == 'Машғулият дар бахши дастони моҳир.':
    q.append('73')
if q5 == 'Навохтани асбобҳои мусиқӣ.':
    q.append('74')
if q5 == 'Бо қалам, фломастер ва  рангҳо расм кашидан.':
    q.append('75')



q6 = st.radio(
    'Аз 15 саволи зерин кадомаш ба шумо маъқул аст',(
        'Мутолиа кардани адабиёти илмӣ дар бораи кашфиётҳои  математикӣ ва математикони машҳур.',
        'МашҒулият дар гурўҳҳои кимиёвӣ, дар олимпиадаҳои кимиёвӣ иштирок кардан.',
        'Нигоҳубин намудани растанӣ ва ҳайвонот, инкишофи онҳоро таҳти назорат гирифтан.',
        'Ба саёҳатҳои дуру дароз  ва мушкиле баромадан, ки дар онҳо мувофиқи барномаи муайяншуда самаранок кор кардан лозим мешавад.',
        'Дарсҳои (санъат ва меҳнат, касбу ҳунар) технология.',
        'Сарфаҳм рафтан ба радиосхемаҳои мураккаб.',
        'Кор бо луҒат ва сарчашмаҳои  адабӣ.',
        'Бо навигариҳои сиёсӣ ба воситаҳои ахбор, радио, рўзнома ва оинаи нилгун шинос шудан.',
        'Шиносоӣ бо қонуниятҳои тараққиётҳои таърихии инсоният.',
        'Гузаронидани вақт бо хурдсолон, ба онҳо нақл кардан, китоб хондан.',
        'Ғамхорию дилсўзӣ зоҳир кардан нисбат ба одамон.'
        'Одобу тамкин нишон додан ҳангом муносибат бо одамон.',
        'Омўхтани таърихи муҳорибаҳои калони ҳарбӣ ва тақдири лашкаркашони бузург.',
        'Тамошо кардани саҳнаҳои театрӣ ба воситаи оинаи нилгун ва театрҳои халқӣ.',
        'Шиносоӣ бо расмҳо, ҳайкалҳо ва дигар асарҳои санъат.'
    )
)


if q6 == 'Мутолиа кардани адабиёти илмӣ дар бораи кашфиётҳои  математикӣ ва математикони машҳур.':
    q.append('76')
if q6 == 'МашҒулият дар гурўҳҳои кимиёвӣ, дар олимпиадаҳои кимиёвӣ иштирок кардан.':
    q.append('77')
if q6 == 'Нигоҳубин намудани растанӣ ва ҳайвонот, инкишофи онҳоро таҳти назорат гирифтан.':
    q.append("78")
if q6 == 'Ба саёҳатҳои дуру дароз  ва мушкиле баромадан, ки дар онҳо мувофиқи барномаи муайяншуда самаранок кор кардан лозим мешавад.':
    q.append('79')
if q6 == 'Дарсҳои (санъат ва меҳнат, касбу ҳунар) технология.':
    q.append('80')
if q6 == 'Сарфаҳм рафтан ба радиосхемаҳои мураккаб.':
    q.append('81')
if q6 == 'Кор бо луҒат ва сарчашмаҳои  адабӣ.':
    q.append('82')
if q6 == 'Бо навигариҳои сиёсӣ ба воситаҳои ахбор, радио, рўзнома ва оинаи нилгун шинос шудан.':
    q.append('83')
if q6 == 'Шиносоӣ бо қонуниятҳои тараққиётҳои таърихии инсоният.':
    q.append('84')
if q6 == 'Гузаронидани вақт бо хурдсолон, ба онҳо нақл кардан, китоб хондан.':
    q.append('85')
if q6 == 'Ғамхорию дилсўзӣ зоҳир кардан нисбат ба одамон.':
    q.append('86')
if q6 == 'Одобу тамкин нишон додан ҳангом муносибат бо одамон.':
    q.append('87')
if q6 == 'Омўхтани таърихи муҳорибаҳои калони ҳарбӣ ва тақдири лашкаркашони бузург.':
    q.append('88')
if q6 == 'Тамошо кардани саҳнаҳои театрӣ ба воситаи оинаи нилгун ва театрҳои халқӣ.':
    q.append('89')
if q6 == 'Шиносоӣ бо расмҳо, ҳайкалҳо ва дигар асарҳои санъат.':
    q.append('90')


if '1' and '16' and '31' and  '46' and '61' and '76' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Математик, иқтисодчӣ-математик, иқтисодчӣ, иқтисодчӣ-муҳосиб, муҳандис-иқтисодчӣ,Техник-математик, барномасоз, математики ҳисоббарор, техник-иқтисодчӣ, техник-нақшакаш, муҳосиб, нозири қарз, молиячӣ, оператори компютерӣ, кассир-назоратчӣ, кассир-оператори почта'
if '2' and '17' and  '32' and '47' and '62' and '77' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Муҳандиси технологияи кимиёвӣ, Техники технологияи кимиёвӣ, дорусоз, Дастгоҳчӣ, лаборанти кимиёвӣ, оператори панели идоракунӣ'
if '3' and '18' and '33' and '48' and '63' in '78' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Биолог, агроном, ҷангалпарвар-муҳандис, агроном-хокшинос, муҳандисӣ ҳайвонот, байтор, Агроном-техник, техник-ҷангалпарвар, техники гидромелиоративй, мутахассиси соҳаи чорводорй, ёрдамчии бойтор, гулпарвар, боғбон, кабудизоркунанда, ҷангалбон, чорводор'
if '4' and '19' and '34' and '49' and '64' and '79'in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Биолог, гидрогеолог, геофизик, географ, харитакаш, муҳандис-геодезист, обуҳавосанҷ, гидролог, уқёнусшинос, гидрограф, Техник-топограф, техник-геодезист, Топограф, рассом-топограф'
if '5' and '20' and '35' and '50' and '65' and '80' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Муҳандис-технолог, механик, бинокор, муҳандиси гармдиҳӣ, муҳандиси энергетикӣ, механики киштӣ, киштибон, ҳавонавард, Техник-технолог, механики бинокорӣ, муҳандиси гармдиҳӣ, киштисоз, механики киштӣ, бофанда, дӯзанда, пойафзолдӯз, кафшергар, таъмингар, хиштчин, андовачӣ, электрик, челогар, идоракунанда маторчӣ, ронанда'
if '6' and '21' and '36' and '51' and '66' and '81' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Муҳандиси барқ, электрик, радиомеханик, Техник-электромеханик, электромонтёри техникӣ, радиотехник, Электромеханик, электромонтер, челонгар-электрик'
if '7' and '22' and '37' and '52' and '67' and '82' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Нависанда, рӯзноманигор, муҳаррири адабиёти оммавӣ, китобдор, ислоҳкунандаи китобу маҷаллаҳо, муҳаррири техникӣ, ҳуруфчин, мошинист-стенограф'
if '8' and '23' and '38' and '53'  and '68' and '83' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Ҳуқуқшинос, муфаттиш, нозӣр, ҳуқуқшиноси кафолати бошуур, Милиса'
if '9' and '24' and '39' and '54' and '69' and '84' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Таърихчӣ, бостоншинос, муаллими таърих'
if '10' and '25' and '40' and '55' and '70' and '85' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Тарбиядиҳанда, профессор, муаллими фан, Мактаби ибтидоӣ, Муаллими боғча, муаллими синфҳои ибтидоӣ, муаллими фан, устои омузишгоҳи касбй-техникй, тарбиятгар'
if '11' and '26' and '41' and  '56' and '71' and '86' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Духтур, дастёри духтур, ҳамшира, Санитар'
if '12' and '27' and '42' and '57' and '72' and '87' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Молшинос, тарҷумон, фурӯшанда, назоратчӣ-кассир, пешхизмат, барандаи экскурсия, роҳнамо, стюардесса'
if 	'13' and '28' and '43' and '58' and '73' and '88' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Ҳарбӣ, устоди варзиш'
if '14' and '29' and '44' and '59' and '74' and '89' in q:
    result = 'Мо ба шумо тавсия медиҳем, ки касбҳои зеринро баррасӣ кунед: Композитор, дирижер, навозанда-вокалист, режиссери опера, балет, драма, театри лӯхтак, эстрада, актёри театр ва кино, Дирижер, навозанда, режиссер'
if '15' and '30' and '45' and '60' and '75' and '90' in q:
    result = 'Меъмор, рассом, ҳайкалтарош, дизайнери графикӣ, санъатшинос, рассоми санъат, дизайнери мӯд, техник-меъмор, ороишгар, рассом-барқароркунанда, техник-тарроҳ, тарҳкаш, Заргар, пармагари булӯр, дуредгари нодиракор, сикказан, суфтакунандаи рангуборкунии чинй, кандакор, барқароркунанда, бинокор, суратгир, сартарош'



if st.button('Result'):
    st.write(result)
