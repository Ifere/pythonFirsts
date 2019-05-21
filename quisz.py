import playsound as pl
import random as r



class Question:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer


q = [
    'Who was the first man on the moon?\n(a) Niel Armstrong\n(b) Buzz Aldrin\n',
    'Who was the first female Prime Minister of Great Britain?\n(a) Theresa May\n(b) Margaret Thatcher\n',
    'Who named the Pacific ocean?\n(a) Vasco da Gama\n(b) Ferdinand Magellan\n',
    'Who was the outlaw?\n(a) Jesse Jackson\n(b) Jesse James\n',
    'Reykjavik is the capital of?\n(a) Greenland\n(b) Iceland\n',
    'What is the Matterhorn?\n(a) Mountain\n(b) Lake\n',
    'What is the capital of Mongolia?\n(a) Ulaan Bator\n(b) Astana\n',
    'The Maori are a people from?\n(a) Australia\n(b) New Zealand\n',
    'The Tutsi are a people from?\n(a) Rwanda\n(b) Uganda\n',
    'Kublai Khan was visited by what famous explorer?\n(a) Marco Polo\n(b) Ferdinand Magellan\n',
    'Volvo is an automobile company that originated from?\n(a) Germany\n(b) Sweden\n',
    'The 1984 nuclear disaster happened in?\n(a) Kyoto\n(b) Chernobyl\n',
    'Mary Shelley wrote?\n(a) Frankenstein\n(b) Dracula\n',
    'The Republic is a book written by?\n(a) Plato\n(b) Homer\n',
    'George R. Martin is famous for which of these?\n(a) Game of Thrones\n(b) Rick and Morty\n',
    'The Quran is divided into how many surahs?\n(a) 106\n(b) 114\n',
    'Captain Ahab is a character from?\n(a) Moby Dick\n(b) The Illiad\n',
    'George Orwell was the literary alias of?\n(a) William Colt\n(b) Eric Blair\n',
    'Who was a British commander during the American Revolution?\n(a) General Patton\n(b) General Cornwalis\n',
    'What is a U-boat?\n(a) Submarine\n(b) Speedboat\n',
    'The space between the eyebrows is called?\n(a) Philtrum\n(b) Glabella\n',
    'Long John Silver is a character from?\n(a) Robinson Crusoe\n(b) Treasure Island\n',
    'Where was the first World Cup tournament held?\n(a) Italy\n(b) Uruguay\n',
    'Pasteurization is a process done on?\n(a) Milk\n(b) Cheese\n',
    'When was the Berlin wall destroyed?\n(a) 1990\n(b) 1989\n',
    'Who gave the world the assembly line?\n(a) Nikola Tesla\n(b) Henry Ford\n',
    'Silk is obtained from?\n(a) Shrubs\n(b) Worms\n',
    'Who is the Crown Prince of Saudi Arabia?\n(a) Mohammed bin Salman\n(b) Faisal al-Farouk\n',
    'Which is second highest mountain in the Himalayas?\n(a) K2\n(b) Sharpa\n',
    'What landamrk is on the Greenwich Meridian line?\n(a) Stonehedge\n(b) Big Ben\n',
    'How many colonies originally made up the American union?\n(a) 11\n(b) 13\n',
    'The Queen of England is from the House of?\n(a) Stuart\n(b) Windsor\n',
    'What is the fastest animal?\n(a) Peregrine Falcon\n(b) Cheetah\n',
    'Which infamous invention is Alfred Nobel known for?\n(a) Dynamite\n(b) Cyanide \n',
    'Sanaa is the capital?\n(a) Bahrain\n(b) Yemen\n',
    'Who is the only Musician to have won the Pulitzer award?\n(a) Aretha Franklin\n(b) Kendrick Lamar\n',
    'King John signed the?\n(a) Magna Carta\n(b) Treaty of Westphalia\n',
    'What is name after a Scandinavian king?\n(a) Skoda\n(b) Bluetooth?\n',
    'Who was the leader of Sudan until recently?\n(a) Omar al-Bashir\n(b) Mohammed Idris\n',
    'Who was prosecuted at the ICC for war crimes?\n(a) Idi Amin\n(b) Charles Taylor\n',
    'Cai Lun invented which of these?\n(a) Paper\n(b) Gunpowder\n',
    'Alexander Fleming invented?\n(a) Stethoscope\n(b) Penicillin\n',
    'Who was the first tennis player to win five straight Wimbledon titles?\n(a) Roger Federer\n(b) Bjorn Borg\n',
    'Who ran the first four minute mile?\n(a) Banastre Tarleton\n(b) Roger Bannister\n',
    'In polo, what is a period of play called?\n(a) set\n(b) chukka\n',
    'How many years old are horses that run in the Kentucky Derby?\n(a) 3 years\n(b) 4 years\n',
    'What follows the deuce in tennis?\n(a) Advantage\n(b) Set\n',
    'The game of rugby was named after Rugby School in?\n(a) England\n(b) Ireland\n',
    'What is a golf ball mostly made of?\n(a) Rubber\n(b) Wood\n',
    'Who was the youngest golfer to ever win the U.S. Junior Amateur title?\n(a) Rory Mcllroy\n(b) Tiger Woods\n',
    'Where was golf invented?\n(a) Scotland\n(b) USA\n',
    'When was the first Super Bowl played?\n(a) 1972\n(b) 1967\n',
    'How many rings are on the Olympic flag?\n(a) 6\n(b) 5\n',
    'Where did James Naismith invent Basketball?\n(a) USA\n(b) Canada\n',
    'In what city were the first Asain games held?\n(a) Beijing\n(b) Delhi\n',
    'David Beckham was a long time ambassador for?\n(a) Motorola\n(b) Calvin Klein\n',
    'The 1994 World Cup was hosted by?\n(a) USA\n(b) Sweden\n',
    "According to the novel Harry Porter, what is the name of Dumbledore's phoenix?\n(a) Fang\n(b) Fawkes\n",
    'The only insect that can turn its head?\n(a) Lady Bug\n(b) Praying Mantis\n',
    'The only bird that can fly backwards?\n(a) Bald Eagle\n(b) Humming Bird\n',
    'The largest cat in the world?\n(a) Black Panther\n(b) Siberian Tiger\n',
    'The largest bird of prey is the?\n(a) White-backed Vulture\n(b) Condor\n',
    'A pinniped is what type of animal?\n(a) Platypus\n(b) Seal\n',
    'The deadliest spider is the?\n(a) Black Widow\n(b) Brazilian Wandering Spider\n',
    'What animal can see both ultra-violet and infra-red?\n(a) Goldfish\n(b) Naked Mole-rat\n',
    'A cat has how many whiskers?\n(a) 20\n(b) 24\n',
    "What bird has nostrils at its beak's end?\n(a) Kiwi\n(b) Pelican\n",
    'A group of rhinoceroses is called?\n(a) Crash\n(b) Troop\n',
    'A baby horse is called?\n(a) Calf\n(b) Shoal\n',
    'The largest reptile is the?\n(a) Komodo Dragon\n(b) Saltwater Crocodile\n',
    'In which field does Robert Hooke have a law?\n(a) Quantum Physics\n(b) Biology\n',
    'Which should not be played into the hole in an eight ball game?\n(a) Black\n(b) White\n',
    'Victims develop positive feelings toward their captors?\n(a) Stockholm Syndrome\n(b) Schizophrenia\n',
    'When did the USSR fall?\n(a) 1991\n(b) 1989\n',
    'Newton Heath Football Club later became?\n(a) Manchester United\n(b) Newcastle United\n',
    'Which famous painting is at the monastery Santa Maria delle Grazie in Milan?\n(a) The Last Supper\n(b) Mona Lisa\n',
    'Which of these cities is in Morocco?\n(a) Marakkesh\n(b) Kairouan\n',
    'What country had the highest GDP per Capita in 2018?\n(a) USA\n(b) China\n',
    'Where is the Suez canal?\n(a) Panama\n(b) Egypt\n',
    'Who discovered Australia?\n(a) Francis Drake\n(b) James Cook\n',
    'Who has an impressive twenty one Grammy award wins?\n(a) Beyonce\n(b) Kanye West\n',
    'Who is the leader of the UK Labour Party?\n(a) Nigel Farge\n(b) Jeremy Corbyn\n',
    'Table Mountain can be found in?\n(a) South Africa\n(b) Nepal\n',
    'The capital of Israel according to the UN is?\n(a) Tel-Aviv\n(b) Jerusalem\n',
    'According to legend, where did King Arthur go after his death?\n(a) Heaven\n(b) Avalon\n',
    'Willam the Conqueror of England was from?\n(a) France\n(b) England\n',
    'Monica Lewinsky is a name associated with?\n(a) Barack Obama\n(b) Bill Clinton\n',
    'Who won a Nobel Peace Prize along with F.W. de Klerk?\n(a) Desmond Tutu\n(b) Nelson Mandela\n',
    'Who was the first Nigerian to win a Grammy Award?\n(a) Kelvin Olusola\n(b) Sade Adu\n',
    'Who wrote the James Bond Series?\n(a) Timothy Lazenby\n(b) Ian Fleming\n',
    'Who was born in Bonn, Germany?\n(a) Ludwig van Beethoven\n(b) Johannes S.Bach\n',
    'What river flows through Paris?\n(a) Seine\n(b) Rhine\n',
    'Which can be seen from space?\n(a) Australian Outback\n(b) Great Barrier Reef\n',
    'What happened on the morning of September 1, 1939?\n(a) Invasion of Poland\n(b) Rutherford split the atom\n',
    'The Fall of the Shah and the Iranian Revolution was in?\n(a) 1970\n(b) 1979\n',
    "In the Bible who is said to have slept with his father's wife?\n(a) Ruben\n(b) Absalom\n",
    'How many Emirates make up the UAE?\n(a) 7\n(b) 5\n',
    'Which was a president of Iran?\n(a) Mohammed Reza Pahlavi\n(b) Mahmoud Ahmadinejad\n',
    '1440 is the current year in the?\n(a) Islamic Calendar\n(b) Jewish Calendar\n',
    'The battery was invented by?\n(a) Alessandro Volta\n(b) Jean-Marie Ampere\n',
    'The Yom Kippur war was fought in?\n(a) South America\n(b) Middle East\n',
    'The military tribunal held after WWII were called?\n(a) Nuremberg Trials\n(b) Yalta Conference',




]

questions = [
    Question(q[0],'a'),
    Question(q[1],'b'),
    Question(q[2],'b'),
    Question(q[3],'b'),
    Question(q[4],'b'),
    Question(q[5],'a'),
    Question(q[6],'a'),
    Question(q[7],'b'),
    Question(q[8],'a'),
    Question(q[9],'a'),
    Question(q[10],'b'),
    Question(q[11],'b'),
    Question(q[12],'a'),
    Question(q[13],'a'),
    Question(q[14],'a'),
    Question(q[15],'b'),
    Question(q[16],'a'),
    Question(q[17],'b'),
    Question(q[18],'b'),
    Question(q[19],'a'),
    Question(q[20],'b'),
    Question(q[21],'b'),
    Question(q[22],'b'),
    Question(q[23],'a'),
    Question(q[24],'b'),
    Question(q[25],'b'),
    Question(q[26],'b'),
    Question(q[27],'a'),
    Question(q[28],'a'),
    Question(q[29],'a'),
    Question(q[30],'b'),
    Question(q[31],'b'),
    Question(q[32],'a'),
    Question(q[33],'a'),
    Question(q[34],'b'),
    Question(q[35],'b'),
    Question(q[36],'a'),
    Question(q[37],'b'),
    Question(q[38],'a'),
    Question(q[39],'b'),
    Question(q[40],'a'),
    Question(q[41],'b'),
    Question(q[42],'b'),
    Question(q[43],'b'),
    Question(q[44],'b'),
    Question(q[45],'a'),
    Question(q[46],'a'),
    Question(q[47],'a'),
    Question(q[48],'a'),
    Question(q[49],'b'),
    Question(q[50],'a'),
    Question(q[51],'b'),
    Question(q[52],'b'),
    Question(q[53],'a'),
    Question(q[54],'b'),
    Question(q[55],'a'),
    Question(q[56],'a'),
    Question(q[57],'b'),
    Question(q[58],'b'),
    Question(q[59],'b'),
    Question(q[60],'b'),
    Question(q[61],'b'),
    Question(q[62],'b'),
    Question(q[63],'b'),
    Question(q[64],'a'),
    Question(q[65],'b'),
    Question(q[66],'a'),
    Question(q[67],'a'),
    Question(q[68],'b'),
    Question(q[69],'b'),
    Question(q[70],'b'),
    Question(q[71],'b'),
    Question(q[72],'a'),
    Question(q[73],'a'),
    Question(q[74],'a'),
    Question(q[75],'a'),
    Question(q[76],'a'),
    Question(q[77],'a'),
    Question(q[78],'b'),
    Question(q[79],'b'),
    Question(q[80],'b'),
    Question(q[81],'b'),
    Question(q[82],'a'),
    Question(q[83],'a'),
    Question(q[84],'b'),
    Question(q[85],'a'),
    Question(q[86],'b'),
    Question(q[87],'b'),
    Question(q[88],'a'),
    Question(q[89],'b'),
    Question(q[90],'a'),
    Question(q[91],'a'),
    Question(q[92],'b'),
    Question(q[93],'a'),
    Question(q[94],'b'),
    Question(q[95],'a'),
    Question(q[96],'a'),
    Question(q[97],'b'),
    Question(q[98],'a'),
    Question(q[99],'a'),
    Question(q[100],'b'),
    Question(q[101],'a')
]

def runQuiz(questions):

    score = 0
    r.shuffle(questions)
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            print('Correct')
            score += 1
            print('score: ',score,'\n')
        else:
            print('Wrong bitch')
            print('score: ',score,'\n')
    print('Score: '+str(score)+'\n')






print('101 Questions!\nHow many can you answer correctly?\n')
runQuiz(questions)