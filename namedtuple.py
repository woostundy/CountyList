# coding:utf-8
from collections import namedtuple

Country = namedtuple('Country',
                     'name alpha2 alpha3 numeric apolitical_name chinese_name')

_records = [
    Country(u"Andorra", "AD", "AND", "020", u"安道尔"),
    Country(u"United Arab Emirates", "AE", "ARE", "784", u"阿拉伯联合酋长国"),
    Country(u"Afghanistan", "AF", "AFG", "004", u"阿富汗"),
    Country(u"Antigua and Barbuda", "AG", "ATG", "028", u"安提瓜和巴布达"),
    Country(u"Anguilla", "AI", "AIA", "660", u"安圭拉"),
    Country(u"Albania", "AL", "ALB", "008", u"阿尔巴尼亚"),
    Country(u"Armenia", "AM", "ARM", "051", u"亚美尼亚"),
    Country(u"Angola", "AO", "AGO", "024", u"安哥拉"),
    Country(u"Antarctica", "AQ", "ATA", "010", u"南极洲"),
    Country(u"Argentina", "AR", "ARG", "032", u"阿根廷"),
    Country(u"American Samoa", "AS", "ASM", "016", u"美属萨摩亚"),
    Country(u"Austria", "AT", "AUT", "040", u"奥地利"),
    Country(u"Australia", "AU", "AUS", "036", u"澳大利亚"),
    Country(u"Aruba", "AW", "ABW", "533", u"阿鲁巴"),
    Country(u"Azerbaijan", "AZ", "AZE", "031", u"阿塞拜疆"),
    Country(u"Bosnia and Herzegovina", "BA", "BIH", "070", u"波斯尼亚和黑塞哥维那"),
    Country(u"Barbados", "BB", "BRB", "052", u"巴巴多斯"),
    Country(u"Bangladesh", "BD", "BGD", "050", u"孟加拉国"),
    Country(u"Belgium", "BE", "BEL", "056", u"比利时"),
    Country(u"Burkina Faso", "BF", "BFA", "854", u"布基纳法索"),
    Country(u"Bulgaria", "BG", "BGR", "100", u"保加利亚"),
    Country(u"Bahrain", "BH", "BHR", "048", u"巴林"),
    Country(u"Burundi", "BI", "BDI", "108", u"布隆迪"),
    Country(u"Benin", "BJ", "BEN", "204", u"贝宁"),
    Country(u"Bermuda", "BM", "BMU", "060", u"百慕大"),
    Country(u"Brunei Darussalam", "BN", "BRN", "096", u"文莱"),
    Country(u"Bolivia, Plurinational State of", "BO", "BOL", "068", u"玻利维亚"),
    Country(u"Brazil", "BR", "BRA", "076", u"巴西"),
    Country(u"Bahamas", "BS", "BHS", "044", u"巴哈马"),
    Country(u"Bhutan", "BT", "BTN", "064", u"不丹"),
    Country(u"Bouvet Island", "BV", "BVT", "074", u"布维特岛"),
    Country(u"Botswana", "BW", "BWA", "072", u"博茨瓦纳"),
    Country(u"Belarus", "BY", "BLR", "112", u"白俄罗斯"),
    Country(u"Belize", "BZ", "BLZ", "084", u"伯利兹"),
    Country(u"Canada", "CA", "CAN", "124", u"加拿大"),
    Country(u"Cocos (Keeling) Islands", "CC", "CCK", "166", u"科科斯群岛"),
    Country(u"Congo, Democratic Republic of the", "CD", "COD", "180", u"刚果（金）"),
    Country(u"Central African Republic", "CF", "CAF", "140", u"中非共和国"),
    Country(u"Congo", "CG", "COG", "178", u"刚果（布）"),
    Country(u"Switzerland", "CH", "CHE", "756", u"瑞士"),
    Country(u"Cook Islands", "CK", "COK", "184", u"库克群岛"),
    Country(u"Chile", "CL", "CHL", "152", u"智利"),
    Country(u"Cameroon", "CM", "CMR", "120", u"喀麦隆"),
    Country(u"China", "CN", "CHN", "156", u"中国"),
    Country(u"Colombia", "CO", "COL", "170", u"哥伦比亚"),
    Country(u"Costa Rica", "CR", "CRI", "188", u"哥斯达黎加"),
    Country(u"Cuba", "CU", "CUB", "192", u"古巴"),
    Country(u"Cabo Verde", "CV", "CPV", "132", u"佛得角"),
    Country(u"Christmas Island", "CX", "CXR", "162", u"圣诞岛"),
    Country(u"Cyprus", "CY", "CYP", "196", u"塞浦路斯"),
    Country(u"Czech Republic", "CZ", "CZE", "203", u"捷克共和国"),
    Country(u"Germany", "DE", "DEU", "276", u"德国"),
    Country(u"Djibouti", "DJ", "DJI", "262", u"吉布提"),
    Country(u"Denmark", "DK", "DNK", "208", u"丹麦"),
    Country(u"Dominica", "DM", "DMA", "212", u"多米尼加"),
    Country(u"Dominican Republic", "DO", "DOM", "214", u"多米尼加共和国"),
    Country(u"Algeria", "DZ", "DZA", "012", u"阿尔及利亚"),
    Country(u"Ecuador", "EC", "ECU", "218", u"厄瓜多尔"),
    Country(u"Estonia", "EE", "EST", "233", u"爱沙尼亚"),
    Country(u"Egypt", "EG", "EGY", "818", u"埃及"),
    Country(u"Western Sahara", "EH", "ESH", "732", u"西撒哈拉"),
    Country(u"Eritrea", "ER", "ERI", "232", u"厄立特里亚"),
    Country(u"Spain", "ES", "ESP", "724", u"西班牙"),
    Country(u"Ethiopia", "ET", "ETH", "231", u"埃塞俄比亚"),
    Country(u"Finland", "FI", "FIN", "246", u"芬兰"),
    Country(u"Fiji", "FJ", "FJI", "242", u"斐济"),
    Country(u"Falkland Islands (Malvinas)", "FK", "FLK", "238", u"福克兰群岛"),
    Country(u"Micronesia, Federated States of", "FM", "FSM", "583", u"密克罗尼西亚联邦"),
    Country(u"Faroe Islands", "FO", "FRO", "234", u"法罗群岛"),
    Country(u"France", "FR", "FRA", "250", u"法国"),
    Country(u"Gabon", "GA", "GAB", "266", u"加蓬"),
    Country(u"United Kingdom", "GB", "GBR", "826", u"英国"),
    Country(u"Grenada", "GD", "GRD", "308", u"格林纳达"),
    Country(u"Georgia", "GE", "GEO", "268", u"格鲁吉亚"),
    Country(u"French Guiana", "GF", "GUF", "254", u"法属圭亚那"),
    Country(u"Guernsey", "GG", "GGY", "831", u"格恩西岛"),
    Country(u"Ghana", "GH", "GHA", "288", u"加纳"),
    Country(u"Gibraltar", "GI", "GIB", "292", u"直布罗陀"),
    Country(u"Greenland", "GL", "GRL", "304", u"格陵兰"),
    Country(u"Gambia", "GM", "GMB", "270", u"冈比亚"),
    Country(u"Guinea", "GN", "GIN", "324", u"几内亚"),
    Country(u"Guadeloupe", "GP", "GLP", "312", u"瓜德罗普岛"),
    Country(u"Equatorial Guinea", "GQ", "GNQ", "226", u"赤道几内亚"),
    Country(u"Greece", "GR", "GRC", "300", u"希腊"),
    Country(u"South Georgia and the South Sandwich Islands", "GS", "SGS", "239", u"南乔治亚岛和南桑威齐群岛"),
    Country(u"Guatemala", "GT", "GTM", "320", u"危地马拉"),
    Country(u"Guam", "GU", "GUM", "316", u"关岛"),
    Country(u"Guinea-Bissau", "GW", "GNB", "624", u"几内亚比绍"),
    Country(u"Guyana", "GY", "GUY", "328", u"圭亚那"),
    Country(u"Hong Kong", "HK", "HKG", "344", u"中国香港特别行政区"),
    Country(u"Heard Island and McDonald Islands", "HM", "HMD", "334", u"赫德与麦克唐纳群岛"),
    Country(u"Honduras", "HN", "HND", "340", u"洪都拉斯"),
    Country(u"Croatia", "HR", "HRV", "191", u"克罗地亚"),
    Country(u"Haiti", "HT", "HTI", "332", u"海地"),
    Country(u"Hungary", "HU", "HUN", "348", u"匈牙利"),
    Country(u"Indonesia", "ID", "IDN", "360", u"印度尼西亚"),
    Country(u"Ireland", "IE", "IRL", "372", u"爱尔兰"),
    Country(u"Israel", "IL", "ISR", "376", u"以色列"),
    Country(u"Isle of Man", "IM", "IMN", "833", u"曼岛"),
    Country(u"India", "IN", "IND", "356", u"印度"),
    Country(u"British Indian Ocean Territory", "IO", "IOT", "086", u"英属印度洋领地"),
    Country(u"Iraq", "IQ", "IRQ", "368", u"伊拉克"),
    Country(u"Iran, Islamic Republic of", "IR", "IRN", "364", u"伊朗"),
    Country(u"Iceland", "IS", "ISL", "352", u"冰岛"),
    Country(u"Italy", "IT", "ITA", "380", u"意大利"),
    Country(u"Jersey", "JE", "JEY", "832", u"泽西岛"),
    Country(u"Jamaica", "JM", "JAM", "388", u"牙买加"),
    Country(u"Jordan", "JO", "JOR", "400", u"约旦"),
    Country(u"Japan", "JP", "JPN", "392", u"日本"),
    Country(u"Kenya", "KE", "KEN", "404", u"肯尼亚"),
    Country(u"Kyrgyzstan", "KG", "KGZ", "417", u"吉尔吉斯斯坦"),
    Country(u"Cambodia", "KH", "KHM", "116", u"柬埔寨"),
    Country(u"Kiribati", "KI", "KIR", "296", u"基里巴斯"),
    Country(u"Comoros", "KM", "COM", "174", u"科摩罗"),
    Country(u"Saint Kitts and Nevis", "KN", "KNA", "659", u"圣基茨和尼维斯"),
    Country(u"Korea, Democratic People's Republic of", "KP", "PRK", "408", u"朝鲜"),
    Country(u"Korea, Republic of", "KR", "KOR", "410", u"韩国"),
    Country(u"Kuwait", "KW", "KWT", "414", u"科威特"),
    Country(u"Cayman Islands", "KY", "CYM", "136", u"开曼群岛"),
    Country(u"Kazakhstan", "KZ", "KAZ", "398", u"哈萨克斯坦"),
    Country(u"Lao People's Democratic Republic", "LA", "LAO", "418", u"老挝人民民主共和国"),
    Country(u"Lebanon", "LB", "LBN", "422", u"黎巴嫩"),
    Country(u"Saint Lucia", "LC", "LCA", "662", u"圣卢西亚"),
    Country(u"Liechtenstein", "LI", "LIE", "438", u"列支敦士登"),
    Country(u"Sri Lanka", "LK", "LKA", "144", u"斯里兰卡"),
    Country(u"Liberia", "LR", "LBR", "430", u"利比里亚"),
    Country(u"Lesotho", "LS", "LSO", "426", u"莱索托"),
    Country(u"Lithuania", "LT", "LTU", "440", u"立陶宛"),
    Country(u"Luxembourg", "LU", "LUX", "442", u"卢森堡"),
    Country(u"Latvia", "LV", "LVA", "428", u"拉脱维亚"),
    Country(u"Libya", "LY", "LBY", "434", u"利比亚"),
    Country(u"Morocco", "MA", "MAR", "504", u"摩洛哥"),
    Country(u"Monaco", "MC", "MCO", "492", u"摩纳哥"),
    Country(u"Moldova, Republic of", "MD", "MDA", "498", u"摩尔多瓦"),
    Country(u"Montenegro", "ME", "MNE", "499", u"黑山共和国"),
    Country(u"Saint Martin (French part)", "MF", "MAF", "663", u"圣马丁"),
    Country(u"Madagascar", "MG", "MDG", "450", u"马达加斯加"),
    Country(u"Marshall Islands", "MH", "MHL", "584", u"马绍尔群岛"),
    Country(u"Macedonia, the former Yugoslav Republic of", "MK", "MKD", "807", u"马其顿"),
    Country(u"Mali", "ML", "MLI", "466", u"马里"),
    Country(u"Myanmar", "MM", "MMR", "104", u"缅甸"),
    Country(u"Mongolia", "MN", "MNG", "496", u"蒙古"),
    Country(u"Macao", "MO", "MAC", "446", u"中国澳门特别行政区"),
    Country(u"Northern Mariana Islands", "MP", "MNP", "580", u"北马里亚纳群岛"),
    Country(u"Martinique", "MQ", "MTQ", "474", u"马提尼克群岛"),
    Country(u"Mauritania", "MR", "MRT", "478", u"毛里塔尼亚"),
    Country(u"Montserrat", "MS", "MSR", "500", u"蒙塞拉特群岛"),
    Country(u"Malta", "MT", "MLT", "470", u"马耳他"),
    Country(u"Mauritius", "MU", "MUS", "480", u"毛里求斯"),
    Country(u"Maldives", "MV", "MDV", "462", u"马尔代夫"),
    Country(u"Malawi", "MW", "MWI", "454", u"马拉维"),
    Country(u"Mexico", "MX", "MEX", "484", u"墨西哥"),
    Country(u"Malaysia", "MY", "MYS", "458", u"马来西亚"),
    Country(u"Mozambique", "MZ", "MOZ", "508", u"莫桑比克"),
    Country(u"Namibia", "NA", "NAM", "516", u"纳米比亚"),
    Country(u"New Caledonia", "NC", "NCL", "540", u"新喀里多尼亚"),
    Country(u"Niger", "NE", "NER", "562", u"尼日尔"),
    Country(u"Norfolk Island", "NF", "NFK", "574", u"诺福克岛"),
    Country(u"Nigeria", "NG", "NGA", "566", u"尼日利亚"),
    Country(u"Nicaragua", "NI", "NIC", "558", u"尼加拉瓜"),
    Country(u"Netherlands", "NL", "NLD", "528", u"荷兰"),
    Country(u"Norway", "NO", "NOR", "578", u"挪威"),
    Country(u"Nepal", "NP", "NPL", "524", u"尼泊尔"),
    Country(u"Nauru", "NR", "NRU", "520", u"瑙鲁"),
    Country(u"Niue", "NU", "NIU", "570", u"纽埃"),
    Country(u"New Zealand", "NZ", "NZL", "554", u"新西兰"),
    Country(u"Oman", "OM", "OMN", "512", u"阿曼"),
    Country(u"Panama", "PA", "PAN", "591", u"巴拿马"),
    Country(u"Peru", "PE", "PER", "604", u"秘鲁"),
    Country(u"French Polynesia", "PF", "PYF", "258", u"法属波利尼西亚"),
    Country(u"Papua New Guinea", "PG", "PNG", "598", u"巴布亚新几内亚"),
    Country(u"Philippines", "PH", "PHL", "608", u"菲律宾"),
    Country(u"Pakistan", "PK", "PAK", "586", u"巴基斯坦"),
    Country(u"Poland", "PL", "POL", "616", u"波兰"),
    Country(u"Saint Pierre and Miquelon", "PM", "SPM", "666", u"圣皮埃尔和密克隆"),
    Country(u"Pitcairn", "PN", "PCN", "612", u"皮特凯恩"),
    Country(u"Puerto Rico", "PR", "PRI", "630", u"波多黎各"),
    Country(u"Palestine, State of", "PS", "PSE", "275", u"巴勒斯坦领土"),
    Country(u"Portugal", "PT", "PRT", "620", u"葡萄牙"),
    Country(u"Palau", "PW", "PLW", "585", u"帕劳"),
    Country(u"Paraguay", "PY", "PRY", "600", u"巴拉圭"),
    Country(u"Qatar", "QA", "QAT", "634", u"卡塔尔"),
    Country(u"Romania", "RO", "ROU", "642", u"罗马尼亚"),
    Country(u"Serbia", "RS", "SRB", "688", u"塞尔维亚"),
    Country(u"Russian Federation", "RU", "RUS", "643", u"俄罗斯"),
    Country(u"Rwanda", "RW", "RWA", "646", u"卢旺达"),
    Country(u"Saudi Arabia", "SA", "SAU", "682", u"沙特阿拉伯"),
    Country(u"Solomon Islands", "SB", "SLB", "090", u"所罗门群岛"),
    Country(u"Seychelles", "SC", "SYC", "690", u"塞舌尔群岛"),
    Country(u"Sudan", "SD", "SDN", "729", u"苏丹"),
    Country(u"Sweden", "SE", "SWE", "752", u"瑞典"),
    Country(u"Singapore", "SG", "SGP", "702", u"新加坡"),
    Country(u"Saint Helena, Ascension and Tristan da Cunha", "SH", "SHN", "654", u"圣赫勒拿"),
    Country(u"Slovenia", "SI", "SVN", "705", u"斯洛文尼亚"),
    Country(u"Svalbard and Jan Mayen", "SJ", "SJM", "744", u"斯瓦尔巴特和扬马延"),
    Country(u"Slovakia", "SK", "SVK", "703", u"斯洛伐克"),
    Country(u"Sierra Leone", "SL", "SLE", "694", u"塞拉利昂"),
    Country(u"San Marino", "SM", "SMR", "674", u"圣马力诺"),
    Country(u"Senegal", "SN", "SEN", "686", u"塞内加尔"),
    Country(u"Somalia", "SO", "SOM", "706", u"索马里"),
    Country(u"Suriname", "SR", "SUR", "740", u"苏里南"),
    Country(u"Sao Tome and Principe", "ST", "STP", "678", u"圣多美和普林西比"),
    Country(u"El Salvador", "SV", "SLV", "222", u"萨尔瓦多"),
    Country(u"Syrian Arab Republic", "SY", "SYR", "760", u"叙利亚"),
    Country(u"Swaziland", "SZ", "SWZ", "748", u"斯威士兰"),
    Country(u"Turks and Caicos Islands", "TC", "TCA", "796", u"特克斯和凯科斯群岛"),
    Country(u"Chad", "TD", "TCD", "148", u"乍得"),
    Country(u"French Southern Territories", "TF", "ATF", "260", u"法属南部领土"),
    Country(u"Togo", "TG", "TGO", "768", u"多哥"),
    Country(u"Thailand", "TH", "THA", "764", u"泰国"),
    Country(u"Tajikistan", "TJ", "TJK", "762", u"塔吉克斯坦"),
    Country(u"Tokelau", "TK", "TKL", "772", u"托克劳"),
    Country(u"Timor-Leste", "TL", "TLS", "626", u"东帝汶"),
    Country(u"Turkmenistan", "TM", "TKM", "795", u"土库曼斯坦"),
    Country(u"Tunisia", "TN", "TUN", "788", u"突尼斯"),
    Country(u"Tonga", "TO", "TON", "776", u"汤加"),
    Country(u"Turkey", "TR", "TUR", "792", u"土耳其"),
    Country(u"Trinidad and Tobago", "TT", "TTO", "780", u"特立尼达和多巴哥"),
    Country(u"Tuvalu", "TV", "TUV", "798", u"图瓦卢"),
    Country(u"Taiwan, Province of China", "TW", "TWN", "158", u"台湾"),
    Country(u"Tanzania, United Republic of", "TZ", "TZA", "834", u"坦桑尼亚"),
    Country(u"Ukraine", "UA", "UKR", "804", u"乌克兰"),
    Country(u"Uganda", "UG", "UGA", "800", u"乌干达"),
    Country(u"United States Minor Outlying Islands", "UM", "UMI", "581", u"美国边远小岛"),
    Country(u"United States", "US", "USA", "840", u"美国"),
    Country(u"Uruguay", "UY", "URY", "858", u"乌拉圭"),
    Country(u"Uzbekistan", "UZ", "UZB", "860", u"乌兹别克斯坦"),
    Country(u"Holy See", "VA", "VAT", "336", u"梵蒂冈"),
    Country(u"Saint Vincent and the Grenadines", "VC", "VCT", "670", u"圣文森特和格林纳丁斯"),
    Country(u"Venezuela, Bolivarian Republic of", "VE", "VEN", "862", u"委内瑞拉"),
    Country(u"Virgin Islands, British", "VG", "VGB", "092", u"英属维京群岛"),
    Country(u"Virgin Islands, U.S.", "VI", "VIR", "850", u"美属维京群岛"),
    Country(u"Viet Nam", "VN", "VNM", "704", u"越南"),
    Country(u"Vanuatu", "VU", "VUT", "548", u"瓦努阿图"),
    Country(u"Wallis and Futuna", "WF", "WLF", "876", u"瓦利斯和富图纳"),
    Country(u"Samoa", "WS", "WSM", "882", u"萨摩亚"),
    Country(u"Yemen", "YE", "YEM", "887", u"也门"),
    Country(u"Mayotte", "YT", "MYT", "175", u"马约特"),
    Country(u"South Africa", "ZA", "ZAF", "710", u"南非"),
    Country(u"Zambia", "ZM", "ZMB", "894", u"赞比亚"),
    Country(u"Zimbabwe", "ZW", "ZWE", "716", u"津巴布韦")
]
