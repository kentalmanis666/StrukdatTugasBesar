# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pajar")
define kr = Character("Ketir")
define i = Character("Ica")
define k = Character("Kipli")
define r = Character("Robby")


# The game starts here.

label start:

    $ love_ketir = 0
    $ love_ica = 0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene p2kk

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show pajar at left

    # These display lines of dialogue.

    p "wohooo akhir nya selesai juga acaranya"

    p "hai aku pajar yang tadi minta foto"

    show ketir at right
    hide pajar

    kr "oh. iya hai ada apa??"

    show pajar at left

    p "btw,kamu dari jurusan apa si??"


    show ketir at right
    kr "hukum jar, kalo kamu?"
    p "coba tebak hahaha *tertawa sedikit*"
    kr "hmmm apa yaa, mungkin HI"
    p "HI juga"
    kr "ihhh ngga gitu, hubungan internasional maksudnya *sedikit kesal*"
    p "aku dari jurusan informatika, btw boleh minta ignya? Punya ga?"
    kr "iyaa boleh, ini” *sembari membuka hp nya menunjukan ke pajar*"
    scene black
    "Singkat cerita kita banyak bercerita tentang satu sama lain dan aku memberanikan diri mengajaknya bertemu teman temanku di salah satu café  dekat kampus."
    scene cafe

    show pajar at right
    p "kenalin ni temen temenku tir"
    hide pajar
    show robby at left
    r "haloo aku robby"
    hide robby
    show kipli at left
    k "hai aku kipli biasa dipanggil kopler"
    hide kipli
    show ketir at right
    kr "haloo aku ketir salam kenal ya  *sambil menyalami teman teman pajar*"

    scene black
    "Selang beberapa waktu kami bercanda jam sudah merujuk pada pukul 09:00. ketir memberi kode dia ingin pulang karena sudah terlalu malam."

    menu:
        kr "pulang yukk,udah malem jugaa"

        "mengantar dan mampir membeli makanan":
            jump great
            $ ketir_love += 1
        "aku tidak ingin mengantarnya pulang":
            jump notgreat
            $ ketir_love -= 1
        "memesan gojek untuk ketir":
            jump notgreat1
            $ ketir_love -= 1
    label great:
        scene cafe
        show pajar at left
        p  "sebentar ya aku ke toilet dulu"
        show ketir at right
        kr  "iyaa jar"
        hide pajar
        hide ketir
        scene black
        "5 menit setelah pajar pergi ke toilet"
        scene cafe
        show pajar at right
        p "ayo tirr"
        show ketir at right
        kr "yukk"
        hide pajar
        hide ketir
        show pajar at right
        p "gimana kalo kita mampir beli makanan atau cemilan, aku tau ada beberapa yang enak di sekitar sini"
        show ketir at left
        kr "boleh, kamu gapapa kah?"
        p "ngga kok gapapa  sans waee hahaha"
        kr "okide  *tersenyum malu*"
        scene black
        "mereka memutus kan untuk membeli camilan.setelah mereka makan camilan tersebut,tidak terasa sudah sampai di depan kos ketir"
        scene jalan malam
        "........."
        jump end


    label notgreat:
        scene cafe
        show ketir at left
        kr "jar udah malem pulang yuk"
        show pajar at right
        p "ntar dulu ya lagian masih jam 9 kok blom terlalu malem"
        hide pajar
        kr "jam set 10 kos ku udah ditutup aku ngga bawa kunci"
        show pajar at right
        p "iyaa bentar aja, atau kamu pulang dulu juga gapapa, gaenak sama yang lain ditinggal pulang"
        kr "yaudah aku pulang dulu yaa"
        p "yaudah iya, hati hati yaa"
        jump next
    label notgreat1:
        scene cafe
        show ketir at left
        kr "jar udah malem pulang yuk"
        show pajar at right
        p "ntaran dulu tir masih jam 9 blom terlalu malem kok"
        kr "tapi jam set 10 gerbang kos ku udah tutup aku ngga bawa kunci"
        p "yaudah aku pesenin gojek ya ngga enak sama yang lain masa aku tinggal"
        kr "yaudah kalo gitu"
        hide ketir
        show pajar at left
        show robby at right
        r "bodo lu jar astagaa"
        hide robby
        show kipli at right
        k "kurang berpendidikan hahahah!"
        hide kipli
        jump next
    label end:
        scene rumah ketir
        kr "makasih ya jarr,tadi seru banget!"
        p "tenang,yaudah masuk sana gih, jan tidur kemaleman :)"
        kr "okee byebye*sambil melambaikan tangan nya*"

    label next:
        scene black
        "akhirnya sampe kamar aku pun tertidur pulas"
        "Keesokan harinya aku diajak teman temanku nongkrong, disitu juga aku bertemu dengan ica cewe basket yang di idamkan dijurusannya, Selain cantik dan baik dia juga salah satu pemain inti di kampus."
        scene cafe
        show robby at right
        r "nih jar kenalin temenku Namanya ica dia anak basket di kampus"
        hide robby
        show pajar at left
        p "haii aku pajar"
        show ica at right
        i "halo jar"

    menu:
            i "halo jar"

            "kamu suka makan katak gaa":
                jump great1
                $ ica_love += 2
            "gimana latihan basketnya":
                jump average
                $ ica_love += 1
label great1:
        scene cafe
        show pajar at left
        p "kamu suka makan katak ga?"
        show ica at right
        i "apa si jar hahahaha” *tertawa terbahak bahak*"
        p "gapapa si tanya aja biar ada yang bisa diobrolin hwhaha"
        i "kamu lucu juga ya ternyata anaknya ngga kaya yang diomongin sama robby & kipli"
        p "selain lucu aku juga rajin menabung kok"
        i "AHAHAHAHAHA!!!!!"
        jump next1

label average:
        scene cafe
        show pajar at left
        p "gimana Latihan baskenya ca"
        show ica at right
        i "ya gitu si, cape tapi seru juga"
        p "denger denger kemaren menang lawan anak ub ya"
        i "iyaa, tau dari mana?"
        p "kemaren aku nonton sama temenku kamu jago ya maen basketnya"
        i "oalah, iyaaa makasih ya"
        jump next1

label next1:
        scene black
        "pulang dari sana aku langsung menuju kos hendak untuk beristirahat. Tapi, setelah melihat hp ternyata ada pesan yang belum kubalas dari ketir, akhirnya aku menelfon dia untuk mengatahui bagaimana kabarnya hari ini."
        scene kamar pajar
        show pajar at left
        p "haloo tir"
        hide pajar
        scene kamar ketir
        kr "haloo jarr"
        hide ketir

menu:
        kr "haloo jar"
        "minta maaf karena lama membalas pesan":
            jump great2
            $ love_ketir += 2

        "memulai obrolan ringan":
            jump notgreat2
            $ love_ketir -= 1
label great2:
    scene kamar pajar
    show pajar at left
    p "sorry ya tir baru sempet ngabarin"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "iya gapapa jar"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "sibuk ga?"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "ngga juga si jar kenapa?"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "ngga ada tugas apa? Kok santai banget?"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "baru selesai ngerjain, kamu gimana ngga ada tugas?"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "ngga ada buat minggu ini tapi hari hari buat kamu selalu ada *jihahahahah*"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "hahahaha bisa aja, ih apasi dasar buaya"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "AHAHAHAHAHHA!!!!! "
    hide pajar
    jump next2
label notgreat2:
    scene kamar pajar
    show pajar at left
    p "maaf ya tir baru bisa ngabarin kamu"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "gapapa kok jar santaii aja"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "ngga enak aja si soalnya udah ngga bales lama"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "gapapa kok jar"
    hide ketir

    menu:
        kr "gapapa kok jar"
        "aku ajak makan dehhhh":
            jump great21
            $ love_ketir += 1

        "aku kerumah mu ya?":
            jump notgreat21
            $ love_ketir -= 1
label great21:
    scene kamar pajar
    show pajar at left
    p "aku traktir makan deh nanti"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "gausah jar ngerepotin nanti"
    hide ketir
    scene kamar pajar
    show pajar at right
    p "gapapa kok skalian ketemu sama kamu"
    hide pajar
    kr "yaudah kalo gitu"
    jump next2
label notgreat21:
    scene kamar pajar
    show pajar at left
    p "aku kerumahmu ya"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "ngapainnn???"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "mau ketemu kamu skalain ngajak keluar"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "ngga usah udah malem” *menolak keras*"
    scene kamar pajar
    show pajar at left
    p "yaudah kalo gitu,..."
    jump next2
label next2:
    scene black
    "Setelah mengobrol lama dengan ketir tiba tiba aku mendapat notif dari ica temen dari si robby & kipli. "
    menu:
        "Melanjutkan telfon dengan ketir":
            jump great22
            $ love_ketir += 1

        "Mematikan telfon tiara dan membalas chat ica":
            jump notgreat22
            $ love_ica += 1

label great22:
    scene kamar ketir
    kr "......."
    scene kamar pajar
    show pajar at left
    p "halo tir??"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "iya iyaaa halo kenapa"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "mau kunyanyiin gaa??"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "nyanyiin apa dulu nii ??"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "BALE BALE!"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "iri bilang boss hahayyy"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "BAL BALE BAL BALE BAL BALE BAL BALE BALEEEEEEEE!!!!"
    p "wkwkwkkwk,serius nih, ku nyanyiin lagu favoritku"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "boleh bolehh awas aja becanda mulu *ketawa dikit*"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "*bernyanyi*......"
    hide pajar
    scene black
    "*bla**bla* *bla* tidak terasa malam pun semakin larut"

    scene kamar pajar
    show pajar at left
    p "udah tidur sono udah malemm,sleepwell yaaa haha"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "iya iyaaa,kamu juga yooo dadaaa"
    hide ketir
    jump next3

label notgreat22:
    scene kamar pajar
    show pajar at left
    p "udah dulu yaa udah malem kamu istirahat,aku juga lagi capee "
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "yaudah iyaaa"
    hide ketir

    scene black
    "....................."

    scene kamar ica
    show ica at right
    i "hai jarr,ini nomerku icaa"
    hide ica
    scene kamar pajar
    show pajar at left
    p "haiii,dapet nomer ku dari manaa?"
    hide pajar
    scene kamar ica
    show ica at right
    i "tadi sebelum kamu pulang aku minta ke kipli hehee"
    hide ica
    scene kamar pajar
    show pajar at left
    p "ohhh, iya ada apaa caa?"
    hide pajar
    scene kamar ica
    show ica at right
    i "gapapasi haha, save nomer ku yaaaw"
    hide ica
    scene kamar pajar
    show pajar at left
    p "oke caaa"
    hide pajar
    jump next3

label next3:
    scene black
    "Keesokan harinya sepulang kelas aku secara tidak sengaja bertemu dengan ica saat sedang berjalan ke arah parkiran dia menyapa ku dengan sangatt kerass."

    scene koridor
    show ica at left
    i "PAJAAARRR!!! *berteriak sambil melambai*"

    menu:

        i "PAJAAARRR!!! *berteriak sambil melambai*"

        "hai dari mana ca??":
            jump next4
            $ love_ica += 1
        "*cuek*":
            jump next4
            $ love_ica += 1

label next4:
    scene koridor
    show pajar at left
    p "haii,dari mana ca??"
    show ica at right
    i "baru selese kelas sihhh"
    jump next5

label next5:
    scene koridor
    show pajar at left
    p "samaaan ni baru selesai kelas haha,udah makan belom?,makan yuk?"
    show ica at left
    i "bolehh dimana??"
    p "bu tatik lahh dimana lagii hahah"
    i "ayokkkk"

    scene black
    "saat sedang asyik makan berdua dengan ica tiba tiba ketir datang dari belakang sambil menepuk pundakku"

    scene bu tati
    show ketir at left
    kr "haii jarr"
    hide ketir

    menu:
        kr "haii jarr"

        "ajak nimbrung":
            jump next6
            $ love_ketir +=1
        "hanya menyapa":
            $ love_ica +=1
            jump notgreat3

label notgreat3:
    scene bu tati
    show pajar at left
    p "eh ketirrr,darimanaa?"
    show ketir at right
    kr "baru selesai kelass nii"
    p "yaudah sini gabungg"
label next6:
    scene bu tati
    show pajar at left
    p "eh ketirrr,darimana??"
    show ketir at right
    kr "boleh gabung  gaa?"
    p "bolehh sini gabungg"
    hide pajar
    show ica at left
    i "halooo,aku icaa *memperkenalkan diri*"
    kr "haiii,aku ketirr *memperkenalkan diri*"
    i "temennya pajar?"
    kr "iyaa temenn acara dulu di asrama"
    i "iyaa temennya jugaa,kenal pas liat pertandingan basket "

    menu:
        "mengganti topik pembicaraan":
            jump next7
        "memesan makanan":
            jump next8

label next7:
    show pajar at left
    p "kalian mau pesen apa?"
    show ketir at right
    kr "sama kaya kamu minumnya esteh yaa"
    hide ketir
    jump next8
label next8:
    scene bu tati
    show pajar at left
    show ica at right
    i "aku juga samain sama kamu tapi minumnya jeruk anget"
    p "oke2 bentar yaaa"

    p "tunggu ya antri agak lama"
    show ica at left
    i "gapapaa kok"
    hide ica
    show ketir at left
    kr "iyaa gapapa jar"
    show pajar at left
    p "abis ini ada kelas lagi ga??"
    show ketir at right
    kr "ada cuma nanti si jam 8"
    hide ketir
    show ica at right
    i "udah gaada jar"
    scene black
    "Setelah mengobrol agak lama,makanan kami pun akhirnya datang"
    scene bu tati
    show pajar at left
    p "makan dulu gihh"
    i "*makan*"
    kr "*makan*"
    scene bu tati
    "*nom**nom**nom**nom*....."
    show ketir at left
    kr "aku duluan ya bentar lagi kelas dimulaii,daaah!"
    hide ketir
    show pajar at left
    p "daaa ati2 yaa"
    show ica at right
    i "oke tirr"

    menu:

        "langsung pulang":
            $ love_ica += 1
            jump next9

        "mengajak ica keluar":
            $ love_ica += 2
            jump next10

label next9:
    scene bu tati
    show ica at right
    i "yaudah jar aku pulang dulu ya?"
    hide ica
    show pajar at left
    p "aku anterin pulang ya??"
    show ica at right
    i "bolehhh ayok"
    jump next11
label next10:
    scene bu tati
    show ica at right
    i "yaudah jar aku pulang dulu yaa"
    show pajar at left
    p "langsung pulang ni??ngga mau kemana dulu gitu?"
    i "ayokk, mau kemana emang?"
    p "kemana aja dah"
    i "bolehh tapi jangan malem2 ya pulangnyaa"
    p "oke caa santaii"
    jump next11

label next11:
    scene black
    "Setelah mengantar ica pulang aku langsung tertidur tanpa sadar ternyata mendapat pesan dari ketir meminta jemput sehabis kelas aku pun terbangun dan segera membalas pesan dari ketir"
    "keesokan harinya aku kembali diajak robby dan kipli seperti biasa kami berkumpul di salah satu café dekat kampus disitu aku mengajak ketir, disana kami tertawa pulas sampai tidak sadar sudah tengah malam. ketir pun meminta pulang disaat perjalanan pulang. "

    menu:
        "Menyatakan perasaan":
            $ love_ketir += 3
            jump great23

        "Mengantar pulang":
            $ love_ketir -= 20
            jump notgreat23

label great23:
    scene jalan malam

    show pajar at left
    p "eeehhh tirrr....."
    hide pajar
    show ketir at right
    kr "kenapa jarr?"
    hide ketir
    show pajar at left
    p "jadi kita kan udah lama kenal, aku Cuma mau ngomong kalo aku suka sama kamu"
    p "aku juga udah lama narok perasaan ke kamu, kamu mau ngga jadi pacarku?"
    show ketir at right
    kr "gimana gimana jar?"
    hide ketir
    show pajar at left
    p "yaaah gituu kamu mau ga?"
    hide pajar
    show ketir at right
    kr "kenapa nanya??"
    show pajar at left
    p "hah? iyaa? iya aapa dulu ni *berhenti secara tiba2* "
    kr "iya mauuu"
    if love_ketir > 2:
        call ending_ketir
        return
    elif love_ica > 2:
        call ending_ica
        return
    else:

        call alone_ending
        return
label notgreat23:
    scene jalan malam

    show pajar at left
    p "eeehhh tirrr....."
    hide pajar
    show ketir at right
    kr "kenapa jarr?"
    hide ketir
    show pajar at left
    p "jadi kita kan udah lama kenal, aku Cuma mau ngomong kalo aku suka sama kamu"
    p "aku juga udah lama narok perasaan ke kamu, kamu mau ngga jadi pacarku?"
    show ketir at right
    kr "gimana gimana jar?"
    hide ketir
    show pajar at left
    p "yaaah gituu kamu mau ga?"
    hide pajar
    show ketir at right
    kr "sorry jar, bukannya apa apa si kita kan Cuma temen ngga lebih lagian kita juga baru kenal beberapa minggu"
    show pajar at left
    p "...... *terdiam*"
    if love_ketir > 2:
        call ending_ketir
        return
    elif love_ica > 2:
        call ending_ica
        return
    else:

        call alone_ending
        return

label ending_ketir:
    scene black
    "aku sangat Bahagia karena telah berani menyatakan perasaan ku pada ketir dan dijawab dengan dia.
Aku Bahagia karena telah mendapat perempuan yang sangat mengerti aku."
"TAMAT"
return
label ending_ica:
    scene black
    "aku merasa sangat kecewa setelah menyatakan perasaanku pada ketir, karena sikapku yang terlalu menyepelekan semua kebaikan yang telah dia lakukan."
    "Keesokan harinya setelah mengantar ketir pulang aku melihat ica sedang Latihan basket, aku menunggu dia selesai latihan dan mencoba berbicara dengan dia."

    scene lapangan

    show pajar at left
    p "hai caa,cape banget kayanya :)"
    show ica at right
    i "ngga juga kok jar, kamu darimana emang?"
    p "hehehe, ini mau ada kelas cuma nanti si sekitar jam 11"
    i "oalah iyaiyaa, selesai jam berapa kelasnya?"
    p "sekitar jam 12 si kenapa"
    i "sama sii aku juga ada kelas jam 11 selesainya juga jam 12"

menu:
    "Mengajak pulang bersama":
        $ love_ketir += 1
        jump great24

    "Mengajak ica makan":
        $ love_ketir += 2
        jump notgreat24

label great24:
    scene lapangan
    show pajar at left
    p "ohhh,ntar pulang bareng yuk?"
    show ica at right
    i "gapapa emang?"
    scene black
    "Setelah kelas pun aku mengantarkan ica pulang"
    jump next12
label notgreat24:
    scene lapangan
    show pajar at left
    p "eeh,abis kelas ntar kosong ga??"
    show ica at right
    i "kosongg sii,kenapaa jarr??"
    p "makan yuk?,pasti cape kan abis latihan?,aku traktir dehh *hahaha*"
    i "bener nii?,hahaha,ayokkk"
    p "yaudah sampe ketemu nanti yoo"
    i "okeeee,dadaa"
    scene black
    "Setelah makan aku pun mengantar ica pulang"
    jump next12

label next12:
    scene black
    "Disaat tengah perjalanan pulang kami bercanda mentertawakan semua yang lewat"
    scene jalan pagi
    show pajar at left
    p "kamu suka makan komodo ga?"
    hide pajar
    show ica at right
    i "apaasi jar udah basi,hahahaha"
    hide ica
    menu:

            "to the point kepada ica":
                $ love_ica += 5
                jump great25

            "Ga ngomong ke ica ":
                $ love_ica += 0
                jump notgreat25

label great25:
    scene jalan pagi
    show pajar at left
    p "wkwk, bingung mau gimana ngomongnya ca"
    hide pajar
    show ica at right
    i "mau ngomng apa sii,santai kaliii haha"
    hide ica
    show pajar at left
    p "jadi gini ca, aku tau kita blom lama kenal cuman dari pertama kita ketemu aku udah suka sama kamu, jadi… kamu mau ngga jadi pacarku?"
    show ica at right
    i "hah? kok tiba2 banget*kaget*"
    p "aku ngerasa sekarang waktu yang tepat buat nyatain perasaan ku ke kamu"
    i "iyaa aku tau kita blom lama kenal, aku juga udah tau kamu gimana kok,jadii"
    p "jadi???"
    hide ica
    i "......."
    show ica at right
    i "iyaa mauu pajarr *tersenyum malu*"
    p "hahh?? *tersenyum senang*"
    if love_ica > 2:
        call ending_ica1
        return
    else:

        call alone_ending
        return
label notgreat25:
    scene rumah ica
    show ica at left
    i "makasii ya jarrr,byeee *melambaikan tangannya*"
    call alone_ending
    return
label ending_ica1:
    scene black
    "Setelah lama menyatakan perasaanku pada ica dan lama berpacaran dengan ica aku akhrinya tau bagaimana dia sebenarnya, dia memang cantik dan dia memang idaman cowo di angkatanku. Tapi aku tau, dia bukan yang terbaik untukku"
    "TAMAT"
label alone_ending:
    scene black
    "Akhirnya aku memutuskan untuk tidak mendekati siapapun, mungkin ini bukan cinta, ini hanya rasa penasaran yang muncul karena aku sudah menghabiskan hari hari ku dengan mereka."
    "Aku tak sedih aku pun tidak menyesal walaupun aku tidak mendapatkan salah satu dari mereka karena yang aku true love doesn’t exist.
THIS IS THE ENDING OF MY STORY BETWEEN YOU AND HER"
    "TAMAT"



    return
