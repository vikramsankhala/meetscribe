from __future__ import annotations

from pathlib import Path
import html
import shutil
import textwrap


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

          <p><a class="button-link" href="index.html">Back to poet index</a></p>
        </section>
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
    build_poet_index()
    build_poet_pages()
    print(f"Generated {len(list(SITE.rglob('*.html')))} HTML pages in {SITE}")


if __name__ == "__main__":
    main()
