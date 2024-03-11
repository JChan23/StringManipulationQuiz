import random

#Arrays and variables
Strings = ['hmajibnvtk', 'kvgbmdp', 'bzefrjua', 'fhnvbecluy', 'mbizwkr', 'aujivsmx', 'kianote', 'wjuczidpv', 'axtczlisdb', 'kgryfdmnp', 'mvxagrcu', 'deyozhsxq', 'heaixgstru', 'fyvhtsgae', 'wqyxreazpd', 'ltcvsgaq', 'qsrinz', 'kzjecuig', 'apmvotfu', 'yxvmfdiap', 'hnevsr', 'jupbxt', 'zjfwqhd', 'oucnvg', 'bcnskfmt', 'idjnepbzx', 'lksbaj', 'nwkdzjr', 'drsvhlxnzb', 'kugyhfr', 'zmfvkdor', 'jepscgza', 'chovgp', 'gpjbouycte', 'nrpgdxo', 'viagrbupy', 'wvscayj', 'egqluodzvm', 'hznuxtsrl', 'qnfltm', 'wfxaulkme', 'yldkxsjauv', 'pdhibz', 'sldrcqhmot', 'tyvixqng', 'nyitaf', 'iondhfgql', 'zvdemtl', 'nbemifh', 'rnhklyvsz', 'onpbmv', 'zcdywvgqam', 'fbamqc', 'xgjoafb', 'fkwpvrstl', 'rhesodt', 'qsyjfi', 'vptwyeuzb', 'zvwsxjgu', 'wqgkzrsmdf', 'slpytcog', 'dqkealsf', 'jpklgynh', 'wcdyqog', 'rhgcve', 'xbzgaq', 'ajibwxyq', 'amuqcdin', 'exmkwz', 'qucdyblxsg', 'gneqrxl', 'bfuvnwzper', 'ptlzasxg', 'qlsukdhj', 'wkhgqi', 'fcuwodngyq', 'mwqlhsxvr', 'pjsorexwg', 'fhxopt', 'ixjlpqvzyo', 'tfuxqbweah', 'mkrogqcaf', 'xdyolpcmj', 'xbkiqfr', 'zvftjgi', 'niacojthq', 'uoazrde', 'aytbcvufd', 'zqwxucvfrk', 'bztgljv', 'behpcwdfo', 'lxigby', 'xvtqgu', 'ejrpdhi', 'ndbtxif', 'lpxjofbayh', 'xkzofelnc', 'dwezirph', 'vagqyn', 'trqysgeuni', 'cqmftyxg', 'xciagr', 'hwrulg', 'rxhiqgctsd', 'aporifjlw', 'xyhfba', 'lrwfhtjzq', 'uerdlsagon', 'brzjdmykqu', 'krsxal', 'xsbgfzwiqa', 'rsvinp', 'ujfpnvqm', 'vlnzcfj', 'vpcigh', 'fsizhmyepn', 'jeqrmvfbu', 'qujkgorcw', 'qxvatceg', 'jdeywfoar', 'mktbae', 'keuwqx', 'bqndugvyx', 'xtnioyv', 'efgsxc', 'vcgwknjx', 'ywobaf', 'xjazruh', 'uxjmywqonz', 'ngxiws', 'damqrtv', 'eyvlhbqgua', 'xgartuq', 'asjwlihkxm', 'pdrjzgh', 'pysdgvqc', 'eigztjbk', 'aqvokgfcb', 'frpaclhkv', 'ndeiocq', 'yrdwbjaznk', 'aqowys', 'nodwvbsic', 'kyxldbzme', 'jbgats', 'hbycgqkv', 'tfxujpr', 'nxagdmly', 'dxgswvcnjm', 'jboexpr', 'ezmluqhnr', 'swjkrtbvg', 'ltyagwkrh', 'nerduocpgt', 'ukfrqxp', 'qzrswoapy', 'fkeudqay', 'onlrebsujz', 'nykorfuxjl', 'fydusmaxk', 'tqilpegb', 'yrjhkbqo', 'mlewtpry', 'luzmxgneib', 'nhrxije', 'waepmc', 'anodgtcfs', 'boazvyus', 'erkbpoiut', 'ygnhozmeu', 'ghyrpacxms', 'bzquplv', 'ldborq', 'zojfuwciga', 'ylhqrgemo', 'surfciykjt', 'xzdlpoqgtk', 'loqbwchnpm', 'mihrezxavb', 'gqetfnodz', 'rvceyts', 'rbgdjnpwcy', 'dpaceqbzf', 'dihbacfe', 'npbyqv', 'kophxzquc', 'eqgikhwl', 'ivsjkcqfty', 'owajgemz', 'ctjhyo', 'vylqpwf', 'rwgxftc', 'hjsefpnlz', 'lnftkehuqv', 'fygwdbti', 'wcykes', 'qgkxezywba', 'lkeaydbupt', 'hkfnqgaj', 'dsncvjpl', 'ebxghj', 'icbakyp', 'tybivxd', 'rcknfm', 'mqynijxk', 'btcgioaz', 'lqjxzp', 'lkhfst', 'adgjinu', 'olypjg', 'vitdpbuwyg', 'dltpvzjk', 'dsbwgu', 'cphfemvgqw', 'fazobwxhks', 'rbtmsdoy', 'vrqxtbad', 'bxugnazyo', 'ptbwcsdoxg', 'diornb', 'jugohav', 'naztjvhblp', 'sngkbjo', 'tezikw', 'tmsarzq', 'sfhcrdoybl', 'yiwlfnph', 'imlapvyu', 'uhkfexln', 'tsuwqozahf', 'uaeyozhf', 'fhxpbr', 'cainuhwey', 'cjhresbyun', 'lfcbiedkv', 'krqwvubnlc', 'wrcvbxlnp', 'hvsnoif', 'pvhfqxotge', 'qhnkbxlt', 'cimnald', 'volprid', 'mdvqxr', 'aptjcyqigh', 'oguibtpxd', 'fehxczly', 'cqlzwthda', 'twqdsxpj', 'rjxeybn', 'wgreid', 'avfgcbq', 'chqzfvodn', 'mlxjnf', 'avbuiy', 'igxkfasyqr', 'ghpsxjcm', 'mjdnrg', 'kijgtcwy', 'zqayokrvp', 'yqxkufj', 'nwrqvglf', 'burmakdjc', 'mhskpqfwlo', 'ntwkxlhe', 'qnwdvbk', 'ybthzikxnm', 'rnvwjpxhz', 'ozrnlh', 'uzsfioh', 'sifmaolqyu', 'cnahoyjmb', 'xfgomyhb', 'hmeapgiq', 'nfxzue', 'qtexsgdlzu', 'ithygxq', 'hukzpifcg', 'wnkozqesg', 'xtrfgjb', 'bgudimnc', 'zpiujqna', 'frhyeqibol', 'rswcpai', 'efupmgnya', 'kcprovlg', 'cfqobpkhwj', 'gdwpnzub', 'gywnapjde', 'fclwsgpja', 'rablwp', 'qoxcphfry', 'pbsekxqd', 'ognpzklmy', 'vrdefx', 'psdtelmazb', 'hswdyn', 'rocdfzjg', 'pckgyx', 'ewkgxi', 'yuhjtdiacv', 'qzegyls', 'owsaih', 'xyhacgnuzp', 'wzxsgboqyt', 'ctpbvlszwu', 'mavhpznoj', 'xczwvmfesg', 'oltexdu', 'ghobvrzp', 'nozpytum', 'qxmhgjascn', 'evdisplmba', 'dhibygnc', 'uzphcxdnr', 'ifgbwu', 'vtyceqgi', 'madgnjvi', 'yotunc', 'qyaltjw', 'rnhozg', 'bzcsvqoad', 'jofrxludbv', 'wxglri', 'ofdpwqmay', 'qjzyem', 'bgjwvuylx', 'ylutgzjovk', 'jtwfik', 'jputacvr', 'uhlrcxj', 'kvbchqm', 'lpdqhjs', 'cnkixzru', 'kmturoqhdi', 'ruqlaziey', 'pdvwlkar', 'jmiqdyhw', 'keobuzga', 'mcfewq', 'uecwfd', 'hnguaeli', 'ptmbskhj', 'pkvrin', 'valdngwsz', 'tcigsjxd', 'hkebyog', 'dctukmae', 'udzgliysb', 'azdvjrnc', 'nudmaqxshg', 'piockueq', 'sfzrjcyvl', 'ueirsbncod', 'rspkfbhyoz', 'vwiblhtdo', 'iuftcjqmhr', 'qwtbdmzijf', 'kbryqiu', 'mwotgedpqk', 'gtoflwm', 'sdoenb', 'kopwhuryf', 'fagymkv', 'abolchviz', 'ieamygvtkh', 'udtyjnvl', 'emiasbrpjo', 'rgmnoavuys', 'zuvicpwjns', 'jqrfhuszy', 'dzsrjwvaft', 'tumsbh', 'xbfwya', 'fzlghbrknd', 'xhneki', 'lnvoabw', 'gtqwjabl', 'drxbpjwkc', 'vdrnikcow', 'peztfrchla', 'phzfxcd', 'htvyknpigl', 'pysuxdogq', 'wjimfba', 'tyvcmi', 'aruhkzfny', 'eqfchab', 'vurtamy', 'knoelifw', 'rjyqgmw', 'aylnvtusrc', 'krleafh', 'ibkfauzjt', 'ctxjzql', 'cqngtxiop', 'mnbapi', 'mjidalqe', 'hflxpkv', 'zanscxpjfd', 'yuplna', 'oyplkrimzg', 'nzcsaeufr', 'bmglxvzd', 'fourckg', 'nxhsge', 'rnyotzcm', 'pksbriwufy', 'nkuelrdm', 'nrfkzp', 'whlupvqaz', 'ixnasoukjg', 'nvrdjhuef', 'ojihwyckrt', 'rktfuvhx', 'upoegtdzfq', 'zkdotg', 'ekntmud', 'nhemcgdw', 'xyekjbq', 'kmfpvsg', 'jiouvckqty', 'tlkauhz', 'hgcrmfuqdt', 'cfetwpsr', 'onvmgeuh', 'yfjuqrdh', 'nhbcuko', 'wlgdobcz', 'dmvpea', 'kvztqdmrg', 'kvbopwfsy', 'mubork', 'lhqcxeavj', 'rsqkctd', 'rgmlostqc', 'sxfdculq', 'ugmncwjfda', 'yqwhnfirl', 'cdhxeji', 'cdymogqhiz', 'eghwobru', 'lfyrbaezv', 'qjyiwt', 'myszup', 'soaycwmf', 'dyzjkubfqp', 'jkcapueyv', 'nkerbvjldm', 'zyqhrotufs', 'ulsghapcdq', 'nklbshfq', 'bhgxrv', 'tfyajzxlmu', 'kwburamnji', 'fspeiruvq', 'rpqjbednft', 'mnhsulr', 'wvcxhlr', 'gzxylktnc', 'aowhpbfcix', 'txewfdyim', 'wduoigyfxj', 'wcbamth', 'onrcqgt', 'xlnaeygk', 'ydcnmoepx', 'ondqck', 'khpizamo', 'rfwlpvj', 'zancljyotu', 'pmqflwih', 'zmusxcvygh', 'cskvtfg', 'tezumhd', 'mbvtxqzocu', 'msfwvpiknz', 'psgtvw', 'miyzke', 'dskitpu', 'oeauvjriz', 'jzetvspowc', 'ekqtaulsno', 'uaqlzswevo', 'mlzdpqwb', 'oehxtf', 'mpnctkzvi', 'ufdrancb', 'ofqcpj', 'rfsukj', 'qisjymon', 'qtougfl', 'cvkrhlf', 'filmzekoxb', 'hgdkom', 'veyuhf', 'pniaoqyk', 'vgqupam', 'lnphegbavw', 'tkbhmyucw', 'krsqxz', 'vzhxac', 'wtxknmpf', 'cpsygbi', 'lhuqcom', 'grmjqvkyfs', 'pfkjrzsac', 'gqteazxhi', 'zgkhpuvd', 'ytemog', 'fzbocuwkx', 'xgztiaekjn', 'xqbvigtr', 'nmocpf', 'mzxwba', 'lgxbpwv', 'yxbhevtk', 'duaizepbf', 'pcgvuwed', 'ygijfvuxd', 'byixpdav', 'wmjdverp', 'qzcnoj', 'czvgax', 'kmrdesqtap', 'gpujnv', 'hpnqid', 'nwvcudiz', 'carqnhb', 'hoyszalm', 'vbhndox', 'ysdxbjnwhg', 'dxnsuv', 'sbtifh', 'uwhsdnvrgk', 'vblnoyp', 'zdfljxnti', 'jwplebio', 'lditxpz', 'ilekghsnzf', 'axsuroew', 'xhbwdptkeq', 'krjdcivogq', 'zwymknucxh', 'glrxfdsj', 'rstgwcxj', 'wbueqckhj', 'gendmjwkf', 'ikxmcj', 'avsnowx', 'kygrhnaeqz', 'idrgxakph', 'hsjmoqfl', 'mgywor', 'deznqybr', 'jgwnvmze', 'jsfampkue', 'mncdzyv', 'ofwqyhrp', 'agnqdz', 'sednku', 'opmugh', 'nmsyitzpqj', 'eouaml', 'kjmhguyz', 'gvliqzya', 'aefbypioq', 'ibhgmxeu', 'atkfrjvu', 'uqcjdpk', 'eyktvo', 'bgnpklqw', 'jegudlzo', 'rlgaxbfiqv', 'jxsctmvb', 'elnguv', 'jvlyqxghsb', 'hfzliudksm', 'xotjmbsu', 'ciqmrnzj', 'zblxjoympk', 'omzvlf', 'kczsnxhd', 'iqldwxu', 'apmlobuckq', 'durcnp', 'ehklpiwt', 'yzatrsx', 'hsjbiwmeyx', 'ocdbaner', 'yfabjod', 'cztibxm', 'qnskwurex', 'yjevzuohrk', 'hrwckal', 'jgeunhdkb', 'yaqixbkoev', 'mybszdqw', 'efirmyu', 'lavmkycq', 'dcgrenfbuv', 'xeyjwvdm', 'vdizybejt', 'tkclonuv', 'xjinhof', 'uzcxlspeh', 'uvfish', 'qognzalry', 'lurvynx', 'zpgcxvjs', 'yvtgzu', 'ovwbtpza', 'ugmxsqvbd', 'fmcrplzhqa', 'utnmadg', 'mrqpjckgyf', 'dbskvgre', 'soutxndfrz', 'azihsoxy', 'yfqvxa', 'mkfgrnlwa', 'mrebksu', 'nvwagpjd', 'hjnaod', 'svkiulrn', 'xoknvcpzy', 'evhjalbf', 'otirka', 'nlmdruaixt', 'lpjqhbem', 'olhrncyft', 'tigmrwsx', 'yuqsobv', 'eqyrwatczl', 'ebgunzmt', 'buqxetfprh', 'epwhcs', 'okmrqgh', 'bxciwlpjd', 'fytain', 'wpcnuleixb', 'kiculya', 'fvdoasrjq', 'pqhkvdu', 'emgvofiq', 'zvcjwdkhbq', 'yhtcmvga', 'tyhlux', 'vysqwhif', 'xydfwlvae', 'fgjnkvhi', 'zfuadt', 'dziplh', 'dsunxbkv', 'vjohat', 'urnhvgtyx', 'obhkix', 'ghpfki', 'fwnrzhjd', 'cqjumhv', 'ymwsgx', 'smuaewron', 'fpivwead', 'qmgtxedfw', 'tqfhczw', 'jdzyuk', 'itzcvyob', 'vektuyi', 'lhinmp', 'oemuqnid', 'zqckvm', 'mdpfusrj', 'lftmjhdi', 'ilopqsyac', 'zcepsorn', 'zshuaxpg', 'wqndkyjtz', 'pgkobxt', 'zjmfrxypbe', 'fumdctzbkp', 'ifxpbqrlg', 'lxuzstmjkc', 'oimnhzvcu', 'dbfomu', 'aymroicf', 'rquoytbls', 'zpaednctgl', 'vqbexzc', 'qifetb', 'qhkxja', 'pbmvfdni', 'kzuqewmt', 'sgetrm', 'qviozweu', 'cypqhz', 'jtuigmf', 'xrwsizmoq', 'nwxhdu', 'uifrxabcv', 'femwlyrhox', 'oefbdvws', 'okxbsinau', 'nlgqydmvax', 'fgqliaj', 'nworda', 'kcsjyazgm', 'lszbaqmdxc', 'tbzndeik', 'rekdznb', 'xbolgf', 'kufzvy', 'gwtkpvf', 'ewsvyxmd', 'obytqupwlz', 'xyngeh', 'xmktjwlh', 'sqhzkptvjl', 'ofzelugap', 'xgwyurfvoh', 'zdkcblfh', 'tfvyblepk', 'ifubyln', 'ajonkyft', 'sgzhqt', 'bytwfpxqra', 'htnkcxeqds', 'xmpawdjt', 'fenrjimqo', 'ijzkdgvaqs', 'hubymefpxo', 'ezbcydwh', 'vefuhp', 'iymwoukrl', 'kjerxpbzu', 'azvbyjsx', 'bpvnkiohte', 'eogqljfh', 'gdpjakhsbf', 'fyshwi', 'nyragqised', 'sawgqt', 'nlpditqu', 'zvbcojpamr', 'suaryctzv', 'ajwzvpx', 'glphcv', 'weylksi', 'juhceylr', 'vxhrcm', 'tomnyasr', 'mekxqyzrsa', 'ouwcfzqh', 'iysklt', 'synfdu', 'zyoqwi', 'rikbuvzfny', 'rnbouyvpas', 'pgbektowz', 'zeajpws', 'cxvtzrn', 'gfvkjr', 'mojcznsfay', 'ezdwrb', 'wdgqrkavl', 'fkzosuxj', 'maeqixu', 'vndurgcit', 'ojlpfvdy', 'gtbnmohr', 'ohanlxg', 'pvqyue', 'dkjfpq', 'cwfazyqmu', 'owluqynxeh', 'bnlsxrheiq', 'ixmrus', 'sakifnboy', 'frzcpyw', 'oxgbav', 'cgantmr', 'rzgxqcvpki', 'bfprvsetcg', 'xjcwimo', 'vinbhux', 'jgezaqb', 'mxufto', 'qucjosltha', 'ixysopfuwn', 'iwlkhbvtg', 'nabesrik', 'mzjscft', 'geyhpu', 'hutgyx', 'ebtnxkl', 'gemswxdt', 'uorsiq', 'cueaishqjm', 'cutxorp', 'hkrwvns', 'tbczked', 'znbvpsx', 'szrfdhky', 'sqdoui', 'qmwrdobtnj', 'ytigcfxeo', 'ywzqctkseg', 'opztlmkcxi', 'lzduewvf', 'zjpbyxsoc', 'wfcvrjaiyn', 'wgoblu', 'qfujnblsap', 'yiefdx', 'bosvxh', 'derlvaqc', 'ktapmz', 'jvwmirthcy', 'cokyhni', 'sopxjtbnc', 'rauqwoix', 'bglnkfde', 'kyftlpm', 'inatlu', 'vtibjxyw', 'dzhstmr', 'eyzqvnwb', 'aujcivpz', 'wvchfptz', 'yvogctf', 'favpqcmle', 'fbjwytgimk', 'epoitc', 'shbukyncv', 'tdkvsihn', 'bywnumlj', 'fxzvop', 'aipcnevzw', 'uiarymje', 'ptdxqlgkae', 'isanpudtec', 'bktehcurij', 'fkzjrxwpna', 'bqtvydp', 'djsvnxiare', 'pslqrfouv', 'bpeaxhdkmq', 'jxlbgqpm', 'utfsek', 'wbeulqtc', 'aqgnyesvxt', 'mixoudh', 'smtduoqfca', 'ndxovpze', 'svdlxgw', 'ohqndtispr', 'fxiwqgzpc', 'scxaiko', 'albikcfuq', 'vcyikrw', 'fsyvin', 'eytifrglwb', 'torwahn', 'uvopzxikdt', 'tskixnvz', 'xvohnyfqbk', 'wfjrlizq', 'yojzpa', 'udpgxi', 'eangyrvdw', 'vwhtjlre', 'bzpuwoye', 'dqejpnsz', 'himqefbl', 'bamrwg', 'ldawrq', 'qhinackuo', 'nmydrsxzv', 'bdxoav', 'rbwnavmjd', 'kajumw', 'badencs', 'zfdaxleu', 'cpsmxwiz', 'lakjob', 'nawftgy', 'cnljszwa', 'czvagwm', 'zpvaiw', 'qbcmklzfpr', 'wzoydung', 'nxwighacdb', 'fpwnoxb', 'jbtryxn', 'nbljgdzf', 'wmbypndquz', 'qderyxzu', 'zhajew', 'teyqzo', 'zacnsbgvkw', 'yfacqjnhr', 'jrgvactpo', 'nbehxsqf', 'gtpoerya', 'ogndeuwlj', 'zmcxqjdry', 'ugwfipercs', 'wmondbix', 'eqdyijbpa', 'nxodykrjpt', 'ypourz', 'optxwsq', 'ceqtgvzyw', 'udehvpmzs', 'nlsczpwf', 'ljifdve', 'yhelfpwj', 'xntovif', 'cpglarufvd', 'yjpzsoqm', 'uoayvts', 'cjrzdnt', 'djfocmkwsx', 'crlvtwp', 'yjkisrdnum', 'zbnpjlus', 'agtlcn', 'ozjdaqeyl', 'wahcetyrgf', 'lmcxjigohf', 'blorid', 'atzikwqxjc', 'zbiqcgmfo', 'hycdaznpfw', 'gyjdlv', 'rzqyox', 'pmsbioglc', 'xroplj', 'xbpvlcd', 'kecvwdhpf', 'gqrptvahbu', 'gojstd', 'lctkoi', 'yzxheafdsv', 'latdxfji', 'dmhxilzgne', 'iewsplgomh', 'cvzkxalt', 'surxvnwgp', 'degnaroc', 'nmjrglqxt', 'pxhdzlj', 'bvmynzhk', 'bwkjgyaf', 'fivboz', 'kahujdepo', 'yvwatp', 'tfbxpkj', 'gviohea', 'pschla', 'rbzfji', 'xyrienq', 'hxidkt', 'qxzvjalks', 'pclevzmoau', 'harpczxdv', 'jkdwabhosu', 'qyzdpjo', 'lbfqawxes', 'mcgvsnfjr', 'gvprmb', 'npwhdtfiq', 'umhrxngoi', 'lpuxdy', 'cxfvwizqsb', 'pvsfbqjm', 'tqwxsvck', 'qjdphovug', 'pgqveu', 'wgkhetjuo', 'icjtgu', 'qtfcuerx', 'gnwidqrmjs', 'ciexvzrl', 'qmkgbol', 'ihavfceto', 'bogcekvl', 'cuihodkf', 'wstykmizbn', 'dgicmrz', 'kzfarcbhu', 'ctpomiq', 'yvdzaelg', 'hfvqxinu', 'sbuogzmh', 'oejtnzr', 'fuoqrgikcz', 'hijlpcbtfs', 'tupwoqlcsa', 'bahpdvis', 'lsvnqw', 'wikjlbrq']
ManipulationTypes = ['ONECHAR', "LEFT", "RIGHT", "MID"]
HighScores = []
Name = ''
Score = 0
CurrentString = ''
CurrentManipulation = ''
Answer = ''
Question = ''
RandomVariable = 0
Guess = ''
RandomLength = 0
Round = 0
OriginalString = ''
NewString = ''
LineOfTExt = ''

#functions and rocedures
#left procedure
def left(S):
    global Score
    if Round == 1:
        RandomVariable = random.randint(1, len(S))
        Answer = S[:RandomVariable]
        Question = f"LEFT({S}, {RandomVariable})"
        print('Input the result of the following string manipulation command')
        print(f"Command: {Question}")
        Guess = input("Answer: ")
        if Guess == Answer:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Answer}")
    else:
        OriginalString = S
        RandomVariable = random.randint(1, len(S))
        NewString = S[:RandomVariable]
        Answer = f"LEFT({OriginalString}, {RandomVariable})"
        print("Input the command used to manipulate the following string to the result:")
        print(f"Original string: {OriginalString}")
        print(f"New string: {NewString}")
        Guess = input("Answer: ")
        if Guess == Answer:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Answer}")

#right procedure
def right(S):
    global Score
    if Round == 1:
        RandomVariable = random.randint(1, len(S))
        Answer = S[-RandomVariable::]
        Question = f"RIGHT({S}, {RandomVariable})"
        print('Input the result of the following string manipulation command')
        print(f"Command: {Question}")
        Guess = input("Answer: ")
        if Guess == Answer:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Answer}")
    else:
        OriginalString = S
        RandomVariable = random.randint(1, len(S))
        NewString = S[-RandomVariable::]
        Answer = f"RIGHT({OriginalString}, {RandomVariable})"
        print("Input the command used to manipulate the following string to the result:")
        print(f"Original string: {OriginalString}")
        print(f"New string: {NewString}")
        Guess = input("Answer: ")
        if Guess == Answer:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Answer}")

#onechar procedure
def onechar(S):
    global Score
    if Round == 1:
        RandomVariable = random.randint(1, len(S))
        Answer = S[RandomVariable-1]
        Question = f"ONECHAR({S}, {RandomVariable})"
        print('Input the result of the following string manipulation command')
        print(f"Command: {Question}")
        Guess = input("Answer: ")
        if Guess == Answer:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Answer}")
    else:
        OriginalString = S
        RandomVariable = random.randint(1, len(S))
        NewString = S[RandomVariable-1]
        Answer = f"ONECHAR({OriginalString}, {RandomVariable})"
        print("Input the command used to manipulate the following string to the result:")
        print(f"Original string: {OriginalString}")
        print(f"New string: {NewString}")
        Guess = input("Answer: ")
        if Guess == Answer:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Answer}")

#mid procedure
def mid(S):
    global Score
    if Round == 1:
        l = len(S)
        RandomVariable = random.randint(0, l - 1)
        RandomLength = random.randint(1, l - RandomVariable)
        Answer = S[RandomVariable:RandomLength + RandomVariable]
        Question = f"MID({S}, {RandomVariable + 1}, {RandomLength})"
        print('Input the result of the following string manipulation command')
        print(f"Command: {Question}")
        Guess = input("Answer: ")
        if Guess == Answer:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Answer}")
    else:
        OriginalString = S
        l = len(S)
        RandomVariable = random.randint(0, l - 1)
        RandomLength = random.randint(1, l - RandomVariable)
        NewString = S[RandomVariable:RandomLength+RandomVariable]
        Answer = f"MID({OriginalString}, {RandomVariable+1}, {RandomLength})"
        print("Input the command used to manipulate the following string to the result:")
        print(f"Original string: {OriginalString}")
        print(f"New string: {NewString}")
        Guess = input("Answer: ")
        if Guess == Answer:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Answer}")

#high score system
def CheckScore(s, n):
    if s <= HighScores[4]:
        return -1
    else:
        HighScores[4] = s
        HighScoreHolders[4] = n
    for i in reversed(range(0, 4)):
        if s <= HighScores[i]:
            return 1
        else:
            Temp = HighScores[i]
            HighScores[i] = HighScores[i+1]
            HighScores[i+1] = Temp

            Temp = HighScoreHolders[i]
            HighScoreHolders[i] = HighScoreHolders[i+1]
            HighScoreHolders[i+1] = Temp
    return 1


#intro messages
print("Welcome to the string manipulation quiz!")
print('Instructions:')
print('1. All answers are case and syntax sensitive, so ensure you input the exact command (e.g. MID must be capitalised)')
print('2. When using commas within a function, ensure you leave a space after the comma (e.g. LEFT("Hello", 2)')
print('')
Name = input('What is you name? ')
Score = 0

#section 1
print("\nSection 1: Input the resultant string based on the function command given (8 questions)")
Round = 1
for i in range(8):
    CurrentString = Strings[random.randint(0, 999)]
    CurrentManipulation = ManipulationTypes[random.randint(0, 3)]
    if CurrentManipulation == 'LEFT':
        print("")
        left(CurrentString)
    elif CurrentManipulation == 'RIGHT':
        print("")
        right(CurrentString)
    elif CurrentManipulation == 'MID':
        print("")
        mid(CurrentString)
    elif CurrentManipulation == 'ONECHAR':
        print("")
        onechar(CurrentString)
    else:
        print('Error')

#section 2
Round = 2
print("\nSection 2: Input the function required to turn the original string into the manipulated string (4 parts, 8 questions total)")
print("\nPart 1: LEFT function. All manipulation is done using the LEFT function (2 questions)")
for i in range(2):
    CurrentString = Strings[random.randint(0, 999)]
    print("")
    left(CurrentString)
print("\nPart 2: RIGHT function. All manipulation is done using the RIGHT function (2 questions)")
for i in range(2):
    CurrentString = Strings[random.randint(0, 999)]
    print("")
    right(CurrentString)
print("\nPart 3: ONECHAR function. All manipulation is done using the ONECHAR function (2 questions)")
for i in range(2):
    CurrentString = Strings[random.randint(0, 999)]
    print("")
    onechar(CurrentString)
print("\nPart 4: MID function. All manipulation is done using the MID function (2 questions)")
for i in range(2):
    CurrentString = Strings[random.randint(0, 999)]
    print("")
    mid(CurrentString)
print("")

#high score system
#read stuff from files
print(f"Score: {Score}/8")
file1 = open('HighScore.txt', 'r')
file2 = open('HighScoreNames.txt', 'r')
HighScores = file1.readlines()
HighScoreHolders = file2.readlines()
for i in range(len(HighScores)):
    HighScores[i] = HighScores[i].strip("\n")
    HighScores[i] = int(HighScores[i])
for i in range(len(HighScoreHolders)):
    HighScoreHolders[i] = HighScoreHolders[i].strip("\n")
file1.close()
file2.close()

if CheckScore(Score, Name) == 1:
    print("Congratulations! You're in the top 5 high scores!")
print('')
print('Current high scores:')
for i in range(0, len(HighScores)):
    if HighScores[i] == 1:
        print(f"{i+1}: {HighScoreHolders[i]}, {HighScores[i]} point")
    else:
        print(f"{i + 1}: {HighScoreHolders[i]}, {HighScores[i]} points")

file1 = open('HighScore.txt', 'w')
file2 = open('HighScoreNames.txt', 'w')
for i in range(0, len(HighScores)):
    file1.write(f'{HighScores[i]}\n')
    file2.write(f'{HighScoreHolders[i]}\n')
file1.close()
file2.close()
