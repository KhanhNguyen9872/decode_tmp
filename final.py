  1           0 LOAD_CONST               0 (0)
              2 LOAD_CONST               1 (None)
              4 IMPORT_NAME              0 (discord)
              6 STORE_NAME               0 (discord)
              8 LOAD_CONST               0 (0)
             10 LOAD_CONST               1 (None)
             12 IMPORT_NAME              1 (time)
             14 STORE_NAME               1 (time)
             16 LOAD_CONST               0 (0)
             18 LOAD_CONST               1 (None)
             20 IMPORT_NAME              2 (random)
             22 STORE_NAME               2 (random)

  2          24 LOAD_CONST               0 (0)
             26 LOAD_CONST               1 (None)
             28 IMPORT_NAME              1 (time)
             30 STORE_NAME               1 (time)

  3          32 LOAD_CONST               0 (0)
             34 LOAD_CONST               1 (None)
             36 IMPORT_NAME              3 (os)
             38 STORE_NAME               3 (os)
             40 LOAD_CONST               0 (0)
             42 LOAD_CONST               1 (None)
             44 IMPORT_NAME              4 (sys)
             46 STORE_NAME               4 (sys)
             48 LOAD_CONST               0 (0)
             50 LOAD_CONST               1 (None)
             52 IMPORT_NAME              5 (requests)
             54 STORE_NAME               5 (requests)
             56 LOAD_CONST               0 (0)
             58 LOAD_CONST               1 (None)
             60 IMPORT_NAME              6 (json)
             62 STORE_NAME               6 (json)

  4          64 LOAD_CONST               0 (0)
             66 LOAD_CONST               2 (('post', 'Session'))
             68 IMPORT_NAME              5 (requests)
             70 IMPORT_FROM              7 (post)
             72 STORE_NAME               7 (post)
             74 IMPORT_FROM              8 (Session)
             76 STORE_NAME               8 (Session)
             78 POP_TOP

  5          80 LOAD_CONST               0 (0)
             82 LOAD_CONST               3 (('ThreadPoolExecutor',))
             84 IMPORT_NAME              9 (concurrent.futures)
             86 IMPORT_FROM             10 (ThreadPoolExecutor)
             88 STORE_NAME              10 (ThreadPoolExecutor)
             90 POP_TOP

  6          92 LOAD_CONST               0 (0)
             94 LOAD_CONST               4 (('commands',))
             96 IMPORT_NAME             11 (discord.ext)
             98 IMPORT_FROM             12 (commands)
            100 STORE_NAME              12 (commands)
            102 POP_TOP

  7         104 LOAD_CONST               0 (0)
            106 LOAD_CONST               5 (('search',))
            108 IMPORT_NAME             13 (re)
            110 IMPORT_FROM             14 (search)
            112 STORE_NAME              14 (search)
            114 POP_TOP

  8         116 LOAD_CONST               0 (0)
            118 LOAD_CONST               1 (None)
            120 IMPORT_NAME             15 (threading)
            122 STORE_NAME              15 (threading)

  9         124 LOAD_CONST               0 (0)
            126 LOAD_CONST               6 (('choice', 'randint', 'shuffle'))
            128 IMPORT_NAME              2 (random)
            130 IMPORT_FROM             16 (choice)
            132 STORE_NAME              16 (choice)
            134 IMPORT_FROM             17 (randint)
            136 STORE_NAME              17 (randint)
            138 IMPORT_FROM             18 (shuffle)
            140 STORE_NAME              18 (shuffle)
            142 POP_TOP

 10         144 LOAD_CONST               7 ('MTAyNDYyMzA5MDQ2ODEyNjczMQ.G2TR8P.ky28XL3KRNg1vU1tzb179AKwAzy-54l8WhkuKs')
            146 STORE_NAME              19 (token)

 11         148 LOAD_CONST               8 ('!')
            150 STORE_NAME              20 (prefix)

 12         152 LOAD_NAME                0 (discord)
            154 LOAD_ATTR               21 (Intents)
            156 LOAD_METHOD             22 (all)
            158 CALL_METHOD              0
            160 STORE_NAME              23 (intents)

 13         162 LOAD_CONST               9 (True)
            164 LOAD_NAME               23 (intents)
            166 STORE_ATTR              24 (messages)

 14         168 LOAD_NAME               12 (commands)
            170 LOAD_ATTR               25 (Bot)
            172 LOAD_NAME               20 (prefix)
            174 LOAD_CONST               1 (None)
            176 LOAD_NAME               23 (intents)
            178 LOAD_CONST              10 (('command_prefix', 'help_command', 'intents'))
            180 CALL_FUNCTION_KW         3
            182 STORE_NAME              26 (bot)

 15         184 LOAD_NAME               10 (ThreadPoolExecutor)
            186 LOAD_NAME               27 (int)
            188 LOAD_CONST              11 (100000000)
            190 CALL_FUNCTION            1
            192 LOAD_CONST              12 (('max_workers',))
            194 CALL_FUNCTION_KW         1
            196 STORE_NAME              15 (threading)

 16         198 LOAD_CONST              13 (<code object cang01 at 0x00000206DD13ED40, file "<k>", line 17>)
            200 LOAD_CONST              14 ('cang01')
            202 MAKE_FUNCTION            0
            204 STORE_NAME              28 (cang01)

 17         206 LOAD_CONST              15 (<code object cang02 at 0x00000206DD13EDF0, file "<k>", line 19>)
            208 LOAD_CONST              16 ('cang02')
            210 MAKE_FUNCTION            0
            212 STORE_NAME              29 (cang02)

 19         214 LOAD_CONST              17 (<code object generateRandomString at 0x00000206DD13EEA0, file "<k>", line 125>)
            216 LOAD_CONST              18 ('generateRandomString')
            218 MAKE_FUNCTION            0
            220 STORE_NAME              30 (generateRandomString)

125         222 LOAD_CONST              19 (<code object get_SECUREID at 0x00000206DD13EF50, file "<k>", line 127>)
            224 LOAD_CONST              20 ('get_SECUREID')
            226 MAKE_FUNCTION            0
            228 STORE_NAME              31 (get_SECUREID)

127         230 LOAD_CONST              21 (<code object getiMEII at 0x00000206DD145030, file "<k>", line 129>)
            232 LOAD_CONST              22 ('getiMEII')
            234 MAKE_FUNCTION            0
            236 STORE_NAME              32 (getiMEII)

129         238 LOAD_CONST              23 (<code object get_TOKEN at 0x00000206DD145190, file "<k>", line 131>)
            240 LOAD_CONST              24 ('get_TOKEN')
            242 MAKE_FUNCTION            0
            244 STORE_NAME              33 (get_TOKEN)

131         246 LOAD_CONST              25 (<code object cang03 at 0x00000206DD145240, file "<k>", line 134>)
            248 LOAD_CONST              26 ('cang03')
            250 MAKE_FUNCTION            0
            252 STORE_NAME              34 (cang03)

134         254 LOAD_CONST              27 (<code object cang1 at 0x00000206DD1453A0, file "<k>", line 138>)
            256 LOAD_CONST              28 ('cang1')
            258 MAKE_FUNCTION            0
            260 STORE_NAME              35 (cang1)

138         262 LOAD_CONST              29 (<code object cang2 at 0x00000206DD145450, file "<k>", line 142>)
            264 LOAD_CONST              30 ('cang2')
            266 MAKE_FUNCTION            0
            268 STORE_NAME              36 (cang2)

142         270 LOAD_CONST              31 (<code object cang3 at 0x00000206DD1455B0, file "<k>", line 145>)
            272 LOAD_CONST              32 ('cang3')
            274 MAKE_FUNCTION            0
            276 STORE_NAME              37 (cang3)

145         278 LOAD_CONST              33 (<code object cang4 at 0x00000206DD145660, file "<k>", line 149>)
            280 LOAD_CONST              34 ('cang4')
            282 MAKE_FUNCTION            0
            284 STORE_NAME              38 (cang4)

149         286 LOAD_CONST              35 (<code object cang5 at 0x00000206DD145710, file "<k>", line 153>)
            288 LOAD_CONST              36 ('cang5')
            290 MAKE_FUNCTION            0
            292 STORE_NAME              39 (cang5)

153         294 LOAD_CONST              37 (<code object cang6 at 0x00000206DD1457C0, file "<k>", line 156>)
            296 LOAD_CONST              38 ('cang6')
            298 MAKE_FUNCTION            0
            300 STORE_NAME              40 (cang6)

156         302 LOAD_CONST              39 (<code object cang7 at 0x00000206DD145920, file "<k>", line 159>)
            304 LOAD_CONST              40 ('cang7')
            306 MAKE_FUNCTION            0
            308 STORE_NAME              41 (cang7)

159         310 LOAD_CONST              41 (<code object cang8 at 0x00000206DD1459D0, file "<k>", line 162>)
            312 LOAD_CONST              42 ('cang8')
            314 MAKE_FUNCTION            0
            316 STORE_NAME              42 (cang8)

162         318 LOAD_CONST              43 (<code object cang9 at 0x00000206DD145A80, file "<k>", line 167>)
            320 LOAD_CONST              44 ('cang9')
            322 MAKE_FUNCTION            0
            324 STORE_NAME              43 (cang9)

167         326 LOAD_CONST              45 (<code object cang10 at 0x00000206DD145B30, file "<k>", line 170>)
            328 LOAD_CONST              46 ('cang10')
            330 MAKE_FUNCTION            0
            332 STORE_NAME              44 (cang10)

170         334 LOAD_CONST              47 (<code object cang11 at 0x00000206DD145BE0, file "<k>", line 173>)
            336 LOAD_CONST              48 ('cang11')
            338 MAKE_FUNCTION            0
            340 STORE_NAME              45 (cang11)

173         342 LOAD_CONST              49 (<code object cang12 at 0x00000206DD145C90, file "<k>", line 179>)
            344 LOAD_CONST              50 ('cang12')
            346 MAKE_FUNCTION            0
            348 STORE_NAME              46 (cang12)

179         350 LOAD_CONST              51 (<code object cang13 at 0x00000206DD145DF0, file "<k>", line 183>)
            352 LOAD_CONST              52 ('cang13')
            354 MAKE_FUNCTION            0
            356 STORE_NAME              47 (cang13)

183         358 LOAD_CONST              53 (<code object cang14 at 0x00000206DD145EA0, file "<k>", line 187>)
            360 LOAD_CONST              54 ('cang14')
            362 MAKE_FUNCTION            0
            364 STORE_NAME              48 (cang14)

187         366 LOAD_CONST              55 (<code object cang15 at 0x00000206DD148030, file "<k>", line 190>)
            368 LOAD_CONST              56 ('cang15')
            370 MAKE_FUNCTION            0
            372 STORE_NAME              49 (cang15)

190         374 LOAD_CONST              57 (<code object cang16 at 0x00000206DD1480E0, file "<k>", line 194>)
            376 LOAD_CONST              58 ('cang16')
            378 MAKE_FUNCTION            0
            380 STORE_NAME              50 (cang16)

194         382 LOAD_CONST              59 (<code object cang17 at 0x00000206DD148190, file "<k>", line 224>)
            384 LOAD_CONST              60 ('cang17')
            386 MAKE_FUNCTION            0
            388 STORE_NAME              51 (cang17)

224         390 LOAD_CONST              61 (<code object CBot at 0x00000206DD148240, file "<k>", line 228>)
            392 LOAD_CONST              62 ('CBot')
            394 MAKE_FUNCTION            0
            396 STORE_NAME              52 (CBot)

228         398 LOAD_CONST              63 (<code object DBot at 0x00000206DD1482F0, file "<k>", line 238>)
            400 LOAD_CONST              64 ('DBot')
            402 MAKE_FUNCTION            0
            404 STORE_NAME              53 (DBot)

238         406 LOAD_CONST              65 (<code object BBot at 0x00000206DD1483A0, file "<k>", line 262>)
            408 LOAD_CONST              66 ('BBot')
            410 MAKE_FUNCTION            0
            412 STORE_NAME              54 (BBot)

262         414 LOAD_NAME               12 (commands)
            416 LOAD_METHOD             55 (has_role)
            418 LOAD_CONST              67 ('vip buy')
            420 CALL_METHOD              1

300         422 LOAD_NAME               26 (bot)
            424 LOAD_ATTR               56 (event)

301         426 LOAD_CONST              68 (<code object on_connect at 0x00000206DD148450, file "<k>", line 300>)
            428 LOAD_CONST              69 ('on_connect')
            430 MAKE_FUNCTION            0
            432 CALL_FUNCTION            1
            434 CALL_FUNCTION            1
            436 STORE_NAME              57 (on_connect)

302         438 LOAD_NAME               12 (commands)
            440 LOAD_METHOD             55 (has_role)
            442 LOAD_CONST              67 ('vip buy')
            444 CALL_METHOD              1

323         446 LOAD_NAME               26 (bot)
            448 LOAD_METHOD             58 (command)
            450 CALL_METHOD              0

324         452 LOAD_CONST              70 ('amount')
            454 LOAD_NAME               27 (int)
            456 BUILD_TUPLE              2
            458 LOAD_CONST              71 (<code object fpt at 0x00000206DD148500, file "<k>", line 323>)
            460 LOAD_CONST              72 ('fpt')
            462 MAKE_FUNCTION            4 (annotations)
            464 CALL_FUNCTION            1
            466 CALL_FUNCTION            1
            468 STORE_NAME              59 (fpt)

325         470 LOAD_NAME               12 (commands)
            472 LOAD_METHOD             55 (has_role)
            474 LOAD_CONST              67 ('vip buy')
            476 CALL_METHOD              1

352         478 LOAD_NAME               26 (bot)
            480 LOAD_METHOD             58 (command)
            482 CALL_METHOD              0

353         484 LOAD_CONST              70 ('amount')
            486 LOAD_NAME               27 (int)
            488 BUILD_TUPLE              2
            490 LOAD_CONST              73 (<code object call at 0x00000206DD148660, file "<k>", line 352>)
            492 LOAD_CONST              74 ('call')
            494 MAKE_FUNCTION            4 (annotations)
            496 CALL_FUNCTION            1
            498 CALL_FUNCTION            1
            500 STORE_NAME              60 (call)

354         502 LOAD_NAME               12 (commands)
            504 LOAD_METHOD             55 (has_role)
            506 LOAD_CONST              67 ('vip buy')
            508 CALL_METHOD              1

381         510 LOAD_NAME               26 (bot)
            512 LOAD_METHOD             58 (command)
            514 CALL_METHOD              0

382         516 LOAD_CONST              70 ('amount')
            518 LOAD_NAME               27 (int)
            520 BUILD_TUPLE              2
            522 LOAD_CONST              75 (<code object sms at 0x00000206DD148710, file "<k>", line 381>)
            524 LOAD_CONST              76 ('sms')
            526 MAKE_FUNCTION            4 (annotations)
            528 CALL_FUNCTION            1
            530 CALL_FUNCTION            1
            532 STORE_NAME              61 (sms)

383         534 LOAD_NAME               26 (bot)
            536 LOAD_METHOD             58 (command)
            538 CALL_METHOD              0

420         540 LOAD_CONST              77 (<code object help at 0x00000206DD1487C0, file "<k>", line 420>)
            542 LOAD_CONST              78 ('help')
            544 MAKE_FUNCTION            0
            546 CALL_FUNCTION            1
            548 STORE_NAME              62 (help)

421         550 LOAD_NAME               26 (bot)
            552 LOAD_METHOD             63 (run)
            554 LOAD_NAME               19 (token)
            556 CALL_METHOD              1
            558 POP_TOP
            560 LOAD_CONST               1 (None)
            562 RETURN_VALUE

Disassembly of <code object cang01 at 0x00000206DD13ED40, file "<k>", line 17>:
 17           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('https://api.vayvnd.vn/v1/users/password-reset')
              6 LOAD_CONST               2 ('api.vayvnd.vn')
              8 LOAD_CONST               3 ('22')
             10 LOAD_CONST               4 ('application/json')
             12 LOAD_CONST               4 ('application/json')
             14 LOAD_CONST               5 ('vi')
             16 LOAD_CONST               6 ('?1')
             18 LOAD_CONST               7 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             20 LOAD_CONST               8 ('"Android"')
             22 LOAD_CONST               9 ('https://vayvnd.vn')
             24 LOAD_CONST              10 ('same-site')
             26 LOAD_CONST              11 ('cors')
             28 LOAD_CONST              12 ('empty')
             30 LOAD_CONST              13 ('https://vayvnd.vn/')
             32 LOAD_CONST              14 ('gzip, deflate, br')
             34 LOAD_CONST              15 (('Host', 'content-length', 'accept', 'content-type', 'accept-language', 'sec-ch-ua-mobile', 'user-agent', 'sec-ch-ua-platform', 'origin', 'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-dest', 'referer', 'accept-encoding'))
             36 BUILD_CONST_KEY_MAP     14
             38 LOAD_GLOBAL              2 (json)
             40 LOAD_METHOD              3 (dumps)
             42 LOAD_CONST              16 ('login')
             44 LOAD_CONST              17 ('0')
             46 LOAD_FAST                0 (phone)
             48 BINARY_ADD
             50 BUILD_MAP                1
             52 CALL_METHOD              1
             54 LOAD_CONST              18 (('headers', 'data'))
             56 CALL_FUNCTION_KW         3
             58 LOAD_ATTR                4 (text)
             60 POP_TOP
             62 LOAD_CONST               0 (None)
             64 RETURN_VALUE

Disassembly of <code object cang02 at 0x00000206DD13EDF0, file "<k>", line 19>:
 19           0 LOAD_GLOBAL              0 (int)
              2 LOAD_GLOBAL              1 (round)
              4 LOAD_GLOBAL              2 (time)
              6 LOAD_METHOD              2 (time)
              8 CALL_METHOD              0
             10 LOAD_CONST               1 (1000)
             12 BINARY_MULTIPLY
             14 CALL_FUNCTION            1
             16 CALL_FUNCTION            1
             18 STORE_FAST               1 (microtime)

 20          20 LOAD_GLOBAL              3 (getiMEII)
             22 CALL_FUNCTION            0
             24 STORE_FAST               2 (iMEII)

 21          26 LOAD_GLOBAL              4 (get_SECUREID)
             28 CALL_FUNCTION            0
             30 STORE_FAST               3 (secureid)

 22          32 LOAD_GLOBAL              5 (get_TOKEN)
             34 CALL_FUNCTION            0
             36 STORE_FAST               4 (token)

 23          38 LOAD_GLOBAL              6 (generateRandomString)
             40 LOAD_CONST               2 (22)
             42 LOAD_CONST               3 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
             44 CALL_FUNCTION            2
             46 STORE_FAST               5 (rkey)

 24          48 LOAD_GLOBAL              3 (getiMEII)
             50 CALL_FUNCTION            0
             52 STORE_FAST               6 (aaid)

 25          54 BUILD_MAP                0

 26          56 LOAD_CONST               4 ('user')
             58 LOAD_CONST               5 ('0')
             60 LOAD_FAST                0 (phone)
             62 BINARY_ADD

 27          64 MAP_ADD                  1

 26          66 LOAD_CONST               6 ('msgType')
             68 LOAD_CONST               7 ('SEND_OTP_MSG')

 28          70 MAP_ADD                  1

 26          72 LOAD_CONST               8 ('cmdId')
             74 LOAD_FAST                1 (microtime)
             76 FORMAT_VALUE             0
             78 LOAD_CONST               9 ('000000')
             80 BUILD_STRING             2

 29          82 MAP_ADD                  1

 26          84 LOAD_CONST              10 ('lang')
             86 LOAD_CONST              11 ('vi')

 30          88 MAP_ADD                  1

 26          90 LOAD_CONST              12 ('time')
             92 LOAD_FAST                1 (microtime)

 31          94 MAP_ADD                  1

 26          96 LOAD_CONST              13 ('channel')
             98 LOAD_CONST              14 ('APP')

 32         100 MAP_ADD                  1

 26         102 LOAD_CONST              15 ('appVer')
            104 LOAD_CONST              16 (31062)

 33         106 MAP_ADD                  1

 26         108 LOAD_CONST              17 ('appCode')
            110 LOAD_CONST              18 ('3.1.6')

 34         112 MAP_ADD                  1

 26         114 LOAD_CONST              19 ('deviceOS')
            116 LOAD_CONST              20 ('ANDROID')

 35         118 MAP_ADD                  1

 26         120 LOAD_CONST              21 ('buildNumber')
            122 LOAD_CONST              22 (0)

 36         124 MAP_ADD                  1

 26         126 LOAD_CONST              23 ('appId')
            128 LOAD_CONST              24 ('vn.momo.platform')

 37         130 MAP_ADD                  1

 26         132 LOAD_CONST              25 ('result')
            134 LOAD_CONST              26 (True)

 38         136 MAP_ADD                  1

 26         138 LOAD_CONST              27 ('errorCode')
            140 LOAD_CONST              22 (0)

 39         142 MAP_ADD                  1

 26         144 LOAD_CONST              28 ('errorDesc')
            146 LOAD_CONST              29 ('')

 40         148 MAP_ADD                  1

 26         150 LOAD_CONST              30 ('momoMsg')

 41         152 LOAD_CONST              31 ('mservice.backend.entity.msg.RegDeviceMsg')

 42         154 LOAD_CONST               5 ('0')
            156 LOAD_FAST                0 (phone)
            158 BINARY_ADD

 43         160 LOAD_FAST                2 (iMEII)

 44         162 LOAD_CONST              32 ('Vietnam')

 45         164 LOAD_CONST              33 ('084')

 46         166 LOAD_CONST              34 ('CPH1605')

 47         168 LOAD_CONST              35 ('23')

 48         170 LOAD_CONST              36 ('mt6755')

 49         172 LOAD_CONST              37 ('OPPO')

 50         174 LOAD_CONST              29 ('')

 51         176 LOAD_CONST              29 ('')

 52         178 LOAD_CONST              38 ('452')

 53         180 LOAD_CONST              39 ('Android')

 54         182 LOAD_FAST                3 (secureid)

 55         184 LOAD_CONST              40 (('_class', 'number', 'iMEII', 'cname', 'ccode', 'device', 'firmware', 'hardware', 'manufacture', 'csp', 'icc', 'mcc', 'device_os', 'secure_id'))
            186 BUILD_CONST_KEY_MAP     14

 41         188 MAP_ADD                  1

 26         190 LOAD_CONST              41 ('extra')

 57         192 LOAD_CONST              42 ('SEND')

 58         194 LOAD_FAST                5 (rkey)

 59         196 LOAD_FAST                6 (aaid)

 60         198 LOAD_CONST              29 ('')

 61         200 LOAD_FAST                4 (token)

 62         202 LOAD_CONST              29 ('')

 63         204 LOAD_FAST                3 (secureid)

 64         206 LOAD_CONST              43 ('oppo cph1605mt6755b6z9qwrwhuy9yhrk')

 65         208 LOAD_CONST              26 (True)

 66         210 LOAD_CONST              26 (True)

 67         212 LOAD_CONST              29 ('')

 68         214 LOAD_CONST              44 (('action', 'rkey', 'AAID', 'IDFA', 'TOKEN', 'SIMULATOR', 'SECUREID', 'MODELID', 'isVoice', 'REQUIRE_HASH_STRING_OTP', 'checkSum'))
            216 BUILD_CONST_KEY_MAP     11

 57         218 MAP_ADD                  1
            220 STORE_FAST               7 (data)

 26         222 BUILD_MAP                0

 71         224 LOAD_CONST               4 ('user')
            226 LOAD_CONST               5 ('0')
            228 LOAD_FAST                0 (phone)
            230 BINARY_ADD

 72         232 MAP_ADD                  1

 71         234 LOAD_CONST               6 ('msgType')
            236 LOAD_CONST              45 ('CHECK_USER_BE_MSG')

 73         238 MAP_ADD                  1

 71         240 LOAD_CONST               8 ('cmdId')
            242 LOAD_FAST                1 (microtime)
            244 FORMAT_VALUE             0
            246 LOAD_CONST               9 ('000000')
            248 BUILD_STRING             2

 74         250 MAP_ADD                  1

 71         252 LOAD_CONST              10 ('lang')
            254 LOAD_CONST              11 ('vi')

 75         256 MAP_ADD                  1

 71         258 LOAD_CONST              12 ('time')
            260 LOAD_FAST                1 (microtime)

 76         262 MAP_ADD                  1

 71         264 LOAD_CONST              13 ('channel')
            266 LOAD_CONST              14 ('APP')

 77         268 MAP_ADD                  1

 71         270 LOAD_CONST              15 ('appVer')
            272 LOAD_CONST              16 (31062)

 78         274 MAP_ADD                  1

 71         276 LOAD_CONST              17 ('appCode')
            278 LOAD_CONST              18 ('3.1.6')

 79         280 MAP_ADD                  1

 71         282 LOAD_CONST              19 ('deviceOS')
            284 LOAD_CONST              20 ('ANDROID')

 80         286 MAP_ADD                  1

 71         288 LOAD_CONST              21 ('buildNumber')
            290 LOAD_CONST              22 (0)

 81         292 MAP_ADD                  1

 71         294 LOAD_CONST              23 ('appId')
            296 LOAD_CONST              24 ('vn.momo.platform')

 82         298 MAP_ADD                  1

 71         300 LOAD_CONST              25 ('result')
            302 LOAD_CONST              26 (True)

 83         304 MAP_ADD                  1

 71         306 LOAD_CONST              27 ('errorCode')
            308 LOAD_CONST              22 (0)

 84         310 MAP_ADD                  1

 71         312 LOAD_CONST              28 ('errorDesc')
            314 LOAD_CONST              29 ('')

 85         316 MAP_ADD                  1

 71         318 LOAD_CONST              30 ('momoMsg')

 86         320 LOAD_CONST              31 ('mservice.backend.entity.msg.RegDeviceMsg')

 87         322 LOAD_CONST               5 ('0')
            324 LOAD_FAST                0 (phone)
            326 BINARY_ADD

 88         328 LOAD_FAST                2 (iMEII)

 89         330 LOAD_CONST              32 ('Vietnam')

 90         332 LOAD_CONST              33 ('084')

 91         334 LOAD_CONST              34 ('CPH1605')

 92         336 LOAD_CONST              35 ('23')

 93         338 LOAD_CONST              36 ('mt6755')

 94         340 LOAD_CONST              37 ('OPPO')

 95         342 LOAD_CONST              29 ('')

 96         344 LOAD_CONST              29 ('')

 97         346 LOAD_CONST              38 ('452')

 98         348 LOAD_CONST              39 ('Android')

 99         350 LOAD_FAST                3 (secureid)

100         352 LOAD_CONST              40 (('_class', 'number', 'iMEII', 'cname', 'ccode', 'device', 'firmware', 'hardware', 'manufacture', 'csp', 'icc', 'mcc', 'device_os', 'secure_id'))
            354 BUILD_CONST_KEY_MAP     14

 86         356 MAP_ADD                  1

 71         358 LOAD_CONST              41 ('extra')

102         360 LOAD_CONST              46 ('checkSum')
            362 LOAD_CONST              29 ('')

103         364 BUILD_MAP                1

102         366 MAP_ADD                  1
            368 STORE_FAST               8 (data1)

 71         370 LOAD_CONST              47 ('undefined')

107         372 LOAD_CONST              29 ('')

108         374 LOAD_CONST              47 ('undefined')

109         376 LOAD_CONST              48 ('Bearer undefined')

110         378 LOAD_CONST               7 ('SEND_OTP_MSG')

111         380 LOAD_CONST              49 ('api.momo.vn')

112         382 LOAD_CONST              50 ('okhttp/3.14.17')

113         384 LOAD_CONST              51 ('31062')

114         386 LOAD_CONST              18 ('3.1.6')

115         388 LOAD_CONST              20 ('ANDROID')

116         390 LOAD_CONST              52 ('application/json')

117         392 LOAD_CONST              53 (('agent_id', 'sessionkey', 'user_phone', 'authorization', 'msgtype', 'Host', 'User-Agent', 'app_version', 'app_code', 'device_os', 'Content-Type'))
            394 BUILD_CONST_KEY_MAP     11
            396 STORE_FAST               9 (h)

106         398 LOAD_GLOBAL              7 (post)
            400 LOAD_CONST              54 ('https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG')
            402 LOAD_FAST                9 (h)
            404 LOAD_FAST                8 (data1)
            406 LOAD_CONST              55 (('headers', 'json'))
            408 CALL_FUNCTION_KW         3
            410 LOAD_ATTR                8 (text)
            412 POP_TOP

119         414 LOAD_GLOBAL              7 (post)
            416 LOAD_CONST              56 ('https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG')
            418 LOAD_FAST                9 (h)
            420 LOAD_FAST                7 (data)
            422 LOAD_CONST              55 (('headers', 'json'))
            424 CALL_FUNCTION_KW         3
            426 LOAD_ATTR                8 (text)
            428 POP_TOP

120         430 SETUP_FINALLY           12 (to 444)

121         432 LOAD_GLOBAL              7 (post)
            434 LOAD_CONST              56 ('https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG')
            436 LOAD_FAST                9 (h)
            438 LOAD_FAST                7 (data)
            440 LOAD_CONST              55 (('headers', 'json'))
            442 CALL_FUNCTION_KW         3
        >>  444 LOAD_METHOD              9 (json)
            446 CALL_METHOD              0
            448 STORE_FAST              10 (t)
            450 POP_BLOCK
            452 LOAD_CONST               0 (None)
            454 RETURN_VALUE

122         456 POP_TOP
            458 POP_TOP
            460 POP_TOP

123         462 LOAD_GLOBAL              7 (post)
            464 LOAD_CONST              56 ('https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG')
            466 LOAD_FAST                9 (h)
            468 LOAD_FAST                7 (data)
            470 LOAD_CONST              55 (('headers', 'json'))
            472 CALL_FUNCTION_KW         3
            474 LOAD_ATTR                8 (text)
            476 STORE_FAST              10 (t)
            478 POP_EXCEPT
            480 LOAD_CONST               0 (None)
            482 RETURN_VALUE

Disassembly of <code object generateRandomString at 0x00000206DD13EEA0, file "<k>", line 125>:
125           0 LOAD_CONST               1 ('')
              2 LOAD_METHOD              0 (join)
              4 LOAD_GLOBAL              1 (random)
              6 LOAD_ATTR                2 (choices)
              8 LOAD_FAST                1 (minh)
             10 LOAD_FAST                0 (length)
             12 LOAD_CONST               2 (('k',))
             14 CALL_FUNCTION_KW         2
             16 CALL_METHOD              1
             18 RETURN_VALUE

Disassembly of <code object get_SECUREID at 0x00000206DD13EF50, file "<k>", line 127>:
127           0 LOAD_CONST               1 ('')
              2 LOAD_METHOD              0 (join)
              4 LOAD_GLOBAL              1 (random)
              6 LOAD_ATTR                2 (choices)
              8 LOAD_CONST               2 ('0123456789abcdef')
             10 LOAD_CONST               3 (17)
             12 LOAD_CONST               4 (('k',))
             14 CALL_FUNCTION_KW         2
             16 CALL_METHOD              1
             18 RETURN_VALUE

Disassembly of <code object getiMEII at 0x00000206DD145030, file "<k>", line 129>:
129           0 LOAD_GLOBAL              0 (generateRandomString)
              2 LOAD_CONST               1 (8)
              4 LOAD_CONST               2 ('0123456789abcdef')
              6 CALL_FUNCTION            2
              8 LOAD_CONST               3 ('-')
             10 BINARY_ADD
             12 LOAD_GLOBAL              0 (generateRandomString)
             14 LOAD_CONST               4 (4)
             16 LOAD_CONST               2 ('0123456789abcdef')
             18 CALL_FUNCTION            2
             20 BINARY_ADD
             22 LOAD_CONST               3 ('-')
             24 BINARY_ADD
             26 LOAD_GLOBAL              0 (generateRandomString)
             28 LOAD_CONST               4 (4)
             30 LOAD_CONST               2 ('0123456789abcdef')
             32 CALL_FUNCTION            2
             34 BINARY_ADD
             36 LOAD_CONST               3 ('-')
             38 BINARY_ADD
             40 LOAD_GLOBAL              0 (generateRandomString)
             42 LOAD_CONST               4 (4)
             44 LOAD_CONST               2 ('0123456789abcdef')
             46 CALL_FUNCTION            2
             48 BINARY_ADD
             50 LOAD_CONST               3 ('-')
             52 BINARY_ADD
             54 LOAD_GLOBAL              0 (generateRandomString)
             56 LOAD_CONST               5 (12)
             58 LOAD_CONST               2 ('0123456789abcdef')
             60 CALL_FUNCTION            2
             62 BINARY_ADD
             64 RETURN_VALUE

Disassembly of <code object get_TOKEN at 0x00000206DD145190, file "<k>", line 131>:
131           0 LOAD_GLOBAL              0 (generateRandomString)
              2 LOAD_CONST               1 (22)
              4 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
              6 CALL_FUNCTION            2
              8 LOAD_CONST               3 (':')
             10 BINARY_ADD
             12 LOAD_GLOBAL              0 (generateRandomString)
             14 LOAD_CONST               4 (9)
             16 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
             18 CALL_FUNCTION            2
             20 BINARY_ADD
             22 LOAD_CONST               5 ('-')
             24 BINARY_ADD
             26 LOAD_GLOBAL              0 (generateRandomString)
             28 LOAD_CONST               6 (20)
             30 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
             32 CALL_FUNCTION            2
             34 BINARY_ADD
             36 LOAD_CONST               5 ('-')
             38 BINARY_ADD
             40 LOAD_GLOBAL              0 (generateRandomString)
             42 LOAD_CONST               7 (12)
             44 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
             46 CALL_FUNCTION            2
             48 BINARY_ADD
             50 LOAD_CONST               5 ('-')
             52 BINARY_ADD
             54 LOAD_GLOBAL              0 (generateRandomString)
             56 LOAD_CONST               8 (7)
             58 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
             60 CALL_FUNCTION            2
             62 BINARY_ADD
             64 LOAD_CONST               5 ('-')
             66 BINARY_ADD
             68 LOAD_GLOBAL              0 (generateRandomString)
             70 LOAD_CONST               8 (7)
             72 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
             74 CALL_FUNCTION            2
             76 BINARY_ADD
             78 LOAD_CONST               5 ('-')
             80 BINARY_ADD
             82 LOAD_GLOBAL              0 (generateRandomString)
             84 LOAD_CONST               9 (53)
             86 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
             88 CALL_FUNCTION            2
             90 BINARY_ADD
             92 LOAD_CONST               5 ('-')
             94 BINARY_ADD
             96 LOAD_GLOBAL              0 (generateRandomString)
             98 LOAD_CONST               4 (9)
            100 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            102 CALL_FUNCTION            2
            104 BINARY_ADD
            106 LOAD_CONST              10 ('_')
            108 BINARY_ADD
            110 LOAD_GLOBAL              0 (generateRandomString)
            112 LOAD_CONST              11 (11)
            114 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            116 CALL_FUNCTION            2
            118 BINARY_ADD
            120 LOAD_CONST               5 ('-')
            122 BINARY_ADD
            124 LOAD_GLOBAL              0 (generateRandomString)
            126 LOAD_CONST              12 (4)
            128 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            130 CALL_FUNCTION            2
            132 BINARY_ADD
            134 RETURN_VALUE

Disassembly of <code object cang03 at 0x00000206DD145240, file "<k>", line 134>:
134           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('http://m.tv360.vn/public/v1/auth/get-otp-login')
              6 LOAD_CONST               2 ('m.tv360.vn')
              8 LOAD_CONST               3 ('keep-alive')
             10 LOAD_CONST               4 ('23')
             12 LOAD_CONST               5 ('application/json, text/plain, */*')
             14 LOAD_CONST               6 ('Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36')
             16 LOAD_CONST               7 ('application/json')
             18 LOAD_CONST               8 ('http://m.tv360.vn')
             20 LOAD_CONST               9 ('http://m.tv360.vn/login?r=http%3A%2F%2Fm.tv360.vn%2F')
             22 LOAD_CONST              10 ('gzip, deflate')
             24 LOAD_CONST              11 (('Host', 'Connection', 'Content-Length', 'Accept', 'User-Agent', 'Content-Type', 'Origin', 'Referer', 'Accept-Encoding'))
             26 BUILD_CONST_KEY_MAP      9
             28 LOAD_CONST              12 ('msisdn')
             30 LOAD_CONST              13 ('0')
             32 LOAD_FAST                0 (phone)
             34 BINARY_ADD
             36 BUILD_MAP                1
             38 LOAD_CONST              14 (('headers', 'json'))
             40 CALL_FUNCTION_KW         3
             42 LOAD_ATTR                2 (text)
             44 POP_TOP
             46 LOAD_CONST               0 (None)
             48 RETURN_VALUE

Disassembly of <code object cang1 at 0x00000206DD1453A0, file "<k>", line 138>:
138           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN')
              6 BUILD_MAP                0
              8 LOAD_CONST               2 ('Host')
             10 LOAD_CONST               3 ('api.alfrescos.com.vn')
             12 MAP_ADD                  1
             14 LOAD_CONST               4 ('content-length')
             16 LOAD_CONST               5 ('124')
             18 MAP_ADD                  1
             20 LOAD_CONST               6 ('accept-language')
             22 LOAD_CONST               7 ('vi-VN')
             24 MAP_ADD                  1
             26 LOAD_CONST               8 ('sec-ch-ua-mobile')
             28 LOAD_CONST               9 ('?1')
             30 MAP_ADD                  1
             32 LOAD_CONST              10 ('user-agent')
             34 LOAD_CONST              11 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             36 MAP_ADD                  1
             38 LOAD_CONST              12 ('content-type')
             40 LOAD_CONST              13 ('application/json')
             42 MAP_ADD                  1
             44 LOAD_CONST              14 ('accept')
             46 LOAD_CONST              15 ('application/json, text/plain, */*')
             48 MAP_ADD                  1
             50 LOAD_CONST              16 ('brandcode')
             52 LOAD_CONST              17 ('ALFRESCOS')
             54 MAP_ADD                  1
             56 LOAD_CONST              18 ('devicecode')
             58 LOAD_CONST              19 ('web')
             60 MAP_ADD                  1
             62 LOAD_CONST              20 ('sec-ch-ua-platform')
             64 LOAD_CONST              21 ('"Android"')
             66 MAP_ADD                  1
             68 LOAD_CONST              22 ('origin')
             70 LOAD_CONST              23 ('https://alfrescos.com.vn')
             72 MAP_ADD                  1
             74 LOAD_CONST              24 ('sec-fetch-site')
             76 LOAD_CONST              25 ('same-site')
             78 MAP_ADD                  1
             80 LOAD_CONST              26 ('sec-fetch-mode')
             82 LOAD_CONST              27 ('cors')
             84 MAP_ADD                  1
             86 LOAD_CONST              28 ('sec-fetch-dest')
             88 LOAD_CONST              29 ('empty')
             90 MAP_ADD                  1
             92 LOAD_CONST              30 ('referer')
             94 LOAD_CONST              31 ('https://alfrescos.com.vn/')
             96 MAP_ADD                  1
             98 LOAD_CONST              32 ('accept-encoding')
            100 LOAD_CONST              33 ('gzip, deflate, br')
            102 MAP_ADD                  1
            104 LOAD_CONST              34 ('0')
            106 LOAD_FAST                0 (phone)
            108 BINARY_ADD
            110 LOAD_CONST              35 ('add789229e0794d8508f948dacd710ae')
            112 LOAD_CONST              36 ('')
            114 LOAD_CONST              37 (1660806807513)
            116 LOAD_CONST              38 (2)
            118 LOAD_CONST              39 (('phoneNumber', 'secureHash', 'deviceId', 'sendTime', 'type'))
            120 BUILD_CONST_KEY_MAP      5
            122 LOAD_CONST              40 (('headers', 'json'))
            124 CALL_FUNCTION_KW         3
            126 LOAD_ATTR                2 (text)
            128 POP_TOP
            130 LOAD_CONST               0 (None)
            132 RETURN_VALUE

Disassembly of <code object cang2 at 0x00000206DD145450, file "<k>", line 142>:
142           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('https://api-stt.sieu-thi-tien.com/app/member/sendSmsCode')
              6 LOAD_CONST               2 ('api-stt.sieu-thi-tien.com')
              8 LOAD_CONST               3 ('647')
             10 LOAD_CONST               4 ('?1')
             12 LOAD_CONST               5 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             14 LOAD_CONST               6 ('"Linux"')
             16 LOAD_CONST               7 ('text/plain;charset=UTF-8')
             18 LOAD_CONST               8 ('*/*')
             20 LOAD_CONST               9 ('https://mobile.sieu-thi-tien.com')
             22 LOAD_CONST              10 ('same-site')
             24 LOAD_CONST              11 ('cors')
             26 LOAD_CONST              12 ('empty')
             28 LOAD_CONST              13 ('https://mobile.sieu-thi-tien.com/')
             30 LOAD_CONST              14 ('gzip, deflate, br')
             32 LOAD_CONST              15 (('Host', 'content-length', 'sec-ch-ua-mobile', 'user-agent', 'sec-ch-ua-platform', 'content-type', 'accept', 'origin', 'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-dest', 'referer', 'accept-encoding'))
             34 BUILD_CONST_KEY_MAP     13
             36 LOAD_CONST              16 ('android')
             38 LOAD_CONST              17 ('h5')
             40 LOAD_CONST              18 ('20220828184826gi3uzymdyykebl2pkbk3dq346byaross64ff772bfe5245cea03bef55055583dc6fef3615b2993ee522a337456bf66777jz6om7z25dngnqifi0yuqurxrr4nihx01')
             42 LOAD_CONST              19 ('8.1.0')
             44 LOAD_CONST              20 ('CPH1803')
             46 LOAD_CONST              21 ('OPPO')
             48 LOAD_CONST              22 ('null')
             50 LOAD_CONST              23 ('6')
             52 LOAD_CONST              24 ('2.0.0')
             54 LOAD_CONST              25 ('')
             56 LOAD_CONST              22 ('null')
             58 LOAD_CONST              22 ('null')
             60 LOAD_CONST              26 (('lon', 'lat'))
             62 BUILD_CONST_KEY_MAP      2
             64 LOAD_CONST              27 ('0000')
             66 LOAD_CONST              28 ('Sieu Thi Tien')
             68 LOAD_CONST              29 ('com.sieuthitiensaas.h5')
             70 LOAD_CONST              30 ('720,1520')
             72 LOAD_CONST              31 (('platformId', 'deviceType', 'deviceIdKh', 'termSysVersion', 'termModel', 'brand', 'termId', 'appType', 'appVersion', 'pValue', 'position', 'bizType', 'appName', 'packageName', 'screenResolution'))
             74 BUILD_CONST_KEY_MAP     15
             76 LOAD_CONST              17 ('h5')
             78 LOAD_CONST              25 ('')
             80 LOAD_CONST              25 ('')
             82 LOAD_CONST              32 ('1661683732495')
             84 LOAD_CONST              33 ('0')
             86 LOAD_FAST                0 (phone)
             88 BINARY_ADD
             90 LOAD_CONST              22 ('null')
             92 LOAD_CONST              34 (200)
             94 LOAD_CONST              35 ('sENV6')
             96 LOAD_CONST              36 (('phoneNum', 'code', 'type', 'channelCode'))
             98 BUILD_CONST_KEY_MAP      4
            100 LOAD_CONST              37 (('baseParams', 'clientTypeFlag', 'token', 'phoneNumber', 'timestamp', 'bizParams'))
            102 BUILD_CONST_KEY_MAP      6
            104 LOAD_CONST              38 (('headers', 'json'))
            106 CALL_FUNCTION_KW         3
            108 LOAD_ATTR                2 (text)
            110 POP_TOP
            112 LOAD_CONST               0 (None)
            114 RETURN_VALUE

Disassembly of <code object cang3 at 0x00000206DD1455B0, file "<k>", line 145>:
145           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('https://latte.lozi.vn/v1.2/auth/register/phone/initial')
              6 BUILD_MAP                0
              8 LOAD_CONST               2 ('Host')
             10 LOAD_CONST               3 ('latte.lozi.vn')
             12 MAP_ADD                  1
             14 LOAD_CONST               4 ('content-length')
             16 LOAD_CONST               5 ('101')
             18 MAP_ADD                  1
             20 LOAD_CONST               6 ('x-city-id')
             22 LOAD_CONST               7 ('50')
             24 MAP_ADD                  1
             26 LOAD_CONST               8 ('accept-language')
             28 LOAD_CONST               9 ('vi_VN')
             30 MAP_ADD                  1
             32 LOAD_CONST              10 ('sec-ch-ua-mobile')
             34 LOAD_CONST              11 ('?1')
             36 MAP_ADD                  1
             38 LOAD_CONST              12 ('user-agent')
             40 LOAD_CONST              13 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             42 MAP_ADD                  1
             44 LOAD_CONST              14 ('content-type')
             46 LOAD_CONST              15 ('application/json')
             48 MAP_ADD                  1
             50 LOAD_CONST              16 ('x-lozi-client')
             52 LOAD_CONST              17 ('1')
             54 MAP_ADD                  1
             56 LOAD_CONST              18 ('x-access-token')
             58 LOAD_CONST              19 ('unknown')
             60 MAP_ADD                  1
             62 LOAD_CONST              20 ('sec-ch-ua-platform')
             64 LOAD_CONST              21 ('"Android"')
             66 MAP_ADD                  1
             68 LOAD_CONST              22 ('accept')
             70 LOAD_CONST              23 ('*/*')
             72 MAP_ADD                  1
             74 LOAD_CONST              24 ('origin')
             76 LOAD_CONST              25 ('https://loship.vn')
             78 MAP_ADD                  1
             80 LOAD_CONST              26 ('sec-fetch-site')
             82 LOAD_CONST              27 ('cross-site')
             84 MAP_ADD                  1
             86 LOAD_CONST              28 ('sec-fetch-mode')
             88 LOAD_CONST              29 ('cors')
             90 MAP_ADD                  1
             92 LOAD_CONST              30 ('sec-fetch-dest')
             94 LOAD_CONST              31 ('empty')
             96 MAP_ADD                  1
             98 LOAD_CONST              32 ('referer')
            100 LOAD_CONST              33 ('https://loship.vn/')
            102 MAP_ADD                  1
            104 LOAD_CONST              34 ('accept-encoding')
            106 LOAD_CONST              35 ('gzip, deflate, br')
            108 MAP_ADD                  1
            110 LOAD_GLOBAL              2 (json)
            112 LOAD_METHOD              3 (dumps)
            114 LOAD_CONST              36 ('Android 8.1.0')
            116 LOAD_CONST              37 ('Chrome/104.0.0.0')
            118 LOAD_CONST              38 ('84')
            120 LOAD_FAST                0 (phone)
            122 LOAD_CONST              39 (('device', 'platform', 'countryCode', 'phoneNumber'))
            124 BUILD_CONST_KEY_MAP      4
            126 CALL_METHOD              1
            128 LOAD_CONST              40 (('headers', 'data'))
            130 CALL_FUNCTION_KW         3
            132 LOAD_ATTR                4 (text)
            134 POP_TOP
            136 LOAD_CONST               0 (None)
            138 RETURN_VALUE

Disassembly of <code object cang4 at 0x00000206DD145660, file "<k>", line 149>:
149           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('https://api.tamo.vn/web/public/client/phone/sms-code-ts')
              6 LOAD_CONST               2 ('api.tamo.vn')
              8 LOAD_CONST               3 ('39')
             10 LOAD_CONST               4 ('application/json, text/plain, */*')
             12 LOAD_CONST               5 ('application/json;charset=UTF-8')
             14 LOAD_CONST               6 ('?1')
             16 LOAD_CONST               7 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             18 LOAD_CONST               8 ('"Linux"')
             20 LOAD_CONST               9 ('https://www.tamo.vn')
             22 LOAD_CONST              10 ('same-site')
             24 LOAD_CONST              11 ('cors')
             26 LOAD_CONST              12 ('empty')
             28 LOAD_CONST              13 ('https://www.tamo.vn/')
             30 LOAD_CONST              14 ('gzip, deflate, br')
             32 LOAD_CONST              15 (('Host', 'content-length', 'accept', 'content-type', 'sec-ch-ua-mobile', 'user-agent', 'sec-ch-ua-platform', 'origin', 'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-dest', 'referer', 'accept-encoding'))
             34 BUILD_CONST_KEY_MAP     13
             36 LOAD_CONST              16 ('mobilePhone')
             38 LOAD_CONST              17 ('number')
             40 LOAD_CONST              18 ('0')
             42 LOAD_FAST                0 (phone)
             44 BINARY_ADD
             46 BUILD_MAP                1
             48 BUILD_MAP                1
             50 LOAD_CONST              19 (('headers', 'json'))
             52 CALL_FUNCTION_KW         3
             54 LOAD_ATTR                2 (text)
             56 POP_TOP
             58 LOAD_CONST               0 (None)
             60 RETURN_VALUE

Disassembly of <code object cang5 at 0x00000206DD145710, file "<k>", line 153>:
153           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('https://fptshop.com.vn/api-data/loyalty/Home/Verification')
              6 LOAD_CONST               2 ('phone')
              8 LOAD_CONST               3 ('84')
             10 LOAD_FAST                0 (phone)
             12 BINARY_ADD
             14 BUILD_MAP                1
             16 LOAD_CONST               4 (('data',))
             18 CALL_FUNCTION_KW         2
             20 LOAD_METHOD              2 (json)
             22 CALL_METHOD              0
             24 POP_TOP
             26 LOAD_CONST               0 (None)
             28 RETURN_VALUE

Disassembly of <code object cang6 at 0x00000206DD1457C0, file "<k>", line 156>:
156           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('https://foreignadmits.com/api/register-otp-generate-student')
              6 LOAD_FAST                0 (phone)
              8 LOAD_CONST               2 ('+84')
             10 LOAD_CONST               3 (('mobile', 'countryCode'))
             12 BUILD_CONST_KEY_MAP      2
             14 LOAD_CONST               4 (('data',))
             16 CALL_FUNCTION_KW         2
             18 LOAD_METHOD              2 (json)
             20 CALL_METHOD              0
             22 POP_TOP
             24 LOAD_CONST               0 (None)
             26 RETURN_VALUE

Disassembly of <code object cang7 at 0x00000206DD145920, file "<k>", line 159>:
159           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('https://apigateway.f88.vn/services/appvay/api/onlinelending/VerifyOTP/sendOTP')
              6 BUILD_MAP                0
              8 LOAD_CONST               2 ('Host')
             10 LOAD_CONST               3 ('apigateway.f88.vn')
             12 MAP_ADD                  1
             14 LOAD_CONST               4 ('content-length')
             16 LOAD_CONST               5 ('595')
             18 MAP_ADD                  1
             20 LOAD_CONST               6 ('content-encoding')
             22 LOAD_CONST               7 ('gzip')
             24 MAP_ADD                  1
             26 LOAD_CONST               8 ('traceparent')
             28 LOAD_CONST               9 ('00-c7d4ad181d561015110814044adf720e-d3fed9b4added2cf-01')
             30 MAP_ADD                  1
             32 LOAD_CONST              10 ('sec-ch-ua-mobile')
             34 LOAD_CONST              11 ('?1')
             36 MAP_ADD                  1
             38 LOAD_CONST              12 ('authorization')
             40 LOAD_CONST              13 ('Bearer null')
             42 MAP_ADD                  1
             44 LOAD_CONST              14 ('content-type')
             46 LOAD_CONST              15 ('application/json')
             48 MAP_ADD                  1
             50 LOAD_CONST              16 ('user-agent')
             52 LOAD_CONST              17 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             54 MAP_ADD                  1
             56 LOAD_CONST              18 ('sec-ch-ua-platform')
             58 LOAD_CONST              19 ('"Linux"')
             60 MAP_ADD                  1
             62 LOAD_CONST              20 ('accept')
             64 LOAD_CONST              21 ('*/*')
             66 MAP_ADD                  1
             68 LOAD_CONST              22 ('origin')
             70 LOAD_CONST              23 ('https://online.f88.vn')
             72 MAP_ADD                  1
             74 LOAD_CONST              24 ('sec-fetch-site')
             76 LOAD_CONST              25 ('same-site')
             78 MAP_ADD                  1
             80 LOAD_CONST              26 ('sec-fetch-mode')
             82 LOAD_CONST              27 ('cors')
             84 MAP_ADD                  1
             86 LOAD_CONST              28 ('sec-fetch-dest')
             88 LOAD_CONST              29 ('empty')
             90 MAP_ADD                  1
             92 LOAD_CONST              30 ('referer')
             94 LOAD_CONST              31 ('https://online.f88.vn/')
             96 MAP_ADD                  1
             98 LOAD_CONST              32 ('accept-encoding')
            100 LOAD_CONST              33 ('gzip, deflate, br')
            102 MAP_ADD                  1
            104 LOAD_CONST              34 ('0')
            106 LOAD_FAST                0 (phone)
            108 BINARY_ADD
            110 LOAD_CONST              35 ('03ANYolqvEe93MY94VJjkvDUIsq6ysACNy1tsnG1xnFq9YLY1gyez-_QvS0YEsxe9D0ddnuXKmlrbWqvT3KTQD2Bhx9yLeQ6M-nzUChGrqS08GEhHIdCpl3JLvHctZYeX18O8qZqcHY-e7qHq1WG7kkPbykyx9KwxMDnzW3j1N0KymuMti1Z0WAUgXHDh-ifJvI3n4lp5Tzsq5k1Nswugf0X3HFexHAm9GACImJIDG46QRucLBRm0df6jfazibClJyKlLXdvnqmrjCt6Wy22C_h-RY9Iilj5Lcy9rawUShIMJoCFX08UOWP_llCE4T5h5kuUk1llSgu9pdHMK2T6OuEROwXt2begTITv-9l534brGibKVlwwbxLtfHWohLRYQC-tjYWWq7avFLPOA9d53_72KLKoYAuKjvqKul683bQ7HtEzZ-eK3VCiBQj1Za1EV3R69e648tCkNkGXr9kpr1n0ccGeNbXSuB3GHQQGPnDIGuYgalvKa77_iX68OQ90PouP2GeT_RvBY3')
            112 LOAD_CONST              36 ('Online')
            114 LOAD_CONST              37 (('phoneNumber', 'recaptchaResponse', 'source'))
            116 BUILD_CONST_KEY_MAP      3
            118 LOAD_CONST              38 (('headers', 'json'))
            120 CALL_FUNCTION_KW         3
            122 LOAD_ATTR                2 (text)
            124 POP_TOP
            126 LOAD_CONST               0 (None)
            128 RETURN_VALUE

Disassembly of <code object cang8 at 0x00000206DD1459D0, file "<k>", line 162>:
162           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_METHOD              1 (get)
              4 LOAD_CONST               1 ('http://vanhihi.ml/sms2.php?sdt=0')
              6 LOAD_FAST                0 (phone)
              8 FORMAT_VALUE             0
             10 BUILD_STRING             2
             12 CALL_METHOD              1
             14 LOAD_ATTR                2 (text)
             16 POP_TOP
             18 LOAD_CONST               0 (None)
             20 RETURN_VALUE

Disassembly of <code object cang9 at 0x00000206DD145A80, file "<k>", line 167>:
167           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_METHOD              1 (get)
              4 LOAD_CONST               1 ('http://vanhihi.ml/sms3.php?sdt=0')
              6 LOAD_FAST                0 (phone)
              8 FORMAT_VALUE             0
             10 BUILD_STRING             2
             12 CALL_METHOD              1
             14 LOAD_ATTR                2 (text)
             16 POP_TOP
             18 LOAD_CONST               0 (None)
             20 RETURN_VALUE

Disassembly of <code object cang10 at 0x00000206DD145B30, file "<k>", line 170>:
170           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_METHOD              1 (get)
              4 LOAD_CONST               1 ('http://vanhihi.ml/sms4.php?sdt=0')
              6 LOAD_FAST                0 (phone)
              8 FORMAT_VALUE             0
             10 BUILD_STRING             2
             12 CALL_METHOD              1
             14 LOAD_ATTR                2 (text)
             16 POP_TOP
             18 LOAD_CONST               0 (None)
             20 RETURN_VALUE

Disassembly of <code object cang11 at 0x00000206DD145BE0, file "<k>", line 173>:
173           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_METHOD              1 (get)
              4 LOAD_CONST               1 ('http://vanhihi.ml/sms5.php?sdt=0')
              6 LOAD_FAST                0 (phone)
              8 FORMAT_VALUE             0
             10 BUILD_STRING             2
             12 CALL_METHOD              1
             14 LOAD_ATTR                2 (text)
             16 POP_TOP
             18 LOAD_CONST               0 (None)
             20 RETURN_VALUE

Disassembly of <code object cang12 at 0x00000206DD145C90, file "<k>", line 179>:
179           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_METHOD              1 (get)
              4 LOAD_CONST               1 ('http://vanhihi.ml/sms6.php?sdt=0')
              6 LOAD_FAST                0 (phone)
              8 FORMAT_VALUE             0
             10 BUILD_STRING             2
             12 CALL_METHOD              1
             14 LOAD_ATTR                2 (text)
             16 POP_TOP
             18 LOAD_CONST               0 (None)
             20 RETURN_VALUE

Disassembly of <code object cang13 at 0x00000206DD145DF0, file "<k>", line 183>:
183           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('https://www.instagram.com/accounts/account_recovery_send_ajax/')
              6 LOAD_CONST               2 ('email_or_username=0')
              8 LOAD_FAST                0 (phone)
             10 FORMAT_VALUE             0
             12 LOAD_CONST               3 ('&recaptcha_challenge_field=')
             14 BUILD_STRING             3
             16 LOAD_CONST               4 ('application/x-www-form-urlencoded')
             18 LOAD_CONST               5 ('XMLHttpRequest')
             20 LOAD_CONST               6 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
             22 LOAD_CONST               7 ('EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD')
             24 LOAD_CONST               8 (('Content-Type', 'X-Requested-With', 'User-Agent', 'x-csrftoken'))
             26 BUILD_CONST_KEY_MAP      4
             28 LOAD_CONST               9 (('data', 'headers'))
             30 CALL_FUNCTION_KW         3
             32 LOAD_ATTR                2 (json)
             34 POP_TOP
             36 LOAD_CONST               0 (None)
             38 RETURN_VALUE

Disassembly of <code object cang14 at 0x00000206DD145EA0, file "<k>", line 187>:
187           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_METHOD              1 (get)
              4 LOAD_CONST               1 ('https://tettrungthu.vn/get-otp?phone=')
              6 LOAD_FAST                0 (phone)
              8 FORMAT_VALUE             0
             10 LOAD_CONST               2 ('&utmstring=?utm_content=942119&utm_medium=Ni1uCKf1MAx2OJ1E8WOEKLm1uCBCX0WXiJzLloWIm1pcn0XZ&utm_source=accesstrade&aff_sid=Ni1uCKf1MAx2OJ1E8WOEKLm1uCBCX0WXiJzLloWIm1pcn0XZ&atnct1=b06f50d1f89bd8b2a0fb771c1a69c2b0&atnct2=Ni1uCKf1MAx2OJ1E8WOEKLm1uCBCX0WXiJzLloWIm1pcn0XZ&atnct3=WgRDa000c5q00k6xz')
             12 BUILD_STRING             3
             14 CALL_METHOD              1
             16 LOAD_ATTR                2 (text)
             18 POP_TOP
             20 LOAD_CONST               0 (None)
             22 RETURN_VALUE

Disassembly of <code object cang15 at 0x00000206DD148030, file "<k>", line 190>:
190           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('https://products.popsww.com/api/v5/auths/register')
              6 BUILD_MAP                0
              8 LOAD_CONST               2 ('Host')
             10 LOAD_CONST               3 ('products.popsww.com')
             12 MAP_ADD                  1
             14 LOAD_CONST               4 ('content-length')
             16 LOAD_CONST               5 ('89')
             18 MAP_ADD                  1
             20 LOAD_CONST               6 ('profileid')
             22 LOAD_CONST               7 ('62e58a27c6f857005396318f')
             24 MAP_ADD                  1
             26 LOAD_CONST               8 ('sec-ch-ua-mobile')
             28 LOAD_CONST               9 ('?1')
             30 MAP_ADD                  1
             32 LOAD_CONST              10 ('authorization')
             34 LOAD_CONST              11 ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InI1aTZqN3dUTERBS3hMV3lZcDdaM2ZnUUJKNWk3U2tmRkJHR2tNNUlCSlYycFdiRDNwbVd1MUM2eTQyVHJRaUIiLCJ1c2VySWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGUiLCJyb2xlcyI6WyJHVUVTVCJdLCJwcm9maWxlcyI6W3siaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGYiLCJhZ2UiOjEzLCJtcGFhIjp7ImlkIjoiNWQyM2UxMjU5NTI1MWI5OGJkMDQzMzc2IiwiYWdlIjoxM319LHsiaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOTAiLCJhZ2UiOjcsIm1wYWEiOnsiaWQiOiI1ZDIzZTFlMjk1MjUxYjk4YmQwNDM0MWQiLCJhZ2UiOjd9fV0sImlhdCI6MTY1OTIxMDI3OSwiZXhwIjoxOTc0NTcwMjc5fQ.3exZEvv0YG1Uw0UYx2Mt9Oj3NhRb8BX-l4tIAcVv9gw')
             36 MAP_ADD                  1
             38 LOAD_CONST              12 ('x-env')
             40 LOAD_CONST              13 ('production')
             42 MAP_ADD                  1
             44 LOAD_CONST              14 ('content-type')
             46 LOAD_CONST              15 ('application/json')
             48 MAP_ADD                  1
             50 LOAD_CONST              16 ('lang')
             52 LOAD_CONST              17 ('vi')
             54 MAP_ADD                  1
             56 LOAD_CONST              18 ('sub-api-version')
             58 LOAD_CONST              19 ('1.1')
             60 MAP_ADD                  1
             62 LOAD_CONST              20 ('user-agent')
             64 LOAD_CONST              21 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36')
             66 MAP_ADD                  1
             68 LOAD_CONST              22 ('api-key')
             70 LOAD_CONST              23 ('5d2300c2c69d24a09cf5b09b')
             72 MAP_ADD                  1
             74 LOAD_CONST              24 ('platform')
             76 LOAD_CONST              25 ('wap')
             78 MAP_ADD                  1
             80 LOAD_CONST              26 ('sec-ch-ua-platform')
             82 LOAD_CONST              27 ('"Linux"')
             84 MAP_ADD                  1
             86 LOAD_CONST              28 ('accept')
             88 LOAD_CONST              29 ('*/*')
             90 MAP_ADD                  1
             92 LOAD_CONST              30 ('origin')
             94 LOAD_CONST              31 ('https://pops.vn')
             96 MAP_ADD                  1
             98 LOAD_CONST              32 ('sec-fetch-site')
            100 LOAD_CONST              33 ('cross-site')
            102 MAP_ADD                  1
            104 LOAD_CONST              34 ('sec-fetch-mode')
            106 LOAD_CONST              35 ('cors')
            108 MAP_ADD                  1
            110 LOAD_CONST              36 ('empty')
            112 LOAD_CONST              37 ('https://pops.vn/auth/signin-signup/signup?isOffSelectProfile=true')
            114 LOAD_CONST              38 ('gzip, deflate, br')
            116 LOAD_CONST              39 (('sec-fetch-dest', 'referer', 'accept-encoding'))
            118 BUILD_CONST_KEY_MAP      3
            120 <165>                    1
            122 LOAD_GLOBAL              2 (json)
            124 LOAD_METHOD              3 (dumps)
            126 LOAD_CONST              40 ('')
            128 LOAD_CONST              41 ('0')
            130 LOAD_FAST                0 (phone)
            132 BINARY_ADD
            134 LOAD_CONST              42 ('Abcxaxgh')
            136 LOAD_CONST              42 ('Abcxaxgh')
            138 LOAD_CONST              43 (('fullName', 'account', 'password', 'confirmPassword'))
            140 BUILD_CONST_KEY_MAP      4
            142 CALL_METHOD              1
            144 LOAD_CONST              44 (('headers', 'data'))
            146 CALL_FUNCTION_KW         3
            148 LOAD_ATTR                4 (text)
            150 POP_TOP
            152 LOAD_CONST               0 (None)
            154 RETURN_VALUE

Disassembly of <code object cang16 at 0x00000206DD1480E0, file "<k>", line 194>:
194           0 LOAD_CONST               1 ('api.zalopay.vn')

196           2 LOAD_CONST               2 ('Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1')

197           4 LOAD_CONST               3 ('iPhone8,2')

198           6 LOAD_CONST               4 ('iphone3x')

199           8 LOAD_CONST               5 ('Bearer ')

200          10 LOAD_CONST               6 ('IOS')

201          12 LOAD_CONST               7 ('off')

202          14 LOAD_CONST               8 ('*/*')

203          16 LOAD_CONST               9 ('7.13.1')

204          18 LOAD_CONST              10 ('vi-VN;q=1.0, en-VN;q=0.9')

205          20 LOAD_CONST              11 ('ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2')

206          22 LOAD_CONST              12 ('NATIVE')

207          24 LOAD_CONST              13 ('14.6')

208          26 LOAD_CONST              14 (('Host', 'x-user-agent', 'x-device-model', 'x-density', 'authorization', 'x-device-os', 'x-drsite', 'accept', 'x-app-version', 'accept-language', 'user-agent', 'x-platform', 'x-os-version'))
             28 BUILD_CONST_KEY_MAP     13
             30 STORE_FAST               1 (headers)

195          32 LOAD_CONST              15 ('phone_number')
             34 LOAD_CONST              16 ('0')
             36 LOAD_FAST                0 (phone)
             38 BINARY_ADD

211          40 BUILD_MAP                1
             42 STORE_FAST               2 (params)

210          44 LOAD_GLOBAL              0 (requests)
             46 LOAD_ATTR                1 (get)
             48 LOAD_CONST              17 ('https://api.zalopay.vn/v2/account/phone/status')
             50 LOAD_FAST                2 (params)
             52 LOAD_FAST                1 (headers)
             54 LOAD_CONST              18 (('params', 'headers'))
             56 CALL_FUNCTION_KW         3
             58 LOAD_METHOD              2 (json)
             60 CALL_METHOD              0
             62 LOAD_CONST              19 ('data')
             64 BINARY_SUBSCR
             66 LOAD_CONST              20 ('send_otp_token')
             68 BINARY_SUBSCR
             70 STORE_FAST               3 (token)

214          72 LOAD_CONST              16 ('0')
             74 LOAD_FAST                0 (phone)
             76 BINARY_ADD

216          78 LOAD_FAST                3 (token)

217          80 LOAD_CONST              21 (('phone_number', 'send_otp_token'))
             82 BUILD_CONST_KEY_MAP      2
             84 STORE_FAST               4 (json_data)

215          86 LOAD_GLOBAL              0 (requests)
             88 LOAD_ATTR                3 (post)
             90 LOAD_CONST              22 ('https://api.zalopay.vn/v2/account/otp')
             92 LOAD_FAST                1 (headers)
             94 LOAD_FAST                4 (json_data)
             96 LOAD_CONST              23 (('headers', 'json'))
             98 CALL_FUNCTION_KW         3
            100 LOAD_ATTR                4 (text)
            102 STORE_FAST               5 (response)
            104 LOAD_CONST               0 (None)
            106 RETURN_VALUE

Disassembly of <code object cang17 at 0x00000206DD148190, file "<k>", line 224>:
224           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_ATTR                1 (post)
              4 LOAD_CONST               1 ('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone')
              6 LOAD_CONST               2 ('0')
              8 LOAD_FAST                0 (phone)
             10 FORMAT_VALUE             0
             12 BUILD_STRING             2
             14 LOAD_GLOBAL              2 (self)
             16 LOAD_METHOD              3 (random_string)
             18 LOAD_CONST               3 (40)
             20 CALL_METHOD              1
             22 LOAD_CONST               4 (('phone_number', 'hash'))
             24 BUILD_CONST_KEY_MAP      2
             26 LOAD_CONST               5 (('json',))
             28 CALL_FUNCTION_KW         2
             30 LOAD_METHOD              4 (json)
             32 CALL_METHOD              0
             34 LOAD_CONST               6 ('meta')
             36 BINARY_SUBSCR
             38 LOAD_CONST               7 ('msg')
             40 BINARY_SUBSCR
             42 STORE_FAST               1 (response)
             44 LOAD_CONST               0 (None)
             46 RETURN_VALUE

Disassembly of <code object CBot at 0x00000206DD148240, file "<k>", line 228>:
228           0 LOAD_GLOBAL              0 (range)
              2 LOAD_FAST                1 (amount)
        >>    4 CALL_FUNCTION            1
              6 GET_ITER
              8 FOR_ITER                 8 (to 18)
             10 STORE_FAST               2 (i)

229          12 LOAD_GLOBAL              1 (threading)
             14 LOAD_METHOD              2 (submit)
             16 LOAD_GLOBAL              3 (cang5)
        >>   18 LOAD_FAST                0 (phone)
             20 CALL_METHOD              2
             22 POP_TOP
             24 JUMP_ABSOLUTE            4

234          26 LOAD_CONST               0 (None)
             28 RETURN_VALUE

Disassembly of <code object DBot at 0x00000206DD1482F0, file "<k>", line 238>:
238           0 LOAD_GLOBAL              0 (range)
              2 LOAD_FAST                1 (amount)
        >>    4 CALL_FUNCTION            1
              6 GET_ITER
              8 FOR_ITER                28 (to 38)
             10 STORE_FAST               2 (i)

239          12 LOAD_GLOBAL              1 (threading)
             14 LOAD_METHOD              2 (submit)
             16 LOAD_GLOBAL              3 (cang01)
             18 LOAD_FAST                0 (phone)
             20 CALL_METHOD              2
             22 POP_TOP

245          24 LOAD_GLOBAL              4 (sleep)
             26 LOAD_CONST               1 (7)
             28 CALL_FUNCTION            1
             30 POP_TOP

246          32 LOAD_GLOBAL              1 (threading)
             34 LOAD_METHOD              2 (submit)
             36 LOAD_GLOBAL              5 (cang02)
        >>   38 LOAD_FAST                0 (phone)
             40 CALL_METHOD              2
             42 POP_TOP

247          44 LOAD_GLOBAL              4 (sleep)
             46 LOAD_CONST               1 (7)
             48 CALL_FUNCTION            1
             50 POP_TOP

248          52 LOAD_GLOBAL              1 (threading)
             54 LOAD_METHOD              2 (submit)
             56 LOAD_GLOBAL              6 (cang4)
             58 LOAD_FAST                0 (phone)
             60 CALL_METHOD              2
             62 POP_TOP
             64 JUMP_ABSOLUTE            4

249          66 LOAD_CONST               0 (None)
             68 RETURN_VALUE

Disassembly of <code object BBot at 0x00000206DD1483A0, file "<k>", line 262>:
262           0 LOAD_GLOBAL              0 (range)
              2 LOAD_FAST                1 (amount)
        >>    4 CALL_FUNCTION            1
              6 GET_ITER
              8 FOR_ITER               128 (to 138)
             10 STORE_FAST               2 (i)

263          12 LOAD_GLOBAL              1 (threading)
             14 LOAD_METHOD              2 (submit)
             16 LOAD_GLOBAL              3 (cang01)
             18 LOAD_FAST                0 (phone)
             20 CALL_METHOD              2
             22 POP_TOP

267          24 LOAD_GLOBAL              1 (threading)
             26 LOAD_METHOD              2 (submit)
             28 LOAD_GLOBAL              4 (cang02)
             30 LOAD_FAST                0 (phone)
             32 CALL_METHOD              2
             34 POP_TOP

268          36 LOAD_GLOBAL              1 (threading)
             38 LOAD_METHOD              2 (submit)
             40 LOAD_GLOBAL              5 (cang03)
             42 LOAD_FAST                0 (phone)
             44 CALL_METHOD              2
             46 POP_TOP

269          48 LOAD_GLOBAL              1 (threading)
             50 LOAD_METHOD              2 (submit)
             52 LOAD_GLOBAL              6 (cang1)
             54 LOAD_FAST                0 (phone)
             56 CALL_METHOD              2
             58 POP_TOP

270          60 LOAD_GLOBAL              1 (threading)
             62 LOAD_METHOD              2 (submit)
             64 LOAD_GLOBAL              7 (cang2)
             66 LOAD_FAST                0 (phone)
             68 CALL_METHOD              2
             70 POP_TOP

271          72 LOAD_GLOBAL              1 (threading)
             74 LOAD_METHOD              2 (submit)
             76 LOAD_GLOBAL              8 (cang3)
             78 LOAD_FAST                0 (phone)
             80 CALL_METHOD              2
             82 POP_TOP

272          84 LOAD_GLOBAL              1 (threading)
             86 LOAD_METHOD              2 (submit)
             88 LOAD_GLOBAL              8 (cang3)
             90 LOAD_FAST                0 (phone)
             92 CALL_METHOD              2
             94 POP_TOP

273          96 LOAD_GLOBAL              1 (threading)
             98 LOAD_METHOD              2 (submit)
            100 LOAD_GLOBAL              9 (cang4)
            102 LOAD_FAST                0 (phone)
            104 CALL_METHOD              2
            106 POP_TOP

274         108 LOAD_GLOBAL              1 (threading)
            110 LOAD_METHOD              2 (submit)
            112 LOAD_GLOBAL             10 (cang5)
            114 LOAD_FAST                0 (phone)
            116 CALL_METHOD              2
            118 POP_TOP

275         120 LOAD_GLOBAL              1 (threading)
            122 LOAD_METHOD              2 (submit)
            124 LOAD_GLOBAL             11 (cang6)
            126 LOAD_FAST                0 (phone)
            128 CALL_METHOD              2
            130 POP_TOP

276         132 LOAD_GLOBAL              1 (threading)
            134 LOAD_METHOD              2 (submit)
            136 LOAD_GLOBAL             12 (cang7)
        >>  138 LOAD_FAST                0 (phone)
            140 CALL_METHOD              2
            142 POP_TOP

277         144 LOAD_GLOBAL              1 (threading)
            146 LOAD_METHOD              2 (submit)
            148 LOAD_GLOBAL             13 (cang8)
            150 LOAD_FAST                0 (phone)
            152 CALL_METHOD              2
            154 POP_TOP

278         156 LOAD_GLOBAL              1 (threading)
            158 LOAD_METHOD              2 (submit)
            160 LOAD_GLOBAL             14 (cang9)
            162 LOAD_FAST                0 (phone)
            164 CALL_METHOD              2
            166 POP_TOP

279         168 LOAD_GLOBAL              1 (threading)
            170 LOAD_METHOD              2 (submit)
            172 LOAD_GLOBAL             15 (cang10)
            174 LOAD_FAST                0 (phone)
            176 CALL_METHOD              2
            178 POP_TOP

280         180 LOAD_GLOBAL              1 (threading)
            182 LOAD_METHOD              2 (submit)
            184 LOAD_GLOBAL             16 (cang11)
            186 LOAD_FAST                0 (phone)
            188 CALL_METHOD              2
            190 POP_TOP

281         192 LOAD_GLOBAL              1 (threading)
            194 LOAD_METHOD              2 (submit)
            196 LOAD_GLOBAL             17 (cang12)
            198 LOAD_FAST                0 (phone)
            200 CALL_METHOD              2
            202 POP_TOP

282         204 LOAD_GLOBAL              1 (threading)
            206 LOAD_METHOD              2 (submit)
            208 LOAD_GLOBAL             18 (cang13)
            210 LOAD_FAST                0 (phone)
            212 CALL_METHOD              2
            214 POP_TOP

283         216 LOAD_GLOBAL              1 (threading)
            218 LOAD_METHOD              2 (submit)
            220 LOAD_GLOBAL             19 (cang14)
            222 LOAD_FAST                0 (phone)
            224 CALL_METHOD              2
            226 POP_TOP

284         228 LOAD_GLOBAL              1 (threading)
            230 LOAD_METHOD              2 (submit)
            232 LOAD_GLOBAL             20 (cang15)
            234 LOAD_FAST                0 (phone)
            236 CALL_METHOD              2
            238 POP_TOP

285         240 LOAD_GLOBAL              1 (threading)
            242 LOAD_METHOD              2 (submit)
            244 LOAD_GLOBAL             21 (cang16)
            246 LOAD_FAST                0 (phone)
            248 CALL_METHOD              2
            250 POP_TOP

286         252 LOAD_GLOBAL              1 (threading)
            254 LOAD_METHOD              2 (submit)
            256 LOAD_GLOBAL             22 (cang17)
            258 LOAD_FAST                0 (phone)
            260 CALL_METHOD              2
            262 POP_TOP
            264 JUMP_ABSOLUTE            4

287         266 LOAD_CONST               0 (None)
            268 RETURN_VALUE

Disassembly of <code object on_connect at 0x00000206DD148450, file "<k>", line 300>:
300           0 <129>                    1

172           2 LOAD_GLOBAL              0 (os)
              4 LOAD_METHOD              1 (system)
              6 LOAD_CONST               1 ('clear')
              8 CALL_METHOD              1
             10 POP_TOP

175          12 LOAD_GLOBAL              2 (print)
             14 LOAD_CONST               2 ('Connecting Bot User : ')
             16 LOAD_GLOBAL              3 (bot)
             18 LOAD_ATTR                4 (user)
             20 FORMAT_VALUE             0
             22 BUILD_STRING             2
             24 CALL_FUNCTION            1
             26 POP_TOP

176          28 LOAD_GLOBAL              5 (time)
             30 LOAD_METHOD              6 (sleep)
             32 LOAD_CONST               3 (1.0)
             34 CALL_METHOD              1
             36 POP_TOP

177          38 LOAD_GLOBAL              2 (print)
             40 LOAD_CONST               4 ('Bot Is Online Now !!!')
             42 CALL_FUNCTION            1
             44 POP_TOP
             46 LOAD_CONST               0 (None)
             48 RETURN_VALUE

Disassembly of <code object fpt at 0x00000206DD148500, file "<k>", line 323>:
323           0 <129>                    1

195           2 LOAD_FAST                2 (amount)
              4 LOAD_CONST               1 (101)
              6 COMPARE_OP               0 (<)
              8 POP_JUMP_IF_FALSE      109

198          10 LOAD_GLOBAL              0 (discord)
             12 LOAD_ATTR                1 (Embed)
Traceback (most recent call last):
  File "dis_out.py", line 3, in <module>
    dis.dis(marshal.loads(decompile))
  File "C:\Users\KhanhNguyen9872\AppData\Local\Programs\Python\Python38\lib\dis.py", line 79, in dis
    _disassemble_recursive(x, file=file, depth=depth)
  File "C:\Users\KhanhNguyen9872\AppData\Local\Programs\Python\Python38\lib\dis.py", line 381, in _disassemble_recursive
    _disassemble_recursive(x, file=file, depth=depth)
  File "C:\Users\KhanhNguyen9872\AppData\Local\Programs\Python\Python38\lib\dis.py", line 373, in _disassemble_recursive
    disassemble(co, file=file)
  File "C:\Users\KhanhNguyen9872\AppData\Local\Programs\Python\Python38\lib\dis.py", line 369, in disassemble
    _disassemble_bytes(co.co_code, lasti, co.co_varnames, co.co_names,
  File "C:\Users\KhanhNguyen9872\AppData\Local\Programs\Python\Python38\lib\dis.py", line 410, in _disassemble_bytes
    print(instr._disassemble(lineno_width, is_current_instr, offset_width),
  File "C:\Users\KhanhNguyen9872\AppData\Local\Programs\Python\Python38\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f680' in position 45: character maps to <undefined>