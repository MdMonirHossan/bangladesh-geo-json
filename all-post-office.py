import json
import uuid

upazila_ids = [
"amtaliUpazilaId",
"bamnaUpazilaId",
"barguna_sadarUpazilaId",
"betagiUpazilaId",
"patharghataUpazilaId",
"taltaliUpazilaId",
"muladiUpazilaId",
"babuganjUpazilaId",
"agailjharaUpazilaId",
"barisal_sadarUpazilaId",
"bakerganjUpazilaId",
"banariparaUpazilaId",
"gaurnadiUpazilaId",
"hizlaUpazilaId",
"mehendiganjUpazilaId",
"wazirpurUpazilaId",
"bhola_sadarUpazilaId",
"burhanuddinUpazilaId",
"char_fassonUpazilaId",
"daulatkhanUpazilaId",
"lalmohanUpazilaId",
"manpuraUpazilaId",
"tazumuddinUpazilaId",
"jhalokati_sadarUpazilaId",
"kathaliaUpazilaId",
"nalchityUpazilaId",
"rajapurUpazilaId",
"bauphalUpazilaId",
"dashminaUpazilaId",
"galachipaUpazilaId",
"kalaparaUpazilaId",
"mirzaganjUpazilaId",
"patuakhali_sadarUpazilaId",
"dumkiUpazilaId",
"rangabaliUpazilaId",
"bhandariaUpazilaId",
"kaukhaliUpazilaId",
"mathbariaUpazilaId",
"nazirpurUpazilaId",
"nesarabadUpazilaId",
"pirojpur_sadarUpazilaId",
"zianagarUpazilaId",
"bandarban_sadarUpazilaId",
"thanchiUpazilaId",
"lamaUpazilaId",
"naikhongchhariUpazilaId",
"ali_kadamUpazilaId",
"rowangchhariUpazilaId",
"rumaUpazilaId",
"brahmanbaria_sadarUpazilaId",
"ashuganjUpazilaId",
"nasirnagarUpazilaId",
"nabinagarUpazilaId",
"sarailUpazilaId",
"shahbazpur_townUpazilaId",
"kasbaUpazilaId",
"akhauraUpazilaId",
"bancharampurUpazilaId",
"bijoynagarUpazilaId",
"chandpur_sadarUpazilaId",
"faridganjUpazilaId",
"haimcharUpazilaId",
"haziganjUpazilaId",
"matlab_uttarUpazilaId",
"matlab_dakkhinUpazilaId",
"shahrastiUpazilaId",
"anwaraUpazilaId",
"banshkhaliUpazilaId",
"boalkhaliUpazilaId",
"chandanaishUpazilaId",
"fatikchhariUpazilaId",
"hathazariUpazilaId",
"lohagaraUpazilaId",
"mirsharaiUpazilaId",
"patiyaUpazilaId",
"ranguniaUpazilaId",
"raozanUpazilaId",
"sandwipUpazilaId",
"satkaniaUpazilaId",
"sitakundaUpazilaId",
"baruraUpazilaId",
"brahmanparaUpazilaId",
"burichongUpazilaId",
"chandinaUpazilaId",
"chauddagramUpazilaId",
"daudkandiUpazilaId",
"debidwarUpazilaId",
"homnaUpazilaId",
"comilla_sadarUpazilaId",
"laksamUpazilaId",
"monohorgonjUpazilaId",
"meghnaUpazilaId",
"muradnagarUpazilaId",
"nangalkotUpazilaId",
"comilla_sadar_southUpazilaId",
"titasUpazilaId",
"chakariaUpazilaId",
"coxs_bazar_sadarUpazilaId",
"kutubdiaUpazilaId",
"maheshkhaliUpazilaId",
"ramuUpazilaId",
"teknafUpazilaId",
"ukhiaUpazilaId",
"pekuaUpazilaId",
"eidgaonUpazilaId",
"feni_sadarUpazilaId",
"chagalnaiyaUpazilaId",
"daganbhyanUpazilaId",
"parshuramUpazilaId",
"fhulgaziUpazilaId",
"sonagaziUpazilaId",
"dighinalaUpazilaId",
"khagrachhariUpazilaId",
"lakshmichhariUpazilaId",
"mahalchhariUpazilaId",
"manikchhariUpazilaId",
"matirangaUpazilaId",
"panchhariUpazilaId",
"ramgarhUpazilaId",
"lakshmipur_sadarUpazilaId",
"raipurUpazilaId",
"ramganjUpazilaId",
"ramgatiUpazilaId",
"komol_nagarUpazilaId",
"noakhali_sadarUpazilaId",
"begumganjUpazilaId",
"chatkhilUpazilaId",
"companyganjUpazilaId",
"shenbagUpazilaId",
"hatiaUpazilaId",
"kobirhatUpazilaId",
"sonaimuriUpazilaId",
"suborno_charUpazilaId",
"rangamati_sadarUpazilaId",
"belaichhariUpazilaId",
"bagaichhariUpazilaId",
"barkalUpazilaId",
"juraichhariUpazilaId",
"rajasthaliUpazilaId",
"kaptaiUpazilaId",
"langaduUpazilaId",
"nannercharUpazilaId",
"dhamraiUpazilaId",
"doharUpazilaId",
"keraniganjUpazilaId",
"savarUpazilaId",
"faridpur_sadarUpazilaId",
"boalmariUpazilaId",
"alfadangaUpazilaId",
"madhukhaliUpazilaId",
"bhangaUpazilaId",
"nagarkandaUpazilaId",
"charbhadrasanUpazilaId",
"sadarpurUpazilaId",
"shalthaUpazilaId",
"gazipur_sadar_joydebpurUpazilaId",
"kaliakiorUpazilaId",
"kapasiaUpazilaId",
"sripurUpazilaId",
"tongiUpazilaId",
"gopalganj_sadarUpazilaId",
"kashianiUpazilaId",
"kotaliparaUpazilaId",
"muksudpurUpazilaId",
"tungiparaUpazilaId",
"astagramUpazilaId",
"bajitpurUpazilaId",
"bhairabUpazilaId",
"hossainpurUpazilaId",
"itnaUpazilaId",
"karimganjUpazilaId",
"katiadiUpazilaId",
"kishoreganj_sadarUpazilaId",
"kuliarcharUpazilaId",
"mithamainUpazilaId",
"nikliUpazilaId",
"pakundiaUpazilaId",
"tarailUpazilaId",
"madaripur_sadarUpazilaId",
"kalkiniUpazilaId",
"rajoirUpazilaId",
"shibcharUpazilaId",
"dasarUpazilaId",
"manikganj_sadarUpazilaId",
"singairUpazilaId",
"shibalayaUpazilaId",
"saturiaUpazilaId",
"harirampurUpazilaId",
"ghiorUpazilaId",
"lohajangUpazilaId",
"sreenagarUpazilaId",
"munshiganj_sadarUpazilaId",
"sirajdikhanUpazilaId",
"tongibariUpazilaId",
"gazariaUpazilaId",
"araihazarUpazilaId",
"sonargaonUpazilaId",
"bandarUpazilaId",
"naryanganj_sadarUpazilaId",
"rupganjUpazilaId",
"siddirgonjUpazilaId",
"belaboUpazilaId",
"monohardiUpazilaId",
"narsingdi_sadarUpazilaId",
"palashUpazilaId",
"raipuraUpazilaId",
"shibpurUpazilaId",
"baliakandiUpazilaId",
"goalandaghatUpazilaId",
"pangshaUpazilaId",
"kalukhaliUpazilaId",
"rajbari_sadarUpazilaId",
"shariatpur_sadar_palongUpazilaId",
"damudyaUpazilaId",
"nariaUpazilaId",
"jajiraUpazilaId",
"bhedarganjUpazilaId",
"gosairhatUpazilaId",
"tangail_sadarUpazilaId",
"sakhipurUpazilaId",
"basailUpazilaId",
"madhupurUpazilaId",
"ghatailUpazilaId",
"kalihatiUpazilaId",
"nagarpurUpazilaId",
"mirzapurUpazilaId",
"gopalpurUpazilaId",
"delduarUpazilaId",
"bhuapurUpazilaId",
"dhanbariUpazilaId",
"bagerhat_sadarUpazilaId",
"chitalmariUpazilaId",
"fakirhatUpazilaId",
"kachuaUpazilaId",
"mollahatUpazilaId",
"monglaUpazilaId",
"morrelganjUpazilaId",
"rampalUpazilaId",
"sarankholaUpazilaId",
"damurhudaUpazilaId",
"chuadanga_sUpazilaId",
"jibannagarUpazilaId",
"alamdangaUpazilaId",
"abhaynagarUpazilaId",
"keshabpurUpazilaId",
"bagherparaUpazilaId",
"jessore_sadarUpazilaId",
"chaugachhaUpazilaId",
"manirampurUpazilaId",
"jhikargachhaUpazilaId",
"sharshaUpazilaId",
"jhenaidah_sadarUpazilaId",
"maheshpurUpazilaId",
"kotchandpurUpazilaId",
"shailkupaUpazilaId",
"harinakundaUpazilaId",
"terokhadaUpazilaId",
"batiaghataUpazilaId",
"dacopeUpazilaId",
"dumuriaUpazilaId",
"dighaliaUpazilaId",
"koyraUpazilaId",
"paikgachhaUpazilaId",
"phultalaUpazilaId",
"rupsaUpazilaId",
"kushtia_sadarUpazilaId",
"kumarkhaliUpazilaId",
"daulatpurUpazilaId",
"mirpurUpazilaId",
"bheramaraUpazilaId",
"khoksaUpazilaId",
"magura_sadarUpazilaId",
"mohammadpurUpazilaId",
"shalikhaUpazilaId",
"sreepurUpazilaId",
"angniUpazilaId",
"mujib_nagarUpazilaId",
"meherpur_sUpazilaId",
"narail_s_upazillaUpazilaId",
"lohagara_upazillaUpazilaId",
"kalia_upazillaUpazilaId",
"satkhira_sadarUpazilaId",
"assasuniUpazilaId",
"debhataUpazilaId",
"talaUpazilaId",
"kalaroaUpazilaId",
"kaliganjUpazilaId",
"shyamnagarUpazilaId",
"adamdighiUpazilaId",
"bogra_sadarUpazilaId",
"sherpurUpazilaId",
"dhunatUpazilaId",
"dhupchanchiaUpazilaId",
"gabtaliUpazilaId",
"kahalooUpazilaId",
"nandigramUpazilaId",
"sahajanpurUpazilaId",
"sariakandiUpazilaId",
"sonatalaUpazilaId",
"joypurhat_sUpazilaId",
"akkelpurUpazilaId",
"kalaiUpazilaId",
"khetlalUpazilaId",
"panchbibiUpazilaId",
"naogaon_sadarUpazilaId",
"mohadevpurUpazilaId",
"mandaUpazilaId",
"niamatpurUpazilaId",
"atraiUpazilaId",
"raninagarUpazilaId",
"patnitalaUpazilaId",
"dhamoirhatUpazilaId",
"sapaharUpazilaId",
"porshaUpazilaId",
"badalgachhiUpazilaId",
"bagatiparaUpazilaId",
"lalpurUpazilaId",
"natore_sadarUpazilaId",
"baraigramUpazilaId",
"bholahatUpazilaId",
"gomastapurUpazilaId",
"nacholeUpazilaId",
"nawabganj_sadarUpazilaId",
"shibganjUpazilaId",
"atghariaUpazilaId",
"beraUpazilaId",
"bhanguraUpazilaId",
"chatmoharUpazilaId",
"faridpurUpazilaId",
"ishwardiUpazilaId",
"pabna_sadarUpazilaId",
"santhiaUpazilaId",
"sujanagarUpazilaId",
"baghaUpazilaId",
"bagmaraUpazilaId",
"charghatUpazilaId",
"durgapurUpazilaId",
"godagariUpazilaId",
"mohanpurUpazilaId",
"pabaUpazilaId",
"puthiaUpazilaId",
"tanoreUpazilaId",
"sirajganj_sadarUpazilaId",
"belkuchiUpazilaId",
"chauhaliUpazilaId",
"kamarkhandaUpazilaId",
"kazipurUpazilaId",
"raiganjUpazilaId",
"shahjadpurUpazilaId",
"tarashUpazilaId",
"ullahparaUpazilaId",
"birampurUpazilaId",
"birganjUpazilaId",
"biralUpazilaId",
"bochaganjUpazilaId",
"chirirbandarUpazilaId",
"phulbariUpazilaId",
"ghoraghatUpazilaId",
"hakimpurUpazilaId",
"kaharoleUpazilaId",
"khansamaUpazilaId",
"dinajpur_sadarUpazilaId",
"nawabganjUpazilaId",
"parbatipurUpazilaId",
"fulchhariUpazilaId",
"gaibandha_sadarUpazilaId",
"gobindaganjUpazilaId",
"palashbariUpazilaId",
"sadullapurUpazilaId",
"saghataUpazilaId",
"sundarganjUpazilaId",
"kurigram_sadarUpazilaId",
"nageshwariUpazilaId",
"bhurungamariUpazilaId",
"rajarhatUpazilaId",
"ulipurUpazilaId",
"chilmariUpazilaId",
"rowmariUpazilaId",
"char_rajibpurUpazilaId",
"lalmanirhat_sadarUpazilaId",
"aditmariUpazilaId",
"hatibandhaUpazilaId",
"patgramUpazilaId",
"nilphamari_sadarUpazilaId",
"saidpurUpazilaId",
"jaldhakaUpazilaId",
"kishoreganjUpazilaId",
"domarUpazilaId",
"dimlaUpazilaId",
"panchagarh_sadarUpazilaId",
"debiganjUpazilaId",
"bodaUpazilaId",
"atwariUpazilaId",
"tetuliaUpazilaId",
"badarganjUpazilaId",
"mithapukurUpazilaId",
"gangacharaUpazilaId",
"kauniaUpazilaId",
"rangpur_sadarUpazilaId",
"pirgachhaUpazilaId",
"pirganjUpazilaId",
"taraganjUpazilaId",
"thakurgaon_sadarUpazilaId",
"baliadangiUpazilaId",
"haripurUpazilaId",
"ranisankailUpazilaId",
"ajmiriganjUpazilaId",
"baniachangUpazilaId",
"bahubalUpazilaId",
"chunarughatUpazilaId",
"habiganj_sadarUpazilaId",
"lakhaiUpazilaId",
"madhabpurUpazilaId",
"nabiganjUpazilaId",
"shaistagonjUpazilaId",
"moulvibazar_sadarUpazilaId",
"barlekhaUpazilaId",
"juriUpazilaId",
"kamalganjUpazilaId",
"kulauraUpazilaId",
"rajnagarUpazilaId",
"sreemangalUpazilaId",
"bishwamvarpurUpazilaId",
"chhatakUpazilaId",
"deraiUpazilaId",
"dharampashaUpazilaId",
"dowarabazarUpazilaId",
"jagannathpurUpazilaId",
"jamalganjUpazilaId",
"sullaUpazilaId",
"sunamganj_sadarUpazilaId",
"shanthiganjUpazilaId",
"tahirpurUpazilaId",
"modhyanagarUpazilaId",
"sylhet_sadarUpazilaId",
"beanibazarUpazilaId",
"bishwanathUpazilaId",
"dakshin_surmaUpazilaId",
"balaganjUpazilaId",
"companiganjUpazilaId",
"fenchuganjUpazilaId",
"golapganjUpazilaId",
"gowainghatUpazilaId",
"jaintiapurUpazilaId",
"kanaighatUpazilaId",
"zakiganjUpazilaId",
"nobigonjUpazilaId",
"dewanganjUpazilaId",
"baksiganjUpazilaId",
"islampurUpazilaId",
"jamalpur_sadarUpazilaId",
"madarganjUpazilaId",
"melandahaUpazilaId",
"sarishabariUpazilaId",
"narundi_police_i_cUpazilaId",
"bhalukaUpazilaId",
"trishalUpazilaId",
"haluaghatUpazilaId",
"muktagachhaUpazilaId",
"dhobauraUpazilaId",
"fulbariaUpazilaId",
"gaffargaonUpazilaId",
"gauripurUpazilaId",
"ishwarganjUpazilaId",
"mymensingh_sadarUpazilaId",
"nandailUpazilaId",
"phulpurUpazilaId",
"kendua_upazillaUpazilaId",
"atpara_upazillaUpazilaId",
"barhatta_upazillaUpazilaId",
"durgapur_upazillaUpazilaId",
"kalmakanda_upazillaUpazilaId",
"madan_upazillaUpazilaId",
"mohanganj_upazillaUpazilaId",
"netrakona_s_upazillaUpazilaId",
"purbadhala_upazillaUpazilaId",
"khaliajuri_upazillaUpazilaId",
"jhenaigatiUpazilaId",
"naklaUpazilaId",
"nalitabariUpazilaId",
"sherpur_sadarUpazilaId",
"sreebardiUpazilaId",
]

post_office_enum = [
"AMTALI",
"BAMNA",
"BARGUNA_SADAR",
"NALI_BANDAR",
"BETAGI",
"DARUL_ULAM",
"KAKCHIRA",
"PATHARGHATA",
"AGAILZHARA",
"GAILA",
"PAISARHAT",
"BABUGANJ",
"BARISAL_CADET",
"CHANDPASHA",
"MADHABPASHA",
"NIZAMUDDIN_COLLEGE",
"RAHAMATPUR",
"THAKUR_MALLIK",
"BARAJALIA",
"OSMAN_MANJIL",
"BARISAL_SADAR",
"BUKHAINAGAR",
"JAGUARHAT",
"KASHIPUR",
"PATANG",
"SAHEBERHAT",
"SUGANDIA",
"BATAJOR",
"GOURANADI",
"KASHEMABAD",
"TARKI_BANDAR",
"LANGUTIA",
"LASKARPUR",
"MAHENDIGANJ",
"NALGORA",
"ULANIA",
"CHARKALEKHAN",
"KAZIRCHAR",
"MULADI",
"CHARAMANDI",
"KALASKATI",
"PADRI_SHIBPUR",
"SAHEBGANJ",
"SHIALGUNI",
"DAKUARHAT",
"DHAMURA",
"JUGIRKANDA",
"SHIKARPUR",
"UZIRPUR",
"BHOLA_SADAR",
"JOYNAGAR",
"BORHANUDDIN_UPO",
"MIRZAKALU",
"CHARFASHION",
"DULARHAT",
"KERAMATGANJ",
"DOULATKHAN",
"HAJIPUR",
"HAJIRHAT",
"HATSHOSHIGANJ",
"DAURIHAT",
"GAZARIA",
"LALMOHAN_UPO",
"BAUKATHI",
"GABHA",
"JHALOKATHI_SADAR",
"NABAGRAM",
"SHEKHERHAT",
"AMUA",
"KATHALIA",
"NIAMATEE",
"SHOULAJALIA",
"BEERKATHI",
"NALCHHITI",
"RAJAPUR",
"BAGABANDAR",
"BAUPHAL",
"BIRPASHA",
"KALAIA",
"KALISHARI",
"DASHMINA",
"GALACHIPA",
"GAZIPUR_BANDAR",
"KHEPUPARA",
"MAHIPUR",
"DUMKEE",
"MOUKARAN",
"PATUAKHALI_SADAR",
"RAHIMABAD",
"SUBIDKHALI",
"BANARIPARA",
"CHAKHAR",
"BHANDARIA",
"DHAOA",
"KANUDASHKATHI",
"JOLAGATI",
"JOYKUL",
"KAUKHALI",
"KEUNDIA",
"BETMOR_NATUN_HAT",
"GULISHAKHALI",
"HALTA",
"MATHBARIA",
"SHILARGANJ",
"TIARKHALI",
"TUSHKHALI",
"NAZIRPUR",
"SRIRAMKATHI",
"HULARHAT",
"PARERHAT",
"PIROJPUR_SADAR",
"DARUS_SUNNAT",
"JALABARI",
"KAURIKHARA",
"SWARUPKATHI",
"ALIKADAM",
"BANDARBAN_SADAR",
"NAIKHONG",
"ROANCHHARI",
"RUMA",
"LAMA",
"THANCHI",
"AKHAURA",
"AZAMPUR",
"GANGASAGAR",
"BANCHHARAMPUR",
"ASHUGANJ_SHARE",
"BRAHAMANBARIA_SADAR",
"POUN",
"TALSHAHAR",
"CHANDIDAR",
"CHARGACHH",
"GOPINATHPUR",
"KASBA",
"KUTI",
"JIBANGANJ",
"KAITALA",
"LAUBFATEHPUR",
"NABINAGAR",
"RASULLABAD",
"SALIMGANJ",
"SHAMGRAM",
"FANDAUK",
"NASIRNAGAR",
"CHANDURA",
"SARIAL",
"SHAHBAJPUR",
"BABURHAT",
"CHANDPUR_SADAR",
"PURANBAZAR",
"SAHATALI",
"CHANDRA",
"FARIDGANJ",
"GRIDKALIANDIA",
"ISLAMPUR_SHAH_ISAIN",
"RAMPURBAZAR",
"BOLAKHAL",
"HAJIGANJ",
"GANDAMARA",
"HAYEMCHAR",
"PAK_SHRIRAMPUR",
"RAHIMA_NAGAR",
"SHACHAR",
"KALIPUR",
"MATLOBGANJ",
"MOHANPUR",
"CHOTOSHI",
"ISLAMIA_MADRASHA",
"KHILABAZAR",
"PASHCHIM_KHERIHAR_AL",
"SHAHRASTI",
"ANOWARA",
"BATTALI",
"PAROIKORA",
"BOALKHALI",
"CHARANDWIP",
"IQBAL_PARK",
"KADURKHAL",
"KANUNGOPARA",
"SAKPURA",
"SAROATOLI",
"AL_AMIN_BARIA_MADRA",
"AMIN_JUTE_MILLS",
"ANANDABAZAR",
"BAYEZID_BOSTAMI",
"CHANDGAON",
"CHAWKBAZAR",
"CHITT_CANTONMENT",
"CHITT_CUSTOMS_ACCA",
"CHITT_POLITECHNIC_IN",
"CHITT_SAILERS_COLON",
"CHITTAGONG_AIRPORT",
"CHITTAGONG_BANDAR",
"CHITTAGONG_GPO",
"EXPORT_PROCESSING",
"FIROZSHAH",
"HALISHSHAR",
"JALALABAD",
"JALDIA_MERINE_ACCADE",
"MIDDLE_PATENGA",
"MOHARD",
"NORTH_HALISHAHAR",
"NORTH_KATULI",
"PAHARTOLI",
"PATENGA",
"RAMPURA_TSO",
"WAZEDIA",
"BARMA",
"DOHAZARI",
"EAST_JOARA",
"GACHBARIA",
"BHANDAR_SHARIF",
"FATIKCHHARI",
"HARUALCHHARI",
"NAJIRHAT",
"NANUPUR",
"NARAYANHAT",
"CHITT_UNIVERSITY",
"FATAHABAD",
"GORDUARA",
"HATHAZARI",
"KATIRHAT",
"MADRASA",
"NURALIBARI",
"YUNUS_NAGAR",
"GUNAGARI",
"JALDI",
"KHAN_BAHADUR",
"CHUNTI",
"LOHAGARA",
"PADUA",
"ABUTORAB",
"BHARAWAZHAT",
"DARROGAHAT",
"JOARGANJ",
"KORERHAT",
"MIRSHARAI",
"MOHAZANHAT",
"BUDHPARA",
"PATIYA_HEAD_OFFICE",
"DHAMAIR",
"RANGUNIA",
"B_I_T_POST_OFFICE",
"BEENAJURI",
"DEWANPUR",
"FATEPUR",
"GAHIRA",
"GUZRA_NOAPARA",
"JAGANNATH_HAT",
"KUNDESHWARI",
"MOHAMUNI",
"ROUZAN",
"SANDWIP",
"SHIBERHAT",
"URIRCHAR",
"BAITUL_IJJAT",
"BAZALIA",
"SATKANIA",
"BARABKUNDA",
"BAROIDHALA",
"BAWASHBARIA",
"BHATIARI",
"FOUZDARHAT",
"JAFRABAD",
"KUMIRA",
"SITAKUNDA",
"BARURA",
"MURDAFARGANJ",
"POYALGACHHA",
"BRAHMANPARA",
"BURICHANG",
"MAYNAMOTI_BAZAR",
"CHANDIA",
"MADHAIABAZAR",
"BATISA",
"CHIORA",
"CHOUDDAGRAM",
"COMILLA_CONTOMENT",
"COMILLA_SADAR",
"COURTBARI",
"HALIMANAGAR",
"SUAGANJ",
"DASHPARA",
"DAUDKANDI",
"ELIOTGANJ",
"BARASHALGHAR",
"DAVIDHAR",
"DHAMTEE",
"GANGAMANDAL",
"HOMNA",
"BIPULASAR",
"LAKSAM",
"LAKSHAMANPUR",
"CHHARIABAZAR",
"DHALUA",
"GUNABATI",
"LANGALKOT",
"BANGRA",
"COMPANYGANJ",
"MURADNAGAR",
"PANTIBAZAR",
"RAMCHANDARPUR",
"SONAKANDA",
"BADARKALI",
"CHIRINGGA_S_O",
"MALUMGHAT",
"COXS_BAZAR_SADAR",
"EIDGA",
"ZHILANJA",
"GORAKGHAT",
"KUTUBDIA",
"RAMU",
"HNILA",
"ST_MARTIN",
"TEKNAF",
"UKHIA",
"CHHAGALNAIA",
"DARAGA_HAT",
"MAHARAJGANJ",
"PUABASHIMULIA",
"CHHILONIA",
"DAGONDHUIA",
"DUDMUKHA",
"FAZILPUR",
"FENI_SADAR",
"LASKARHAT",
"SHARSHADIE",
"FULGAZI",
"PASHURAMPUR",
"SHUARBAZAR",
"AHMADPUR",
"KAZIRHAT",
"MOTIGANJ",
"SONAGAZI",
"DIGINALA",
"KHAGRACHARI_SADAR",
"LAXMICHHARI",
"MAHALCHHARI",
"MANIKCHHARI",
"MATIRANGA",
"PANCHHARI",
"RAMGHAR_HEAD_OFFICE",
"CHAR_ALEXGANDER",
"HAJIRGHAT",
"RAMGATIRHAT",
"AMANI_LAKSHIMPUR",
"CHANDRAGANJ",
"CHOUPALLI",
"DALAL_BAZAR",
"DUTTAPARA",
"LAKSHIMPUR_SADAR",
"MANDARI",
"RUPCHARA",
"ALIPUR",
"DOLTA",
"KANCHANPUR",
"NAAGMUD",
"PANPARA",
"RAMGANJ",
"BHUABARI",
"HAYDARGANJ",
"NAGERDIGHIRPAR",
"RAKHALLIA",
"RAYPUR",
"BASUR_HAT",
"CHARHAJARI",
"ALAIARPUR",
"AMISHA_PARA",
"BANGLABAZAR",
"BAZRA",
"BEGUMGANJ",
"BHABANI_JIBANPUR",
"CHOUMOHANI",
"DAUTI",
"JAMIDAR_HAT",
"JOYAG",
"JOYNARAYANPUR",
"KHALAFAT_BAZAR",
"KHALISHPUR",
"MAHESHGANJ",
"MIR_OWARISHPUR",
"NADONA",
"NANDIAPARA",
"OACHHEKPUR",
"RAJGANJ",
"SONAIMURI",
"TANGIRPAR",
"THANAR_HAT",
"BANSA_BAZAR",
"BODALCOURT",
"CHATKHIL",
"DOSH_GHARIA",
"KARIHATI",
"KHILPARA",
"PALLA",
"REZZAKPUR",
"SAHAPUR",
"SAMPARA",
"SHINGBAHURA",
"SOLLA",
"AFAZIA",
"HATIYA",
"TAMORADDI",
"CHAPRASHIR_HAT",
"CHAR_JABBAR",
"CHARAM_TUA",
"DIN_MONIR_HAT",
"KABIRHAT",
"KHALIFAR_HAT",
"MRIDDARHAT",
"NOAKHALI_COLLEGE",
"NOAKHALI_SADAR",
"PAK_KISHOREGANJ",
"SONAPUR",
"BEEZBAG",
"CHATARPAIA",
"KALLYANDI",
"KANKIRHAT",
"SENBAG",
"T_P_LAMUA",
"BARAKAL",
"BILAICHHARI",
"JARACHHARI",
"BETBUNIA",
"KALAMPATI",
"CHANDRAGHONA",
"KAPTAI",
"KAPTAI_NUTON_BAZAR",
"KAPTAI_PROJECT",
"LONGACHH",
"MARISHYA",
"NANICHHAR",
"RAJSTHALI",
"RANGAMATI_SADAR",
"DEMRA",
"MATUAIL",
"SARULIA",
"DHAKA_CANTONMENTTSO",
"DHAMRAI",
"KAMALPUR",
"JIGATALA_TSO",
"BANANI_TSO",
"GULSHAN_MODEL_TOWN",
"DHANIA_TSO",
"JOYPARA",
"NARISHA",
"PALAMGANJ",
"ATI",
"DHAKA_JUTE_MILLS",
"KALATIA",
"KERANIGANJ",
"KHILGAONTSO",
"KHILKHETTSO",
"POSTA_TSO",
"MIRPUR_TSO",
"MOHAMMADPUR_HOUSING",
"SANGSAD_BHABANTSO",
"BANGABHABANTSO",
"DILKUSHATSO",
"AGLA",
"CHURAIN",
"DAUDPUR",
"HASNABAD",
"KHALPAR",
"NAWABGANJ",
"NEW_MARKET_TSO",
"DHAKA_GPO",
"SHANTINAGR_TSO",
"BASABO_TSO",
"AMIN_BAZAR",
"DAIRY_FARM",
"EPZ",
"JAHANGIRNAGAR_UNIVER",
"KASHEM_COTTON_MILLS",
"RAJPHULBARIA",
"SAVAR",
"SAVAR_CANTTONMENT",
"SAVER_P_A_T_C",
"SHIMULIA",
"DHAKA_SADAR_HO",
"GENDARIA_TSO",
"WARI_TSO",
"TEJGAON_TSO",
"DHAKA_POLITECHNIC",
"UTTARA_MODEL_TWONTSO",
"ALFADANGA",
"BHANGA",
"BOALMARI",
"RUPATPAT",
"CHARBADRASHAN",
"AMBIKAPUR",
"BAITULAMAN_POLITECNI",
"FARIDPURSADAR",
"KANAIPUR",
"KAMARKALI",
"MADUKHALI",
"NAGARKANDA",
"TALMA",
"BISHWA_JAKER_MANJIL",
"HAT_KRISHAPUR",
"SADARPUR",
"SHRIANGAN",
"B_O_F",
"B_R_R",
"CHANDNA",
"GAZIPUR_SADAR",
"NATIONAL_UNIVERSITY",
"KALIAKAAR",
"SAFIPUR",
"KALIGANJ",
"PUBAIL",
"SANTANPARA",
"VAOAL_JAMALPUR",
"KAPASHIA",
"ERSHAD_NAGAR",
"MONNUNAGAR",
"NISHAT_NAGAR",
"BARMI",
"BASHAMUR",
"BOUBI",
"KAWRAID",
"SATKHAMAIR",
"SREEPUR",
"RAJENDRAPUR",
"RAJENDRAPUR_CANTTOME",
"BARFA",
"CHANDRADIGHALIA",
"GOPALGANJ_SADAR",
"ULPUR",
"JONAPUR",
"KASHIANI",
"RAMDIA_COLLEGE",
"RATOIL",
"KOTALIPARA",
"BATKIAMARI",
"KHANDARPARA",
"MAKSUDPUR",
"PATGATI",
"TUNGIPARA",
"DEWANGONJ",
"DEWANGONJ_S__MILLS",
"DURMOOT",
"GILABARI",
"ISLAMPUR",
"NANDINA",
"NARUNDI",
"JAMALPUR",
"MAHMOODPUR",
"MALANCHA",
"MALANDAH",
"BALIJHURI",
"MATHARGONJ",
"BAUSEE",
"GUNERBARI",
"JAGANNATH_GHAT",
"JAMUNA_SAR_KARKHANA",
"PINGNA",
"SHORISHABARI",
"BAJITPUR",
"LAKSMIPUR",
"SARARCHAR",
"BHAIRAB",
"HOSSENPUR",
"ITNA",
"KARIMGANJ",
"GOCHHIHATA",
"KATIADI",
"KISHOREGANJ_S_MILLS",
"KISHOREGANJ_SADAR",
"MAIZHATI",
"NILGANJ",
"CHHOYSUTI",
"KULIARCHAR",
"ABDULLAHPUR",
"MITHAMOIN",
"NIKLI",
"OSTAGRAM",
"PAKUNDIA",
"TARIAL",
"BAHADURPUR",
"BARHAMGANJ",
"NILAKSMIBANDAR",
"UMEDPUR",
"KALKINI",
"SAHABRAMPUR",
"CHARMUGRIA",
"HABIGANJ",
"KULPADDI",
"MADARIPUR_SADAR",
"MUSTAFAPUR",
"KHALIA",
"RAJOIR",
"GHEOR",
"JHITKA",
"LECHHRAGANJ",
"BARANGAIL",
"GORPARA",
"MAHADEBPUR",
"MANIKGANJ_BAZAR",
"MANIKGANJ_SADAR",
"BALIATI",
"SATURIA",
"ARICHA",
"SHIBALOY",
"TEWTA",
"UTHLI",
"BAIRA",
"JOYMANTOP",
"SINGAIR",
"GAJARIA",
"HOSSENDI",
"RASULPUR",
"GOURAGONJ",
"HALDIA_SO",
"HARIDIA",
"HARIDIA_DESO",
"KORHATI",
"LOHAJANG",
"MADINI_MANDAL",
"MEDINI_MANDAL_EDSO",
"KATHAKHALI",
"MIRKADIM",
"MUNSHIGANJ_SADAR",
"RIKABIBAZAR",
"ICHAPUR",
"KOLA",
"MALKHA_NAGAR",
"SHEKHER_NAGAR",
"SIRAJDIKHAN",
"BAGHRA",
"BARIKHAL",
"BHAGGYAKUL",
"HASHARA",
"KOLAPARA",
"KUMARBHOG",
"MAZPARA",
"SRINAGAR",
"VAGGYAKUL_SO",
"BAJRAJUGINI",
"BALIGAO",
"BETKAHAT",
"DIGHIRPAR",
"HASAIL",
"PURA",
"PURA_EDSO",
"TANGIBARI",
"BHALUKA",
"FULBARIA",
"DUTTARBAZAR",
"GAFORGAON",
"KANDIPARA",
"SHIBGANJ",
"USTI",
"GOURIPUR",
"RAMGOPALPUR",
"DHARA",
"HALUAGHAT",
"MUNSHIRHAT",
"ATHARABARI",
"ISSHWARGONJ",
"SOHAGI",
"MUKTAGACHHA",
"AGRICULTURE_UNIVERSI",
"BIDDYAGANJ",
"KAWATKHALI",
"MYMENSINGH_SADAR",
"PEARPUR",
"SHOMBHUGANJ",
"GANGAIL",
"NANDAIL",
"BELTIA",
"PHULPUR",
"TARAKANDA",
"AHMADBAD",
"DHALA",
"RAM_AMRITAGANJ",
"TRISHAL",
"ARAIHAZAR",
"GOPALDI",
"BAIDDER_BAZAR",
"BARA_NAGAR",
"BARODI",
"BANDAR",
"BIDS",
"D_C_MILLS",
"MADANGANJ",
"FATULLA_BAZAR",
"FATULLAH",
"NARAYANGANJ_SADAR",
"BHULTA",
"KANCHAN",
"MURAPARA",
"NAGRI",
"RUPGANJ",
"ADAMJEENAGAR",
"LN_MILLS",
"SIDDIRGANJ",
"BELABO",
"HATIRDIA",
"KATABARIA",
"MONOHORDI",
"MADHABDI",
"NARSHINGDI_COLLEGE",
"NARSHINGDI_SADAR",
"PANCHDONA",
"UMC_JUTE_MILLS",
"CHAR_SINDHUR",
"GHORASHAL",
"GHORASHAL_UREA_FACTO",
"PALASH",
"BAZAR_HASNABAD",
"RADHAGANJ_BAZAR",
"RAYPURA",
"SHIBPUR",
"SUSNNG_DURGAPUR",
"ATPARA",
"BARHATTA",
"DHARAMPASHA",
"DHOBAURA",
"SAKOAI",
"KALMAKANDA",
"KENDUA",
"KHALIAJHRI",
"SHALDIGHA",
"MADAN",
"MODDOYNAGAR",
"MOHANGANJ",
"BAIKHERHATI",
"NETRAKONA_SADAR",
"JARIA_JHANJHAIL",
"PURBADHOLA",
"SHAMGONJ",
"BALIAKANDI",
"NALIA",
"MRIGIBAZAR",
"PANGSHA",
"RAMKOL",
"RATANDIA",
"GOALANDA",
"KHANKHANAPUR",
"RAJBARI_SADAR",
"BHEDORGANJ",
"DAMUDHYA",
"GOSAIRHAT",
"JAJIRA",
"BHOZESHWAR",
"GHARISAR",
"KARTIKPUR",
"NARIA",
"UPSHI",
"ANGARIA",
"CHIKANDI",
"SHARIATPUR_SADAR",
"BAKSHIGONJ",
"JHINAIGATI",
"GONOPADDI",
"NAKLA",
"HATIBANDHA",
"NALITABARI",
"SHERPUR_SHADAR",
"SHRIBARDI",
"BASAIL",
"BHUAPUR",
"DELDUAR",
"ELASIN",
"HINGA_NAGAR",
"JANGALIA",
"LOWHATI",
"PATHARAIL",
"D__PAKUTIA",
"DHALAPARA",
"GHATIAL",
"LOHANI",
"ZAHIDGANJ",
"GOPALPUR",
"HEMNAGAR",
"JHOWAIL",
"BALLABAZAR",
"ELINGA",
"KALIHATI",
"NAGARBARI",
"NAGARBARI_SO",
"NAGBARI",
"PALISHA",
"RAJAFAIR",
"KASHKAWLIA",
"DHOBARI",
"MADHUPUR",
"GORAI",
"JARMUKI",
"M_C__COLLEGE",
"MIRZAPUR",
"MOHERA",
"WARRI_PAIKPARA",
"DHUBURIA",
"NAGARPUR",
"SALIMABAD",
"KOCHUA",
"SAKHIPUR",
"KAGMARI",
"KOROTIA",
"PURABARI",
"SANTOSH",
"TANGAIL_SADAR",
"BAGERHAT_SADAR",
"P_C_COLLEGE",
"RANGDIA",
"CHALNA_ANKORAGE",
"MONGLA_PORT",
"BARABARIA",
"CHITALMARI",
"BHANGANPAR_BAZAR",
"FAKIRHAT",
"MANSA",
"KACHUA",
"SONARKOLA",
"CHARKULIA",
"DARIALA",
"KAHALPUR",
"MOLLAHAT",
"NAGARKANDI",
"PAK_GANGNI",
"MORELGANJ",
"SANNASI_BAZAR",
"TELISATEE",
"FOYLAHAT",
"GOURAMBHA",
"RAMPAL",
"SONATUNIA",
"RAYENDA",
"ALAMDANGA",
"HARDI",
"CHUADANGA_SADAR",
"MUNSHIGANJ",
"ANDULBARIA",
"DAMURHUDA",
"DARSHANA",
"DOULATGANJ",
"BAGHARPARA",
"GOURANAGAR",
"CHOUGACHHA",
"BASUNDIA",
"CHANCHRA",
"CHURAMANKATHI",
"JESSORE_AIRBACH",
"JESSORE_CANTTONMENT",
"JESSORE_SADAR",
"JESSORE_UPA_SHAHAR",
"RUPDIA",
"JHIKARGACHHA",
"KESHOBPUR",
"MONIRAMPUR",
"BHUGILHAT",
"NOAPARA",
"RAJGHAT",
"BAG_ACHRA",
"BENAPOLE",
"JADABPUR",
"SARSA",
"HARINAKUNDU",
"JINAIDAHA_CADET_COLLEGE",
"JINAIDAHA_SADAR",
"KOTCHANDPUR",
"MAHESHPUR",
"HATBAR_BAZAR",
"NALDANGA",
"KUMIRADAHA",
"SHAILAKUPA",
"ALAIPUR",
"BELPHULIA",
"RUPSHA",
"BATIAGHAT",
"SURKALEE",
"BAJUA",
"CHALNA_BAZAR",
"DAKUP",
"NALIAN",
"CHANDNI_MAHAL",
"DIGALIA",
"GAZIRHAT",
"GHOSHGHATI",
"SENHATI",
"ATRA_SHILPA_AREA",
"BIT_KHULNA",
"DOULATPUR",
"JAHANABAD_CANTTONMEN",
"KHULA_SADAR",
"KHULNA_G_P_O",
"KHULNA_SHIPYARD",
"KHULNA_UNIVERSITY",
"SIRAMANI",
"SONALI_JUTE_MILLS",
"AMADEE",
"MADINABAD",
"CHANDKHALI",
"GARAIKHALI",
"GODAIPUR",
"KAPILMONI",
"KATIPARA",
"PAIKGACHHA",
"PHULTALA",
"CHUKNAGAR",
"GHONABANDA",
"SAJIARA",
"SHAHAPUR",
"PAK_BARASAT",
"TERAKHADA",
"ALLARDARGA",
"BHERAMARA",
"GANGES_BHERAMARA",
"JANIPUR",
"KHOKSA",
"KUMARKHALI",
"PANTI",
"ISLAMI_UNIVERSITY",
"JAGATI",
"KUSHTIA_MOHINI",
"KUSTIA_SADAR",
"AMLA_SADARPUR",
"MIRPUR",
"PORADAHA",
"KHASMATHURAPUR",
"RAFAYETPUR",
"TARAGUNIA",
"ARPARA",
"MAGURA_SADAR",
"BINODPUR",
"MOHAMMADPUR",
"NAHATA",
"LANGALBADH",
"NACHOL",
"SHRIPUR",
"GANGNI",
"AMJHUPI",
"MEHERPUR_SADAR",
"MUJIB_NAGAR_COMPLEX",
"KALIA",
"BARADIA",
"LAXMIPASHA",
"LOHAGORA",
"NALDI",
"MOHAJAN",
"NARAIL_SADAR",
"RATANGANJ",
"ASHASHUNI",
"BARADAL",
"DEBBHATA",
"GURUGRAM",
"HAMIDPUR",
"JHAUDANGA",
"KALAROA",
"KHORDO",
"MURARIKATI",
"KALIGANJ_UPO",
"NALTA_MUBAROKNAGAR",
"RATANPUR",
"BURI_GOALINI",
"GABURA",
"HABINAGAR",
"NAKIPUR",
"NAOBEKI",
"NOORNAGAR",
"BUDHHAT",
"GUNAKAR_KATI",
"SATKHIRA_ISLAMIA_ACC",
"SATKHIRA_SADAR",
"PATKELGHATA",
"TAALA",
"ADAMDIGHI",
"NASHARATPUR",
"SANTAHAR",
"BOGRA_CANTTONMENT",
"BOGRA_SADAR",
"DHUNAT",
"GOSAIBARI",
"DUPCHACHIA",
"TALORA",
"GABTOLI",
"SUKHANPUKUR",
"KAHALU",
"NANDIGRAM",
"CHANDAN_BAISHA",
"SARIAKANDI",
"CHANDAIKONA",
"PALLI_UNNYAN_ACCADEM",
"SHERPUR",
"SONATOLA",
"BHOLAHAT",
"AMNURA",
"CHAPINAWBGANJ_SADAR",
"RAJARAMPUR",
"RAMCHANDRAPUR",
"MANDUMALA",
"GOMASHTAPUR",
"ROHANPUR",
"KANSART",
"MANAKSHA",
"SHIBGANJ_U_P_O",
"AKKLEPUR",
"JAMALGANJ",
"TILAKPUR",
"JOYPURHAT_SADAR",
"KALAI",
"KHETLAL",
"PANCHBIBI",
"AHSANGANJ",
"BANDAI",
"BADALGACHHI",
"DHAMUIRHAT",
"NAOGAON_SADAR",
"NIAMATPUR",
"NITPUR",
"PANGURIA",
"PORSA",
"PATNITALA",
"BALIHAR",
"MANDA",
"PRASADPUR",
"KASHIMPUR",
"RANINAGAR",
"MODUHIL",
"SAPAHAR",
"ABDULPUR",
"GOPALPUR_U_P_O",
"LALPUR_S_O",
"BARAIGRAM",
"DAYARAMPUR",
"HARUA",
"HATGURUDASPUR",
"LAXMAN",
"BAIDDYABAL_GHARIA",
"DIGAPATIA",
"MADHNAGAR",
"NATORE_SADAR",
"SINGRA",
"BANWARINAGAR",
"BERA",
"KASHINATHPUR",
"NAKALIA",
"PURAN_BHARENGA",
"BHANGURA",
"CHATMOHAR",
"DEBOTTAR",
"DHAPARI",
"ISHWARDI",
"PAKSHI",
"HAMAYETPUR",
"KALIKO_COTTON_MILLS",
"PABNA_SADAR",
"SATHIA",
"SAGARKANDI",
"SUJANAGAR",
"ARANI",
"BAGHA",
"BHABANIGANJ",
"TAHARPUR",
"CHARGHAT",
"SARDA",
"DURGAPUR",
"GODAGARI",
"PREMTOLI",
"KHODMOHANPUR",
"LALITGANJ",
"RAJSHAHI_SUGAR_MILLS",
"SHYAMPUR",
"PUTIA",
"BINODPUR_BAZAR",
"GHURAMARA",
"KAZLA",
"RAJSHAHI_CANTTONMENT",
"RAJSHAHI_COURT",
"RAJSHAHI_SADAR",
"RAJSHAHI_UNIVERSITY",
"SAPURA",
"TANOR",
"BAIDDYA_JAM_TOIL",
"BELKUCHI",
"ENAYETPUR",
"SOHAGPUR",
"STHAL",
"DHANGORA",
"MALONGA",
"GANDAIL",
"KAZIPUR",
"SHUVGACHHA",
"JAMIRTA",
"KAIJURI",
"PORJANA",
"SHAHJADPUR",
"RAIPUR",
"RASHIDABAD",
"SIRAJGANJ_SADAR",
"TARASH",
"LAHIRI_MOHANPUR",
"SALAP",
"ULLAPARA",
"ULLAPARA_R_S",
"BANGLA_HILI",
"BIRAL",
"BIRAMPUR",
"BIRGANJ",
"CHRIRBANDAR",
"RANIRBANDAR",
"DINAJPUR_RAJBARI",
"DINAJPUR_SADAR",
"KHANSAMA",
"PAKARHAT",
"NABABGANJ",
"GHORAGHAT",
"OSMANPUR",
"PARBATIPUR",
"PHULBARI",
"SETABGANJ",
"BONARPARA",
"SAGHATA",
"GAIBANDHA_SADAR",
"GOBINDHAGANJ",
"MAHIMAGANJ",
"PALASHBARI",
"BHARATKHALI",
"PHULCHHARI",
"SAADULLAPUR",
"BAMANDANGA",
"SUNDARGANJ",
"BHURUNGAMARI",
"CHILMARI",
"JORGACHH",
"KURIGRAM_SADAR",
"PANDUL",
"NAGESHWAR",
"NAZIMKHAN",
"RAJARHAT",
"RAJIBPUR",
"ROUMARI",
"BAZARHAT",
"ULIPUR",
"ADITMARI",
"KULAGHAT_SO",
"LALMONIRHAT_SADAR",
"MOGHALHAT",
"BAURA",
"BURIMARI",
"PATGRAM",
"TUSHBHANDAR",
"DIMLA",
"GHAGA_KHARIBARI",
"CHILAHATI",
"DOMAR",
"JALDHAKA",
"KISHORIGANJ",
"NILPHAMARI_SADAR",
"NILPHAMARI_SUGAR_MIL",
"SYEDPUR_UPASHAHAR",
"BODA",
"CHOTTO_DAB",
"MIRJAPUR",
"DABIGANJ",
"PANCHAGARH_SADAR",
"TETULIA",
"BADARGANJ",
"GANGACHARA",
"HARAGACHH",
"KAUNIA",
"MITHAPUKUR",
"PIRGACHHA",
"ALAMNAGAR",
"MAHIGANJ",
"RANGPUR_CADET_COLLEG",
"RANGPUR_CARMIECAL_COL",
"RANGPUR_SADAR",
"RANGPUR_UPA_SHAHAR",
"TARAGANJ",
"BALIADANGI",
"LAHIRI",
"JIBANPUR",
"PIRGANJ",
"NEKMARAD",
"RANI_SANKAIL",
"RUHIA",
"THAKURGAON_ROAD",
"THAKURGAON_SADAR",
"AZMIREEGANJ",
"BAHUBAL",
"BANIACHANG",
"JATRAPASHA",
"KADIRGANJ",
"CHANDPURBAGAN",
"CHUNARUGHAT",
"NARAPATI",
"GOPAYA",
"HOBIGANJ_SADAR",
"SHAESTAGANJ",
"KALAUK",
"LAKHAI",
"ITAKHOLA",
"MADHABPUR",
"SAIHAMNAGAR",
"SHAHAJIBAZAR",
"DIGALBAK",
"GOLDUBA",
"GOPLARBAZAR",
"INATHGANJ",
"NABIGANJ",
"BARALEKHA",
"DHAKKHINBAG",
"JURI",
"PURBASHAHABAJPUR",
"KAMALGANJ",
"KERAMATNAGA",
"MUNSHIBAZAR",
"PATRAKHOLA",
"SHAMSHER_NAGAR",
"BARAMCHAL",
"KAJALDHARA",
"KARIMPUR",
"KULAURA",
"LANGLA",
"PRITHIMPASHA",
"TILLAGAON",
"AFROZGANJ",
"BARAKAPAN",
"MONUMUKH",
"MOULVIBAZAR_SADAR",
"RAJNAGAR",
"KALIGHAT",
"KHEJURICHHARA",
"NARAIN_CHORA",
"SATGAON",
"SRIMANGAL",
"BISHAMSAPUR",
"CHHATAK",
"CHHATAK_CEMENT_FACTO",
"CHHATAK_PAPER_MILLS",
"CHOURANGI_BAZAR",
"GABINDAGANJ",
"GABINDAGANJ_NATUN_BA",
"ISLAMABAD",
"JAHIDPUR",
"KHURMA",
"MOINPUR",
"DHIRAI_CHANDPUR",
"JAGDAL",
"DUARA_BAZAR",
"GHUNGIAR",
"ATUAJAN",
"HASAN_FATEMAPUR",
"JAGNNATHPUR",
"RASULGANJ",
"SHIRAMSI",
"SYEDPUR",
"SACHNA",
"PAGLA",
"PATHARIA",
"SUNAMGANJ_SADAR",
"TAHIRPUR",
"BALAGANJ",
"BEGUMPUR",
"BRAHMAN_SHASHON",
"GAHARPUR",
"GOALA_BAZAR",
"KARUA",
"KATHAL_KHAIR",
"NATUN_BAZAR",
"OMARPUR",
"TAJPUR",
"BIANIBAZAR",
"CHURKAI",
"JALDUP",
"KURAR_BAZAR",
"MATHIURA",
"SALIA_BAZAR",
"BISHWANATH",
"DASHGHAR",
"DEOKALAS",
"DOULATHPUR",
"SINGER_KANCH",
"FENCHUGANJ",
"FENCHUGANJ_SAREKARKH",
"CHIKNAGUL",
"GOAINHAT",
"JAFLONG",
"BANIGRAM",
"CHANDANPUR",
"DAKKHIN_BHADASHORE",
"DHAKA_DAKKHIN",
"GOPALGANNJ",
"RANAPING",
"JAINTHAPUR",
"ICHHAMATI",
"JAKIGANJ",
"CHATULBAZAR",
"GACHBARI",
"KANAIGHAT",
"MANIKGANJ",
"KOMPANYGANJ",
"BIRAHIMPUR",
"JALALABAD_CANTOMENT",
"KADAMTALI",
"KAMALBAZER",
"KHADIMNAGAR",
"LALBAZAR",
"MOGLA",
"RANGA_HAJIGANJ",
"SHAHAJALAL_SCIENCE",
"SILAM",
"SYLHE_SADAR",
"SYLHET_BIMAN_BONDAR",
"SYLHET_CADET_COL",
"JHALOKATI_SADAR",
"PATIYA",
"RAMGATI",
"BATIAGHATA",
"BAGATIPARA",
"NAWABGANJ_SADAR",
"GAZIPUR_SADAR_JOYDEBPUR",
"HATIA",
"JHENAIGATI",
"JAMALPUR_SADAR",
"NARUNDI_POLICE_I_C",
"CHAR_RAJIBPUR",
"NAGESHWARI",
"RAJASTHALI",
"RAIPURA",
"TANORE",
"DURGAPUR_UPAZILLA",
"SHERPUR_SADAR",
"KALIA_UPAZILLA",
"MONOHARDI",
"SHARIATPUR_SADAR_PALONG",
"CHIRIRBANDAR",
"BIJOYNAGAR",
"NAIKHONGCHHARI",
"LOHAGARA_UPAZILLA",
"COMILLA_SADAR_SOUTH",
"HABIGANJ_SADAR",
"KHALIAJURI_UPAZILLA",
"PURBADHALA_UPAZILLA",
"KENDUA_UPAZILLA",
"ATPARA_UPAZILLA",
"BARHATTA_UPAZILLA",
"KALMAKANDA_UPAZILLA",
"MADAN_UPAZILLA",
"MOHANGANJ_UPAZILLA",
"GOALANDAGHAT",
"KALIAKIOR"
]

district_ids = [
"dhakaDistrictId",
"faridpurDistrictId",
"gazipurDistrictId",
"gopalganjDistrictId",
"jamalpurDistrictId",
"kishoreganjDistrictId",
"madaripurDistrictId",
"manikganjDistrictId",
"munshiganjDistrictId",
"mymensinghDistrictId",
"narayanganjDistrictId",
"narsingdiDistrictId",
"netrokonaDistrictId",
"rajbariDistrictId",
"shariatpurDistrictId",
"sherpurDistrictId",
"tangailDistrictId",
"boguraDistrictId",
"joypurhatDistrictId",
"naogaonDistrictId",
"natoreDistrictId",
"nawabganjDistrictId",
"pabnaDistrictId",
"rajshahiDistrictId",
"sirajgonjDistrictId",
"dinajpurDistrictId",
"gaibandhaDistrictId",
"kurigramDistrictId",
"lalmonirhatDistrictId",
"nilphamariDistrictId",
"panchagarhDistrictId",
"rangpurDistrictId",
"thakurgaonDistrictId",
"bargunaDistrictId",
"barishalDistrictId",
"bholaDistrictId",
"jhalokatiDistrictId",
"patuakhaliDistrictId",
"pirojpurDistrictId",
"bandarbanDistrictId",
"brahmanbariaDistrictId",
"chandpurDistrictId",
"chattogramDistrictId",
"cumillaDistrictId",
"coxs_bazarDistrictId",
"feniDistrictId",
"khagrachariDistrictId",
"lakshmipurDistrictId",
"noakhaliDistrictId",
"rangamatiDistrictId",
"habiganjDistrictId",
"maulvibazarDistrictId",
"sunamganjDistrictId",
"sylhetDistrictId",
"bagerhatDistrictId",
"chuadangaDistrictId",
"jashoreDistrictId",
"jhenaidahDistrictId",
"khulnaDistrictId",
"kushtiaDistrictId",
"maguraDistrictId",
"meherpurDistrictId",
"narailDistrictId",
"satkhiraDistrictId"
]

division_ids = [
"stateDhakaId",
"stateChattogramId",
"stateBarishalId",
"stateKhulnaId",
"stateMymensinghId",
"stateRajshahiId",
"stateRangpurId",
"stateSylhetId"
]

enum = []

district = ""
division = ''
upazila = ""

with open('bd-postcodes.json') as f:
  post_offices = json.load(f)

with open('bd-upazilas.json') as f:
  upazilas = json.load(f)

with open('bd-districts.json') as f:
  districts = json.load(f)

with open('bd-divisions.json') as f:
  divisions = json.load(f)

# for en in upazila_enum:
#   rep = en.replace('_', ' ')
#   cap = rep.capitalize()
#   enum.append(cap)

import re

# for post in post_offices['postcodes']:
#     post_upper = post['postOffice'].upper()
#     with open('post_office_list.txt', 'a') as f:
#         f.write(f'{post_upper} = "{post_upper}",\n')

# count = 0
# for post in post_offices['postcodes']:
#   if 'district_id' in post:
#     count += 1

# print(count)

# for post in post_offices['postcodes']:
#   if 'district_id' in post:
#     with open('post_office.json', 'a', encoding='utf-8') as outfile:
#       json.dump(post, outfile)

# for div in divisions['divisions']:
#   for dis in districts['districts']:
#     for u in upazilas['upazilas']:
#       for post in post_offices['postcodes']:
#         if 'district_id' in post:
#           post_upper = post['postOffice']
#           if div['id'] == post['division_id'] and dis['id'] == post['district_id']:
#             for div_ids in division_ids:
#               div_name = div['name'].lower()
#               if re.search(div_name, div_ids, re.IGNORECASE):
#                 for dis_ids in district_ids:
#                   dis_name = dis['name'].lower()
#                   if re.search(dis_name, dis_ids, re.IGNORECASE):
#                     if re.search(post['upazila'], u['name'], re.IGNORECASE):
#                       for en in upazila_enum:
#                         rep = en.replace('_', ' ')
#                         cap = rep.capitalize()
#                         if re.search(post['postOffice'], cap, re.IGNORECASE):
#                           for id in upazila_ids:
#                             low = en.lower()
#                             if re.search(low, id, re.IGNORECASE):
#                               with open('post_office_seeder.ts', 'a') as f:
#                                   f.write(f"""[CoreLocalisationServicePostOfficeInformations.{en}]: {{
#                                               id: '{uuid.uuid4()}',
#                                               country_id: bangladeshCountryId,
#                                               state_id: {div_ids},
#                                               district_id: _district.{dis_ids},
#                                               upazila_id: _upazila.{id},
#                                               postal_code: '{post['postCode']}',
#                                               name: '{post_upper}',
#                                               name_bn: '{str(post['postOffice'])}',
#                                               iso_code: '',
#                                               is_active: true,
#                                               deleted_at: null,
#                                           }},""")

num = 0
for post in post_offices['postcodes']:
  num += 1
  if 'district_id' in post:
    post_upper = post['postOffice']
    for div in divisions['divisions']:
      if div['id'] == post['division_id']:
        for div_ids in division_ids:
          div_name = div['name'].lower()
          if re.search(div_name, div_ids, re.IGNORECASE):
            for dis in districts['districts']:
              if dis['id'] == post['district_id']:
                for dis_ids in district_ids:
                  dis_name = dis['name'].lower()
                  if re.search(dis_name, dis_ids, re.IGNORECASE):
                    for upazila_id in upazila_ids:
                      if re.search(post['upazila'].replace(' ', '_'), upazila_id, re.IGNORECASE):
                        for en in post_office_enum:
                          rep = en.replace('_', ' ')
                          cap = rep.capitalize()
                          if re.search(cap, post['postOffice'], re.IGNORECASE):
                            with open('post_office_seeder_2.ts', 'a') as f:
                              f.write(f"""[CoreLocalisationServicePostOfficeInformations.{en}]: {{
                                          id: '{uuid.uuid4()}',
                                          country_id: bangladeshCountryId,
                                          state_id: {div_ids},
                                          district_id: _district.{dis_ids},
                                          upazila_id: _upazila.{upazila_id},
                                          postal_code: '{post['postCode']}',
                                          name: '{post_upper}',
                                          name_bn: '{str(post['postOffice'])}',
                                          iso_code: '{en[:3]}-{num}',
                                          is_active: true,
                                          deleted_at: null,
                                      }},""")