inpt = '217523428149337669381721216749768791113624176532615223578558168936\
56462449168377359285244818489723869987861247912289729579296691684761143544956\
99158394221523656896187585175585497794614717874646467522769914992522722713755\
74797699485697888843993798211113825367226995757594744732739397563489927146679\
63596189765734743169489599125771443348193383566159843593541134749392569865481\
57835982584439445417321985791934934144214828222968954156116934162222235465139\
73429286784964786713393839237698564257952113236733897231819679339338327115458\
85653952861879231537976292517866354812943192728263269524735698423336673735158\
99385355614883386132795926225475664782773914528357779348152676815692113842831\
89393618597217785562645196434358718357448592431672278895627387129536511283176\
24673985213525897522378259178625416722152155728615936587369515254936828668564\
85728322643988126687194599879648847224918253888335418657392518315266386268399\
54496716632857753974538762627225674524359147773635228175947419466389865717936\
55889466419895996924122915777224499481496837343194149123735355268151941712871\
24586355383695334988783194978886985292914784948926532584393466999939184628631\
92686867893725139765222825875268661481663372159614935362628515122187941392723\
61292811529888161198799297966893366553115353639298256788819385272471187213579\
18552352134165111794767678534114623544141144181324251481322782184381942461997\
49798868716466219188652745745389517615678558456812723646461385847163335998438\
35167373525248547542442942583122624534494442516259616973235858469131159773167\
33495365867327159974894295698195469944452868962884869444681882546548512286974\
28397114711298626321286357796583657563628636271359836176133328497563719863769\
67117549251566281992964573929655589313871976556784849231916513831538254812347\
11625394981863352718517422156527977576674226268771311411434484353495883337263\
41821768663154415838871777592225988537351141918742777114346538548168415892299\
14164681364497429324463193669337827467661773833517841763711156376147664749175\
26721256232156772857576584489323271897147128984117164286894885213681866174123\
8178676857381583155547755219837116125995361896562498721571413742'

sum = 0
half = int(len(inpt) / 2)
inpt += inpt[0:half]
length = len(inpt)

for i in range(length-half):
    if inpt[i] == inpt[i+half]:
        sum += int(inpt[i])

print(sum)
