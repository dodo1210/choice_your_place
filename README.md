# Choice your place

This is a project that get text and articles of tourism sites and analyse with the Kmeans and separate for groups according with text. The files use are: data.csv, run.py and choice_cities.txt

<h3>Metodology </h3>
For do this project got caught the 10 cities in 20 coutries most biggest of worlds in 2018, secound https://www.e-unwto.org/doi/pdf/10.18111/9789284421152. Before get the text in web sites (oficials of government and tourism)

<h3>Files </h3>
<ul>
  <li>choice_cities.txt: List of coutries and cities</li>
  <li>data.csv: Cotains 3 columns city, description, reference</li>
  <li>run.py: Executable</li>
</ul>

<h3>Libraries</h3>
<ul>
  <li>nltk: Library of Neuro-linguistic programming for download use pip install nltk</li>
  <li>pandas: Library for manipulate csv for donwload pip install pandas</li>
  <li>sklearn: Library of Marchine Leaning and tecnicals of AI (Artificial Inteligence) for donwload pip install skleanr</li>
  <li>math: Library for mathematical calculations</li>
  <li>string: Library for manipulate strings</li>
</ul>
  
<h3>Texto das cidades</h3>
<p>Paris https://www.lonelyplanet.com/france/paris"</p>
<p>Lyon https://www.lonelyplanet.com/france/burgundy-and-the-rhone/lyon"</p>
<p>Nice https://www.lonelyplanet.com/france/nice"</p>
<p>Marseille https://www.lonelyplanet.com/france/provence/marseille"</p>
<p>Bordeaux https://www.lonelyplanet.com/france/southwestern-france/bordeaux"</p>
<p>Toulouse https://www.lonelyplanet.com/france/toulouse"</p>
<p>Strasbourg https://www.lonelyplanet.com/france/alsace-and-lorraine/strasbourg"</p>
<p>Montpellier https://www.lonelyplanet.com/france/languedoc-roussillon/montpellier"</p>
<p>Lille https://www.lonelyplanet.com/france/northern-france/lille"</p>
<p>Nantes https://www.lonelyplanet.com/france/southwestern-france/nantes"</p>
<p>Udon Thani http://www.thailand-guide.com/udon-thani/"</p>
<p>Bangkok https://www.hoteis.com/go/thailand/bangkok?pos=HCOM_BR&locale=pt_BR"</p>
<p>Samut Prakan https://portal.tourismthailand.org/About-Thailand/Destination/Samut-Prakan"</p>
<p>Nonthaburi https://www.tourismthailand.org/Destinations/Provinces/Nonthaburi/226"</p>
<p>Chonburi https://www.tourismthailand.org/Destinations/Provinces/Chon-Buri/464"</p>
<p>Nakhon Ratchasima https://www.tourismthailand.org/Destinations/Provinces/Nakhon-Ratchasima/580"</p>
<p>Chiang Mai https://www.lonelyplanet.com/thailand/chiang-mai-province/chiang-mai"</p>
<p>Hat Yai https://www.tourismthailand.org/Destinations/Provinces/Hat-Yai/362"</p>
<p>Sri racha https://thailandlongstay.info/Sriracha.html"</p>
<p>Pak Kret http://tourismthailand.in/destinations/things-to-do-in-pak-kret/"</p>
<p>New York City https://www.visiteosusa.com.br/destination/cidade-de-nova-york"</p>
<p>Los Angeles https://www.visiteosusa.com.br/destination/los-angeles"</p>
<p>Houston https://www.visiteosusa.com.br/destination/houston"</p>
<p>Philadelaphia https://www.visiteosusa.com.br/destination/filadelfia"</p>
<p>Phoenix https://www.visiteosusa.com.br/destination/phoenix"</p>
<p>San Antonio https://www.visiteosusa.com.br/destination/san-antonio"</p>
<p>San Diego https://www.lonelyplanet.com/usa/san-diego"</p>
<p>Chicago https://www.lonelyplanet.com/usa/chicago"</p>
<p>Dallas https://www.visittheusa.com/destination/dallas </p>
<p>San Jose Tourism-g33020-San_Jose_California-Vacations.html?fid=5363fadd-8963-48b9-9dee-70cbc0dc8d67"</p>
<p>Madrid https://www.spain.info/en/que-quieres/ciudades-pueblos/grandes-ciudades/madrid.html"</p>
<p>Barcelona https://www.spain.info/en/que-quieres/ciudades-pueblos/grandes-ciudades/barcelona.html"</p>
<p>Sevilla https://www.spain.info/en/que-quieres/ciudades-pueblos/grandes-ciudades/sevilla.html"</p>
<p>Valencia https://www.spain.info/en_US/que-quieres/ciudades-pueblos/grandes-ciudades/valencia.html</p>
<p>Malaga https://www.spain.info/en/que-quieres/ciudades-pueblos/grandes-ciudades/malaga.html"</p>
<p>Zaragoza https://www.spain.info/en/que-quieres/ciudades-pueblos/grandes-ciudades/zaragoza.html"</p>
<p>Bilbao https://www.spain.info/en/que-quieres/ciudades-pueblos/grandes-ciudades/bilbao.html"</p>
<p>Murcia https://www.spain.info/en/que-quieres/ciudades-pueblos/otros-destinos/murcia.html"</p>
<p>Palma https://www.spain.info/en/que-quieres/ciudades-pueblos/grandes-ciudades/palma.html"</p>
<p>Las Palmas Canary Island https://www.spain.info/en_US/que-quieres/ciudades-pueblos/provincias/la_palma.html </p>
<p>Pequim https://www.lonelyplanet.com/china/beijing"</p>
<p>Shanghai https://www.lonelyplanet.com/china/shanghai"</p>
<p>Xian https://www.lonelyplanet.com/china/shaanxi-shanxi/xian"</p>
<p>Guilin https://www.lonelyplanet.com/china/guangxi/guilin"</p>
<p>Chengdu https://www.lonelyplanet.com/china/sichuan/chengdu"</p>
<p>Shenzhen https://www.lonelyplanet.com/china/guangdong/shenzhen"</p>
<p>Wuhan https://www.lonelyplanet.com/china/hubei/wuhan"</p>
<p>Dongguan https://trip101.com/article/best-things-to-do-in-dongguan-china"</p>
<p>Guangzhou https://www.lonelyplanet.com/china/guangdong/guangzhou"</p>
<p>Tiajin https://www.lonelyplanet.com/china/tianjin"</p>
<p>Rome http://www.italia.it/en/discover-italy/lazio/rome.html?no_cache=1&h=rome"</p>
<p>Milan http://www.visititaly.com/holiday/milan.aspx"</p>
<p>Naples https://www.lonelyplanet.com/italy/campania/naples"</p>
<p>Genoa https://www.lonelyplanet.com/italy/liguria-piedmont-and-valle-daosta/genoa"</p>
<p>Bologna https://www.lonelyplanet.com/italy/emilia-romagna-and-san-marino/bologna"</p>
<p>Florence https://www.lonelyplanet.com/italy/florence </p>
<p>Catania https://www.lonelyplanet.com/italy/sicily/catania"</p>
<p>Bari https://www.lonelyplanet.com/italy/puglia/bari"</p>
<p>Turin https://www.lonelyplanet.com/italy/lombardia/turin"</p>
<p>Istanbul https://www.lonelyplanet.com/turkey/istanbul"</p>
<p>Ankara https://www.lonelyplanet.com/turkey/central-anatolia/ankara"</p>
<p>Ismir https://www.lonelyplanet.com/turkey/aegean-coast/izmir"</p>
<p>Bursa https://www.lonelyplanet.com/turkey/bursa"</p>
<p>Adana https://www.lonelyplanet.com/turkey/adana"</p>
<p>Gaziantep https://www.lonelyplanet.com/turkey/central-anatolia/gaziantep-antep"</p>
<p>Konya https://www.lonelyplanet.com/turkey/central-anatolia/konya"</p>
<p>Bagcilar https://www.turkeyexpert.com/Istanbul/Bagcilar-basin-express-highway?p=9"</p>
<p>Antalya https://www.lonelyplanet.com/turkey/mediterranean-coast/antalya"</p>
<p>Cankaya https://www.expedia.co.in/Cankaya.d6323099.Holidays-City-Breaks"</p>
<p>Hong Kong https://www.lonelyplanet.com/china/hong-kong"</p>
<p>Mexico City https://www.visitmexico.com/es/destinos-principales/ciudad-de-mexico/ciudad-de-mexico"</p>
<p>Puebla City https://www.visitmexico.com/es/destinos-principales/puebla/puebla"</p>
<p>Guadalajara https://www.visitmexico.com/en/main-destinations/jalisco/guadalajara"</p>
<p>Juarez https://www.visitmexico.com/en/main-destinations/chihuahua/juarez"</p>
<p>Leon https://www.visitmexico.com/en/main-destinations/guanajuato/leon"</p>
<p>Tijuana https://www.visitmexico.com/es/destinos-principales/baja-california/tijuana"</p>
<p>Iztapalapa http://cdmxtravel.com/en/visitor-info/districts/iztapalapa.html"</p>
<p>Zapopan https://cityofguadalajara.com/zapopan/"</p>
<p>Ecatepec https://www.expedia.com.sg/Ecatepec-De-Morelos.d179274.Destination-Travel-Guides"</p>
<p>Gustavo Adolfo Madero  https://www.tripmondo.com/mexico/ciudad-de-mexico/gustavo-a-madero/gustavo-adolfo-madero/"</p>
<p>Berlin https://www.germany.travel/en/towns-cities-culture/towns-cities/berlin.html"</p>
<p>Hamburg https://www.germany.travel/en/towns-cities-culture/towns-cities/magic-cities/hamburg.html"</p>
<p>Munich https://www.germany.travel/en/towns-cities-culture/towns-cities/munich.html"</p>
<p>Cologne https://www.germany.travel/en/towns-cities-culture/towns-cities/magic-cities/cologne.html"</p>
<p>Frankfurt https://www.germany.travel/en/towns-cities-culture/towns-cities/magic-cities/frankfurt.html"</p>
<p>Stuttgart https://www.germany.travel/en/towns-cities-culture/towns-cities/stuttgart.html </p>
<p>Düsseldorf https://www.germany.travel/en/towns-cities-culture/towns-cities/magic-cities/duesseldorf.html"</p>
<p>Bremen https://www.germany.travel/en/towns-cities-culture/towns-cities/magic-cities/bremen.html"</p>
<p>Dortmund https://www.lonelyplanet.com/germany/north-rhine-westphalia/dortmund </p>
<p>Essen https://www.lonelyplanet.com/germany/north-rhine-westphalia/essen"</p>
<p>London https://www.visitbritain.com/gb/en/england/london"</p>
<p>Birmingham https://www.visitbritain.com/gb/en/england/central-england/birmingham"</p>
<p>Liverpool https://www.visitbritain.com/gb/en/england/northern-england/liverpool"</p>
<p>Nottingham https://www.visitbritain.com/gb/en/england/central-england/nottingham"</p>
<p>Bristol https://www.visitbritain.com/gb/en/england/south-west/bristol"</p>
<p>Glasgow https://www.visitbritain.com/gb/en/scotland/glasgow"</p>
<p>Leicester https://www.visitbritain.com/gb/en/england/central-england/leicester"</p>
<p>Edinburgh https://www.visitbritain.com/gb/en/scotland/edinburgh"</p>
<p>Leeds https://www.visitbritain.com/gb/en/england/northern-england/leeds"</p>
<p>Sheffield http://www.welcometosheffield.co.uk/visit"</p>
<p>Tokyo https://www.japan.travel/en/destinations/kanto/tokyo/"</p>
<p>Kyoto https://www.japan.travel/en/destinations/kansai/kyoto/</p>
<p>Yokohama https://www.japan-guide.com/e/e2156.html"</p>
<p>Osaka https://www.japan-guide.com/e/e2157.html"</p>
<p>Nagoya https://www.japan-guide.com/e/e2155.html"</p>
<p>Sapporo https://www.japan-guide.com/e/e2163.html"</p>
<p>Kobe https://www.japan-guide.com/e/e2159.html"</p>
<p>Fukuoka https://www.japan-guide.com/e/e2161.html"</p>
<p>Kawasaki https://www.japan-guide.com/e/e3250.html"</p>
<p>Saitama https://www.japan-guide.com/e/e6525.html"</p>
<p>Vienna https://www.lonelyplanet.com/austria/vienna"</p>
<p>Graz https://www.lonelyplanet.com/austria/the-south/graz"</p>
<p>Linz https://www.lonelyplanet.com/austria/the-danube-valley/linz"</p>
<p>Salzburg https://www.lonelyplanet.com/austria/salzburg"</p>
<p>Innsbruck https://www.lonelyplanet.com/austria/tirol/innsbruck"</p>
<p>Klagenfurt https://www.lonelyplanet.com/austria/the-south/klagenfurt"</p>
<p>Villac https://www.lonelyplanet.com/austria/tirol/villach"</p>
<p>Dornbirn https://www.lonelyplanet.com/austria/dornbirn"</p>
<p>Wiener https://www.lonelyplanet.com/austria/wiener-neustadt"</p>
<p>Steyr https://www.lonelyplanet.com/austria/steyr"</p>
<p>Athens https://www.lonelyplanet.com/greece/athens"</p>
<p>Thessaloniki https://www.lonelyplanet.com/greece/northern-greece/thessaloniki"</p>
<p>Larissa https://www.lonelyplanet.com/greece/larisa"</p>
<p>Piraeus https://www.lonelyplanet.com/greece/athens/piraeus"</p>
<p>Acharnes https://www.hellotravel.com/greece/acharnes"</p>
<p>Kallith http://visitkassandra.com/halkidiki/kallithea/"</p>
<p>Heraklion http://www.visitgreece.gr/en/main_cities/heraklion"</p>
<p>Peristeri https://www.triphobo.com/places/peristeri-attica-greece/things-to-do"</p>
<p>Kalamaria https://www.triphobo.com/places/kalamaria-greece/things-to-do"</p>
<p>Kuala Lumpur http://www.kuala-lumpur.ws"</p>
<p>Johor Bahru http://www.malaysia-hotels.net/culturalcities/johor-bahru.htm"</p>
<p>Kota Bharu https://www.lonelyplanet.com/malaysia/peninsular-malaysia-east-coast/kota-bharu"</p>
<p>Klang https://www.lonelyplanet.com/malaysia/klang-pelabuhan-klang"</p>
<p>Kampung Baru Suba https://www.lonelyplanet.com/malaysia/kampung-benuk"</p>
<p>Ipoh hops https://www.lonelyplanet.com/malaysia/peninsular-malaysia-west-coast/ipoh"</p>
<p>Kuching https://www.lonelyplanet.com/malaysia/malaysian-borneo-sarawak/kuching"</p>
<p>Petaling https://www.lonelyplanet.com/malaysia/petaling-jaya-shah-alam"</p>
<p>Shah Alam hah Alam https://www.triphobo.com/places/shah-alam-malaysia/things-to-do"</p>
<p>Kota Kinabalu https://www.lonelyplanet.com/malaysia/malaysian-borneo-sabah/kota-kinabalu"</p>
<p>Moscow https://www.lonelyplanet.com/russia/moscow"</p>
<p>St Petersburg https://www.lonelyplanet.com/russia/moscow"</p>
<p>Kazan https://www.lonelyplanet.com/russia/volga-region/kazan"</p>
<p>Novosibirsk https://www.lonelyplanet.com/russia/siberia/novosibirsk"</p>
<p>Ekaterinburg https://www.lonelyplanet.com/russia/the-urals/yekaterinburg"</p>
<p>Nizhny Novgorod https://www.lonelyplanet.com/russia/volga-region/nizhny-novgorod"</p>
<p>Samara https://www.lonelyplanet.com/russia/volga-region/samara"</p>
<p>Omsk https://www.lonelyplanet.com/russia/siberia/omsk"</p>
<p>Chelyabinsk https://www.lonelyplanet.com/russia/the-urals/chelyabinsk"</p>
<p>Rostov-on-Don https://www.lonelyplanet.com/russia/russian-caucasus/rostov-on-don"</p>
<p>Lisbon https://www.lonelyplanet.com/portugal/lisbon"</p>
<p>Porto https://www.lonelyplanet.com/portugal/the-north/porto"</p>
<p>Amadora https://www.visitlisboa.com/pt-pt/regions/arredores-de-lisboa/amadora"</p>
<p>Braga https://www.lonelyplanet.com/portugal/the-north/braga"</p>
<p>Setúbal https://www.lonelyplanet.com/portugal/lisbon/setubal"</p>
<p>Coimbra https://www.lonelyplanet.com/portugal/central-portugal/coimbra"</p>
<p>Queluz https://www.portugalrotasetours.com/pt/tour/tour-queluz-sintra"</p>
<p>Funchal https://www.lonelyplanet.com/portugal/funchal"</p>
<p>Cacem https://www.visitportugal.com/en/NR/exeres/2E42BEB7-3958-463F-9601-89A6C3A1B4F2"</p>
<p>Vila Nova de Gaia https://www.lonelyplanet.com/portugal/porto/vila-nova-de-gaia"</p>
<p>Scarborough https://www.seetorontonow.com/explore-toronto/neighbourhoods/scarborough/"</p>
<p>Toronto https://www.lonelyplanet.com/canada/toronto</p>
<p>Montreal https://www.lonelyplanet.com/canada/montreal"</p>
<p>Calgary https://www.lonelyplanet.com/canada/alberta/calgary"</p>
<p>Montreal https://www.lonelyplanet.com/canada/montreal"</p>
<p>Ottawa https://www.lonelyplanet.com/canada/ontario/ottawa"</p>
<p>Edmonton https://www.lonelyplanet.com/canada/alberta/edmonton"</p>
<p>Mississauga https://www.thecrazytourist.com/15-best-things-mississauga-ontario-canada/"</p>
<p>North York https://www.rome2rio.com/s/Downtown-Toronto/North-York"</p>
<p>Winnipeg https://www.lonelyplanet.com/canada/manitoba/winnipeg"</p>
<p>Vancouver https://www.lonelyplanet.com/canada/vancouver"</p>
<p>Warsaw https://www.poland.travel/en/cities/warsaw"</p>
<p>Łódź https://www.poland.travel/en/cities/lodz"</p>
<p>Krakow https://www.poland.travel/en/cities/krakow"</p>
<p>Wrocław https://www.poland.travel/en/cities/wroclaw"</p>
<p>Poznan https://www.poland.travel/en/cities/poznan"</p>
<p>Gdańsk https://www.poland.travel/en/cities/gdansk-and-tricity"</p>
<p>Szczecin https://www.lonelyplanet.com/poland/pomerania/szczecin"</p>
<p>Bydgoszcz https://www.poland.travel/en/cities/bydgoszcz"</p>
<p>Lublin https://www.poland.travel/en/cities/lublin"</p>
<p>Katowice https://www.poland.travel/en/cities/katowice"</p>
<p>Amsterdam https://www.lonelyplanet.com/the-netherlands/amsterdam"</p>
<p>Rotterdam https://www.lonelyplanet.com/the-netherlands/rotterdam"</p>
<p>The Hague https://www.iamsterdam.com/en/plan-your-trip/day-trips/netherlands/the-hague"</p>
<p>Utrecht https://www.lonelyplanet.com/the-netherlands/the-randstad/utrecht-city"</p>
<p>Eindhoven https://www.lonelyplanet.com/the-netherlands/eindhoven"</p>
<p>Tilburg https://www.lonelyplanet.com/the-netherlands/tilburg"</p>
<p>Groningen https://www.lonelyplanet.com/the-netherlands/the-north-and-east/groningen-city"</p>
<p>Almere https://www.triphobo.com/places/almere-the-netherlands"</p>
<p>Breda https://www.lonelyplanet.com/the-netherlands/breda"</p>
<p>Nijmegen https://www.lonelyplanet.com/the-netherlands/nijmegen"</p>
