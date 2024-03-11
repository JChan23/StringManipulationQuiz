import random

#Arrays and variables
Strings = ['espdiaifs', 'nddvkz', 'hvqkgpw', 'ygbrlxyvvu', 'yzirwaq', 'iuvudutmy', 'ksgwfwm', 'uuahlzwvly', 'actaikedfo', 'hhaodrm', 'xidjzpqic', 'ldautuf', 'gnfvvsww', 'cizpjunnh', 'gftsksxvt', 'senhbu', 'dpbypndwzc', 'dujfldogz', 'bmunujpoa', 'eitdmrg', 'krkaydc', 'zyuyxn', 'etxxgngjt', 'jthsxvie', 'wolcvnqu', 'olqgjk', 'iaslrdxbyi', 'hobweh', 'shshyodio', 'gasxwzdb', 'orfvjakv', 'pqyhqiq', 'bagfxuifi', 'zvhdhffa', 'qsjvpljaf', 'iurhxidoz', 'lzvbcz', 'qnhgjn', 'qawaaxet', 'vadeamr', 'hfbljlukc', 'gkflfrdtwo', 'imlkmh', 'yirkxfv', 'edzhgtdh', 'bnbecj', 'xcekjklag', 'rixusuu', 'wrgatinzcl', 'qrljtatien', 'cjifkxlhl', 'jwckreq', 'mowmylhvk', 'wkggladf', 'ghvysdbtlh', 'xdudzdtn', 'ereqsvpy', 'aagecqlfp', 'vomdyrs', 'oxvbmpkm', 'cdioge', 'ivfjhhpll', 'prewfstfpi', 'fdgyfab', 'pddevmx', 'keeukptqsk', 'ubdlkhbhbt', 'tjwwux', 'hibztltua', 'gxdjbehek', 'huphbf', 'yilbgox', 'tgutcytygn', 'rmuhymz', 'jyeraxxefo', 'iqweaet', 'vdawwxuylb', 'wpumdcpobv', 'rfebpdhqps', 'pxogmmq', 'kywxuq', 'rcwwegl', 'tqkoklant', 'kfpriputm', 'mwrzhryx', 'ypwprdbw', 'dvugwxyzi', 'ejavgbcp', 'fqmooeycb', 'ljovijgg', 'lypncjpjx', 'mbdcrgos', 'doywtdgidp', 'vteobzvxh', 'cmwvldlw', 'ejzmhp', 'jwmsbhrw', 'pilrrujqc', 'txfcbuwgl', 'pydskldm', 'yvmyug', 'ajjmpxgegc', 'aximvwoko', 'mdrhecwxu', 'asftvarada', 'onueiaw', 'ghbtal', 'hprvmwskg', 'bqtzpr', 'opccriarhp', 'lvjztk', 'dqihfmszyb', 'zdzrqjwul', 'gvkkumst', 'ggxszr', 'mwfjjduht', 'gsltilwy', 'oaelji', 'qjgtrsi', 'zkmkfs', 'kxxojh', 'nysfpysorx', 'qqkrvlliv', 'fealyqiy', 'gonukri', 'jyylihtyf', 'ezfsrvyhc', 'otvscs', 'pbafrwe', 'eqynmcigzl', 'ohsaodwde', 'jtaqmzn', 'owgmrxrgvk', 'jspxmuag', 'qitkihqap', 'fefotga', 'xfratrmw', 'ivzbphmr', 'yrtfxhrr', 'wihmbrub', 'ydtrgavyps', 'kuqawpjo', 'scdlduhyd', 'dgamawyepa', 'xanfzr', 'vnasxq', 'dvcvme', 'kesgmsytu', 'dtxoslg', 'srdafbxy', 'qvzfllbw', 'vibrifrap', 'jrdsdkcuw', 'rxruiyze', 'juitfqku', 'rrhwedref', 'zijdeuuqvw', 'syntzz', 'sjhkkg', 'snutkftdk', 'bbgvdugnj', 'xfldkmwoq', 'zlyzfei', 'avvnjure', 'bmahafshg', 'zpuktnrtn', 'arxgptphjk', 'xihzjgyvhs', 'ynnuku', 'wiaecef', 'katlylq', 'qhmihttrsw', 'duuccsc', 'xgalgqachy', 'xjmonytzpo', 'byvrwavwle', 'hqwuwdq', 'rwbjamgg', 'bpddffmqea', 'jpnvojcocn', 'pzkxgydzcy', 'zxkellqxj', 'paytuvfqtf', 'jhaurxiegb', 'alvwwxgo', 'rwziyhf', 'scksyucmx', 'llpxejw', 'onwpxos', 'npheibk', 'taqzocrchg', 'txnyaf', 'qytcsz', 'ljuzord', 'npwkio', 'wxvhiwush', 'arytcplz', 'unbhxrr', 'ptniyqv', 'eutbfrw', 'nympxvhs', 'uhakbrt', 'wjrkhshfkp', 'bsfijxqkc', 'dhtuifpw', 'fjrwvki', 'hzfjysnfyf', 'ffpzcinhh', 'abbuytkoor', 'xmvzyesd', 'geedbgom', 'ifnmehkesj', 'suxqikgo', 'pjmnojx', 'chqheptp', 'wjuufflwy', 'jlplbiuad', 'lpnmeha', 'ckqgau', 'qobrhe', 'iwctzbxtq', 'qchazerlce', 'ocynoftmqe', 'suteaqgfg', 'znpnagn', 'dopajiz', 'kgwszpjib', 'ygigga', 'xsiwyomo', 'dqsemztg', 'jlqswmv', 'bgfzdsylab', 'mqiuxsl', 'wdihnzz', 'qpwwqtdf', 'fioklduec', 'tzbycozv', 'xpsfgq', 'spefmt', 'jqvkbhve', 'qunarn', 'ulfgargvpd', 'lsvdccd', 'vgzohwork', 'dpzpddqnq', 'xhkiaqnk', 'ysvyyu', 'wupthtlds', 'weacouzajp', 'voffvpv', 'gytgwn', 'pkrbqxsvg', 'xztclnhrje', 'qupotiuvrh', 'nhfrbci', 'advayl', 'ttuumisyx', 'wmhyidt', 'uxterbi', 'xwkyhj', 'ycpmgqnq', 'nwyfwt', 'vrihrfivl', 'ldbqdbe', 'wcahsa', 'rulrfp', 'bikpbou', 'xwgytuyaf', 'slyxoykr', 'thzlodvq', 'yoylqu', 'qwvcysov', 'hotrgcbi', 'kkfjviet', 'dwgqvo', 'ogwmgfqvlf', 'kcdagxjc', 'vcxcnoxbt', 'nshuidcycx', 'xbefxh', 'wrebbls', 'xaicuyiixw', 'unpwryr', 'xvcedcfjj', 'pssxbr', 'sifsvjwxo', 'tcazebuudl', 'xaqpviovpr', 'ebaqes', 'wirbzl', 'hffpsps', 'mgpbdj', 'sajizbbt', 'ggoijxhao', 'asqurxo', 'psoubo', 'brfqelgk', 'pybrkjqoqv', 'trngjgspz', 'wywedo', 'skxnzsi', 'ucbchtw', 'nlcosy', 'luphng', 'jfdivn', 'gljgyeicj', 'ogfpscvu', 'wnsmssl', 'kqveazxof', 'idgfursd', 'qdvrisqc', 'dgtaslepro', 'bjlfamd', 'topbdr', 'vozvkd', 'ouxkyu', 'vvygdfzz', 'zaogmkalpp', 'sayajosa', 'peqqqtqkl', 'jfzjmsjv', 'njhdze', 'rgvusc', 'bnqjkxpih', 'yzzjotrtrz', 'zkmmarfvu', 'omlhldw', 'bhmlswnzmt', 'bwpmldumh', 'hdrxdt', 'bxtqyees', 'wpuozuxnau', 'ogviqothv', 'godmqi', 'bpfrchr', 'iehyapfi', 'bjdavxgf', 'mdpapofz', 'vrxvfg', 'qhgbubccfp', 'wjeyiudjj', 'jpnnjacqg', 'rkvndi', 'kobdugvses', 'fqbjjo', 'ebabmm', 'jzwezg', 'qtlogpbcuj', 'mbvlvsf', 'ssbgukcd', 'mfltkuupfs', 'qfnyvg', 'betnpmvypr', 'rclsivbjet', 'fojiohylc', 'mrellat', 'jlycwpgb', 'tctuoejsb', 'rannqm', 'sbspxtenp', 'hkmmfan', 'ivhnykjakv', 'wxbsyt', 'sozuolic', 'ukdzhat', 'tuyanyz', 'oouzmgj', 'rfiideqxta', 'eiluirii', 'hcjckh', 'fzfjvrwp', 'gqnmxppl', 'oiwiaaeipk', 'ndyqtmeqlc', 'jnqfknlgrp', 'mymyvpyfj', 'wtqdpxr', 'qypjlwuluc', 'auqidmdwn', 'dkwvpgrz', 'tcobgj', 'emsrvrd', 'qocrduilyl', 'bqbcqt', 'zmqcfraso', 'xfhxttego', 'iduboxcbrv', 'jjvrfg', 'avmixlqo', 'imewmwe', 'qqbkbpdf', 'fqzlehiu', 'pvzsmvxdrp', 'zcvucnlggi', 'tsmwedmd', 'fstsqehybd', 'yqychsmfu', 'tmmwbkml', 'jclicb', 'tjbmeqh', 'jpqjrot', 'lslwlrhga', 'dvsmsodqqh', 'gxpxzsv', 'muxbtwfob', 'sqypub', 'mmzvygw', 'eqbdzmku', 'toxdmhej', 'hhstwwa', 'qpqgpcu', 'zssaqt', 'jhrvhevjzt', 'gqmqjb', 'mlwoswrz', 'ymemlc', 'nvkdjjwq', 'izlaed', 'tgmrmjgrw', 'dpcxcu', 'ldtvqsuu', 'icnzlu', 'fqwwseffq', 'vtbvde', 'cpjhyqirt', 'pvjbyx', 'ibrxlgw', 'ajmgag', 'sykseg', 'znzswsfylq', 'lwbymylf', 'muvltulvhr', 'vtbvygsp', 'afaqfkpnx', 'tnmlkervg', 'rdqaptab', 'vqbtrfbe', 'snnxkqr', 'gbbnoro', 'zcdlxrrvu', 'ihosjvfndn', 'adfrag', 'ammkycos', 'gzwthadyg', 'gkdptc', 'rioocyfpp', 'smrhtogj', 'qltfzk', 'aidorf', 'vagujojd', 'ofgmmbb', 'fykwkoaf', 'eekmaygzal', 'hjtwofmj', 'oztipiokrk', 'xqgrgudb', 'lriipzxph', 'denkgfyq', 'dpaboaa', 'sqrxxsp', 'nfwpiuf', 'oxneuflfd', 'uujopop', 'liygxuutd', 'mvelgcu', 'gmtcjfprr', 'ptimcdx', 'tfuhvwuy', 'ozvqziad', 'ibnvilarc', 'rbuiumwwxp', 'cabjaxqltw', 'ndmhywbay', 'uapzfmboyd', 'mdkojoy', 'nlijjkjum', 'zhmsfmgso', 'gqdbzhcl', 'bnfqbfmj', 'izhpeyv', 'tdycvqlo', 'gopbyrkpi', 'gzarsevn', 'smbqkqe', 'fkpjcqlhh', 'scmgsixg', 'bkntei', 'gutxncetq', 'fbuaaj', 'ickjoxzhf', 'mruthk', 'hncbdlomj', 'mhywubxfyb', 'tmkvnmfy', 'jasrxcs', 'ksrofmtypv', 'lbvcrpawpw', 'oujljos', 'vdlsewtj', 'joqxjsmos', 'dfhumogzu', 'zsbstrukec', 'rnfspoekrh', 'audbenps', 'qpxiuqgdei', 'egyyors', 'xktomxeo', 'rmyrrqhdtg', 'yosgumc', 'bgfoyqujvs', 'vglwgpaewu', 'uwyokdpxjm', 'qpelgwig', 'nvtqltwozx', 'lnuenbtl', 'rbjfbrmb', 'kgzffs', 'pfqofeevq', 'jqbrhbkr', 'hgnvuvzt', 'gimxuzopmx', 'rvkrwj', 'nximwlrpt', 'ermqeegmk', 'ehhtwydo', 'oqsmkbbmef', 'tcynyeu', 'gowdpkdpz', 'ydxgwjc', 'phqlkbzv', 'lwbuedqc', 'wcwlczwbhq', 'tsujaq', 'rvkgjhmw', 'xuiunbvh', 'qttoqgjdn', 'yczugwu', 'rtawlczgu', 'ibxmbvktc', 'jissrrd', 'jlmgbrjmaj', 'iamgoswp', 'xhjsyzzoi', 'cputirpkxs', 'yxckppen', 'ngeabdznht', 'fdcjvdpqz', 'mxuzbxzvmq', 'xrzfdnpyou', 'hdiaqkuv', 'zmvolt', 'emjroxkys', 'szhozgzm', 'cfpcauhych', 'sobmcygx', 'xnatai', 'zdfekffbn', 'xwbnyqwvic', 'zatzuiedb', 'ykrsxg', 'nczuoayba', 'hmxhskkjnv', 'apclpsq', 'qionhx', 'ogtvhrcqix', 'znjxvekjq', 'hvnllww', 'ploinynfk', 'jglsmn', 'ilkubvhgi', 'swnzxld', 'kgmcbp', 'zgbywoq', 'wibccibjw', 'aayzltcj', 'aeagcrm', 'cdyelh', 'nwfykmatsz', 'osmmnzxmf', 'mwcgcbnsfn', 'izrzptnqcp', 'bgricaydmm', 'igjrutti', 'yujtwtqjk', 'qacrndrtlh', 'svclxfxyd', 'pgbornkdvj', 'iohuyxjx', 'cjldsjbou', 'gpjmod', 'hokdre', 'hfcexchh', 'vlxjgfo', 'ubcrorez', 'hpjjsvqexg', 'ewjhdfoqhi', 'nksyhg', 'skbvazth', 'jfcnbjuoj', 'wkimrt', 'rhumyu', 'alyqzvyw', 'clwgihlbh', 'gcoxvt', 'slnvpxkceo', 'ctwkey', 'swhcfno', 'sqlzyyiay', 'trbyjw', 'kergwwqrrj', 'crinurvant', 'mfzkydgp', 'dnbnbj', 'vwenafgf', 'hkdqzwxiks', 'othqds', 'qkmzumceab', 'szxqlz', 'iihogotiah', 'vccsgsjtue', 'acarrvc', 'flvutzkmv', 'nvksbu', 'cftzmyespg', 'irgvoyrofz', 'isahttkae', 'ueqrauk', 'ghmvvqitdn', 'lkyiyg', 'xqgcmzi', 'kpibltrb', 'zyiqfdnbd', 'headvutqw', 'yngqdvw', 'pnznacd', 'rqwnfbpud', 'fuaivz', 'wsikwpleu', 'crpzqtj', 'zxuishi', 'ayfqtobh', 'hymorwwwh', 'amekxsi', 'ztussiu', 'jzvqsppbv', 'wgmonv', 'mnxdlk', 'cgleqvm', 'itsxjqq', 'tpffqarn', 'grmechuf', 'zjqyshyylv', 'uaitzilu', 'skmehs', 'psvowik', 'fwkbvtsnl', 'dmslclewd', 'bsotrff', 'urkskvmf', 'tavtoiw', 'pyuezwo', 'suhumfhtre', 'wdjfununt', 'tzrjycccq', 'veajpa', 'ybqcdwp', 'hobbzmdfy', 'shihivvpyt', 'uphilv', 'ukdjhus', 'jmzdvkncib', 'lznghfhkx', 'ajtnct', 'uufcxn', 'aukzbef', 'fojsrnu', 'lwguaza', 'yvmxujreg', 'qbuiapue', 'xnusqkij', 'lwpfkuy', 'udrodan', 'mklvde', 'tvkslzs', 'vkjwqpecpi', 'vpznfdjkfr', 'jlvugopgs', 'cakzfi', 'ekoznhs', 'edeucyyk', 'zdhrsiulo', 'rxbtgdkbp', 'zjohwrewt', 'nkbxkqfdaz', 'bakiaw', 'xpkxkj', 'liechny', 'jiprek', 'oxrhmq', 'mxrouspx', 'mjzentz', 'rybmskhzf', 'eqlidbhuuv', 'bkmzdkqp', 'iiqduq', 'nvpihfmabs', 'jbknckxocu', 'rwyaia', 'qogoywi', 'rssrilools', 'ptxbjeokha', 'xwwaexuaul', 'hhgwxoexi', 'uoixnkbowz', 'mdflmi', 'jxyxccdti', 'jevunbc', 'rzkggzfv', 'yqlotrkxu', 'xyhtddnki', 'vjpplyso', 'kpirliezrp', 'yubzywlqv', 'klwhogxe', 'gulbes', 'dszcoa', 'npyixygy', 'giwcqyqeh', 'vsmudhjjqq', 'axqhggfmng', 'jclobag', 'kyvgrkozi', 'xssnogi', 'zjtavsyie', 'cjduudm', 'frsxilvt', 'wgwapbf', 'imqneydn', 'hekgsmo', 'ofmfucsio', 'rdasvhu', 'dqexpskqk', 'opndqayu', 'mvqhczo', 'vdszsodac', 'ztpzyx', 'xkindqvsn', 'byqbheq', 'qxwhkxr', 'ktpyxuymhk', 'nenhiqkqpa', 'zzoqyszlpm', 'akskigi', 'eovlkpilg', 'iwctxqjmxb', 'qhyshkyqq', 'tjnkcgiu', 'owsvmzsyld', 'ixifprrny', 'egcjoqbw', 'xaqnntrwr', 'ssqbxviwh', 'dzuquatc', 'xsvytpov', 'uqpeuzk', 'vnodbyv', 'etpnli', 'joqfrflii', 'uznqzhfub', 'mrzotsd', 'rchkohtpp', 'aagxhxu', 'atidywzt', 'ixunsrz', 'ahtvbqd', 'klpqxuflh', 'vkvjwwm', 'tcnzpw', 'atahkkj', 'mqafymfwl', 'rlbuyh', 'dumqfvwh', 'xhgufic', 'fnfzcrduia', 'bvvpkqkcr', 'rmqubjhc', 'mtsyzdvda', 'jydcaqw', 'hbvjhg', 'oboccoh', 'zbuazpfkz', 'nbprlr', 'khsylmgtj', 'kuhvclr', 'bjwllkb', 'rsvdpihml', 'mkpmseh', 'srwydqrtzm', 'rdachgpxnq', 'kqtlsq', 'pjpzejzakk', 'pdyknq', 'rlfkscx', 'swyksgncza', 'ivozmbprnv', 'kftsgcw', 'ykzoaev', 'uvbkzv', 'rxurdx', 'oxtaohqoa', 'lcjncy', 'rxsgdmblqw', 'xxioqybvk', 'ufmlreupt', 'uwuyoj', 'rtuxqcxfmx', 'apjlqq', 'ctvzoeespj', 'aekdxfl', 'gyklqbco', 'shaglhsnqh', 'nhusukewst', 'znpwmnlufo', 'titlnhnfjc', 'vnzjyxkyod', 'cmskymwkf', 'cmrjutke', 'inzxmfsevf', 'yuawvsd', 'qhaxbwjd', 'ydejtcszpy', 'mvubwt', 'wzauwld', 'kvcjsvsdze', 'gvsnzudr', 'reldbtjeuj', 'tqqmcki', 'wvktmuri', 'yvdvdxgol', 'gsajpj', 'mdizeknijy', 'vknykf', 'cylahvvdpi', 'nmycbygf', 'olmjszzt', 'yzgjaew', 'yudywpras', 'nayqpjp', 'nrpraebc', 'nwsoeivejp', 'oexmffb', 'bxaosinjq', 'lzecjd', 'mirxuwdr', 'zdbuijfb', 'sihbsjcn', 'hxwhpwq', 'qpdopmdg', 'yaurhjk', 'yelnrkau', 'dibhfazy', 'evmklgzh', 'hjmkelw', 'mhlzno', 'sozppuyavh', 'maxokx', 'wvfjspxt', 'iprwjobqps', 'diupvou', 'ozkyuojgtq', 'vtqhwomyt', 'deaqzurmc', 'wocjjt', 'wjhegzfh', 'rzscasg', 'wzemzmnpsz', 'jdgeeh', 'zvepepzqe', 'kvhcbrs', 'hstnntsiiq', 'lwjjkogrnx', 'wuyqgl', 'yrhztwj', 'idzmfmyta', 'zrtyxmmw', 'osaefbs', 'iifdcniga', 'mapayxdh', 'suzscpr', 'gpidwzs', 'mbkpep', 'vevitz', 'tfygcc', 'wppeirzxxw', 'gwtpeip', 'lnqrtnbx', 'uplxvmtf', 'mhgeglbrb', 'jsgfznw', 'rahfdkmbn', 'oqgzulmttv', 'khjmojiw', 'tuuhdg', 'uetlrir', 'vvknylwaxm', 'aiwmgtdqhk', 'yswruvte', 'rmkdnksn', 'rnmjrowo', 'ogsufkxhx', 'eivwla', 'mfhlhzcj', 'hsjspjccux', 'ivwpdjzmp', 'mbkutww', 'azvgya', 'jmodem', 'mupaebfp', 'fqoziuy', 'masbjiy', 'vhtqnq', 'wcyjgdtweq', 'owdhbstax', 'wrzrtdqh', 'mkanzbzys', 'jxcmjyy', 'bzaknmelji', 'qcrdppyn', 'namuomhaaa', 'uwiteqdfd', 'aiaeji', 'znjdcox', 'zrnenff', 'zpravmw', 'rniqydavo', 'drqgfvh', 'krxnfgcv', 'lfocazy', 'ubpkukwx', 'pfbirja', 'kvovuwqg', 'gfuvpzdz', 'bsncbqnt', 'iaacyjrcdm', 'hycevjlx', 'onodjjpbe', 'lskzczwzi', 'dgrexjqj', 'ehnndrtndb', 'ediuag', 'kvkvxmhfqo', 'famupsvsok', 'zhrtxlm', 'ekqcbpaf', 'ypaxcbuxm', 'hnwgfrjz', 'qojyqedd', 'tkvvhp', 'efjmjccd', 'exsuhkepw', 'jyahzjlzn', 'vrfuru', 'qisucytklp', 'lkkqhmsu', 'pvnbkc', 'hvwimoq', 'inesyhdtb', 'ujtorqr', 'uvlirk', 'qmsbygddad', 'aqcqsba', 'xnjcek', 'ssdfpdkf', 'puckgqxgea', 'rpsjnnznzi', 'xzuvyi', 'riilkzatxr', 'jxwsnm', 'xgznjcjmq', 'avhmxieuzv', 'wijjttf', 'rshtni', 'cfpkseta', 'qulrrvjyv', 'dqdnkjcu', 'xcxhts', 'mszxljscar', 'exdqpy', 'shxeepj', 'jfzydand', 'pqdpyn', 'faddlzyeuk', 'bghqgoxt', 'cogensuqz', 'lwpqtkowjt', 'gkptdhwtyh', 'mcjnemsbpo', 'letzaze', 'tfpnfl', 'jaozjlkzoz']
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
LineOfTExt = ''

#left function
def left(S):
    global Score
    if Round == 1:
        RandomVariable = random.randint(1, len(S))
        Answer = S[:RandomVariable]
        print("Here's the string:",S,"and it's a LEFT function")
        print("Here's the answer:",Answer)
        print("Input the command that will lead you to this answer using the string given")
        Command = (f"LEFT({S},{RandomVariable})")
        Guess = input("Answer: ")
        if Guess == Command:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Command}")

#right function
def right(S):
    global Score
    if Round == 1:
        RandomVariable = random.randint(1, len(S))
        Answer = S[-RandomVariable::]
        print("Here's the string:",S,"and it's a RIGHT function")
        print("Here's the answer:",Answer)
        print("Input the command that will lead you to this answer using the string given")
        Command = (f"RIGHT({S},{RandomVariable})")
        Guess = input("Answer: ")
        if Guess == Command:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Command}")

#onechar function
def onechar(S):
    global Score
    if Round == 1:
        RandomVariable = random.randint(1, len(S))
        Answer = S[RandomVariable-1]
        print("Here's the string:",S,"and it's a ONECHAR function")
        print("Here's the answer:",Answer)
        print("Input the command that will lead you to this answer using the string given")
        Command = (f"ONECHAR({S},{RandomVariable})")
        Guess = input("Answer: ")
        if Guess == Command:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Command}")

#mid function
def mid(S):
    global Score
    if Round == 1:
        l = len(S)
        RandomVariable = random.randint(0, l-1)
        RandomLength = random.randint(1, l-RandomVariable)
        Answer = S[RandomVariable:RandomLength+RandomVariable]
        print("Here's the string:",S,"and it's a MID function")
        print("Here's the answer:",Answer)
        print("Input the command that will lead you to this answer using the string given")
        Command = (f"MID({S},{RandomVariable+1},{RandomLength})")
        Guess = input("Answer: ")
        if Guess == Command:
            print("Correct!")
            Score = Score + 1
        else:
            print("Wrong!")
            print(f"Correct answer: {Command}")

Name = input('What is you name? ')
Score = 0

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

print("")
print(f"Score: {Score}/8")
