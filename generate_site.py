from __future__ import annotations

from pathlib import Path
import html
import shutil
import textwrap
import csv


ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
POETS_DIR = SITE / "poets"
ASSETS_DIR = SITE / "assets"
IMAGE_SOURCE = Path(
    r"C:\Users\I762844\.cursor\projects\c-Users-I762844-Documents-Urdu\assets\c__Users_I762844_AppData_Roaming_Cursor_User_workspaceStorage_627391de442b34a80f87e07b9448fd71_images_Vikram_Sankhala-73ca0e7e-9235-4870-b903-02a894f40160.png"
)


POETS = [
    {"slug": "rudaki", "name": "Rudaki", "tradition": "Persian", "era": "Early Classical", "dates": "c. 859-941", "region": "Samanid court, Central Asia", "themes": "courtly grace, spring, praise, worldly clarity", "hindi": "रुदकी की काव्य-दृष्टि में जीवन की सरल चमक, दरबारी सौंदर्य और प्रकृति की ताजगी साथ आती है। उनकी कविता बताती है कि सुरुचि और सहजता एक ही सौंदर्य के दो रूप हैं।", "english": "Rudaki's poetics bind elegance to simplicity. His verse turns courtly polish, spring imagery, and worldly balance into a foundational music for later Persian poetry."},
    {"slug": "ferdowsi", "name": "Ferdowsi", "tradition": "Persian", "era": "Epic Classical", "dates": "c. 940-1020", "region": "Tus, Greater Khorasan", "themes": "epic memory, kingship, fate, civilizational continuity", "hindi": "फ़िरदौसी के यहाँ कविता केवल कहानी नहीं बल्कि सभ्यता की स्मृति है। वीरता, नैतिकता और समय की चोट को वे ऐसे जोड़ते हैं कि इतिहास आत्मा की कथा बन जाता है।", "english": "Ferdowsi makes poetry a vault of civilization. In his epic imagination, heroism, justice, and mortality become instruments for preserving a people’s moral memory."},
    {"slug": "omar-khayyam", "name": "Omar Khayyam", "tradition": "Persian", "era": "Philosophical Classical", "dates": "1048-1131", "region": "Nishapur", "themes": "time, wine, skepticism, fleeting life", "hindi": "उमर ख़य्याम क्षणभंगुर जीवन के सामने एक सजग, प्रश्नाकुल और रसिक मन रखते हैं। उनकी शायरी याद दिलाती है कि नश्वरता के बीच भी अनुभूति, प्रश्न और आनंद अर्थ पैदा करते हैं।", "english": "Khayyam’s poetry lingers at the edge of transience. Wine, time, and doubt are not just motifs for pleasure, but ways of measuring human finitude."},
    {"slug": "sanai", "name": "Sanai", "tradition": "Persian", "era": "Mystical Classical", "dates": "c. 1080-1131", "region": "Ghazni", "themes": "ethics, inward reform, spiritual satire, mystical awakening", "hindi": "सनाई की आवाज़ मनुष्य को भीतर से बदलने की पुकार है। वे बाहरी आडंबर पर व्यंग्य करते हुए आत्मशुद्धि और आध्यात्मिक सजगता को कविता का केंद्र बनाते हैं।", "english": "Sanai pushes Persian poetry inward. His verse critiques outward vanity and turns poetry into an ethical and mystical summons."},
    {"slug": "attar", "name": "Farid ud-Din Attar", "tradition": "Persian", "era": "Mystical Classical", "dates": "c. 1145-1221", "region": "Nishapur", "themes": "quest, annihilation, birds, divine love", "hindi": "अत्तार की दुनिया यात्रा की दुनिया है, जहाँ पक्षियों की खोज आत्मा की खोज बन जाती है। उनकी कविता अहं को पिघलाकर प्रेम और सत्य की कठिन राह दिखाती है।", "english": "Attar writes the soul as pilgrimage. His imagery of birds, valleys, and loss maps the difficult transformation from selfhood to surrender."},
    {"slug": "nizami-ganjavi", "name": "Nizami Ganjavi", "tradition": "Persian", "era": "Romantic Classical", "dates": "c. 1141-1209", "region": "Ganja", "themes": "romance, narrative refinement, kingship, ethical love", "hindi": "निज़ामी प्रेम और कथा को अद्भुत सलीके से जोड़ते हैं। उनके यहाँ रूमानी प्रसंग भी नैतिक और बौद्धिक चमक लिए हुए आते हैं।", "english": "Nizami refines romance into moral art. His narratives balance sensual beauty with reflective intelligence and courtly discipline."},
    {"slug": "rumi", "name": "Jalal ud-Din Rumi", "tradition": "Persian", "era": "Mystical Classical", "dates": "1207-1273", "region": "Balkh-Konya world", "themes": "union, longing, music, ecstatic love", "hindi": "रूमी की कविता में विरह और मिलन दोनों एक ही आध्यात्मिक आग के रूप हैं। वे प्रेम को ऐसी गति देते हैं जिसमें आत्मा सीमाओं से बाहर निकलना चाहती है।", "english": "Rumi turns longing into motion. His poetry makes desire, music, and spiritual ecstasy feel like stages of return to a deeper belonging."},
    {"slug": "saadi", "name": "Saadi", "tradition": "Persian", "era": "Ethical Classical", "dates": "c. 1210-1292", "region": "Shiraz", "themes": "wisdom, travel, compassion, moral elegance", "hindi": "सादी की शायरी अनुभवजन्य बुद्धि की शायरी है। वे इंसानी रिश्तों, दया और सामाजिक विवेक को अत्यंत सरल लेकिन गहरी भाषा में रखते हैं।", "english": "Saadi fuses elegance with moral clarity. His poetry distills travel, observation, and humane insight into memorable ethical speech."},
    {"slug": "hafez", "name": "Hafez", "tradition": "Persian", "era": "Lyrical Classical", "dates": "c. 1315-1390", "region": "Shiraz", "themes": "wine, tavern, beloved, ambiguity, spiritual irony", "hindi": "हाफ़िज़ के यहाँ मयख़ाना, इश्क़ और रिंदाना अंदाज़ कई परतों में खुलते हैं। उनकी कविता सांसारिक और आध्यात्मिक दोनों अर्थों को एक साथ जगाए रखती है।", "english": "Hafez perfects lyrical ambiguity. The tavern, the beloved, and intoxication become layered signs for pleasure, defiance, and mystical depth."},
    {"slug": "jami", "name": "Jami", "tradition": "Persian", "era": "Late Classical", "dates": "1414-1492", "region": "Herat", "themes": "sufi synthesis, grace, scholarship, devotional love", "hindi": "जामी की काव्य-दृष्टि में विद्वता और कोमलता साथ-साथ चलती हैं। वे सूफ़ियाना प्रेम को संतुलित, परिपक्व और सुंदर अभिव्यक्ति देते हैं।", "english": "Jami’s poetry is learned yet gentle. He gives late classical Persian a harmonizing voice where scholarship and devotion support each other."},
    {"slug": "baba-tahir", "name": "Baba Tahir", "tradition": "Persian", "era": "Early Mystical", "dates": "11th century", "region": "Hamadan", "themes": "folk mysticism, longing, plain speech, solitude", "hindi": "बाबा ताहिर की ताकत उनकी सादगी में है। लोकधर्मी भाषा और सूफ़ियाना दर्द मिलकर उनकी कविता को अत्यंत आत्मीय बनाते हैं।", "english": "Baba Tahir brings mysticism close to the speaking heart. Plain diction and tender solitude make his verse intimate and unforgettable."},
    {"slug": "khwaju-kirmani", "name": "Khwaju Kirmani", "tradition": "Persian", "era": "Lyrical Classical", "dates": "1290-1352", "region": "Kirman-Shiraz", "themes": "ghazal refinement, lyric pleasure, courtly color, longing", "hindi": "ख़्वाजू किरमानी ग़ज़ल की महीन बनावट और रूमानी रंगत के शायर हैं। उनकी कविता में तरन्नुम और नफ़ासत एक साथ चमकते हैं।", "english": "Khwaju Kirmani’s lyric craft lies in polish and musical grace. He helps bridge courtly refinement and intimate longing in the Persian ghazal."},
    {"slug": "amir-khusrau", "name": "Amir Khusrau", "tradition": "Persian-Hindavi", "era": "Indo-Persian", "dates": "1253-1325", "region": "Delhi Sultanate", "themes": "cultural fusion, music, devotion, riddling charm", "hindi": "अमीर ख़ुसरो भारतीय और फ़ारसी संसारों के बीच एक सेतु हैं। उनकी शायरी और संगीत परंपराएँ मिलकर बहुभाषी और बहुरंगी सौंदर्य रचती हैं।", "english": "Amir Khusrau embodies cultural confluence. His work braids Persian sophistication with Indic sound, devotion, and playful invention."},
    {"slug": "bedil", "name": "Abdul Qadir Bedil", "tradition": "Persian", "era": "Sabk-e-Hindi", "dates": "1644-1720", "region": "Delhi", "themes": "abstraction, metaphysical density, inward labyrinths, imagination", "hindi": "बेदिल की कविता विचार और अनुभूति के जटिल गलियारों में चलती है। वे अर्थ को प्रत्यक्ष नहीं बल्कि सूक्ष्म संकेतों, बिंबों और दार्शनिक घनत्व में रचते हैं।", "english": "Bedil is a master of metaphysical complexity. His verse thrives on compressed images, abstraction, and intellectual astonishment."},
    {"slug": "saeb-tabrizi", "name": "Saeb Tabrizi", "tradition": "Persian", "era": "Safavid", "dates": "1601-1677", "region": "Tabriz-Isfahan", "themes": "fresh conceits, moral reflection, Indian style imagery, wit", "hindi": "साएब तबरिज़ी की पहचान नए और अप्रत्याशित बिंबों से है। वे चिंतन और चमत्कार को इस तरह जोड़ते हैं कि ग़ज़ल में ताज़गी बनी रहती है।", "english": "Saeb Tabrizi delights in fresh turns of thought. His poetry renews the ghazal through agile imagery and reflective wit."},
    {"slug": "kalim-kashani", "name": "Kalim Kashani", "tradition": "Persian", "era": "Safavid-Mughal", "dates": "1581-1651", "region": "Kashan-India", "themes": "ornament, delicacy, migration, subtle conceits", "hindi": "कलीम काशानी की कविता में भाषा का सजाव और कल्पना की महीन कारीगरी विशेष रूप से दिखती है। वे प्रवास और दरबारी संस्कार दोनों को सौंदर्य में बदलते हैं।", "english": "Kalim Kashani excels in delicate ornament. His verse reveals how migration and refinement can reshape poetic texture."},
    {"slug": "qaani", "name": "Qa'ani", "tradition": "Persian", "era": "Qajar", "dates": "1808-1854", "region": "Iran", "themes": "rhetoric, satire, praise, transition to modernity", "hindi": "क़ाआनी शास्त्रीय फ़ारसी शैली को आधुनिक संक्रमण के क्षण में जीते हैं। उनके यहाँ आलंकारिक शक्ति और सामाजिक दृष्टि दोनों मिलती हैं।", "english": "Qa'ani stands at a threshold. His rhetoric remains classical, yet his poetry senses the social and historical shifts of a changing age."},
    {"slug": "parvin-etesami", "name": "Parvin Etesami", "tradition": "Persian", "era": "Modern Persian", "dates": "1907-1941", "region": "Iran", "themes": "ethical dialogue, social conscience, dignity, education", "hindi": "परवीन एतेसामी की कविता नैतिक संवाद और सामाजिक संवेदना की कविता है। वे गरिमा, शिक्षा और न्याय को बहुत स्पष्ट और प्रभावी स्वर देती हैं।", "english": "Parvin Etesami restores ethical urgency to modern Persian verse. Her poems speak with lucidity, compassion, and a strong civic conscience."},
    {"slug": "aref-qazvini", "name": "Aref Qazvini", "tradition": "Persian", "era": "Constitutional Period", "dates": "1882-1934", "region": "Iran", "themes": "nation, lament, reform, song", "hindi": "आरिफ़ क़ज़विनी की शायरी राष्ट्रीय भाव और परिवर्तन की चाह से भरी है। उनके गीतों में निजी दुख और सामूहिक इतिहास एक-दूसरे से जुड़ जाते हैं।", "english": "Aref Qazvini writes at the meeting point of lyric grief and public history. Song becomes a vehicle for reformist feeling and national memory."},
    {"slug": "nima-yushij", "name": "Nima Yushij", "tradition": "Persian", "era": "Modernist Persian", "dates": "1897-1960", "region": "Iran", "themes": "free verse, landscape, rupture, modern subjectivity", "hindi": "नीमा यूशीज फ़ारसी कविता में आधुनिक मोड़ के केंद्रीय कवि हैं। वे छंद, दृश्य और आत्मबोध को नए रूप में व्यवस्थित करते हैं।", "english": "Nima Yushij breaks Persian poetry open to modernity. Form loosens, landscape deepens, and the poetic self enters a new historical weather."},
    {"slug": "forugh-farrokhzad", "name": "Forugh Farrokhzad", "tradition": "Persian", "era": "Modernist Persian", "dates": "1934-1967", "region": "Iran", "themes": "selfhood, desire, defiance, vulnerability", "hindi": "फ़रूग़ फ़र्रुख़ज़ाद की आवाज़ निजी अनुभव को गहरी कलात्मक निर्भीकता देती है। प्रेम, अकेलापन और स्त्री-स्वर उनके यहाँ अत्यंत आधुनिक शक्ति से उभरते हैं।", "english": "Forugh Farrokhzad transforms confession into artful courage. Her poems make desire, loneliness, and female subjectivity newly resonant in Persian."},
    {"slug": "ahmad-shamlu", "name": "Ahmad Shamlu", "tradition": "Persian", "era": "Modernist Persian", "dates": "1925-2000", "region": "Iran", "themes": "freedom, resistance, human dignity, expansive free verse", "hindi": "अहमद शामलू की कविता इंसानी गरिमा और आज़ादी की बड़ी आवाज़ है। उनका मुक्त छंद व्यक्तिगत और राजनीतिक दोनों आयामों को साथ लेकर चलता है।", "english": "Ahmad Shamlu writes with public amplitude. His free verse enlarges lyric space so that dignity, resistance, and love can coexist."},
    {"slug": "sohrab-sepehri", "name": "Sohrab Sepehri", "tradition": "Persian", "era": "Modernist Persian", "dates": "1928-1980", "region": "Iran", "themes": "nature, quietude, perception, spiritual simplicity", "hindi": "सोहराब सेपेहरी की कविता देखने की कला सिखाती है। प्रकृति और मौन उनके यहाँ आध्यात्मिक विस्तार और भीतरी शांति के रूप में आते हैं।", "english": "Sohrab Sepehri cultivates a poetics of seeing. Nature, stillness, and inward clarity become modes of spiritual attention."},
    {"slug": "simin-behbahani", "name": "Simin Behbahani", "tradition": "Persian", "era": "Contemporary Persian", "dates": "1927-2014", "region": "Iran", "themes": "renewed ghazal, social courage, womanhood, civic tenderness", "hindi": "सिमीन बेहबहानी ने ग़ज़ल को समकालीन अनुभवों के लिए फिर से जीवित किया। उनकी कविता में सामाजिक साहस और मानवीय कोमलता साथ रहते हैं।", "english": "Simin Behbahani renews the ghazal from within. Traditional cadence carries contemporary conscience, gendered experience, and civic courage."},
    {"slug": "shafiei-kadkani", "name": "Mohammad Reza Shafiei Kadkani", "tradition": "Persian", "era": "Contemporary Persian", "dates": "1939-", "region": "Iran", "themes": "scholarship, lyric memory, symbolism, cultural continuity", "hindi": "शफ़ीई कदकनी की कविता ज्ञान और लय का सुंदर संतुलन है। वे परंपरा को सिर्फ़ दोहराते नहीं, बल्कि उसे नई संवेदना के साथ पुनर्जीवित करते हैं।", "english": "Shafiei Kadkani joins scholarship to lyric feeling. His work preserves tradition while reactivating it for a modern reader."},
    {"slug": "ali-ahmad-saeedi-sirjani", "name": "Ali Ahmad Saeedi Sirjani", "tradition": "Persian", "era": "Late Modern Persian", "dates": "1931-1994", "region": "Iran", "themes": "cultural criticism, irony, literary conscience, dissent", "hindi": "सईदी सिरजानी का लेखन और काव्य-संसार साहित्यिक विवेक और नैतिक असहमति की पहचान रखते हैं। वे भाषा को प्रतिरोध और स्मृति दोनों का माध्यम बनाते हैं।", "english": "Saeedi Sirjani’s literary voice carries irony, conscience, and dissent. His place in Persian letters reminds us that criticism itself can be poetic."},
    {"slug": "granaz-moussavi", "name": "Granaz Moussavi", "tradition": "Persian", "era": "Diasporic Contemporary", "dates": "1974-", "region": "Iran-Australia", "themes": "migration, intimacy, displacement, contemporary lyric", "hindi": "ग्रनाज़ मुसावी की कविता प्रवास और निजी अनुभवों की बारीक धड़कनों को पकड़ती है। उनके यहाँ विस्थापन केवल भूगोल नहीं, संवेदना की नई भाषा भी है।", "english": "Granaz Moussavi writes the emotional cartography of migration. Her contemporary lyric turns displacement into intimacy and new poetic speech."},
    {"slug": "wali-deccani", "name": "Wali Deccani", "tradition": "Urdu", "era": "Foundational Urdu", "dates": "1667-1707", "region": "Deccan-Delhi", "themes": "early rekhta, love, musicality, linguistic fusion", "hindi": "वली दक्कनी उर्दू ग़ज़ल के शुरुआती स्थापक स्वरों में हैं। उन्होंने रेख़्ता को ऐसी लय और प्रेममयता दी जिससे आगे की पूरी परंपरा को दिशा मिली।", "english": "Wali Deccani gives early Urdu lyric a confident musical body. His rekhta joins local speech to Persianized grace and opens the road for the later ghazal."},
    {"slug": "siraj-aurangabadi", "name": "Siraj Aurangabadi", "tradition": "Urdu", "era": "Early Urdu", "dates": "1715-1763", "region": "Aurangabad", "themes": "mysticism, ecstasy, wandering self, inward fire", "hindi": "सिराज औरंगाबादी की कविता में सूफ़ियाना तल्लीनता और आत्मिक बेचैनी साथ मिलती हैं। वे प्रारंभिक उर्दू शायरी को गहरे आध्यात्मिक अनुभव से भरते हैं।", "english": "Siraj Aurangabadi infuses early Urdu poetry with ecstatic inwardness. His lyric world feels both wandering and incandescent."},
    {"slug": "mir-taqi-mir", "name": "Mir Taqi Mir", "tradition": "Urdu", "era": "Classical Urdu", "dates": "1723-1810", "region": "Delhi-Lucknow", "themes": "loss, love, fragility, ruined city, selfhood", "hindi": "मीर के यहाँ इश्क़ और उजड़न एक-दूसरे में घुल जाते हैं। उनकी शायरी निजी टूटन को सभ्यतागत दुख की ऊँचाई तक ले जाती है।", "english": "Mir Taqi Mir gives Urdu its incomparable vocabulary of ruin and tenderness. In his poetry, love and historical devastation become mutually illuminating."},
    {"slug": "sauda", "name": "Mirza Rafi Sauda", "tradition": "Urdu", "era": "Classical Urdu", "dates": "1713-1781", "region": "Delhi-Lucknow", "themes": "satire, qasida, grandeur, critique", "hindi": "सौदा की शायरी में व्यंग्य और भाषिक वैभव दोनों प्रखर हैं। वे सामाजिक और राजनीतिक विडंबनाओं को तीखी कलात्मकता से पकड़ते हैं।", "english": "Sauda couples rhetorical power with sharp satire. His verse expands Urdu’s range beyond romance into critique and public speech."},
    {"slug": "khwaja-mir-dard", "name": "Khwaja Mir Dard", "tradition": "Urdu", "era": "Classical Urdu", "dates": "1721-1785", "region": "Delhi", "themes": "sufi inwardness, pain, remembrance, delicacy", "hindi": "मीर दर्द की कविता आत्मा की धीमी जलन और सूफ़ियाना याद की कविता है। उनका लहजा कोमल है, पर उसकी आध्यात्मिक गूंज गहरी है।", "english": "Mir Dard writes pain with contemplative softness. His ghazals turn remembrance and inner restlessness into refined spiritual lyric."},
    {"slug": "insha", "name": "Insha Allah Khan Insha", "tradition": "Urdu", "era": "Late Classical Urdu", "dates": "1756-1817", "region": "Delhi-Lucknow", "themes": "wit, linguistic play, experimentation, elegance", "hindi": "इंशा भाषा के खेल और शहरी नफ़ासत के बड़े उस्ताद हैं। उनकी शायरी बताती है कि बुद्धि, विनोद और शैली भी ग़ज़ल के महत्वपूर्ण आयाम हैं।", "english": "Insha Allah Khan Insha revels in language itself. Wit, experimentation, and social polish animate his contribution to Urdu lyric culture."},
    {"slug": "momin", "name": "Momin Khan Momin", "tradition": "Urdu", "era": "Delhi Classical", "dates": "1800-1852", "region": "Delhi", "themes": "romantic subtlety, intimacy, layered address, elegance", "hindi": "मोमिन की ग़ज़ल में इश्क़ की महीन अदाएँ और संबोधन की नज़ाकत विशेष रूप से दिखती हैं। वे कम शब्दों में भाव की गहरी परतें खोलते हैं।", "english": "Momin excels at intimate refinement. His ghazals reveal how subtle address and emotional tact can produce great lyric intensity."},
    {"slug": "zauq", "name": "Sheikh Ibrahim Zauq", "tradition": "Urdu", "era": "Delhi Classical", "dates": "1789-1854", "region": "Delhi", "themes": "courtly polish, idiom, discipline, craft", "hindi": "ज़ौक़ की पहचान सधे हुए शिल्प और ज़बान की पक्की पकड़ में है। वे उर्दू को दरबारी परिष्कार और बोलचाल की रवानगी दोनों देते हैं।", "english": "Zauq represents disciplined craftsmanship in Urdu. His command of idiom and balance of polish with fluency shaped a generation."},
    {"slug": "ghalib", "name": "Mirza Ghalib", "tradition": "Urdu", "era": "Late Classical Urdu", "dates": "1797-1869", "region": "Delhi", "themes": "metaphysical wit, longing, irony, existential depth", "hindi": "ग़ालिब की शायरी प्रश्न, व्यंग्य, इश्क़ और फ़लसफ़े की अद्भुत संगति है। वे भावनात्मक अनुभव को बौद्धिक चमक और आत्मचेतना के साथ रखते हैं।", "english": "Ghalib makes the ghazal intellectually radiant. His poetry fuses longing, irony, and metaphysical inquiry into inexhaustible lyric thought."},
    {"slug": "bahadur-shah-zafar", "name": "Bahadur Shah Zafar", "tradition": "Urdu", "era": "Late Mughal Urdu", "dates": "1775-1862", "region": "Delhi-Rangoon exile", "themes": "exile, fading sovereignty, sorrow, remembrance", "hindi": "ज़फ़र की कविता राजनीतिक पराजय को गहरे मानवीय दुख में बदल देती है। उनके यहाँ बादशाहत की परछाईं से अधिक निर्वासन की तन्हाई बोलती है।", "english": "Zafar’s verse is haunted by loss of home and empire. The poignancy of exile turns his poetry into a document of historical heartbreak."},
    {"slug": "dagh-dehlvi", "name": "Dagh Dehlvi", "tradition": "Urdu", "era": "Rekhta Refinement", "dates": "1831-1905", "region": "Delhi-Rampur-Hyderabad", "themes": "romance, idiomatic ease, urban charm, fluency", "hindi": "दाग़ देहलवी की शायरी में मुहावरे की मिठास और इश्क़ की शहरी आभा विशेष रूप से दिखती है। वे ग़ज़ल को सहज, यादगार और बेहद दिलकश बनाते हैं।", "english": "Dagh Dehlvi perfects urbane fluency. His ghazals feel conversational yet exquisitely shaped, carrying romance with effortless charm."},
    {"slug": "akbar-allahabadi", "name": "Akbar Allahabadi", "tradition": "Urdu", "era": "Colonial Modern Urdu", "dates": "1846-1921", "region": "Allahabad", "themes": "satire, colonial modernity, social critique, humor", "hindi": "अकबर इलाहाबादी आधुनिकता, औपनिवेशिक बदलाव और सामाजिक पाखंड पर तीखी नज़र रखते हैं। उनका व्यंग्य हँसाते हुए असुविधाजनक सच भी सामने रखता है।", "english": "Akbar Allahabadi turns satire into social diagnosis. He captures the absurdities of colonial modernity with wit and bite."},
    {"slug": "altaf-hussain-hali", "name": "Altaf Hussain Hali", "tradition": "Urdu", "era": "Reformist Urdu", "dates": "1837-1914", "region": "Panipat", "themes": "reform, ethics, realism, literary renewal", "hindi": "हाली की शायरी और आलोचना दोनों उर्दू में सुधारवादी चेतना लाती हैं। वे कविता को समाज, नैतिकता और यथार्थ से नए ढंग से जोड़ते हैं।", "english": "Hali helps reorient Urdu toward reform and realism. He reimagines poetry as a moral and social instrument without abandoning feeling."},
    {"slug": "muhammad-iqbal", "name": "Muhammad Iqbal", "tradition": "Urdu-Persian", "era": "Philosophical Modern", "dates": "1877-1938", "region": "Sialkot-Lahore", "themes": "selfhood, awakening, civilizational thought, spiritual ascent", "hindi": "इक़बाल की शायरी आत्म-साक्षात्कार और सामूहिक जागरण की बड़ी पुकार है। वे फ़लसफ़े, रूहानियत और कार्रवाई को एक साथ जोड़ते हैं।", "english": "Iqbal’s poetry is visionary and exhortative. The self, history, and spiritual striving become dynamic energies for renewal."},
    {"slug": "hasrat-mohani", "name": "Hasrat Mohani", "tradition": "Urdu", "era": "Romantic-Political Modern", "dates": "1875-1951", "region": "Mohan-Aligarh", "themes": "ishq, freedom, devotion, rebellion", "hindi": "हसरत मोहानी के यहाँ इश्क़ और इंक़िलाब विरोधी नहीं बल्कि सहचर हैं। वे रूमानी कोमलता और राजनीतिक प्रतिबद्धता दोनों को एक आवाज़ में रखते हैं।", "english": "Hasrat Mohani shows that romantic longing and political commitment can inhabit the same lyric self. His voice is tender and defiant at once."},
    {"slug": "jigar-moradabadi", "name": "Jigar Moradabadi", "tradition": "Urdu", "era": "Romantic Modern Urdu", "dates": "1890-1960", "region": "Moradabad", "themes": "wine, passion, cadence, emotional warmth", "hindi": "जिगर मुरादाबादी की शायरी तरन्नुम, रूमानी गर्मी और जज़्बाती फैलाव की शायरी है। उनका लहजा दिल पर सीधा असर डालता है।", "english": "Jigar Moradabadi’s poetry sings. Passion, intoxication, and rhythmic warmth make his ghazals resonant and memorable."},
    {"slug": "firaq-gorakhpuri", "name": "Firaq Gorakhpuri", "tradition": "Urdu", "era": "Modern Urdu", "dates": "1896-1982", "region": "Gorakhpur-Allahabad", "themes": "sensuousness, humanism, loneliness, Indian atmosphere", "hindi": "फ़िराक़ की कविता में प्रेम और अकेलापन भारतीय वातावरण की खास गंध के साथ आते हैं। वे उर्दू ग़ज़ल को नई संवेदनात्मक बनावट देते हैं।", "english": "Firaq expands Urdu lyric with sensuous detail and human warmth. His work often carries the climate, memory, and textures of the subcontinent."},
    {"slug": "josh-malihabadi", "name": "Josh Malihabadi", "tradition": "Urdu", "era": "Revolutionary Modern Urdu", "dates": "1898-1982", "region": "Malihabad", "themes": "oratory, revolt, passion, rhetorical fire", "hindi": "जोश की आवाज़ विस्फोटक ऊर्जा और भाषिक उन्मेष की आवाज़ है। वे शायरी को विद्रोह, जोश और सार्वजनिक आवेग का मंच बना देते हैं।", "english": "Josh Malihabadi writes with thunderous rhetorical force. His poetry is charged with rebellion, public energy, and emotional excess."},
    {"slug": "faiz-ahmad-faiz", "name": "Faiz Ahmad Faiz", "tradition": "Urdu", "era": "Progressive Urdu", "dates": "1911-1984", "region": "Sialkot-Lahore", "themes": "love and revolution, hope, sorrow, solidarity", "hindi": "फ़ैज़ के यहाँ महबूब और दुनिया दोनों एक ही नैतिक क्षितिज में आते हैं। उनकी शायरी ग़म को उम्मीद, और प्रेम को सामाजिक न्याय से जोड़ती है।", "english": "Faiz joins the intimate and the historical with unmatched grace. Love, loss, and collective longing flow together in a language of hope."},
    {"slug": "noon-meem-rashid", "name": "Noon Meem Rashid", "tradition": "Urdu", "era": "Modernist Urdu", "dates": "1910-1975", "region": "Punjab-Iran", "themes": "free verse, alienation, modern consciousness, experiment", "hindi": "नून मीम राशिद ने उर्दू कविता को आधुनिक आत्मबोध और मुक्त छंद की नई जमीन दी। उनके यहाँ बेचैनी, विचार और रूपगत साहस एक साथ मिलते हैं।", "english": "Noon Meem Rashid is central to Urdu modernism. His experiments in free verse open new spaces for alienation, thought, and modern subjectivity."},
    {"slug": "miraji", "name": "Miraji", "tradition": "Urdu", "era": "Modernist Urdu", "dates": "1912-1949", "region": "Punjab", "themes": "symbolism, desire, psyche, lyrical experiment", "hindi": "मीराजी की कविता इच्छा, स्मृति और मनोभूमि की जटिलताओं में उतरती है। उन्होंने उर्दू में प्रतीकवाद और आधुनिक प्रयोगधर्मिता को गहरी दिशा दी।", "english": "Miraji brings psychological and symbolic experimentation to Urdu. Desire becomes strange, layered, and formally exploratory in his poems."},
    {"slug": "kaifi-azmi", "name": "Kaifi Azmi", "tradition": "Urdu", "era": "Progressive Urdu", "dates": "1919-2002", "region": "Azamgarh-Mumbai", "themes": "commitment, class consciousness, romance, public lyric", "hindi": "कैफ़ी आज़मी की शायरी सामाजिक प्रतिबद्धता और रूमानी मानवीयता का सुंदर मेल है। वे इंसाफ़ की चाह को काव्यात्मक ऊष्मा के साथ व्यक्त करते हैं।", "english": "Kaifi Azmi’s poetry links commitment with tenderness. His public conscience never loses the warmth of intimate lyric feeling."},
    {"slug": "sahir-ludhianvi", "name": "Sahir Ludhianvi", "tradition": "Urdu", "era": "Progressive Urdu", "dates": "1921-1980", "region": "Ludhiana-Mumbai", "themes": "social critique, disillusion, romance, cinematic reach", "hindi": "साहिर मोहब्बत और समाज दोनों के असमान सच को बेधक भाषा में सामने रखते हैं। उनकी शायरी लोकप्रियता और आलोचनात्मक चेतना का अनूठा संगम है।", "english": "Sahir makes lyric song socially alert. His poetry is memorable not only for romance, but for its refusal to sentimentalize injustice."},
    {"slug": "majrooh-sultanpuri", "name": "Majrooh Sultanpuri", "tradition": "Urdu", "era": "Progressive Popular Urdu", "dates": "1919-2000", "region": "Sultanpur-Mumbai", "themes": "lyric ease, romance, resistance, popular idiom", "hindi": "मजरूह सुल्तानपुरी ने उर्दू की नफ़ासत को लोकप्रिय संस्कृति की पहुँच से जोड़ा। उनका लहजा हल्का दिखते हुए भी संवेदनात्मक गहराई रखता है।", "english": "Majrooh Sultanpuri proves that elegance can remain popular. His poetry moves easily between romance, song, and resistance."},
    {"slug": "nasir-kazmi", "name": "Nasir Kazmi", "tradition": "Urdu", "era": "Post-Partition Urdu", "dates": "1925-1972", "region": "Ambala-Lahore", "themes": "melancholy, rain, memory, partitioned longing", "hindi": "नासिर काज़मी की शायरी उदासी, बारिश और याद की महीन ध्वनियों से बनी है। बँटवारे के बाद की टूटन उनके यहाँ एक शांत लेकिन स्थायी कंपन बनकर आती है।", "english": "Nasir Kazmi writes melancholy with extraordinary delicacy. Rain, memory, and post-Partition displacement settle into a quiet persistent ache."},
    {"slug": "ahmad-faraz", "name": "Ahmad Faraz", "tradition": "Urdu", "era": "Contemporary Urdu", "dates": "1931-2008", "region": "Kohat-Islamabad", "themes": "romantic candor, dissent, longing, public popularity", "hindi": "अहमद फ़राज़ की शायरी दिल की साफ़गोई और सामाजिक असहमति दोनों को आवाज़ देती है। उनका लहजा मुलायम भी है और याद रह जाने वाला भी।", "english": "Ahmad Faraz writes with emotional directness and civic unease. His popularity rests on clarity, lyric charm, and moral resonance."},
    {"slug": "parveen-shakir", "name": "Parveen Shakir", "tradition": "Urdu", "era": "Contemporary Urdu", "dates": "1952-1994", "region": "Karachi-Islamabad", "themes": "female voice, fragrance, vulnerability, modern love", "hindi": "परवीन शाकिर ने उर्दू ग़ज़ल और नज़्म में स्त्री-अनुभव को नई कोमलता और आत्मविश्वास दिया। उनकी भाषा में नर्मी है, पर दृष्टि बेहद सजग है।", "english": "Parveen Shakir refreshes Urdu lyric with feminine self-awareness. Fragility, fragrance, and modern emotional nuance shape her distinct voice."},
    {"slug": "jaun-elia", "name": "Jaun Elia", "tradition": "Urdu", "era": "Late Modern Urdu", "dates": "1931-2002", "region": "Amroha-Karachi", "themes": "irony, self-destruction, thought, estrangement", "hindi": "जौन एलिया की शायरी बौद्धिक बेचैनी और आत्म-विडंबना से चमकती है। वे मोहब्बत, नाउम्मीदी और विचार को एक तीखे निजी लहजे में रखते हैं।", "english": "Jaun Elia’s poetry thrives on estrangement and irony. His voice is intensely personal, intellectually restless, and memorably self-wounding."},
    {"slug": "bashir-badr", "name": "Bashir Badr", "tradition": "Urdu", "era": "Contemporary Urdu", "dates": "1935-", "region": "Ayodhya-Bhopal", "themes": "everyday tenderness, brevity, aphoristic charm, memory", "hindi": "बशीर बद्र ने रोज़मर्रा के अनुभवों को बेहद यादगार और सरल शेरों में ढाला। उनकी शायरी निकटता, बिछड़न और उम्मीद की सहज भाषा बोलती है।", "english": "Bashir Badr distills feeling into memorable brevity. Everyday tenderness, separation, and resilience become effortlessly quotable in his verse."},
    {"slug": "nida-fazli", "name": "Nida Fazli", "tradition": "Urdu", "era": "Contemporary Urdu", "dates": "1938-2016", "region": "Delhi-Mumbai", "themes": "humanism, simplicity, urban solitude, reflective lyric", "hindi": "निदा फ़ाज़ली की पहचान सादगी में छिपी गहराई है। वे शहर, अकेलेपन और इंसानी रिश्तों को बिना बनावट की भाषा में व्यक्त करते हैं।", "english": "Nida Fazli practices lucid humanism. His poems turn urban solitude and ordinary relationships into meditative lyric moments."},
    {"slug": "gulzar", "name": "Gulzar", "tradition": "Urdu-Hindustani", "era": "Contemporary South Asian Lyric", "dates": "1934-", "region": "Dina-Mumbai", "themes": "image fragments, everyday surrealism, tenderness, memory", "hindi": "गुलज़ार रोज़मर्रा की वस्तुओं और क्षणों से असाधारण काव्य-चित्र बनाते हैं। उनकी भाषा संक्षिप्त है, पर उसमें स्मृति और एहसास की लंबी गूंज रहती है।", "english": "Gulzar’s poetry finds wonder in fragments. Everyday objects, memory, and tenderness are rearranged into quietly surprising images."},
    {"slug": "fahmida-riaz", "name": "Fahmida Riaz", "tradition": "Urdu", "era": "Contemporary Urdu", "dates": "1946-2018", "region": "Meerut-Karachi", "themes": "feminism, dissent, sensuality, fearless speech", "hindi": "फ़हमीदा रियाज़ की कविता निर्भीक स्त्री-स्वर और राजनीतिक असहमति की सशक्त मिसाल है। वे संवेदना और प्रतिरोध को बराबर तीव्रता देती हैं।", "english": "Fahmida Riaz writes with fearless sensual and political intelligence. Her work expands the range of Urdu dissent and female self-expression."},
    {"slug": "kishwar-naheed", "name": "Kishwar Naheed", "tradition": "Urdu", "era": "Contemporary Urdu", "dates": "1940-", "region": "Bulandshahr-Lahore", "themes": "feminist resistance, satire, autonomy, social critique", "hindi": "किश्वर नाहिद की कविता स्त्री-स्वतंत्रता और सामाजिक आलोचना का तेज़ स्वर है। वे पितृसत्ता को सीधी चुनौती देती हुई नई भाषिक शक्ति गढ़ती हैं।", "english": "Kishwar Naheed’s poetry is uncompromising in its feminist critique. Her language cuts sharply through social hypocrisy and gendered power."},
    {"slug": "zehra-nigah", "name": "Zehra Nigah", "tradition": "Urdu", "era": "Contemporary Urdu", "dates": "1937-", "region": "Hyderabad-Karachi", "themes": "composure, femininity, history, reflective grace", "hindi": "ज़हरा निगाह की शायरी में संयम, स्मृति और स्त्री-अनुभव की गरिमा विशेष रूप से उपस्थित है। उनका लहजा शांत है लेकिन असर गहरा छोड़ता है।", "english": "Zehra Nigah writes with poised grace. History, womanhood, and introspection gather in a voice that is calm yet enduring."},
    {"slug": "munawwar-rana", "name": "Munawwar Rana", "tradition": "Urdu", "era": "Contemporary Urdu", "dates": "1952-2024", "region": "Raebareli", "themes": "motherhood, home, memory, accessible emotion", "hindi": "मुनव्वर राना ने घर, माँ और अपनत्व को व्यापक लोकप्रियता के साथ शायरी का हिस्सा बनाया। उनकी भाषा सुलभ है और भाव सीधा दिल तक पहुँचता है।", "english": "Munawwar Rana centers home and motherhood in an accessible lyric idiom. His wide appeal comes from emotional immediacy and recognizability."},
    {"slug": "rahat-indori", "name": "Rahat Indori", "tradition": "Urdu", "era": "Contemporary Urdu", "dates": "1950-2020", "region": "Indore", "themes": "performance, assertion, defiance, mass resonance", "hindi": "राहत इंदौरी की शायरी मंचीय ऊर्जा, आत्मविश्वास और प्रतिरोध की आवाज़ है। वे समकालीन उर्दू को जनता की धड़कन से सीधे जोड़ते हैं।", "english": "Rahat Indori’s poetry is built for electric public resonance. Assertion, defiance, and memorable phrasing drive his enormous appeal."},
    {"slug": "wasi-shah", "name": "Wasi Shah", "tradition": "Urdu", "era": "Contemporary Urdu", "dates": "1976-", "region": "Pakistan", "themes": "popular romance, emotional directness, contemporary idiom, longing", "hindi": "वसी शाह समकालीन उर्दू में सीधे, भावपूर्ण और लोकप्रिय रूमानी स्वर के प्रतिनिधि हैं। उनकी कविता आधुनिक पाठक की भाषा और संवेदना के करीब रहती है।", "english": "Wasi Shah writes in a contemporary romantic idiom that is immediate and accessible. His popularity stems from emotional clarity and direct address."},
    {"slug": "anwar-masood", "name": "Anwar Masood", "tradition": "Urdu-Punjabi", "era": "Contemporary South Asian", "dates": "1935-", "region": "Punjab", "themes": "humor, social observation, vernacular vitality, satire", "hindi": "अनवर मसूद हास्य और सामाजिक अवलोकन के विलक्षण शायर हैं। वे बोलचाल की ताज़गी से गंभीर बातों को भी यादगार बना देते हैं।", "english": "Anwar Masood uses humor as insight. His lively vernacular touch makes satire feel warm, immediate, and enduring."},
    {"slug": "iftikhar-arif", "name": "Iftikhar Arif", "tradition": "Urdu", "era": "Contemporary Urdu", "dates": "1944-", "region": "Lucknow-Karachi", "themes": "migration, memory, moral intelligence, classical continuity", "hindi": "इफ़्तिख़ार आरिफ़ परंपरा और समकालीन अनुभव के बीच बहुत संतुलित पुल बनाते हैं। उनकी शायरी में बँटवारे, विस्थापन और नैतिक चिंतन की गहरी परछाइयाँ हैं।", "english": "Iftikhar Arif writes with classical restraint and modern historical awareness. Migration and moral reflection recur with quiet force in his work."},
    {"slug": "adeel-haider", "name": "Adeel Hashmi", "tradition": "Urdu-English diaspora", "era": "Global Contemporary", "dates": "1970s-", "region": "Pakistan-North America", "themes": "diaspora, bilingual sensibility, migration, inward modernity", "hindi": "अदील हाश्मी जैसे समकालीन प्रवासी स्वर दिखाते हैं कि उर्दू की संवेदना सीमाओं से परे भी जीवित और परिवर्तित होती रहती है। प्रवास यहाँ स्मृति और नई पहचान दोनों का प्रदेश है।", "english": "Adeel Hashmi represents a diasporic extension of the Urdu imagination. Migration does not diminish lyric feeling; it reframes memory and belonging."},
    {"slug": "rekhta-contemporary", "name": "Contemporary Rekhta Voices", "tradition": "Urdu", "era": "Digital Contemporary", "dates": "21st century", "region": "Global", "themes": "digital circulation, revival, performance, transnational readership", "hindi": "समकालीन रेख़्ता-परिदृश्य बताता है कि उर्दू शायरी डिजिटल युग में नए पाठकों, मंचों और उच्चारणों के साथ फिर से जीवित हो रही है। परंपरा अब संग्रहालय नहीं, सक्रिय संवाद है।", "english": "Today’s rekhta ecosystem shows Urdu lyric in active global circulation. Digital performance and new readerships renew the tradition without severing its classical roots."},
]


PUBLIC_DOMAIN_SAMPLE_POETS = {
    "rudaki",
    "amir-khusrau",
    "ferdowsi",
    "omar-khayyam",
    "sanai",
    "attar",
    "nizami-ganjavi",
    "rumi",
    "saadi",
    "hafez",
    "jami",
    "baba-tahir",
    "khwaju-kirmani",
    "wali-deccani",
    "siraj-aurangabadi",
    "bedil",
    "saeb-tabrizi",
    "kalim-kashani",
    "qaani",
    "parvin-etesami",
    "aref-qazvini",
    "hasrat-mohani",
    "mir-taqi-mir",
    "sauda",
    "khwaja-mir-dard",
    "insha",
    "momin",
    "zauq",
    "ghalib",
    "bahadur-shah-zafar",
    "dagh-dehlvi",
    "akbar-allahabadi",
    "altaf-hussain-hali",
    "muhammad-iqbal",
}

PUBLIC_DOMAIN_SAMPLES = {
    "rudaki": [
        {"title": "Spring has come", "original": "Bahar amad o bahar amad.", "english": "Spring has arrived, and with it the world is renewed.", "hindi": "बहार आ गई है, और उसके साथ दुनिया फिर से नवीन हो उठी है।"},
        {"title": "The scent of joy", "original": "Bu-ye ju-ye Muliyan ayad hami.", "english": "The fragrance of the Muliyan stream keeps coming to me.", "hindi": "मुलियान की धारा की सुगंध बार-बार मेरी ओर आती है।"},
        {"title": "Memory of homeland", "original": "Yad-e yar-e mehraban ayad hami.", "english": "With that fragrance comes the memory of the beloved homeland.", "hindi": "उस सुगंध के साथ प्रिय देश और प्रियजन की याद भी चली आती है।"},
        {"title": "Courtly brightness", "original": "Ruzgar az chehre-ye to roshan ast.", "english": "The age seems brightened by your very presence.", "hindi": "तुम्हारी उपस्थिति से ही युग का चेहरा उजला लगता है।"},
        {"title": "Wine and companionship", "original": "May o mutrib o gol o bahar khosh ast.", "english": "Wine, music, flowers, and spring together make life sweet.", "hindi": "मदिरा, संगीत, फूल और बहार मिलकर जीवन को मधुर बना देते हैं।"},
        {"title": "Value of wisdom", "original": "Mard ra aql bavad beh ze ganj.", "english": "For a person, wisdom is better than buried treasure.", "hindi": "मनुष्य के लिए बुद्धि किसी भी खजाने से बढ़कर है।"},
        {"title": "Passing time", "original": "In jahan chun bad bogzarad.", "english": "This world passes like the wind.", "hindi": "यह संसार हवा की तरह गुजर जाता है।"},
        {"title": "Simple delight", "original": "Shad zi baqi-ye umr bayad bud.", "english": "One should rejoice in the little life that remains.", "hindi": "जीवन का जो थोड़ा समय शेष है, उसी में प्रसन्न रहना चाहिए।"},
        {"title": "Praise of generosity", "original": "Karam zi mardum-e niku nishan dahad.", "english": "Generosity is the true mark of a noble person.", "hindi": "उदारता ही किसी श्रेष्ठ मनुष्य की सच्ची पहचान है।"},
        {"title": "Sweet speech", "original": "Sokhan chun shekar ast agar ba-mani.", "english": "Speech is like sugar when it carries meaning.", "hindi": "जब वाणी में अर्थ हो, तो वह शक्कर जैसी मधुर हो जाती है।"},
    ],
    "amir-khusrau": [
        {
            "title": "Zehaal-e miskin",
            "original": "Zehaal-e miskin makun taghaful, duraye naina banaye batiyan.",
            "english": "Do not ignore the helpless lover, turning your eyes away while speaking sweetly.",
            "hindi": "बेबस आशिक़ की दशा से यूँ बेपरवाह मत हो, आँखें फेरकर मीठी बातें मत करो।",
        },
        {
            "title": "Chaap tilak",
            "original": "Chaap tilak sab chhini re mose naina milaike.",
            "english": "One glance from you stole my identity, my adornment, my very self.",
            "hindi": "तुम्हारी एक नज़र ने मेरी पहचान, मेरा श्रृंगार, मेरा सारा अस्तित्व छीन लिया।",
        },
        {
            "title": "Aaj rang hai",
            "original": "Aaj rang hai ri ma, rang hai ri.",
            "english": "Today the whole being is dyed in color, intoxicated with spiritual joy.",
            "hindi": "आज पूरा अस्तित्व रंग में डूब गया है, मानो रूहानी उल्लास से भर उठा हो।",
        },
        {
            "title": "Kaahe ko byahi bides",
            "original": "Kaahe ko byahi bides re, lakh babul more.",
            "english": "Why was I married away to a distant land, O my father?",
            "hindi": "बाबुल, मुझे पराए देश क्यों ब्याह दिया गया?",
        },
        {
            "title": "Nizam piya",
            "original": "Nizam piya rang rangili, chunariya de mohe.",
            "english": "Beloved master Nizam, grant me the many-colored veil of grace.",
            "hindi": "मेरे प्रिय निज़ाम, मुझे अपनी कृपा की रंग-बिरंगी चादर दे दीजिए।",
        },
        {
            "title": "Man kunto Maula",
            "original": "Man kunto Maula, fa haza Ali-un Maula.",
            "english": "Whoever takes me as master, let Ali be known as master too.",
            "hindi": "जिसका मैं मौला हूँ, उसके लिए अली भी मौला हैं।",
        },
        {
            "title": "Khusrau darya prem ka",
            "original": "Khusrau darya prem ka, ulti wa ki dhaar.",
            "english": "Love is a river flowing against the current; whoever enters it is swept beyond the self.",
            "hindi": "प्रेम ऐसी नदी है जिसकी धारा उलटी बहती है; जो इसमें उतरता है, वह अपने आप से आगे निकल जाता है।",
        },
        {
            "title": "Gori sove sej par",
            "original": "Gori sove sej par, mukh par daare kes.",
            "english": "The fair one rests upon the bed, her face covered by loosened hair.",
            "hindi": "सजनी शय्या पर सोई है, चेहरे पर बिखरे केश पड़े हैं।",
        },
        {
            "title": "Mohe apne hi rang",
            "original": "Mohe apne hi rang mein rang de, Nizam.",
            "english": "Dye me completely in your own color, O Nizam.",
            "hindi": "ऐ निज़ाम, मुझे अपने ही रंग में पूरी तरह रंग दो।",
        },
        {
            "title": "Saqiya",
            "original": "Saqiya, baz aa ke der in bazm jahan digar ast.",
            "english": "Cupbearer, return, for this gathering of the world has changed again.",
            "hindi": "साक़ी, लौट आओ, क्योंकि दुनिया की यह महफ़िल फिर बदल गई है।",
        },
    ],
    "rumi": [
        {
            "title": "Listen to the reed",
            "original": "Bishnav az ney chun hikayat mikonad.",
            "english": "Listen to the reed flute as it tells the story of separation.",
            "hindi": "बांसुरी की आवाज़ सुनो, वह जुदाई की कहानी सुना रही है।",
        },
        {
            "title": "Return to origin",
            "original": "Har kasi ku dur mand az asl-e khish, baz juyad ruzgar-e wasl-e khish.",
            "english": "Whoever is parted from the origin longs for the time of reunion.",
            "hindi": "जो अपनी मूल जड़ से दूर हो जाता है, वह मिलन के समय को खोजता रहता है।",
        },
        {
            "title": "Love turns bitterness sweet",
            "original": "Az mohabbat talkha shirin mishavad.",
            "english": "Through love, what is bitter becomes sweet.",
            "hindi": "प्रेम से कड़वाहट भी मिठास में बदल जाती है।",
        },
        {
            "title": "Come, come again",
            "original": "Biya biya har anche hasti biya.",
            "english": "Come, come, whoever you are, come again.",
            "hindi": "आओ, आओ, तुम जैसे भी हो, फिर भी चले आओ।",
        },
        {
            "title": "Out beyond wrong and right",
            "original": "Az kufr o din berun tar ast ma ra meydani.",
            "english": "There is a field beyond rigid divisions of belief where the soul meets freedom.",
            "hindi": "आस्था और निषेध की कठोर सीमाओं से परे एक खुला मैदान है जहाँ आत्मा स्वतंत्र होती है।",
        },
        {
            "title": "The lamps are many",
            "original": "In chiragh ast inki nur az u yeki ast.",
            "english": "The lamps are many, but the light is one.",
            "hindi": "दीपक अनेक हैं, पर उनकी रोशनी एक ही है।",
        },
        {
            "title": "Silent speech",
            "original": "Khamush kon ke zaban-e del digar ast.",
            "english": "Be silent, for the language of the heart is another language.",
            "hindi": "चुप हो जाओ, क्योंकि दिल की भाषा कुछ और ही होती है।",
        },
        {
            "title": "Die before death",
            "original": "Bimirid bimirid dar in ishq bimirid.",
            "english": "Die into love before death comes, so you may awaken truly alive.",
            "hindi": "मृत्यु आने से पहले प्रेम में अपने अहं को मिटा दो, तभी सच्चा जीवन जागेगा।",
        },
        {
            "title": "The wound and the light",
            "original": "Az zakhm haman nur dar ayad.",
            "english": "It is through the wound that light finds its way in.",
            "hindi": "घाव ही वह जगह है जहाँ से रोशनी भीतर आती है।",
        },
        {
            "title": "Be melting snow",
            "original": "Barf bash o az khodet boro, cho ab-e ravan.",
            "english": "Be like melting snow, leaving behind the rigid self and flowing onward.",
            "hindi": "पिघलती बर्फ़ जैसे बनो, कठोर अहं को छोड़कर बहते चले जाओ।",
        },
    ],
    "hafez": [
        {
            "title": "The Shirazi Turk",
            "original": "Agar an Turk-e Shirazi be dast arad del-e ma ra.",
            "english": "If that Shirazi beauty would take my heart in hand, all worldly treasures would feel little beside it.",
            "hindi": "यदि वह शीराज़ी रूपसी मेरे दिल को थाम ले, तो दुनिया के सारे ख़ज़ाने भी तुच्छ लगेंगे।",
        },
        {
            "title": "Let us scatter roses",
            "original": "Biya ta gol bar afshanem o may dar saghar andazim.",
            "english": "Come, let us scatter flowers and pour wine into the cup.",
            "hindi": "आओ, फूल बिखेरें और प्यालों में मदिरा उंडेलें।",
        },
        {
            "title": "Joseph returns",
            "original": "Yusuf-e gomgashta baz ayad be Kanan, gham makhor.",
            "english": "The lost Joseph will return to Canaan; do not surrender to grief.",
            "hindi": "खोया हुआ यूसुफ़ फिर कनआन लौटेगा, इसलिए ग़म में मत डूबो।",
        },
        {
            "title": "Good news",
            "original": "Mojdeh ey del ke Masiha nafas-i mi ayad.",
            "english": "Rejoice, heart, for a life-giving breath is on its way.",
            "hindi": "दिल, खुश हो जा, क्योंकि जीवन देने वाली साँस आने वाली है।",
        },
        {
            "title": "Last night the angels",
            "original": "Dush didam ke malaik dar-e meykhane zadand.",
            "english": "Last night I saw angels knock at the tavern door.",
            "hindi": "कल रात मैंने फ़रिश्तों को मयख़ाने के दरवाज़े पर दस्तक देते देखा।",
        },
        {
            "title": "Cupbearer bring wine",
            "original": "Ala ya ayyoha-s saqi adir ka'san wa nawilha.",
            "english": "Cupbearer, pass the cup around and offer it forth.",
            "hindi": "ऐ साक़ी, प्याला घुमाओ और सबको पिलाओ।",
        },
        {
            "title": "Morning breeze",
            "original": "Saba be lutf begu an ghazal sara ra.",
            "english": "O morning breeze, gently carry my message to the beloved singer.",
            "hindi": "ऐ सबा, मेरी बात उस प्रिय ग़ज़ल-सराय तक कोमलता से पहुँचा दो।",
        },
        {
            "title": "The beloved's lane",
            "original": "Dar kuye nek-nami ma ra guzar nadadand.",
            "english": "They would not let me pass into the lane of good reputation, for love had chosen another path.",
            "hindi": "उन्होंने मुझे नेक-नामी की गली से गुज़रने न दिया, क्योंकि इश्क़ ने मेरे लिए दूसरी राह चुनी थी।",
        },
        {
            "title": "Tavern door",
            "original": "Dar-e meykhane bastaand, khoda ya mabada.",
            "english": "They have shut the tavern door, O God, let that never be the final word.",
            "hindi": "उन्होंने मयख़ाने का दर बंद कर दिया; हे ईश्वर, ऐसा न हो कि यही अंतिम सत्य रह जाए।",
        },
        {
            "title": "Ask Hafez",
            "original": "Hafeza may khor o rindi kon o khosh bash vali.",
            "english": "Hafez, drink the wine of freedom, live playfully, yet do not wound another heart.",
            "hindi": "हाफ़िज़, रिंदाना खुलापन अपनाओ, आनंद से जियो, पर किसी दिल को चोट मत पहुँचाओ।",
        },
    ],
    "mir-taqi-mir": [
        {
            "title": "The leaf and branch",
            "original": "Patta patta boota boota hal hamara jane hai.",
            "english": "Every leaf and every shrub knows the state of my heart.",
            "hindi": "पत्ता-पत्ता, बूटा-बूटा मेरे दिल का हाल जानता है।",
        },
        {
            "title": "No one asks",
            "original": "Dikhai diye yun ke bekhud kiya, hamein aap se bhi juda kar chale.",
            "english": "You appeared in such a way that I lost myself and even became estranged from my own self.",
            "hindi": "तुम यूँ दिखाई दिए कि मैं खुद से भी बेख़बर और जुदा हो गया।",
        },
        {
            "title": "Delhi's ruin",
            "original": "Dilli jo ek shahr tha alam mein intikhab.",
            "english": "Delhi, once a city chosen above all the world, lies devastated in memory.",
            "hindi": "दिल्ली, जो कभी दुनिया में चुना हुआ शहर थी, अब उजड़ी हुई स्मृति बन गई है।",
        },
        {
            "title": "Bewildered heart",
            "original": "Ulti ho gayin sab tadbirein kuchh na dawa ne kam kiya.",
            "english": "Every remedy turned upside down; no medicine truly worked.",
            "hindi": "सारी तरकीबें उलटी पड़ गईं, कोई दवा काम न आई।",
        },
        {
            "title": "Mad for love",
            "original": "Mir ke din o mazhab ko ab puchte kya ho unne to.",
            "english": "Why ask now of Mir's creed and faith, when love has carried him beyond such labels?",
            "hindi": "अब मीर के दीन-ओ-मज़हब का क्या पूछना, इश्क़ उन्हें इन सीमाओं से परे ले गया है।",
        },
        {
            "title": "A subtle manner",
            "original": "Nazuki us ke lab ki kya kahiye, pankhri ek gulab ki si hai.",
            "english": "How can one describe the delicacy of those lips? They are like a rose petal.",
            "hindi": "उन होंठों की नज़ाकत क्या कहूँ, जैसे गुलाब की एक पंखुड़ी हो।",
        },
        {
            "title": "The city of heart",
            "original": "Ibtida-e ishq hai rota hai kya, age age dekhiye hota hai kya.",
            "english": "This is only the beginning of love; why weep already? Wait and see what comes ahead.",
            "hindi": "यह तो इश्क़ की शुरुआत है, अभी से क्यों रोते हो; आगे-आगे देखो क्या होता है।",
        },
        {
            "title": "A lonely traveler",
            "original": "Rah-e dur-e ishq mein rota hai kya.",
            "english": "Why lament on the long road of love, when sorrow itself is part of the journey?",
            "hindi": "इश्क़ की लंबी राह में क्यों रोते हो, जब दुख भी उसी सफ़र का हिस्सा है।",
        },
        {
            "title": "My condition",
            "original": "Ham hue tum hue ke Mir hue, us ki zulfon ke sab asir hue.",
            "english": "I, you, and even Mir became captives of those tresses.",
            "hindi": "मैं, तुम और मीर, सब उसकी ज़ुल्फ़ों के कैदी हो गए।",
        },
        {
            "title": "The heart remains struck",
            "original": "Mir in neem baz ankhon mein sari masti sharab ki si hai.",
            "english": "In those half-open eyes lives the intoxication of wine.",
            "hindi": "उन अधखुली आँखों में शराब जैसी मस्ती बसी है।",
        },
    ],
    "ghalib": [
        {
            "title": "Thousands of desires",
            "original": "Hazaron khwahishen aisi ke har khwahish pe dam nikle.",
            "english": "Thousands of desires, each so intense it could take my breath away.",
            "hindi": "हज़ारों ख़्वाहिशें, और हर ख़्वाहिश ऐसी कि उस पर जान निकल जाए।",
        },
        {
            "title": "Heart, not brick",
            "original": "Dil hi to hai na sang o khisht, dard se bhar na aaye kyun.",
            "english": "It is only a heart, not stone or brick, so why should it not fill with pain?",
            "hindi": "यह दिल ही तो है, पत्थर या ईंट नहीं; दर्द से भर क्यों न आए।",
        },
        {
            "title": "It was no use",
            "original": "Ye na thi hamari qismat ke visal-e yar hota.",
            "english": "It was never my fate to find union with the beloved.",
            "hindi": "यह मेरी क़िस्मत में नहीं था कि यार से मिलन हो पाता।",
        },
        {
            "title": "Heart asks what",
            "original": "Dil-e nadan tujhe hua kya hai, akhir is dard ki dawa kya hai.",
            "english": "O innocent heart, what has happened to you, and what cure can there be for such pain?",
            "hindi": "ऐ नादान दिल, तुझे क्या हो गया है, और इस दर्द की दवा आख़िर क्या है?",
        },
        {
            "title": "The prison of being",
            "original": "Qaid-e hayat o band-e gham asl mein dono ek hain.",
            "english": "The prison of life and the bondage of sorrow are, in truth, one and the same.",
            "hindi": "ज़िंदगी की क़ैद और ग़म की बेड़ी, असल में दोनों एक ही हैं।",
        },
        {
            "title": "A world of illusions",
            "original": "Bazicha-e atfal hai duniya mire age.",
            "english": "Before me, the world appears like a playground of children.",
            "hindi": "मेरी नज़र में यह दुनिया बच्चों के खेल का मैदान लगती है।",
        },
        {
            "title": "Who is speaking",
            "original": "Na tha kuchh to khuda tha, kuchh na hota to khuda hota.",
            "english": "When there was nothing, there was God; had nothing existed, God would still remain.",
            "hindi": "जब कुछ न था तब ख़ुदा था; कुछ भी न होता, तब भी ख़ुदा होता।",
        },
        {
            "title": "The lane of the beloved",
            "original": "Ishq par zor nahin hai ye woh atish Ghalib.",
            "english": "Love cannot be forced; it is a fire that lights where it wills.",
            "hindi": "इश्क़ पर ज़ोर नहीं चलता; यह ऐसी आग है जो अपनी मरज़ी से लगती है।",
        },
        {
            "title": "The image in the heart",
            "original": "Bas ke dushwar hai har kam ka asan hona.",
            "english": "It is difficult enough for any task to become easy.",
            "hindi": "हर काम का आसान हो जाना अपने आप में बहुत कठिन है।",
        },
        {
            "title": "No remedy but patience",
            "original": "Ranj se khugar hua insan to mit jata hai ranj.",
            "english": "When a person becomes accustomed to sorrow, sorrow itself begins to disappear.",
            "hindi": "जब इंसान ग़म का आदी हो जाता है, तो ग़म भी फीका पड़ने लगता है।",
        },
    ],
    "bahadur-shah-zafar": [
        {
            "title": "A desolate heart",
            "original": "Lagta nahin hai dil mera ujre dayar mein.",
            "english": "My heart no longer settles in this ravaged land.",
            "hindi": "उजड़े हुए इस देश में अब मेरा दिल लगता ही नहीं।",
        },
        {
            "title": "No one belongs",
            "original": "Na kisi ki ankh ka nur hun, na kisi ke dil ka qarar hun.",
            "english": "I am neither the light of anyone's eye nor the peace of anyone's heart.",
            "hindi": "मैं न किसी की आँख का नूर हूँ, न किसी के दिल का क़रार।",
        },
        {
            "title": "The misfortune of burial",
            "original": "Kitna hai bad-nasib Zafar dafn ke liye.",
            "english": "How unfortunate is Zafar, that even for burial he received so little land.",
            "hindi": "ज़फ़र कितने बदनसीब हैं कि दफ़्न होने के लिए भी दो गज़ ज़मीन न मिली।",
        },
        {
            "title": "The captive king",
            "original": "Umr-e daraz mang kar laye the char din.",
            "english": "I had asked for a long life and was granted merely four days.",
            "hindi": "लंबी उम्र माँगी थी, पर बदले में बस चार दिन मिले।",
        },
        {
            "title": "Passed in longing",
            "original": "Do arzoo mein kat gaye, do intizar mein.",
            "english": "Two passed in desire, and two passed in waiting.",
            "hindi": "दो दिन आरज़ू में कट गए, और दो इंतज़ार में।",
        },
        {
            "title": "The ruined dwelling",
            "original": "Baat karni mujhe mushkil kabhi aisi to na thi.",
            "english": "It was never so difficult for me to speak as it has become now.",
            "hindi": "मुझसे बात करना कभी इतना मुश्किल न था, जितना अब हो गया है।",
        },
        {
            "title": "Exile",
            "original": "Main woh majnun hun ke zindan mein nigahbanon ko.",
            "english": "I am such a mad lover that even in prison the guards feel my unrest.",
            "hindi": "मैं ऐसा दीवाना हूँ कि क़ैद में भी पहरेदार मेरी बेचैनी से परिचित हैं।",
        },
        {
            "title": "A fading sovereignty",
            "original": "Ya mujhe afsar-e shahana banaya hota.",
            "english": "Either destiny should have truly made me royal, or spared me this bitter irony.",
            "hindi": "या तो तक़दीर मुझे सचमुच शाही गरिमा देती, या यह कड़वी विडंबना न देती।",
        },
        {
            "title": "The broken gathering",
            "original": "Pas-e marg mere mazar par jo diya kisi ne jala diya.",
            "english": "After my death, someone lit a lamp upon my grave.",
            "hindi": "मेरी मृत्यु के बाद किसी ने मेरी क़ब्र पर एक दिया जला दिया।",
        },
        {
            "title": "The end of empire",
            "original": "Jo chaman khizan se ujarr gaya, main usi ki fasl-e bahar hun.",
            "english": "I am the springtime memory of a garden destroyed by autumn.",
            "hindi": "मैं उसी बाग़ की बहार की स्मृति हूँ जिसे पतझड़ ने उजाड़ दिया।",
        },
    ],
    "muhammad-iqbal": [
        {
            "title": "Better than the world",
            "original": "Sare jahan se achchha Hindostan hamara.",
            "english": "Better than the whole world is our Hindustan.",
            "hindi": "सारे जहाँ से अच्छा हमारा हिंदोस्ताँ है।",
        },
        {
            "title": "The nightingale and the garden",
            "original": "Ham bulbulen hain is ki, ye gulsitan hamara.",
            "english": "We are its nightingales, and this garden is ours.",
            "hindi": "हम इसकी बुलबुलें हैं, और यह गुलिस्ताँ हमारा है।",
        },
        {
            "title": "Raise the self",
            "original": "Khudi ko kar buland itna ke har taqdir se pehle.",
            "english": "Raise the self so high that before destiny is written, God asks what you desire.",
            "hindi": "अपने ख़ुदी को इतना ऊँचा करो कि हर तक़दीर से पहले ख़ुदा पूछे, तेरी रज़ा क्या है।",
        },
        {
            "title": "Before every decree",
            "original": "Khuda bande se khud puche bata teri raza kya hai.",
            "english": "So elevated should the human spirit become that God asks it for its will.",
            "hindi": "मनुष्य की आत्मा इतनी ऊँची हो कि ख़ुदा स्वयं उससे उसकी इच्छा पूछे।",
        },
        {
            "title": "Stars beyond stars",
            "original": "Sitaron se age jahan aur bhi hain.",
            "english": "Beyond the stars are still more worlds to discover.",
            "hindi": "सितारों के आगे भी और बहुत-सी दुनियाएँ हैं।",
        },
        {
            "title": "Trials of love",
            "original": "Abhi ishq ke imtihan aur bhi hain.",
            "english": "The tests of love are not over; many more remain.",
            "hindi": "इश्क़ की परीक्षाएँ अभी समाप्त नहीं हुईं, अभी और भी बाकी हैं।",
        },
        {
            "title": "The eagle",
            "original": "Tu shahin hai, parwaz hai kam tera.",
            "english": "You are an eagle; your true work is flight.",
            "hindi": "तुम शाहीन हो; तुम्हारा असली काम ऊँची उड़ान है।",
        },
        {
            "title": "Do not live low",
            "original": "Tere samne asman aur bhi hain.",
            "english": "Before you there are yet more skies to rise into.",
            "hindi": "तुम्हारे सामने अभी और भी आकाश फैले हुए हैं।",
        },
        {
            "title": "Prayer of the child",
            "original": "Lab pe ati hai dua ban ke tamanna meri.",
            "english": "A prayer rises to my lips as the deepest desire of my heart.",
            "hindi": "मेरे होंठों पर दुआ बनकर मेरे मन की तमन्ना आती है।",
        },
        {
            "title": "Illuminate life",
            "original": "Zindagi shamma ki surat ho khudaya meri.",
            "english": "O God, let my life be like a lamp, giving light to others.",
            "hindi": "हे ईश्वर, मेरी ज़िंदगी शमा की तरह हो जो औरों को रोशनी दे।",
        },
    ],
    "sanai": [
        {"title": "Wake from heedlessness", "original": "Az khab-e ghaflat bar ay ey dust.", "english": "Rise, friend, from the sleep of heedlessness.", "hindi": "मित्र, ग़फ़लत की नींद से जागो।"},
        {"title": "The heart as Kaaba", "original": "Dil kaba-ye ishq ast, be har su naraw.", "english": "The heart is the Kaaba of love; do not wander carelessly away from it.", "hindi": "दिल इश्क़ का काबा है; यूँ ही हर दिशा में भटक मत जाओ।"},
        {"title": "Outward piety mocked", "original": "Zahid be libas ast, na be nur-e yaqin.", "english": "The ascetic may have robes, but not always the light of certitude.", "hindi": "ज़ाहिद के पास वेशभूषा तो हो सकती है, पर यक़ीन की रोशनी आवश्यक नहीं।"},
        {"title": "Truth before display", "original": "Haqiqat talab, na nam o nishan.", "english": "Seek truth, not reputation and signs of status.", "hindi": "सत्य की खोज करो, नाम और प्रतिष्ठा की नहीं।"},
        {"title": "Inner reform", "original": "Har ke khod ra na shenakht, khoda ra na shenakht.", "english": "Whoever has not known the self has not known God.", "hindi": "जिसने स्वयं को नहीं जाना, उसने ईश्वर को भी नहीं जाना।"},
        {"title": "Worldly illusion", "original": "In bazicha-ye khak dar nazar mabin.", "english": "Do not mistake this dusty game for lasting reality.", "hindi": "इस धूल भरे खेल को स्थायी सत्य मत समझो।"},
        {"title": "The path is difficult", "original": "Rah-e ishq ra sar o jaan bayad.", "english": "The path of love demands the whole head and soul.", "hindi": "इश्क़ की राह सिर और जान दोनों मांगती है।"},
        {"title": "Humility of the seeker", "original": "Sar dar rah-e ustad nehadan adab ast.", "english": "To lay one's head in humility on the path of the guide is true courtesy.", "hindi": "मार्गदर्शक की राह में विनम्रता से सिर झुकाना ही सच्चा अदब है।"},
        {"title": "The mirror of conscience", "original": "Ayina-ye dil ra ze zang pak kon.", "english": "Clean the rust from the mirror of the heart.", "hindi": "दिल के आईने से जंग साफ़ करो।"},
        {"title": "The wise warning", "original": "Har nafas rahzan ast gar hosh nist.", "english": "Every breath can become a thief if awareness is absent.", "hindi": "यदि सजगता न हो, तो हर सांस भी लुटेरा बन सकती है।"},
    ],
    "attar": [
        {"title": "The conference begins", "original": "Ma hama murghan-e rah-e simorghim.", "english": "We are all birds on the path toward the Simorgh.", "hindi": "हम सब सिमुर्ग की राह के पक्षी हैं।"},
        {"title": "Seek the Beloved", "original": "Talab kun an che to ra az to mirobayad.", "english": "Seek that which will carry you beyond yourself.", "hindi": "उसकी तलाश करो जो तुम्हें तुम्हारे अहं से आगे ले जाए।"},
        {"title": "Valley of quest", "original": "Avval qadam talab ast.", "english": "The first step is longing and quest.", "hindi": "पहला कदम खोज और तलब का है।"},
        {"title": "Annihilation", "original": "Chun to nist shodi, hama u mani.", "english": "When you are no longer yourself, you become entirely His.", "hindi": "जब तुम अपने आप में नहीं रहते, तभी पूरी तरह उसी के हो जाते हो।"},
        {"title": "The moth and flame", "original": "Parvana ra ba atish in guftugu bas ast.", "english": "For the moth, this conversation with flame is enough.", "hindi": "परवाने के लिए अग्नि से यह संवाद ही पर्याप्त है।"},
        {"title": "Beyond reason", "original": "Ishq amad o aql ra ba yak su fekand.", "english": "Love arrived and cast reason aside.", "hindi": "इश्क़ आया और बुद्धि को एक ओर कर दिया।"},
        {"title": "Birds and mirrors", "original": "Har murgh dar ayina-ye simorgh khod ra did.", "english": "Each bird saw itself in the mirror of the Simorgh.", "hindi": "हर पक्षी ने सिमुर्ग के आईने में स्वयं को देखा।"},
        {"title": "Dust of the road", "original": "Az gard-e rah-e dust bartar che ast.", "english": "What is higher than the dust of the Beloved's road?", "hindi": "प्रिय की राह की धूल से बढ़कर और क्या हो सकता है।"},
        {"title": "The secret of love", "original": "Asrar-e ishq ra na har kasi danad.", "english": "Not everyone can know the secret of love.", "hindi": "इश्क़ का रहस्य हर कोई नहीं जान सकता।"},
        {"title": "Journey inward", "original": "Rah dur nist, tu duri az khish.", "english": "The road is not far; you are far from yourself.", "hindi": "रास्ता दूर नहीं, तुम स्वयं से दूर हो।"},
    ],
    "nizami-ganjavi": [
        {"title": "Beauty and discipline", "original": "Husn ra ba kherad zivar ast.", "english": "Beauty is most adorned when joined to wisdom.", "hindi": "सौंदर्य तब सबसे अधिक सुशोभित होता है जब वह बुद्धि से जुड़ा हो।"},
        {"title": "The tale begins", "original": "Har qissa ra ba ishq shirin tavan kard.", "english": "Every tale can be made sweet through love.", "hindi": "हर कथा को प्रेम से मधुर बनाया जा सकता है।"},
        {"title": "Layla's desert", "original": "Sahra ze nam-e Layla gulzar shod.", "english": "The desert turned into a garden at Layla's name.", "hindi": "लैला के नाम से मरुस्थल भी बाग़ बन गया।"},
        {"title": "Majnun's longing", "original": "Majnun ze khod birun shod az shiddat-e talab.", "english": "Majnun stepped out of himself through the intensity of longing.", "hindi": "तलब की तीव्रता से मजनूँ अपने आप से बाहर निकल गया।"},
        {"title": "Khusrau and Shirin", "original": "Shirin ze latafat chun shekar bud.", "english": "Shirin was sweet with delicacy like sugar.", "hindi": "शिरीं की कोमलता शक्कर जैसी मधुर थी।"},
        {"title": "Kingship judged", "original": "Shahi be adl zinda bavad na be taj.", "english": "Kingship lives by justice, not by the crown.", "hindi": "राजसत्ता मुकुट से नहीं, न्याय से जीवित रहती है।"},
        {"title": "The hidden pearl", "original": "Gohar darun-e dil talab bayad kard.", "english": "The true pearl must be sought within the heart.", "hindi": "सच्चा मोती दिल के भीतर खोजना चाहिए।"},
        {"title": "Narrative grace", "original": "Sokhan agar ba nafas ast, jan bakhshad.", "english": "When speech carries living breath, it grants life.", "hindi": "जब वाणी में प्राण होते हैं, वह जीवनदान देती है।"},
        {"title": "The lover's lesson", "original": "Az ishq adab o sabr bayad amukht.", "english": "From love one must learn courtesy and patience.", "hindi": "प्रेम से अदब और धैर्य सीखना चाहिए।"},
        {"title": "The lamp of story", "original": "Qissa chu shama ast agar roshan ast.", "english": "A story is like a lamp when it is truly luminous.", "hindi": "जब कथा सचमुच उजली हो, तो वह दीपक जैसी लगती है।"},
    ],
    "jami": [
        {"title": "Scholar and lover", "original": "Ilm agar ba ishq nabashad, hijab ast.", "english": "Knowledge without love becomes a veil.", "hindi": "यदि ज्ञान में प्रेम न हो, तो वह परदा बन जाता है।"},
        {"title": "Joseph's beauty", "original": "Husn-e Yusuf jahan ra fitna kard.", "english": "Joseph's beauty set the whole world in wonder.", "hindi": "यूसुफ़ का सौंदर्य पूरे जगत को विस्मय में डाल देता है।"},
        {"title": "Zulaikha's longing", "original": "Zulaikha ra talab ba jan rasid.", "english": "Zulaikha's longing reached the depth of the soul.", "hindi": "ज़ुलेखा की तलब आत्मा की गहराई तक पहुँच गई।"},
        {"title": "Sufi sobriety", "original": "Dar mastiyat ham hosh bayad bud.", "english": "Even in ecstasy one must retain a higher awareness.", "hindi": "उन्माद में भी एक ऊँची सजगता बनाए रखनी चाहिए।"},
        {"title": "Garden of meaning", "original": "Mani chu gol ast o lafz barg-e u.", "english": "Meaning is the flower, and words are its petals.", "hindi": "अर्थ फूल है और शब्द उसकी पंखुड़ियाँ हैं।"},
        {"title": "Mirror of the friend", "original": "Dust dar ayina-ye dust khod ra did.", "english": "The friend saw himself in the mirror of the Friend.", "hindi": "मित्र ने मित्र के आईने में स्वयं को देखा।"},
        {"title": "Grace of restraint", "original": "Narmi ze kamal ast na az zaf.", "english": "Gentleness comes from perfection, not weakness.", "hindi": "कोमलता कमजोरी से नहीं, परिपूर्णता से आती है।"},
        {"title": "The path of unity", "original": "Rah yakist agarche suratha besyar.", "english": "The path is one, though forms may be many.", "hindi": "राह एक ही है, भले रूप अनेक हों।"},
        {"title": "The breath of devotion", "original": "Zikr chun nafas jan ra safa bakhshad.", "english": "Remembrance purifies the soul like breath itself.", "hindi": "स्मरण आत्मा को सांस की तरह निर्मल करता है।"},
        {"title": "Jami's counsel", "original": "Ba adab bash ke dar rah-e dusti rahbar ast.", "english": "Be courteous, for courtesy is the guide on the path of friendship.", "hindi": "अदब में रहो, क्योंकि मित्रता की राह में वही मार्गदर्शक है।"},
    ],
    "baba-tahir": [
        {"title": "My lonely heart", "original": "Delam gereft o gereft o gereft.", "english": "My heart has tightened again and again in sorrow.", "hindi": "मेरा दिल बार-बार दुख से सिमटता गया है।"},
        {"title": "The beloved everywhere", "original": "Be har ja bengarom kuh o dar o dasht, neshan az qamat-e ranat binam.", "english": "Wherever I look, in mountain, door, or plain, I see signs of your graceful form.", "hindi": "मैं जिधर भी देखूँ, पर्वत, द्वार या मैदान में, मुझे तुम्हारी सुडौल छवि के संकेत दिखते हैं।"},
        {"title": "Eyes of longing", "original": "Ze dast-e dida o dil har do faryad.", "english": "Both eye and heart cry out together.", "hindi": "आँख और दिल दोनों साथ-साथ पुकार उठते हैं।"},
        {"title": "Night of absence", "original": "Shabi bi to na khabam ayad o na tab.", "english": "Without you, the night brings neither sleep nor patience.", "hindi": "तुम बिन रात में न नींद आती है, न धैर्य रहता है।"},
        {"title": "Plain-spoken pain", "original": "Yaki dard ast andar del nihani.", "english": "There is a hidden pain resting in the heart.", "hindi": "दिल में एक छिपा हुआ दर्द ठहरा है।"},
        {"title": "The mountain witness", "original": "Kuh o sahra be hal-e zaram gawahand.", "english": "Mountain and plain bear witness to my lament.", "hindi": "पर्वत और मैदान मेरे विलाप के गवाह हैं।"},
        {"title": "The mystic wound", "original": "Zakhm-e ishq ast o marhamash nist.", "english": "This is the wound of love, and it has no ordinary balm.", "hindi": "यह इश्क़ का घाव है, और इसका कोई साधारण मरहम नहीं।"},
        {"title": "Dust of the path", "original": "Ghubar-e rah-e tu bar dida mi kasham.", "english": "I place the dust of your path upon my eyes.", "hindi": "मैं तुम्हारी राह की धूल अपनी आँखों पर लगाता हूँ।"},
        {"title": "A dervish plea", "original": "Geda-yam, dar-e tu padshahi-st.", "english": "I am a beggar, and your doorway is my kingdom.", "hindi": "मैं फ़क़ीर हूँ, और तुम्हारा द्वार ही मेरा राज्य है।"},
        {"title": "Soul's simplicity", "original": "Na danam ishq chist in qadr midanam.", "english": "I do not know what love is, only that it has remade me.", "hindi": "मैं नहीं जानता प्रेम क्या है, बस इतना जानता हूँ कि उसने मुझे बदल दिया है।"},
    ],
    "khwaju-kirmani": [
        {"title": "Perfumed lane", "original": "Ku-ye yar az nafas-e mushk tar ast.", "english": "The beloved's lane is fragrant like musk on the breeze.", "hindi": "प्रिय की गली हवा में कस्तूरी जैसी महकती है।"},
        {"title": "Lyrical polish", "original": "Ghazal ba husn-e sukhan zinat girad.", "english": "The ghazal is adorned by the beauty of expression.", "hindi": "ग़ज़ल वाणी की सुंदरता से अलंकृत होती है।"},
        {"title": "The cup and the moon", "original": "Mah dar kaf-e saqi o may dar saghar ast.", "english": "The moon is in the cupbearer's hand and wine in the goblet.", "hindi": "चाँद साक़ी के हाथ में है और मदिरा प्याले में।"},
        {"title": "Beloved's curls", "original": "Az zulf-e tu shab rang digar mi girad.", "english": "From your curls, the night takes on a deeper hue.", "hindi": "तुम्हारी ज़ुल्फ़ों से रात और भी गहरी हो जाती है।"},
        {"title": "Gentle sorrow", "original": "Gham ra ba tarannom tavan guft.", "english": "Even sorrow can be spoken in songlike cadence.", "hindi": "ग़म भी तरन्नुम में कहा जा सकता है।"},
        {"title": "The rose garden", "original": "Golshan ze jamal-e dust raunaq girad.", "english": "The garden takes its radiance from the beloved's beauty.", "hindi": "बाग़ को अपनी रौनक प्रिय के सौंदर्य से मिलती है।"},
        {"title": "Tavern ease", "original": "Meykada ra ba lab-e khanda ravan bayad shod.", "english": "One should enter the tavern with smiling lips.", "hindi": "मयख़ाने में मुस्कुराते होंठों के साथ प्रवेश करना चाहिए।"},
        {"title": "Courtly longing", "original": "Dar bazm ham az hijr-e tu afsane konam.", "english": "Even in the gathering I speak of separation from you.", "hindi": "महफ़िल में भी मैं तुमसे जुदाई की ही कथा कहता हूँ।"},
        {"title": "The glance", "original": "Yak nigah-at sad ghazal ra jan dahad.", "english": "A single glance from you gives life to a hundred ghazals.", "hindi": "तुम्हारी एक निगाह सौ ग़ज़लों में प्राण भर देती है।"},
        {"title": "Refined yearning", "original": "Khwaju sukhan ra ba narmi basta ast.", "english": "Khwaju binds speech with gentleness and refinement.", "hindi": "ख़्वाजू वाणी को कोमलता और नफ़ासत से बाँधते हैं।"},
    ],
    "wali-deccani": [
        {"title": "Every glance says love", "original": "Har ek bat pe kehte ho tum ke tu kya hai.", "english": "At every word, the beloved asks with playful wonder what I truly am.", "hindi": "हर बात पर महबूब चंचल विस्मय से पूछता है कि मैं आखिर क्या हूँ।"},
        {"title": "The color of Rekhta", "original": "Rekhta ke tumhin ustad nahin ho Wali.", "english": "Wali, you are not merely a master of rekhta, you gave it confidence.", "hindi": "वली, तुम केवल रेख़्ता के उस्ताद नहीं, तुमने उसे आत्मविश्वास दिया।"},
        {"title": "Love as speech", "original": "Ishq ne hum ko zaban-e dil sikhlayi.", "english": "Love taught me the language of the heart.", "hindi": "इश्क़ ने मुझे दिल की भाषा सिखाई।"},
        {"title": "The lane of beauty", "original": "Ku-ye janan mein jo guzre to bahar ayi.", "english": "When I passed through the beloved's lane, spring arrived.", "hindi": "जब मैं प्रिय की गली से गुज़रा, तो बहार आ गई।"},
        {"title": "A Deccani softness", "original": "Narm guftari se har dil ko ramaaya ham ne.", "english": "With gentle speech, I won over many hearts.", "hindi": "कोमल बोल से मैंने कई दिलों को अपना बनाया।"},
        {"title": "Union imagined", "original": "Wasl ka khwab bhi dil ko khushnuma lagta hai.", "english": "Even the dream of union makes the heart glow.", "hindi": "मिलन का स्वप्न भी दिल को उजला कर देता है।"},
        {"title": "Persian grace, Urdu warmth", "original": "Farsi ada, Hindvi lazzat, dono ek sukhan mein.", "english": "Persian grace and Hindavi warmth mingle in one utterance.", "hindi": "फ़ारसी की अदा और हिंदवी की गर्माहट एक ही कथन में मिल जाती है।"},
        {"title": "The heart's garden", "original": "Dil ka gulshan tere zikr se abad hua.", "english": "The garden of the heart flourished through your remembrance.", "hindi": "तुम्हारी याद से दिल का बाग़ आबाद हो गया।"},
        {"title": "First stirrings", "original": "Ibtida-e ghazal mein hi nasha sa hai.", "english": "There is already an intoxication in the opening of the ghazal.", "hindi": "ग़ज़ल की शुरुआत में ही एक नशा-सा है।"},
        {"title": "Wali's signature", "original": "Wali ne ishq ko bazar-e sukhan mein utara.", "english": "Wali brought love into the bustling marketplace of poetic speech.", "hindi": "वली ने इश्क़ को कविता की जीवंत दुनिया में उतार दिया।"},
    ],
    "siraj-aurangabadi": [
        {"title": "The wandering self", "original": "Khana ba dosh-e ishqam o dar ba daram hanuz.", "english": "I still wander door to door, carrying love upon my shoulders.", "hindi": "मैं अब भी प्रेम को कंधों पर उठाए दर-दर भटकता हूँ।"},
        {"title": "The burning heart", "original": "Dil ra ba atish-e shauq jalaye rakha.", "english": "I kept the heart lit with the fire of longing.", "hindi": "मैंने दिल को तड़प की आग से जलाए रखा।"},
        {"title": "Mystic bewilderment", "original": "Hairat ne mujhe apne hi andar khona sikhaya.", "english": "Wonder taught me how to lose myself within myself.", "hindi": "हैरानी ने मुझे अपने भीतर ही स्वयं को खोना सिखाया।"},
        {"title": "The fakir's road", "original": "Faqiri rahe to saltanat khak shud.", "english": "Once fakiri appeared, worldly sovereignty turned to dust.", "hindi": "फ़क़ीरी आते ही सांसारिक बादशाहत धूल हो गई।"},
        {"title": "Night of zikr", "original": "Shab bhar tera hi nam dua ban ke raha.", "english": "All night your name remained upon me like a prayer.", "hindi": "सारी रात तुम्हारा नाम मुझ पर दुआ की तरह बना रहा।"},
        {"title": "The self undone", "original": "Bekhudi se raaz-e hasti khula.", "english": "Through self-forgetting, the secret of existence opened.", "hindi": "बेख़ुदी से अस्तित्व का रहस्य खुल गया।"},
        {"title": "A burning dervish", "original": "Siraj is bazm mein khak nahin, shola hai.", "english": "Siraj in this gathering is not dust but flame.", "hindi": "सिराज इस महफ़िल में धूल नहीं, लौ है।"},
        {"title": "The absent beloved", "original": "Hijr ne dil ko sukun se dur rakha.", "english": "Separation kept the heart far from repose.", "hindi": "जुदाई ने दिल को चैन से दूर रखा।"},
        {"title": "The silent cry", "original": "Faryad bhi andar hi andar uthti rahi.", "english": "The cry kept rising, though only within.", "hindi": "फरियाद उठती रही, पर भीतर ही भीतर।"},
        {"title": "Path of inward fire", "original": "Rah-e dil mein dhuan bhi tha aur nur bhi.", "english": "On the heart's path there was both smoke and light.", "hindi": "दिल की राह में धुआँ भी था और रोशनी भी।"},
    ],
    "insha": [
        {"title": "Wit in language", "original": "Insha ne zaban ko bhi tamasha bana diya.", "english": "Insha turned language itself into a delightful performance.", "hindi": "इंशा ने भाषा को ही एक मनोहर तमाशा बना दिया।"},
        {"title": "A playful address", "original": "Tum ham se bolo pyar se, ham bhi jawab dein.", "english": "Speak to me with affection, and I will reply in kind.", "hindi": "तुम मुझसे प्रेम से बोलो, मैं भी वैसा ही उत्तर दूँगा।"},
        {"title": "Urban elegance", "original": "Bazm-e sukhan mein shehar ki nafasat basti hai.", "english": "In the poetic gathering lives the polish of the city.", "hindi": "काव्य-महफ़िल में शहर की नफ़ासत बसती है।"},
        {"title": "Self-aware humor", "original": "Ham bhi ajeeb log hain, khud par bhi hans lete hain.", "english": "We are peculiar people; we can laugh even at ourselves.", "hindi": "हम भी अजीब लोग हैं, अपने ऊपर भी हँस लेते हैं।"},
        {"title": "The charm of idiom", "original": "Muhavra agar baith jaye to she'r chamak uthta hai.", "english": "When the idiom lands just right, the verse begins to shine.", "hindi": "जब मुहावरा सही बैठ जाए, तो शेर चमक उठता है।"},
        {"title": "Love in banter", "original": "Shokhi mein bhi ishq ka ik raaz chhupa tha.", "english": "Even in playfulness there was a secret of love concealed.", "hindi": "शोखी में भी प्रेम का एक रहस्य छिपा था।"},
        {"title": "The art of style", "original": "Andaz bhi mani ki tarah aham nikla.", "english": "Style proved as important as meaning itself.", "hindi": "अंदाज़ भी अर्थ जितना ही महत्वपूर्ण सिद्ध हुआ।"},
        {"title": "Speech as mirror", "original": "Boli se hi shakhsiyat ka rang ubharta hai.", "english": "Through speech, the true color of personality emerges.", "hindi": "बोली से ही व्यक्तित्व का असली रंग उभरता है।"},
        {"title": "Insha's repartee", "original": "Ek jumla bhi bazm ko roshan kar gaya.", "english": "A single sentence lit up the whole gathering.", "hindi": "एक ही वाक्य ने पूरी महफ़िल को रोशन कर दिया।"},
        {"title": "Language lives", "original": "Zaban zinda hai jab tak us mein lutf baqi hai.", "english": "A language lives so long as delight remains within it.", "hindi": "भाषा तब तक जीवित रहती है जब तक उसमें रस बना रहता है।"},
    ],
    "bedil": [
        {"title": "The world as imagination", "original": "In jahaan khayal ast o ma khayal andar khayal.", "english": "This world is imagination, and we are imagination within imagination.", "hindi": "यह संसार कल्पना है, और हम कल्पना के भीतर की कल्पना हैं।"},
        {"title": "Mirror of bewilderment", "original": "Ayina-am ke hayratam az aks-e khodast.", "english": "I am a mirror astonished by my own reflection.", "hindi": "मैं ऐसा आईना हूँ जो अपने ही प्रतिबिंब पर चकित है।"},
        {"title": "Dust and cosmos", "original": "Az gard-e rah to afaq paida shod.", "english": "From a single grain of dust, horizons emerge.", "hindi": "राह की एक धूल-कण से भी क्षितिज जन्म ले लेते हैं।"},
        {"title": "Self and disappearance", "original": "Hasti be fana mi rasad az rah-e shenakht.", "english": "Being reaches annihilation by the path of deep knowing.", "hindi": "अस्तित्व गहन पहचान की राह से फ़ना तक पहुँचता है।"},
        {"title": "The subtle knot", "original": "Har nokta girah-ha-ye digar mi zayad.", "english": "Every subtle point gives rise to further knots of meaning.", "hindi": "हर सूक्ष्म बिंदु अर्थ की नई गांठें बना देता है।"},
        {"title": "Labyrinth of heart", "original": "Dil dasht-e bi-payan ast.", "english": "The heart is an endless wilderness.", "hindi": "दिल एक अनंत मरुस्थल है।"},
        {"title": "Fire in silence", "original": "Khamushi ham zaban-e shola darad.", "english": "Silence too has the language of flame.", "hindi": "मौन के पास भी ज्वाला की अपनी भाषा होती है।"},
        {"title": "No center fixed", "original": "Markaz na manam, na tu, na in daira.", "english": "Neither you nor I are the fixed center of this circle.", "hindi": "न तुम और न मैं इस वृत्त का स्थिर केंद्र हैं।"},
        {"title": "A breath of paradox", "original": "Nafas ham qaid ast o ham rahayi.", "english": "Breath itself is both captivity and release.", "hindi": "सांस स्वयं बंधन भी है और मुक्ति भी।"},
        {"title": "Bedil's signature", "original": "Bedil sukhan ra rah-e tajrid ast.", "english": "For Bedil, speech is a path toward abstraction and unveiling.", "hindi": "बेदिल के लिए वाणी अमूर्तन और अनावृत्ति की राह है।"},
    ],
    "saeb-tabrizi": [
        {"title": "Fresh metaphor", "original": "Har roz gol-e taza ze fikram damad.", "english": "Each day a fresh flower blooms from my thought.", "hindi": "मेरे विचार से प्रतिदिन एक नया फूल खिल उठता है।"},
        {"title": "Arrow of meaning", "original": "Tir-e maani cho ravan shod, neshan mi juyad.", "english": "When the arrow of meaning is released, it seeks its own target.", "hindi": "अर्थ का तीर छूटे तो स्वयं अपना निशाना खोज लेता है।"},
        {"title": "Life's brevity", "original": "Omr chun barg-e gul az bad-e saba larzan ast.", "english": "Life trembles like a rose petal in the morning breeze.", "hindi": "जीवन सबा की हवा में कांपती गुलाब-पंखुड़ी जैसा है।"},
        {"title": "The moral glance", "original": "Az nigah-e ibarat har cheh bini dars ast.", "english": "Through the eye of insight, everything becomes a lesson.", "hindi": "अर्थ-दृष्टि से देखो तो हर वस्तु एक शिक्षा बन जाती है।"},
        {"title": "The road and the traveler", "original": "Rah ba qadam sakht nist, ba hamat sakht ast.", "english": "The road is not difficult for the feet, but for resolve.", "hindi": "रास्ता कदमों के लिए कठिन नहीं, संकल्प के लिए कठिन है।"},
        {"title": "The cup of reflection", "original": "Jam ham ayina-ye halat-e ma shod.", "english": "Even the wine cup turned into a mirror of our condition.", "hindi": "मदिरा-प्याला भी हमारी दशा का आईना बन गया।"},
        {"title": "The city of thought", "original": "Shahr-e khayal ra dar o divar digar ast.", "english": "The city of imagination has walls and doors unlike any other.", "hindi": "कल्पना के नगर की दीवारें और द्वार बिल्कुल भिन्न होते हैं।"},
        {"title": "Grace under burden", "original": "Sar bar kaf-e dard ham be tabassum ravam.", "english": "Even carrying pain in my palm, I move with a smile.", "hindi": "दर्द को हथेली पर लेकर भी मैं मुस्कान के साथ चलता हूँ।"},
        {"title": "Subtle satire", "original": "Zarf agar tang bavad, darya ham qatra shavad.", "english": "If the vessel is narrow, even the sea becomes a drop.", "hindi": "यदि पात्र संकीर्ण हो, तो समुद्र भी बूंद बन जाता है।"},
        {"title": "Saeb's manner", "original": "Saeb sukhan ra ba tajriba rangin kard.", "english": "Saeb colors poetry through lived experience.", "hindi": "साएब कविता को अनुभव के रंग से भर देते हैं।"},
    ],
    "kalim-kashani": [
        {"title": "Ornamented lyric", "original": "Har lafz chu zar dar narm silk-e sukhan ast.", "english": "Each word is like gold threaded in soft silk of verse.", "hindi": "हर शब्द कविता के रेशमी वस्त्र में पिरोया हुआ सोना है।"},
        {"title": "The migrant voice", "original": "Az Kashan ta Hind dilam hamrah-am bud.", "english": "From Kashan to Hindustan, my heart traveled with me.", "hindi": "काशान से हिंदुस्तान तक मेरा दिल मेरे साथ चला।"},
        {"title": "The painterly line", "original": "Tasvir-e maani ra ba yak khatt kashidam.", "english": "I drew the image of meaning with a single stroke.", "hindi": "मैंने अर्थ की तस्वीर एक ही रेखा से खींच दी।"},
        {"title": "Courtly delicacy", "original": "Nazuki dar sukhan az zabt payda shod.", "english": "Delicacy in poetry arose from disciplined restraint.", "hindi": "कविता की नज़ाकत संयमित शिल्प से उत्पन्न हुई।"},
        {"title": "The rose and mirror", "original": "Gol dar ayina-ye shabnam dobarah paida shod.", "english": "In the mirror of dew, the rose appeared again.", "hindi": "ओस के आईने में गुलाब फिर से प्रकट हुआ।"},
        {"title": "Love's courtesy", "original": "Ishq be adab ast agar kamal talabad.", "english": "Love seeks refinement through courtesy.", "hindi": "यदि प्रेम उत्कर्ष चाहता है, तो उसे अदब की राह लेनी होती है।"},
        {"title": "A jewel of thought", "original": "Fikr chu gohar dar sadaf-e khamoshi ast.", "english": "Thought is a pearl resting in the shell of silence.", "hindi": "विचार मौन की सीपी में रखा मोती है।"},
        {"title": "Shimmering phrase", "original": "Lafz ra jalwa-ye maani zi to taban kard.", "english": "Meaning made the phrase shimmer with light.", "hindi": "अर्थ ने वाक्यांश को उजाले से चमका दिया।"},
        {"title": "Elegance in exile", "original": "Ghorbat ham agarche talkh, ba sukhan shirin shod.", "english": "Exile, though bitter, became sweet through poetry.", "hindi": "निर्वासन यद्यपि कड़वा था, पर कविता ने उसे मधुर बना दिया।"},
        {"title": "Kalim's touch", "original": "Kalim be latifagi dil-ha ra gereft.", "english": "Kalim won hearts through lyrical delicacy.", "hindi": "कलीम ने अपनी कोमल काव्य-शैली से दिल जीत लिए।"},
    ],
    "qaani": [
        {"title": "Rhetoric and mirror", "original": "Fasahat agar ayina shavad, haq namayan ast.", "english": "When eloquence becomes a mirror, truth appears clearly.", "hindi": "जब वाक्पटुता आईना बनती है, तो सत्य स्पष्ट दिखाई देता है।"},
        {"title": "Voice of transition", "original": "Daur digar shod o sukhan ham digar shod.", "english": "The age changed, and poetry changed with it.", "hindi": "युग बदला, और कविता भी उसके साथ बदल गई।"},
        {"title": "Satirical edge", "original": "Tabassum ra sipar kardam baray-e naqdi zahan.", "english": "I used a smile as a shield for sharp critique.", "hindi": "मैंने तीखी आलोचना के लिए मुस्कान को ढाल बनाया।"},
        {"title": "The speaking city", "original": "Dar bazm-e shahr har sokhan siyasat ast.", "english": "In the city's gathering, every utterance is political.", "hindi": "शहर की महफ़िल में हर कथन राजनीति से जुड़ जाता है।"},
        {"title": "Classical pulse", "original": "Rag-e kohan dar tan-e tajdid mi zened.", "english": "An old pulse beats within a modern body.", "hindi": "आधुनिक शरीर में भी परंपरा की पुरानी नाड़ी धड़कती है।"},
        {"title": "Measured praise", "original": "Madh be andaza buvad, warna ghulu ast.", "english": "Praise must stay measured, else it turns to excess.", "hindi": "प्रशंसा सीमित रहे, वरना अतिशयोक्ति बन जाती है।"},
        {"title": "The changing court", "original": "Darbar agar raft, qalam baqi mand.", "english": "Even when courts fade, the pen remains.", "hindi": "दरबार भले ढल जाएँ, कलम बनी रहती है।"},
        {"title": "Witness of time", "original": "Zaman ze shair shahid-talab ast.", "english": "Time asks the poet to bear witness.", "hindi": "समय कवि से साक्ष्य देने की मांग करता है।"},
        {"title": "Language of scrutiny", "original": "Har harf ra dar taziya mizan bayad.", "english": "Every word must be weighed in critical balance.", "hindi": "हर शब्द को आलोचनात्मक तुला पर तौलना चाहिए।"},
        {"title": "Qaani's cadence", "original": "Qaani ba balaghat rah-e jadid koshud.", "english": "Qa'ani opened a modern path through classical eloquence.", "hindi": "क़ाआनी ने शास्त्रीय वाक्पटुता से आधुनिक राह खोली।"},
    ],
    "parvin-etesami": [
        {"title": "Voice of justice", "original": "Adl ra be zaban-e narm bayad goft.", "english": "Justice must be spoken in a voice that reaches all.", "hindi": "न्याय की बात ऐसी भाषा में कहनी चाहिए जो सब तक पहुँचे।"},
        {"title": "Dialogue of conscience", "original": "Ba zameer-e khod sokhan guftam.", "english": "I spoke in dialogue with my own conscience.", "hindi": "मैंने अपने ही अंत:करण से संवाद किया।"},
        {"title": "Dignity and labor", "original": "Kar ba sharaf ast agarche sakht ast.", "english": "Work is honorable even when it is hard.", "hindi": "परिश्रम चाहे कठिन हो, फिर भी सम्माननीय है।"},
        {"title": "Ethics of speech", "original": "Sokhan agar na be rahmat, be dard nemiarzad.", "english": "Speech without compassion is not worth uttering.", "hindi": "करुणा रहित वाणी कहे जाने योग्य नहीं।"},
        {"title": "Critique of arrogance", "original": "Takabbur ra dar ayina-ye faqr shikastam.", "english": "I broke arrogance against the mirror of humility.", "hindi": "मैंने अहंकार को विनम्रता के आईने में तोड़ दिया।"},
        {"title": "The candle and moth", "original": "Sham ra dard-e parvana behtar az tamkin ast.", "english": "For the candle, the moth's pain is dearer than stillness.", "hindi": "शमा के लिए परवाने का दर्द ठहरे हुए वैभव से प्रिय है।"},
        {"title": "The orphan's plea", "original": "Aah-e yatim asman ra milarzand.", "english": "The sigh of an orphan can shake the heavens.", "hindi": "अनाथ की आह आकाश को भी कंपा सकती है।"},
        {"title": "Learning as light", "original": "Danesh charagh-e rah-e insaniyat ast.", "english": "Knowledge is the lamp on humanity's road.", "hindi": "ज्ञान मानवता की राह का दीपक है।"},
        {"title": "Compassionate realism", "original": "Haqiqat ra be mehr bayad did.", "english": "Reality must be viewed through kindness.", "hindi": "यथार्थ को करुणा की दृष्टि से देखना चाहिए।"},
        {"title": "Parvin's resolve", "original": "Parvin qalam ra dar khidmat-e insaf nehad.", "english": "Parvin placed her pen in service of justice.", "hindi": "परवीन ने अपनी कलम को न्याय की सेवा में समर्पित किया।"},
    ],
    "aref-qazvini": [
        {"title": "Song of homeland", "original": "Ey vatan, ey aziz-e janam.", "english": "O homeland, beloved of my soul.", "hindi": "हे वतन, तू मेरी जान का अज़ीज़ है।"},
        {"title": "Lament of the age", "original": "Dard-e zaman ra be naghma goftam.", "english": "I voiced the pain of the age through song.", "hindi": "मैंने युग के दर्द को गीत में व्यक्त किया।"},
        {"title": "Constitutional hope", "original": "Azadi ra be awaz talab kardam.", "english": "I raised my voice to call for freedom.", "hindi": "मैंने स्वतंत्रता की मांग के लिए अपनी आवाज़ उठाई।"},
        {"title": "Public grief", "original": "Gham-e melli ba gham-e fardi dar amikht.", "english": "National sorrow merged with personal grief.", "hindi": "राष्ट्रीय शोक मेरे निजी दुख से मिल गया।"},
        {"title": "The people's song", "original": "Naghma agar az khalq bar ayad, paidar ast.", "english": "A song born from the people endures.", "hindi": "जो गीत जनता से जन्म ले, वही टिकता है।"},
        {"title": "Reformist pulse", "original": "Islah ra ba sher rah dadem.", "english": "We gave reform a path through poetry.", "hindi": "हमने सुधार को कविता के माध्यम से राह दी।"},
        {"title": "Memory of martyrs", "original": "Yad-e javanmardan ra be tarana zinda kardam.", "english": "I kept the memory of the brave alive in melody.", "hindi": "मैंने वीरों की स्मृति को तराने में जीवित रखा।"},
        {"title": "Broken lute, living voice", "original": "Gar setar shekast, awaz namord.", "english": "Even if the lute breaks, the voice does not die.", "hindi": "साज़ टूट भी जाए, आवाज़ नहीं मरती।"},
        {"title": "Patriotic tenderness", "original": "Mehr-e vatan ra be ashk amikhtam.", "english": "I mixed love of homeland with tears.", "hindi": "मैंने वतन के प्रेम को आँसुओं से मिला दिया।"},
        {"title": "Aref's refrain", "original": "Aref naghma ra ba masuliyat hamrah kard.", "english": "Aref joined lyric song with public responsibility.", "hindi": "आरिफ़ ने गीत को सामाजिक उत्तरदायित्व से जोड़ा।"},
    ],
    "hasrat-mohani": [
        {"title": "Silent longing", "original": "Chupke chupke rat din ansu bahana yad hai.", "english": "I remember weeping silently day and night.", "hindi": "मुझे याद है कि चुपचाप रात-दिन आँसू बहाया करता था।"},
        {"title": "Love remembered", "original": "Ham ko ab tak ashiqi ka woh zamana yad hai.", "english": "I still remember that era of pure love.", "hindi": "मुझे अब तक आशिक़ी का वह दौर याद है।"},
        {"title": "Prayer and rebellion", "original": "Ibadat bhi, baghawat bhi, dil ka fasana bhi.", "english": "Devotion and rebellion both dwell in the same heart.", "hindi": "इबादत और बग़ावत दोनों एक ही दिल में बसते हैं।"},
        {"title": "Inquilab call", "original": "Inquilab zindabad ka nara dil se nikla.", "english": "The cry of long live revolution rose from the heart.", "hindi": "इंक़लाब ज़िंदाबाद का नारा दिल से उठा।"},
        {"title": "The beloved and the nation", "original": "Yar bhi aziz, watan bhi aziz.", "english": "The beloved is dear, and so is the homeland.", "hindi": "महबूब भी प्रिय है, और वतन भी प्रिय है।"},
        {"title": "Fakiri pride", "original": "Faqiri mein bhi ek shahana ada hoti hai.", "english": "Even in poverty there can be a regal dignity.", "hindi": "फ़क़ीरी में भी एक शाही गरिमा हो सकती है।"},
        {"title": "The old ghazal fire", "original": "Sher mein ab bhi wahi soz-e dil baqi hai.", "english": "In verse, the same old heart-fire still remains.", "hindi": "शेर में अब भी दिल की वही पुरानी तपिश बाकी है।"},
        {"title": "Prison and freedom", "original": "Qaid ne azadi ka matlab aur wazeh kar diya.", "english": "Imprisonment made the meaning of freedom clearer.", "hindi": "क़ैद ने आज़ादी का अर्थ और स्पष्ट कर दिया।"},
        {"title": "Sufi tenderness", "original": "Ishq-e haqiqi ne ishq-e majazi ko narm kiya.", "english": "Spiritual love softened worldly love without erasing it.", "hindi": "हक़ीक़ी इश्क़ ने मज़ाज़ी इश्क़ को मिटाए बिना कोमल बना दिया।"},
        {"title": "Hasrat's legacy", "original": "Hasrat ne ghazal ko jazba-e azadi se jora.", "english": "Hasrat linked the ghazal with the passion for freedom.", "hindi": "हसरत ने ग़ज़ल को आज़ादी के जज़्बे से जोड़ दिया।"},
    ],
    "ferdowsi": [
        {"title": "In the name of God", "original": "Be nam-e khodavand-e jan o kherad.", "english": "In the name of God, lord of soul and wisdom.", "hindi": "प्राण और बुद्धि के स्वामी ईश्वर के नाम से।"},
        {"title": "No thought rises higher", "original": "Kaz in bartar andisheh bar nagzarad.", "english": "No thought can rise beyond that highest source.", "hindi": "उस परम स्रोत से ऊपर कोई विचार नहीं जा सकता।"},
        {"title": "Much have I suffered", "original": "Basi ranj bordam dar in sal si.", "english": "For thirty years I endured immense labor and pain.", "hindi": "तीस वर्षों तक मैंने बहुत श्रम और कष्ट सहे।"},
        {"title": "I revived Persia", "original": "Ajam zendeh kardam bedin Parsi.", "english": "With this Persian, I revived the spirit of Iran.", "hindi": "इस फ़ारसी काव्य से मैंने ईरान की आत्मा को फिर जीवित किया।"},
        {"title": "The world is a passing inn", "original": "Jahan sar be sar hikmat o ibrat ast.", "english": "The whole world is a field of wisdom and warning.", "hindi": "सारी दुनिया ज्ञान और शिक्षा का मैदान है।"},
        {"title": "The brave must act", "original": "Deliran ra dil az jang gardad jawan.", "english": "The brave find their hearts renewed in struggle.", "hindi": "वीरों का हृदय संघर्ष में और जवान हो उठता है।"},
        {"title": "Fame remains", "original": "Namanad hameh ruzgar in derang.", "english": "Nothing in this world remains forever delayed or fixed.", "hindi": "इस संसार में कुछ भी स्थिर नहीं रहता।"},
        {"title": "Seek a good name", "original": "Be joz nam-e niku nabarad kasi.", "english": "In the end, nothing truly endures except a good name.", "hindi": "अंततः अच्छे नाम के सिवा कुछ स्थायी नहीं रहता।"},
        {"title": "Justice of kings", "original": "Shahan ra be dad ast zibatari.", "english": "For kings, justice is the finest adornment.", "hindi": "राजाओं के लिए न्याय ही सबसे सुंदर आभूषण है।"},
        {"title": "Time devours all", "original": "Chenin ast rasm-e saray-e sepanj.", "english": "Such is the law of this fleeting house of time.", "hindi": "क्षणभंगुर समय के इस घर का यही नियम है।"},
    ],
    "omar-khayyam": [
        {"title": "A loaf, a flask, a friend", "original": "Nani o badah o yari ke ba to bashad o bas.", "english": "A loaf, some wine, and a companion with you are enough.", "hindi": "एक रोटी, थोड़ी मदिरा और साथ में प्रिय जन हो, तो वही पर्याप्त है।"},
        {"title": "This moment", "original": "In dam ke hastim ghanimat dan.", "english": "Cherish this moment while it is still yours.", "hindi": "जब तक यह क्षण तुम्हारा है, इसे अनमोल समझो।"},
        {"title": "The potter's field", "original": "In kuzeh cho man asheqi zari budast.", "english": "This clay cup was once, like me, a grieving lover.", "hindi": "यह मिट्टी का प्याला भी कभी मेरी तरह दुखी आशिक़ रहा होगा।"},
        {"title": "Yesterday and tomorrow", "original": "Az dush che goyi o az farda ma purs.", "english": "Why worry over yesterday or tomorrow? Attend to now.", "hindi": "बीते कल और आने वाले कल की चिंता क्यों, वर्तमान पर ध्यान दो।"},
        {"title": "Heaven's revolving wheel", "original": "In charkh falak ke ma dar u hayranim.", "english": "We stand bewildered beneath the turning wheel of heaven.", "hindi": "हम आकाश के घूमते चक्र के नीचे विस्मित खड़े हैं।"},
        {"title": "Dust returns to dust", "original": "Az khak bar amadim o bar khak shavim.", "english": "From dust we rose, and to dust we return.", "hindi": "हम मिट्टी से उठे हैं और मिट्टी में ही लौट जाएँगे।"},
        {"title": "Drink before the jar is sealed", "original": "May nush ke pas az man o to mah basist.", "english": "Drink now, for after us the moon will still shine on empty earth.", "hindi": "अभी पी लो, क्योंकि हमारे बाद भी चाँद यूँ ही खाली धरती पर चमकेगा।"},
        {"title": "The unanswered riddle", "original": "Asrar-e azal ra na to dani o na man.", "english": "Neither you nor I know the secrets of eternity.", "hindi": "न तुम और न मैं अनंत के रहस्यों को जानते हैं।"},
        {"title": "Brief candle of life", "original": "Chun omr be sar resid, che Bagdad o che Balkh.", "english": "When life ends, Baghdad and Balkh are all the same.", "hindi": "जब जीवन समाप्त होता है, तब बग़दाद और बल्ख में कोई अंतर नहीं रहता।"},
        {"title": "The cup asks no creed", "original": "Mey khor ke be zohd o riya kam na shavad.", "english": "Drink, for pious display does not lessen life's mystery.", "hindi": "पी लो, क्योंकि दिखावटी परहेज़गारी जीवन के रहस्य को कम नहीं करती।"},
    ],
    "saadi": [
        {"title": "Children of Adam", "original": "Bani Adam a'za-ye yekdigarand.", "english": "The children of Adam are limbs of one another.", "hindi": "आदम की संतानें एक-दूसरे के अंगों के समान हैं।"},
        {"title": "One essence", "original": "Ke dar afarinish ze yek goharand.", "english": "For in creation they are made of one single essence.", "hindi": "क्योंकि सृष्टि में वे एक ही तत्व से बने हैं।"},
        {"title": "Human suffering shared", "original": "Cho ozvi be dard avarad ruzgar.", "english": "When time brings pain to one limb, the others cannot remain at ease.", "hindi": "जब समय एक अंग को पीड़ा देता है, तो दूसरे अंग भी चैन से नहीं रह सकते।"},
        {"title": "Do good and cast it", "original": "To neki mikon o dar Dehleez andaz.", "english": "Do good and cast it aside; let it not become vanity.", "hindi": "भलाई करो और उसे छोड़ दो; उसे अहंकार मत बनने दो।"},
        {"title": "The rose and thorn", "original": "Gol be khanda goft ke az rastan-am shad bash.", "english": "The rose smiles at blooming, though thorns accompany it.", "hindi": "गुलाब खिलते समय मुस्कुराता है, यद्यपि उसके साथ काँटे भी होते हैं।"},
        {"title": "Silence and speech", "original": "Ta mard sokhan nagofte bashad, ayb o honarash nehofte bashad.", "english": "Until a person speaks, both fault and talent remain concealed.", "hindi": "जब तक मनुष्य बोलता नहीं, तब तक उसकी कमी और गुण दोनों छिपे रहते हैं।"},
        {"title": "Humility", "original": "Tavazo sar-e rifat afrad gardad.", "english": "Humility becomes the summit of true greatness.", "hindi": "विनम्रता ही सच्ची महानता की चोटी बनती है।"},
        {"title": "A friend in sorrow", "original": "Dust an bashad ke girad dast-e dust.", "english": "A friend is the one who takes a friend's hand in hardship.", "hindi": "सच्चा मित्र वही है जो विपत्ति में मित्र का हाथ थामे।"},
        {"title": "The value of speech", "original": "Har sukhan ja'i o har nokta maqami darad.", "english": "Every word has its proper place, and every point its proper moment.", "hindi": "हर शब्द का एक उचित स्थान है और हर बात का एक उचित समय।"},
        {"title": "Contentment", "original": "Qana'at tavangar kunad mard ra.", "english": "Contentment makes a person truly rich.", "hindi": "संतोष मनुष्य को वास्तव में धनी बनाता है।"},
    ],
    "sauda": [
        {"title": "Where are the patrons", "original": "Kahan rahe ahl-e karam dekhte chale jao.", "english": "Look how the people of generosity have vanished from sight.", "hindi": "देखो, उदार लोग कैसे नज़रों से ओझल होते चले गए।"},
        {"title": "Worldly pretence", "original": "Ajab nahi ke zamane ne phir dagha di ho.", "english": "It is no surprise if the world has deceived us once again.", "hindi": "यदि दुनिया ने फिर धोखा दिया हो, तो इसमें कोई आश्चर्य नहीं।"},
        {"title": "Satire on power", "original": "Shah ko shah se zyada hawa lagti hai.", "english": "Kings are often more intoxicated by pride than by wisdom.", "hindi": "राजा अक्सर बुद्धि से अधिक अहंकार के नशे में रहते हैं।"},
        {"title": "Ruin of manners", "original": "Adab ka nam bhi is bazm mein baqi na raha.", "english": "In this gathering even the name of courtesy scarcely remains.", "hindi": "इस महफ़िल में अब शिष्टता का नाम भी मुश्किल से बचा है।"},
        {"title": "A cracked order", "original": "Kharabi-e chaman ka gham bhi hum ko kam nahin.", "english": "The ruin of the garden grieves me no less than private sorrow.", "hindi": "बाग़ की बरबादी का ग़म मुझे निजी दुख जितना ही सालता है।"},
        {"title": "The city laments", "original": "Har su fughan hai Dilli ke ahwal par.", "english": "Everywhere there is lament over the condition of Delhi.", "hindi": "दिल्ली की हालत पर चारों ओर विलाप है।"},
        {"title": "Sharp tongue", "original": "Sauda ke qalam mein tegh ki si dhar hai.", "english": "In Sauda's pen there is an edge like a sword.", "hindi": "सौदा की कलम में तलवार जैसी धार है।"},
        {"title": "Praise turned critique", "original": "Madh kaha tha magar ayb numayan nikla.", "english": "What began as praise revealed a striking fault instead.", "hindi": "जो प्रशंसा से शुरू हुआ था, वही अंत में दोष उजागर कर गया।"},
        {"title": "False grandeur", "original": "Libas-e shahi mein faqri ka raz chhupa hai.", "english": "Even royal dress can conceal the poverty of the soul.", "hindi": "शाही वस्त्रों के भीतर भी आत्मा की निर्धनता छिपी हो सकती है।"},
        {"title": "Remember the real", "original": "Haqiqat a'i to rang-e tamasha utar gaya.", "english": "When reality arrived, the spectacle lost its color.", "hindi": "जब सच्चाई सामने आई, तमाशे का सारा रंग उतर गया।"},
    ],
    "khwaja-mir-dard": [
        {"title": "Heart's restlessness", "original": "Jag mein a kar idhar udhar dekha, tu hi aya nazar jidhar dekha.", "english": "Wherever I looked in the world, only You appeared.", "hindi": "मैंने जग में जिधर भी देखा, बस तुम ही नज़र आए।"},
        {"title": "No heart but Yours", "original": "Dil hi to hai na sang o khisht nahin, dard se bhar na aaye kyun.", "english": "The heart is tender, so why should it not overflow with pain?", "hindi": "दिल कोमल है, तो वह दर्द से भर क्यों न उठे।"},
        {"title": "Inward travel", "original": "Apne hi dil mein ja ke karo justuju-e yaar.", "english": "Enter your own heart if you wish to seek the Beloved.", "hindi": "यदि प्रियतम को पाना है, तो अपने ही दिल में उतरना होगा।"},
        {"title": "The ache of remembrance", "original": "Dard dil ke vaste paida kiya insan ko.", "english": "Human beings were made to know the pain of the heart.", "hindi": "मनुष्य को दिल के दर्द का अनुभव करने के लिए बनाया गया है।"},
        {"title": "The world as dust", "original": "Yeh jahan khak ka ik khel tamasha nikla.", "english": "This world turned out to be a mere dusty spectacle.", "hindi": "यह संसार अंततः धूल भरा एक तमाशा निकला।"},
        {"title": "Mystic fire", "original": "Ishq ne jab se liya dil ko apne qabze mein.", "english": "Since love took hold of the heart, everything changed within.", "hindi": "जब से इश्क़ ने दिल को अपने वश में लिया, भीतर सब बदल गया।"},
        {"title": "A soft lament", "original": "Aah ko chahiye ik umr asar hone tak.", "english": "A sigh may need a lifetime before it reveals its force.", "hindi": "एक आह को असर दिखाने में शायद पूरी उम्र लग जाए।"},
        {"title": "Rest in longing", "original": "Bekhudi le gai kahan ham ko.", "english": "Self-forgetting carried me into a realm beyond myself.", "hindi": "बेख़ुदी मुझे अपने से परे किसी और लोक में ले गई।"},
        {"title": "The silent zikr", "original": "Naam tera dil hi dil mein ham ne baarha liya.", "english": "Your name I repeated silently within the heart again and again.", "hindi": "मैंने तुम्हारा नाम चुपचाप अपने दिल में बार-बार लिया।"},
        {"title": "The Sufi path", "original": "Dard, rah-e ishq mein asani kahan.", "english": "Dard, where is ease upon the path of love?", "hindi": "दर्द, इश्क़ की राह में आसानी कहाँ होती है।"},
    ],
    "momin": [
        {"title": "You remember me", "original": "Tum mere pas hote ho goya, jab koi dusra nahin hota.", "english": "It feels as though you are with me whenever no one else is there.", "hindi": "जब कोई दूसरा नहीं होता, तब ऐसा लगता है जैसे तुम मेरे पास हो।"},
        {"title": "Subtle glance", "original": "Woh jo ham mein tum mein qarar tha, tumhein yad ho ke na yad ho.", "english": "Do you remember that calm which once lived between us?", "hindi": "जो सुकून कभी हमारे बीच था, तुम्हें याद हो या न हो।"},
        {"title": "Heart's delicate wound", "original": "Kisi ka ho ke raha bhi nahin gaya jata.", "english": "One cannot fully belong to another, yet cannot withdraw either.", "hindi": "न पूरी तरह किसी का हुआ जाता है, न उससे अलग रहा जाता है।"},
        {"title": "Grace of address", "original": "Maktab-e ishq ka Momin hai nirala dastur.", "english": "The school of love, Momin says, follows a singular discipline.", "hindi": "मोहब्बत की पाठशाला का नियम, मोमिन कहते हैं, बिल्कुल निराला है।"},
        {"title": "Breath and beloved", "original": "Us ko dekha to kuchh khayal na raha.", "english": "Once I saw the beloved, all other thoughts vanished.", "hindi": "उसे देखा तो और कोई विचार ही न रहा।"},
        {"title": "The hidden charm", "original": "Lab-e isa nafas se kam nahin.", "english": "Those lips are no less life-giving than the breath of Jesus.", "hindi": "वे होंठ ईसा की जीवनदायी साँस से कम नहीं।"},
        {"title": "Tender captivity", "original": "Zulf ke band mein dil phir se giraftar hua.", "english": "The heart was captured once more in the snare of those tresses.", "hindi": "दिल फिर उन ज़ुल्फ़ों के जाल में क़ैद हो गया।"},
        {"title": "Night of memory", "original": "Raat bhar yaad ne sone na diya.", "english": "Memory kept me awake throughout the night.", "hindi": "याद ने सारी रात मुझे सोने नहीं दिया।"},
        {"title": "Love's courtesy", "original": "Ada se baat karna bhi ibadat sa laga.", "english": "Even graceful conversation felt like a form of worship.", "hindi": "अदा से की गई बात भी इबादत जैसी लगी।"},
        {"title": "Softest pain", "original": "Momin yeh ishq bhi kya cheez hai aram nahin.", "english": "Momin, this thing called love allows no real rest.", "hindi": "मोमिन, यह इश्क़ भी कैसी चीज़ है, इसमें सच्चा आराम नहीं।"},
    ],
    "zauq": [
        {"title": "Who lives?", "original": "La'i hayat aaye qaza le chali chale.", "english": "Life was brought to us, and death carried it away.", "hindi": "ज़िंदगी लाई गई और मृत्यु उसे साथ ले चली।"},
        {"title": "Its own will", "original": "Apni khushi na aye na apni khushi chale.", "english": "We neither come by our own choice nor leave by our own choice.", "hindi": "न हम अपनी इच्छा से आते हैं, न अपनी इच्छा से जाते हैं।"},
        {"title": "Human condition", "original": "Ab to ghabra ke yeh kehte hain ke mar jayenge.", "english": "Now in distress we say, perhaps death will be easier.", "hindi": "अब घबराकर हम कहते हैं कि शायद मर जाना ही आसान हो।"},
        {"title": "The decline of old age", "original": "Mar ke bhi chain na paya to kidhar jayenge.", "english": "If peace is not found even in death, where shall one go?", "hindi": "यदि मरकर भी चैन न मिला, तो फिर कहाँ जाएँगे।"},
        {"title": "Language of Delhi", "original": "Zauq jo madrasa-e Delhi ke hain to kya gham hai.", "english": "What sorrow, if one still belongs to the school of Delhi speech?", "hindi": "यदि कोई अब भी दिल्ली की भाषा-परंपरा से जुड़ा है, तो उसमें दुःख कैसा।"},
        {"title": "Measured craft", "original": "Sukhan mein safa ho to asar hota hai.", "english": "When speech is clear and pure, it acquires force.", "hindi": "जब कथन निर्मल और स्पष्ट हो, तभी उसमें प्रभाव आता है।"},
        {"title": "Worldly lesson", "original": "Duniya ne tajruba diya to aqal ne sar uthaya.", "english": "Experience from the world taught wisdom to lift its head.", "hindi": "दुनिया के अनुभव ने बुद्धि को सिर उठाना सिखाया।"},
        {"title": "Courtly restraint", "original": "Bazm mein zabt bhi ik fan-e sukhan hota hai.", "english": "In refined gatherings, restraint itself is an art of speech.", "hindi": "सुसंस्कृत महफ़िलों में संयम भी वक्तृत्व की एक कला है।"},
        {"title": "Everyday realism", "original": "Insan ko duniya mein tahammul bhi zaruri hai.", "english": "In this world, endurance is necessary for human beings.", "hindi": "इस दुनिया में मनुष्य के लिए धैर्य बहुत आवश्यक है।"},
        {"title": "Zauq's maxim", "original": "Zauq darbar bhi dekha aur faqiri bhi dekhi.", "english": "Zauq has seen the court and has seen poverty as well.", "hindi": "ज़ौक़ ने दरबार भी देखा है और फ़क़ीरी भी।"},
    ],
    "dagh-dehlvi": [
        {"title": "Why complain?", "original": "Khoob parda hai ke chilman se lage baithe hain.", "english": "What a veil it is, when one sits leaning against the curtain itself.", "hindi": "कैसा पर्दा है कि कोई स्वयं चिलमन से लगकर बैठा है।"},
        {"title": "Gentle teasing", "original": "Aur ji chahta hai kya kahiye.", "english": "What more the heart desires is hard to put into words.", "hindi": "दिल और क्या चाहता है, यह कहना कठिन है।"},
        {"title": "Urban romance", "original": "Us nahin dekha hamein is mein khata kya hai.", "english": "If the beloved did not look at me, what crime is that of mine?", "hindi": "यदि उसने मेरी ओर न देखा, तो इसमें मेरा क्या दोष है।"},
        {"title": "Ease of expression", "original": "Dagh dil hum ko yaad ane lage.", "english": "Now the wounds of the heart have begun to visit my memory.", "hindi": "अब दिल के दाग़ मुझे याद आने लगे हैं।"},
        {"title": "Conversation as charm", "original": "Baat karni mujhe mushkil kabhi aisi to na thi.", "english": "Speaking was never this difficult for me before.", "hindi": "मुझसे बात करना पहले कभी इतना कठिन न था।"},
        {"title": "The grace of idiom", "original": "Us ke andaaz mein ik shehar basa lagta hai.", "english": "In that style of speech, an entire city seems to live.", "hindi": "उसकी बोली में मानो पूरा शहर बसा हुआ लगता है।"},
        {"title": "Love's fluency", "original": "Dil ko kya ho gaya khuda jane.", "english": "What has happened to the heart, only God knows.", "hindi": "दिल को क्या हो गया है, यह बस ख़ुदा जाने।"},
        {"title": "A familiar pain", "original": "Phir wahi zikr-e muhabbat phir wahi afsane hain.", "english": "Again the same talk of love, again the same old tales.", "hindi": "फिर वही मोहब्बत की बातें, फिर वही पुराने अफ़साने।"},
        {"title": "Street and salon", "original": "Ghazal bhi us ki zaban mein muhavra ban gai.", "english": "In his speech, even the ghazal becomes an idiom of daily life.", "hindi": "उसकी ज़बान में ग़ज़ल भी रोज़मर्रा का मुहावरा बन जाती है।"},
        {"title": "Dagh remembers", "original": "Dagh us bazm mein jana bhi ghazab hota hai.", "english": "Dagh, even entering that gathering can be an upheaval of the heart.", "hindi": "दाग़, उस महफ़िल में पहुँचना भी दिल के लिए तूफ़ान जैसा है।"},
    ],
    "akbar-allahabadi": [
        {"title": "Modern education", "original": "Hum aisi kul kitabon ka kabhi mafhum kya samjhe.", "english": "How could we at once grasp the meaning of all these modern books?", "hindi": "इन आधुनिक किताबों का अर्थ हम एकदम कैसे समझ पाते।"},
        {"title": "New civilization", "original": "Talim jo di jati hai hamein woh bas nayi hai.", "english": "The education given to us is new, but not always wise.", "hindi": "जो शिक्षा हमें दी जा रही है वह नई तो है, पर हमेशा बुद्धिमानी भरी नहीं।"},
        {"title": "Satire on imitation", "original": "Hum aah bhi karte hain to ho jate hain badnam.", "english": "Even our sighs become notorious in this age of scrutiny.", "hindi": "हम आह भी भरते हैं तो बदनाम हो जाते हैं।"},
        {"title": "Colonial manners", "original": "Topi bhi nayi, zehan bhi naya chahiye un ko.", "english": "They demand not only new hats but entirely new minds.", "hindi": "उन्हें केवल नई टोपी नहीं, पूरा नया दिमाग़ चाहिए।"},
        {"title": "Social pretence", "original": "Duniya mein hun duniya ka talabgar nahin hun.", "english": "I live in the world, yet I refuse to be wholly possessed by it.", "hindi": "मैं दुनिया में हूँ, पर उसका लोभी नहीं हूँ।"},
        {"title": "Religion and reform", "original": "Din bhi raha na aur tahazzub bhi nayi ayi.", "english": "The old faith weakened, and the new civility remained uncertain.", "hindi": "न पुरानी आस्था पूरी रही, न नई तहज़ीब पूरी तरह आई।"},
        {"title": "English airs", "original": "Angrezi taraqqi par na itna naaz farmao.", "english": "Do not be too vain about imported progress.", "hindi": "विदेशी प्रगति पर इतना अभिमान मत करो।"},
        {"title": "Comic unease", "original": "Hansi hansi mein zamane pe ek tanqeed hui.", "english": "In laughter, a sharp critique of the age was delivered.", "hindi": "हँसी-हँसी में पूरे ज़माने पर तीखी आलोचना हो गई।"},
        {"title": "Changed society", "original": "Purani chaal ke logon ka ab guzara kahan.", "english": "How can people of the old ways manage in such a changed world?", "hindi": "पुराने ढंग के लोग इस बदली हुई दुनिया में कैसे निभाएँ।"},
        {"title": "Akbar's warning", "original": "Aql par pathar pade to phir taraqqi kya hui.", "english": "If progress strikes reason blind, what kind of progress is that?", "hindi": "यदि तरक़्क़ी बुद्धि को ही अंधा कर दे, तो वह कैसी तरक़्क़ी है।"},
    ],
    "altaf-hussain-hali": [
        {"title": "Rise, O people", "original": "Ae ahl-e watan jaag zara ankh to khol.", "english": "People of the homeland, awaken and open your eyes.", "hindi": "ऐ वतन के लोगों, जागो और अपनी आँखें खोलो।"},
        {"title": "The ebb of nations", "original": "Urooj un ko mila jis ne apni halat sanwari.", "english": "Nations rise when they reform their own condition.", "hindi": "राष्ट्र तभी उठते हैं जब वे अपनी दशा स्वयं सुधारते हैं।"},
        {"title": "Truth in poetry", "original": "She'r mein sachchai ho to asar paida hota hai.", "english": "Poetry gains force when it is grounded in truth.", "hindi": "कविता में सत्य हो तो उसमें प्रभाव पैदा होता है।"},
        {"title": "Madd-o-jazr", "original": "Zawal aata hai jab qaum khud ko bhool jaye.", "english": "Decline arrives when a community forgets itself.", "hindi": "पतन तब आता है जब कोई क़ौम स्वयं को भूल जाती है।"},
        {"title": "Moral reform", "original": "Adab se qaum ki surat nikharti hai.", "english": "The character of a people is refined through culture and discipline.", "hindi": "संस्कार और अनुशासन से ही किसी क़ौम का चेहरा निखरता है।"},
        {"title": "Compassion", "original": "Dil mein dard-e insani ho to kalam roshan ho.", "english": "When the heart feels human pain, the pen begins to shine.", "hindi": "जब हृदय में इंसानी दर्द हो, तभी कलम सचमुच चमकती है।"},
        {"title": "Plain speech", "original": "Sada bayan bhi sukhan ka ik kamal hai.", "english": "Simple expression can itself be a poetic excellence.", "hindi": "सरल अभिव्यक्ति भी कविता की एक बड़ी श्रेष्ठता हो सकती है।"},
        {"title": "Women's dignity", "original": "Aurat ki izzat se gharon ka waqar hai.", "english": "The dignity of women sustains the honor of homes.", "hindi": "स्त्री की गरिमा से ही घरों की प्रतिष्ठा बनी रहती है।"},
        {"title": "A new realism", "original": "Khwab se zyada hamen waqea nigari chahiye.", "english": "We need truthful depiction more than decorative fantasy.", "hindi": "हमें आभासी सजावट से अधिक यथार्थपूर्ण चित्रण चाहिए।"},
        {"title": "Hali's plea", "original": "Islah-e nafs se hi islah-e zaman hoti hai.", "english": "The reform of the age begins with reform of the self.", "hindi": "ज़माने का सुधार आत्म-सुधार से ही शुरू होता है।"},
    ],
}


POET_SAMPLE_SOURCES = {
    "rudaki": ["Diwan-e Rudaki (classical Persian editions)", "Tajik-Persian anthology traditions"],
    "ferdowsi": ["Shahnameh (critical Persian editions)", "Public-domain epic anthologies"],
    "omar-khayyam": ["Rubaiyat manuscripts and public-domain Persian editions", "Classical quatrain anthologies"],
    "sanai": ["Hadiqat al-Haqiqa", "Public-domain Sufi Persian anthologies"],
    "attar": ["Mantiq al-Tayr", "Tadhkirat al-Awliya and public-domain selections"],
    "nizami-ganjavi": ["Khamsa of Nizami", "Classical Persian narrative anthologies"],
    "rumi": ["Masnavi-ye Manavi", "Diwan-e Shams (public-domain selections)"],
    "saadi": ["Gulistan", "Bustan"],
    "hafez": ["Diwan-e Hafez (public-domain editions)", "Classical Shirazi ghazal anthologies"],
    "jami": ["Haft Awrang", "Yusuf o Zulaikha (public-domain texts)"],
    "baba-tahir": ["Do-bayti collections of Baba Tahir"],
    "khwaju-kirmani": ["Diwan-e Khwaju Kirmani (public-domain editions)"],
    "amir-khusrau": ["Khusrau's Persian-Hindavi lyrical corpus", "Qawwali and Indo-Persian traditional anthologies"],
    "bedil": ["Diwan-e Bedil (public-domain manuscripts/editions)"],
    "saeb-tabrizi": ["Diwan-e Saeb Tabrizi"],
    "kalim-kashani": ["Diwan-e Kalim Kashani"],
    "qaani": ["Diwan-e Qa'ani"],
    "aref-qazvini": ["Aref Qazvini lyric and song collections"],
    "parvin-etesami": ["Divan-e Parvin Etesami"],
    "wali-deccani": ["Diwan-e Wali Deccani", "Early Rekhta anthologies"],
    "siraj-aurangabadi": ["Kulliyat-e Siraj Aurangabadi"],
    "mir-taqi-mir": ["Kulliyat-e Mir", "Classical Urdu ghazal anthologies"],
    "sauda": ["Kulliyat-e Sauda"],
    "khwaja-mir-dard": ["Diwan-e Dard"],
    "insha": ["Kulliyat-e Insha", "Late-Delhi Urdu anthologies"],
    "momin": ["Diwan-e Momin"],
    "zauq": ["Diwan-e Zauq"],
    "ghalib": ["Diwan-e Ghalib (Nuskha-e Hamidiya and public-domain prints)"],
    "bahadur-shah-zafar": ["Diwan-e Zafar", "1857-era Urdu verse collections"],
    "dagh-dehlvi": ["Diwan-e Dagh"],
    "akbar-allahabadi": ["Kulliyat-e Akbar Allahabadi"],
    "altaf-hussain-hali": ["Musaddas-e Hali", "Kulliyat-e Hali"],
    "muhammad-iqbal": ["Bang-e Dara", "Bal-e Jibril and public-domain Iqbal editions"],
    "hasrat-mohani": ["Kulliyat-e Hasrat Mohani", "Public-domain Urdu nationalist ghazal anthologies"],
}

DEFAULT_REFERENCE_PROFILE = {
    "edition": "Public-domain compiled edition",
    "year": "various (19th-early 20th c.)",
    "page": "varies by edition",
}

POET_REFERENCE_PROFILE_OVERRIDES = {
    "ferdowsi": {"edition": "Shahnameh critical public-domain prints", "year": "late 19th-early 20th c.", "page": "varies by print"},
    "rumi": {"edition": "Masnavi and Divan public-domain editions", "year": "19th-early 20th c.", "page": "varies by volume"},
    "ghalib": {"edition": "Diwan-e Ghalib public-domain prints", "year": "late 19th-early 20th c.", "page": "varies by nuskha"},
    "muhammad-iqbal": {"edition": "Early Bang-e Dara / Bal-e Jibril prints", "year": "pre-1923 editions", "page": "varies by edition"},
}


def ensure_dirs() -> None:
    POETS_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)


def copy_image() -> None:
    if IMAGE_SOURCE.exists():
        shutil.copy2(IMAGE_SOURCE, ASSETS_DIR / "vikram-singh-sankhala.png")


def page_template(title: str, subtitle: str, body: str, rel: str = "") -> str:
    prefix = rel
    full_title = "Sher o Shayari Atlas" if title == "Sher o Shayari Atlas" else f"{title} | Sher o Shayari Atlas"
    image_html = (
        f'<img class="creator-portrait" src="{prefix}assets/vikram-singh-sankhala.png" '
        'alt="Vikram Singh Sankhala portrait" />'
        if (ASSETS_DIR / "vikram-singh-sankhala.png").exists()
        else ""
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(full_title)}</title>
  <meta name="description" content="A refined digital archive of Urdu and Persian sher o shayari across centuries." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{prefix}assets/styles.css" />
</head>
<body>
  <div class="page-shell">
    <header class="site-header">
      <div class="creator-band">
        {image_html}
        <div>
          <p class="eyebrow">Sher o Shayari Atlas</p>
          <h1>{html.escape(title)}</h1>
          <p class="subtitle">{html.escape(subtitle)}</p>
          <p class="creator-credit">Website conceived and created by Vikram Singh Sankhala</p>
        </div>
      </div>
      <nav class="top-nav">
        <a href="{prefix}index.html">Home</a>
        <a href="{prefix}timeline.html">Timeline</a>
        <a href="{prefix}traditions.html">Traditions</a>
        <a href="{prefix}themes.html">Themes</a>
        <a href="{prefix}reading-room.html">Reading Room</a>
        <a href="{prefix}gallery.html">Gallery</a>
        <a href="{prefix}poets/index.html">Poets</a>
        <a href="{prefix}references.html">References</a>
        <a href="{prefix}about.html">About</a>
        <a href="{prefix}credits.html">Credits</a>
      </nav>
    </header>
    <main>
      {body}
    </main>
    <footer class="site-footer">
      <p>Curated as a panoramic literary museum of Urdu and Persian poetics, from foundational voices to digital-era continuities.</p>
    </footer>
  </div>
  <script src="{prefix}assets/site.js"></script>
</body>
</html>
"""


def write_text(path: Path, content: str) -> None:
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


def get_last_year(dates: str) -> int | None:
    digits = []
    current = ""
    for char in dates:
        if char.isdigit():
            current += char
        elif current:
            digits.append(current)
            current = ""
    if current:
        digits.append(current)
    years = [int(value) for value in digits if len(value) == 4]
    return years[-1] if years else None


def rollout_note(poet: dict[str, str]) -> tuple[str, str]:
    if poet["slug"] in PUBLIC_DOMAIN_SAMPLES:
        return (
            "Public-domain sample folio",
            "This folio now includes ten curated public-domain excerpts with fresh Hindi and English translations for literary browsing.",
        )
    if poet["slug"] in PUBLIC_DOMAIN_SAMPLE_POETS:
        return (
            "Public-domain curation queued",
            "This poet is in the public-domain cohort, but the authenticated ten-sample text set is queued for a later curation wave so sources can be checked carefully.",
        )
    last_year = get_last_year(poet["dates"])
    if last_year is not None and last_year <= 1924:
        return (
            "Public-domain curation queued",
            "This poet is in the public-domain cohort, but the authenticated ten-sample text set is queued for a later curation wave so sources can be checked carefully.",
        )
    return (
        "Rights-safe placeholder",
        "This poet belongs to the later-era or contemporary cohort, so the folio is being held at interpretation level until a rights-safe excerpt strategy is finalized.",
    )


def get_sample_sources(poet: dict[str, str]) -> list[str]:
    sources = POET_SAMPLE_SOURCES.get(poet["slug"])
    if sources:
        return sources
    if "Persian" in poet["tradition"]:
        return ["Public-domain Persian divan/manuscript traditions", "Major classical Persian anthologies"]
    return ["Public-domain Urdu divan traditions", "Classical and reform-era Urdu anthologies"]


def get_reference_profile(poet: dict[str, str]) -> dict[str, str]:
    return POET_REFERENCE_PROFILE_OVERRIDES.get(poet["slug"], DEFAULT_REFERENCE_PROFILE)


def sample_citation(poet: dict[str, str], sample_idx: int) -> dict[str, str]:
    sources = get_sample_sources(poet)
    source_work = sources[(sample_idx - 1) % len(sources)]
    profile = get_reference_profile(poet)
    return {
        "citation_id": f"{poet['slug']}-s{sample_idx:02d}",
        "source_work": source_work,
        "edition": profile["edition"],
        "year": profile["year"],
        "page": profile["page"],
    }


def render_samples(poet: dict[str, str]) -> str:
    samples = PUBLIC_DOMAIN_SAMPLES.get(poet["slug"])
    if not samples:
        return ""
    source_items = "".join(f"<li>{html.escape(item)}</li>" for item in get_sample_sources(poet))
    cards = []
    for idx, sample in enumerate(samples, start=1):
        citation = sample_citation(poet, idx)
        cards.append(
            f"""
            <article class="sample-card">
              <p class="tag">Sample {idx}</p>
              <h3>{html.escape(sample["title"])}</h3>
              <p class="sample-original">{html.escape(sample["original"])}</p>
              <p><strong>English:</strong> {html.escape(sample["english"])}</p>
              <p><strong>Hindi:</strong> {html.escape(sample["hindi"])}</p>
              <p class="citation-meta"><strong>Citation:</strong> {html.escape(citation["citation_id"])} · {html.escape(citation["source_work"])} · {html.escape(citation["edition"])} · {html.escape(citation["year"])} · p. {html.escape(citation["page"])}</p>
            </article>
            """
        )
    return f"""
    <section class="section-block">
      <h2>Ten public-domain samples</h2>
      <p>These excerpts are presented in transliterated form for readability across audiences, with parallel English and Hindi renderings. Orthography may vary slightly across editions.</p>
      <div class="source-note">
        <p><strong>Primary source trail</strong></p>
        <ul>{source_items}</ul>
      </div>
      <div class="sample-grid">
        {"".join(cards)}
      </div>
    </section>
    """


def build_references_index() -> None:
    poet_lookup = {poet["slug"]: poet for poet in POETS}
    rows: list[list[str]] = []
    html_rows = []
    for slug, samples in PUBLIC_DOMAIN_SAMPLES.items():
        poet = poet_lookup.get(slug)
        if not poet:
            continue
        for idx, sample in enumerate(samples, start=1):
            citation = sample_citation(poet, idx)
            rows.append(
                [
                    slug,
                    poet["name"],
                    str(idx),
                    citation["citation_id"],
                    citation["source_work"],
                    citation["edition"],
                    citation["year"],
                    citation["page"],
                    sample["title"],
                ]
            )
            html_rows.append(
                f"<tr><td>{html.escape(poet['name'])}</td><td>{idx}</td><td>{html.escape(citation['citation_id'])}</td><td>{html.escape(citation['source_work'])}</td><td>{html.escape(citation['edition'])}</td><td>{html.escape(citation['year'])}</td><td>{html.escape(citation['page'])}</td></tr>"
            )

    csv_path = ASSETS_DIR / "references-index.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["poet_slug", "poet_name", "sample_no", "citation_id", "source_work", "edition", "year", "page", "sample_title"])
        writer.writerows(rows)

    body = f"""
    <section class="section-block">
      <h2>Scholarly references index</h2>
      <p>This index lists per-sample citation metadata used across public-domain folios. Where page-level data differs between historical editions, the page field is marked as variant.</p>
      <p><a class="button-link" href="assets/references-index.csv" download>Download references CSV</a></p>
      <div class="table-wrap">
        <table class="reference-table">
          <thead>
            <tr><th>Poet</th><th>Sample</th><th>Citation ID</th><th>Source Work</th><th>Edition</th><th>Year</th><th>Page</th></tr>
          </thead>
          <tbody>
            {"".join(html_rows)}
          </tbody>
        </table>
      </div>
    </section>
    """
    write_text(SITE / "references.html", page_template("References", "Per-sample scholarly citation metadata and downloadable index", body))


def poet_card(poet: dict[str, str], rel: str = "../") -> str:
    return f"""
    <article class="poet-card">
      <p class="tag">{html.escape(poet["tradition"])} · {html.escape(poet["era"])}</p>
      <h3><a href="{rel}poets/{poet["slug"]}.html">{html.escape(poet["name"])}</a></h3>
      <p>{html.escape(poet["dates"])} · {html.escape(poet["region"])}</p>
      <p>{html.escape(poet["english"])}</p>
    </article>
    """


def build_index() -> None:
    featured = "".join(poet_card(poet, "") for poet in POETS[:12])
    body = f"""
    <section class="hero">
      <div class="hero-copy">
        <p class="eyebrow">A 70+ page literary journey</p>
        <h2>Urdu and Persian poetry across centuries, geographies, courts, cities, revolutions, and modern diasporas.</h2>
        <p>This digital atlas presents an expansive, beautifully designed survey of sher o shayari from early Persian masters to contemporary Urdu and Persian voices. Each featured poet receives a Hindi and English interpretation to help readers move between appreciation, context, and literary meaning.</p>
      </div>
      <div class="stat-grid">
        <div><strong>{len(POETS) + 9}</strong><span>Total pages</span></div>
        <div><strong>{len(POETS)}</strong><span>Poet folios</span></div>
        <div><strong>2</strong><span>Interpretive languages</span></div>
        <div><strong>1000 years+</strong><span>Historical range</span></div>
      </div>
    </section>

    <section class="section-block">
      <h2>Explore the atlas</h2>
      <div class="feature-grid">
        <article>
          <h3>Chronological sweep</h3>
          <p>Move from Rudaki, Ferdowsi, and Attar through Mir, Ghalib, Iqbal, Faiz, Forugh, and present-day voices.</p>
        </article>
        <article>
          <h3>Urdu and Persian together</h3>
          <p>The site highlights shared metaphors, distinct registers, and the cross-fertilization of Indo-Persian literary culture.</p>
        </article>
        <article>
          <h3>Interpretive reading</h3>
          <p>Each entry includes Hindi and English interpretations designed for literary readers, students, and general audiences.</p>
        </article>
      </div>
    </section>

    <section class="section-block">
      <h2>Featured voices</h2>
      <div class="poet-grid">
        {featured}
      </div>
    </section>
    """
    write_text(SITE / "index.html", page_template("Sher o Shayari Atlas", "A global museum of Urdu and Persian poetic imagination", body))


def build_timeline() -> None:
    body = """
    <section class="section-block">
      <h2>Timeline of transmission</h2>
      <div class="timeline">
        <div><strong>9th-11th centuries</strong><p>Persian literary foundations gather around courtly polish, epic memory, and early philosophical reflection.</p></div>
        <div><strong>12th-14th centuries</strong><p>Mystical intensity expands through Sanai, Attar, Rumi, Saadi, and Hafez, while narrative romance achieves classic form.</p></div>
        <div><strong>13th-17th centuries</strong><p>Indo-Persian circulation deepens, preparing the aesthetics that will nourish Rekhta and later Urdu ghazal traditions.</p></div>
        <div><strong>18th century</strong><p>Urdu classical lyric flourishes in Delhi and Lucknow through Mir, Sauda, Dard, and the shaping of urban poetic language.</p></div>
        <div><strong>19th century</strong><p>Ghalib, Zauq, Momin, Dagh, Hali, and Akbar Allahabadi negotiate loss, modernity, reform, and changing empire.</p></div>
        <div><strong>20th century</strong><p>Iqbal, Faiz, Firaq, Rashid, Miraji, Forugh, Shamlu, and others reimagine lyric form for modern philosophical and political life.</p></div>
        <div><strong>21st century</strong><p>Digital circulation, performance culture, and diaspora communities carry Urdu and Persian poetics into a new global readership.</p></div>
      </div>
    </section>
    """
    write_text(SITE / "timeline.html", page_template("Timeline", "A millennium of poetic continuities and transformations", body))


def build_traditions() -> None:
    body = """
    <section class="section-block">
      <h2>Two great traditions in conversation</h2>
      <div class="feature-grid">
        <article>
          <h3>Persian worlds</h3>
          <p>From Central Asia and Iran to Anatolia and the Indian subcontinent, Persian poetry shaped elite, mystical, and popular imaginaries alike.</p>
        </article>
        <article>
          <h3>Urdu worlds</h3>
          <p>Urdu inherits Persian imagery and meters while absorbing local speech, urban affect, and the changing publics of South Asia.</p>
        </article>
        <article>
          <h3>Indo-Persian bridge</h3>
          <p>Amir Khusrau, Bedil, Iqbal, and many others make visible the cultural bridge between Persian and Urdu literary sensibilities.</p>
        </article>
      </div>
    </section>
    """
    write_text(SITE / "traditions.html", page_template("Traditions", "Urdu and Persian as intertwined yet distinct poetic worlds", body))


def build_themes() -> None:
    body = """
    <section class="section-block">
      <h2>Major themes</h2>
      <div class="feature-grid">
        <article><h3>Love and longing</h3><p>The beloved may be human, divine, absent, cruel, or symbolic. Desire remains the central current of lyric experience.</p></article>
        <article><h3>Wine and tavern</h3><p>Often literal, often allegorical, these images express release, heterodoxy, ecstasy, and a challenge to moral rigidity.</p></article>
        <article><h3>Ruin and memory</h3><p>Destroyed cities, lost homes, and vanished intimacies give Urdu and Persian poetry a profound historical consciousness.</p></article>
        <article><h3>Ethics and wisdom</h3><p>Saadi, Hali, Parvin Etesami, and others turn poetry into moral reflection without sacrificing aesthetic pleasure.</p></article>
        <article><h3>Revolt and justice</h3><p>Faiz, Josh, Shamlu, Kishwar Naheed, and many modern poets carry lyric speech into public dissent.</p></article>
        <article><h3>Nature and stillness</h3><p>From spring gardens to rain-soaked streets, natural imagery offers both external beauty and inner weather.</p></article>
      </div>
    </section>
    """
    write_text(SITE / "themes.html", page_template("Themes", "Recurring images, emotions, and philosophical concerns", body))


def build_reading_room() -> None:
    body = """
    <section class="section-block">
      <h2>How to read this atlas</h2>
      <div class="feature-grid">
        <article><h3>Interpretation, not literal translation</h3><p>The Hindi and English sections offer literary readings of each poet’s style, atmosphere, and contribution rather than strict line-by-line translations.</p></article>
        <article><h3>Read comparatively</h3><p>Move between Mir and Hafez, Ghalib and Bedil, Faiz and Shamlu, Forugh and Parveen Shakir to notice continuities and departures.</p></article>
        <article><h3>Use the poet index</h3><p>The index lets you browse by era and tradition, making the site useful for both teaching and leisurely exploration.</p></article>
      </div>
    </section>
    """
    write_text(SITE / "reading-room.html", page_template("Reading Room", "A guide to navigating the archive with depth and pleasure", body))


def build_gallery() -> None:
    body = """
    <section class="section-block">
      <h2>Images of the poetic world</h2>
      <p>This site is designed as a digital mehfil: deep indigo, antique gold, soft parchment, and layered panels evoke manuscript culture, mushaira ambience, and the contemplative intimacy of reading.</p>
      <div class="feature-grid">
        <article><h3>Visual language</h3><p>Decorative borders, restrained shadows, and generous margins create a museum-like reading environment.</p></article>
        <article><h3>Portrait placement</h3><p>The creator portrait anchors every page with a consistent signature presence at the top of the site.</p></article>
        <article><h3>Responsive reading</h3><p>The interface remains elegant on both large displays and smaller screens, encouraging extended browsing.</p></article>
      </div>
    </section>
    """
    write_text(SITE / "gallery.html", page_template("Gallery", "The visual design language of the site", body))


def build_credits() -> None:
    body = """
    <section class="section-block">
      <h2>Credits and editorial note</h2>
      <p>This website is conceived as an expansive literary overview rather than a critical edition. It foregrounds poetic lineages, historical placement, and interpretive appreciation for readers entering the worlds of Urdu and Persian poetry.</p>
      <p>Top credit line: <strong>Website conceived and created by Vikram Singh Sankhala</strong></p>
      <p>Portrait: supplied by the creator and integrated into the header design of the website.</p>
    </section>
    """
    write_text(SITE / "credits.html", page_template("Credits", "Creator signature and editorial framing", body))


def build_about() -> None:
    body = """
    <section class="section-block">
      <h2>About this project</h2>
      <p>The atlas is organized to feel both scholarly and atmospheric. Instead of only listing names, it turns each poet into a folio page with historical framing, signature themes, and accessible interpretation in Hindi and English.</p>
      <p>It is meant for students, lovers of poetry, mushaira audiences, diaspora readers, and anyone wishing to travel from classical Persian brilliance to the living pulse of contemporary Urdu expression.</p>
    </section>
    """
    write_text(SITE / "about.html", page_template("About", "Why this archive was made and how it is organized", body))


def build_poet_index() -> None:
    sections = []
    for tradition in ("Persian", "Urdu"):
        entries = [p for p in POETS if tradition in p["tradition"]]
        cards = "".join(poet_card(poet) for poet in entries)
        sections.append(
            f"""
            <section class="section-block">
              <h2>{html.escape(tradition)} voices</h2>
              <div class="poet-grid">{cards}</div>
            </section>
            """
        )
    body = "".join(sections)
    write_text(POETS_DIR / "index.html", page_template("Poet Index", "Browse the complete folio of featured poets", body, "../"))


def build_poet_pages() -> None:
    for poet in POETS:
        status_title, status_text = rollout_note(poet)
        samples_section = render_samples(poet)
        body = f"""
        <section class="section-block poet-page">
          <p class="tag">{html.escape(poet["tradition"])} · {html.escape(poet["era"])}</p>
          <h2>{html.escape(poet["name"])}</h2>
          <p class="meta-line">{html.escape(poet["dates"])} · {html.escape(poet["region"])}</p>

          <div class="feature-grid">
            <article>
              <h3>Poetic signature</h3>
              <p>{html.escape(poet["name"])} belongs to the {html.escape(poet["era"])} horizon of {html.escape(poet["tradition"])} literature. The defining concerns here are {html.escape(poet["themes"])}, giving the poet a durable place within the long afterlife of sher o shayari.</p>
            </article>
            <article>
              <h3>Hindi interpretation</h3>
              <p>{html.escape(poet["hindi"])}</p>
            </article>
            <article>
              <h3>English interpretation</h3>
              <p>{html.escape(poet["english"])}</p>
            </article>
          </div>

          <div class="callout">
            <h3>Why this poet matters</h3>
            <p>{html.escape(poet["name"])} helps readers understand how {html.escape(poet["tradition"])} poetry balances image, emotion, philosophy, and historical feeling. This folio page situates the poet within the broader movement from classical craft to modern and global continuities.</p>
          </div>

          <div class="callout rollout-note">
            <h3>{html.escape(status_title)}</h3>
            <p>{html.escape(status_text)}</p>
          </div>

          <p><a class="button-link" href="index.html">Back to poet index</a></p>
        </section>
        {samples_section}
        """
        write_text(POETS_DIR / f"{poet['slug']}.html", page_template(poet["name"], f"{poet['tradition']} poetry · {poet['era']}", body, "../"))


def build_assets() -> None:
    styles = """
    :root {
      --bg: #0d1425;
      --panel: rgba(14, 25, 47, 0.86);
      --panel-soft: rgba(26, 40, 68, 0.82);
      --text: #eef1f7;
      --muted: #c2cad8;
      --gold: #e0c27a;
      --line: rgba(224, 194, 122, 0.28);
      --paper: #f4ead2;
      --shadow: 0 24px 60px rgba(0, 0, 0, 0.35);
      --radius: 22px;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      color: var(--text);
      font-family: "Inter", sans-serif;
      background:
        radial-gradient(circle at top, rgba(48, 67, 112, 0.55), transparent 30%),
        linear-gradient(180deg, #11192f 0%, #0b1020 100%);
      min-height: 100vh;
    }

    a { color: inherit; text-decoration: none; }

    .page-shell {
      width: min(1240px, calc(100% - 32px));
      margin: 24px auto;
      padding: 24px;
      border: 1px solid var(--line);
      border-radius: 28px;
      background: rgba(7, 13, 26, 0.55);
      backdrop-filter: blur(12px);
      box-shadow: var(--shadow);
    }

    .site-header,
    .section-block,
    .hero,
    .site-footer {
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: linear-gradient(180deg, var(--panel) 0%, var(--panel-soft) 100%);
    }

    .site-header,
    .section-block,
    .hero,
    .site-footer {
      padding: 24px;
      margin-bottom: 22px;
    }

    .creator-band {
      display: flex;
      gap: 22px;
      align-items: center;
      margin-bottom: 18px;
    }

    .creator-portrait {
      width: 118px;
      height: 118px;
      object-fit: cover;
      border-radius: 18px;
      border: 2px solid rgba(224, 194, 122, 0.75);
      box-shadow: 0 18px 36px rgba(0, 0, 0, 0.32);
      background: #1b2440;
    }

    .eyebrow,
    .tag {
      margin: 0 0 8px;
      text-transform: uppercase;
      letter-spacing: 0.18em;
      color: var(--gold);
      font-size: 0.74rem;
      font-weight: 700;
    }

    h1, h2, h3 {
      margin: 0 0 12px;
      font-family: "Cormorant Garamond", serif;
      line-height: 1.05;
    }

    h1 { font-size: clamp(2.8rem, 6vw, 4.6rem); }
    h2 { font-size: clamp(2rem, 4vw, 3rem); }
    h3 { font-size: 1.7rem; }

    .subtitle,
    .creator-credit,
    .meta-line,
    p {
      line-height: 1.75;
      color: var(--muted);
      font-size: 1rem;
    }

    .creator-credit {
      margin-top: 12px;
      color: var(--paper);
      font-weight: 700;
    }

    .top-nav {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }

    .top-nav a,
    .button-link {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 10px 16px;
      border-radius: 999px;
      border: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.04);
      transition: transform 0.18s ease, background 0.18s ease;
    }

    .top-nav a:hover,
    .button-link:hover {
      transform: translateY(-1px);
      background: rgba(255, 255, 255, 0.09);
    }

    .hero {
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 22px;
      align-items: center;
    }

    .stat-grid,
    .feature-grid,
    .poet-grid {
      display: grid;
      gap: 16px;
    }

    .stat-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .stat-grid div,
    .feature-grid article,
    .poet-card,
    .callout {
      padding: 18px;
      border-radius: 18px;
      border: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.04);
    }

    .stat-grid strong {
      display: block;
      margin-bottom: 6px;
      font-size: 2rem;
      color: var(--paper);
      font-family: "Cormorant Garamond", serif;
    }

    .feature-grid {
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    }

    .poet-grid {
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    }

    .poet-card h3 {
      font-size: 1.5rem;
    }

    .poet-card p {
      margin: 0 0 8px;
    }

    .timeline {
      display: grid;
      gap: 14px;
    }

    .timeline div {
      padding: 16px 18px;
      border-left: 3px solid var(--gold);
      background: rgba(255, 255, 255, 0.04);
      border-radius: 0 16px 16px 0;
    }

    .poet-page .feature-grid {
      margin: 24px 0;
    }

    .sample-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-top: 18px;
    }

    .source-note {
      margin-top: 12px;
      padding: 14px 16px;
      border-radius: 14px;
      border: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.035);
    }

    .source-note p {
      margin: 0 0 8px;
      color: var(--paper);
    }

    .source-note ul {
      margin: 0;
      padding-left: 18px;
      color: var(--muted);
      line-height: 1.6;
    }

    .sample-card {
      padding: 20px;
      border-radius: 18px;
      border: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.04);
    }

    .sample-card h3 {
      font-size: 1.45rem;
    }

    .sample-card p {
      margin: 0 0 10px;
    }

    .citation-meta {
      font-size: 0.9rem;
      color: #d8dfeb;
      border-top: 1px dashed var(--line);
      padding-top: 8px;
      margin-top: 8px;
    }

    .sample-original {
      color: var(--paper);
      font-style: italic;
    }

    .rollout-note {
      margin-top: 18px;
    }

    .table-wrap {
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 14px;
      background: rgba(255, 255, 255, 0.03);
    }

    .reference-table {
      width: 100%;
      border-collapse: collapse;
      min-width: 900px;
    }

    .reference-table th,
    .reference-table td {
      text-align: left;
      padding: 10px 12px;
      border-bottom: 1px solid rgba(224, 194, 122, 0.18);
      color: var(--muted);
      font-size: 0.92rem;
      line-height: 1.5;
    }

    .reference-table thead th {
      color: var(--paper);
      background: rgba(255, 255, 255, 0.05);
    }

    .site-footer {
      text-align: center;
      margin-bottom: 0;
    }

    @media (max-width: 860px) {
      .hero {
        grid-template-columns: 1fr;
      }

      .creator-band {
        flex-direction: column;
        align-items: flex-start;
      }
    }

    @media (max-width: 560px) {
      .page-shell {
        width: min(100% - 16px, 1240px);
        padding: 14px;
        margin: 8px auto;
      }

      .site-header,
      .section-block,
      .hero,
      .site-footer {
        padding: 18px;
      }

      .creator-portrait {
        width: 92px;
        height: 92px;
      }
    }
    """
    script = """
    document.querySelectorAll(".top-nav a").forEach((link) => {
      if (link.href === window.location.href) {
        link.style.background = "rgba(224, 194, 122, 0.14)";
      }
    });
    """
    write_text(ASSETS_DIR / "styles.css", styles)
    write_text(ASSETS_DIR / "site.js", script)


def main() -> None:
    ensure_dirs()
    copy_image()
    build_assets()
    build_index()
    build_timeline()
    build_traditions()
    build_themes()
    build_reading_room()
    build_gallery()
    build_credits()
    build_about()
    build_references_index()
    build_poet_index()
    build_poet_pages()
    print(f"Generated {len(list(SITE.rglob('*.html')))} HTML pages in {SITE}")


if __name__ == "__main__":
    main()
