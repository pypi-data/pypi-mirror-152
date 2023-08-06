Identificazione argomento e analisi tramite specifico dizionario
Vittorio Haardt, Luca Porcelli & Riccardo Fossato May 25, 2022
Abstract
L’obiettivo di questo progetto (Progetto per l’esame di Statistica Spaziale ed Ambientale dell’anno 2022, Appello del 27 giugno) `e proporre una nuova strada di sviluppo per la sentiment anal- isi, in particolare centrata su una resa piu` accurata di Vader e sull’individuazione di argomenti di discussione. Il progetto descrive le principali strategie sperimentate e descrive brevemente l’implementazione del pacchetto proposto.
1 Introduzione
Il progetto parte dall’idea di base del superamento dei limiti di Vader, il quale risulta troppo generale e non applicabile a contesti specifici. Un esempio del problema appena esposto si ritrova in termini quali ”bull” che in lingua quotidiana significa ”toro” ma in un contesto finanziario significa che un determinato titolo azionario `e destinato a crescere. Il progetto verr`a articolato in due parti, che hanno il fine di creare la base per un sistema articolato e coeso di riconoscimento e analisi specifica di argomenti di discussione. I passi verranno affrontati in ordine temporale di esecuzione ed infine verr`a proposta una visione generale del funzionamento immaginato.
Il primo passaggio consiste nell’allenamento di dizionari specifici per ogni argomento, partendo dalla base di Vader. Il problema viene affrontato sia con l’utilizzo di modelli supervisionati che non supervisionati. Si usa un modello logistico per capire le parole piu` importanti (supervisionato). Suc- cessivamente si `e optato per un word embedding per trovare le parole piu` simili a quelle ottenute precedentemente (non supervisionato). Le parole ottenute verranno poi messe in un dizionario as- segnando un punteggio scelto arbitrariamente. Come ultimo passo si `e attuata una valutazione tra i dizionari di partenza e quelli modificati per capire se il cambiamento porti ad un risultato sensato.
Il secondo passo affrontato consiste nella creazione e valutazione di un modello che sia in grado di cogliere il contesto di cui si parla. Il modello ottimale che viene scelto, non necessariamente corrisponde al modello ottimale in generale, si `e scelto piuttosto un modello semplice e facilmente replicabile. Questa seconda fase, ha lo scopo non tanto di trovare il modello ottimale per classificare argomenti, dato che modelli piu` complessi potrebbero gestire meglio un numero di target anche superiore a quello usato, quanto piu` uno scopo dimostrativo per le potenzialit`a dell’idea di partenza.
In generale il lavoro svolto vuole avere la funzione di ispirare un punto di partenza per un lavoro di specializzazione di Vader il quale nonostante la sua utilit`a risulta molto generale e poco adeguato per contesti specifici. Si immagina quindi in prospettiva un sistema coeso ed articolato per la sentiment analysis, o piu` in generale per l’analisi dei testi, che sia in grado di cogliere l’argomento o gli argomenti trattati in testi specifici ed effettuare analisi riferendosi ad un dizionario Vader modellato per cogliere tutte le sfumature dell’argomento in questione.
La valutazione dei risultati avverr`a per comparazione con Vader, si spera che i dizionari specializzati abbiano un accuratezza maggiore nel capire il sentiment, tuttavia se si dovesse giungere al risultato disatteso, si arriverebbe all’interessante conclusione secondo la quale si necessiti di modelli piu` complessi o addirittura di interventi manuali per ottenere dizionari specializzati.
1.1 Vader
Per poter partire da una base autorevole e consolidata, si `e scelto di utilizzare il tool Vader, ovvero il tool rule-based per la sentiment analisi piu` efficace (in particolare per i social media). Il quale come gi`a detto in precedenza verr`a aggiornato e manipolato a seconda dell’argomento trattato, in modo da specializzarsi il piu` possibile.
1
1.2 Lime
Crediamo fortemente che l’expleinability del progetto vada messa in primo piano, con un doppio scopo. Il primo `e quello di comprensione da parte degli sviluppatori dei problemi altrimenti non visibili. Il secondo `e quello di poter fornire una trasparenza tale da poter far comprendere all’ipotetico utilizzatore del sistema come i testi vengono classificati e valutati. Per la parte di XAI verr`a utilizzato Lime per la sua semplicit`a ed intuibilit`a.
1.3 Github
Poich ́e il progetto ha una prospettiva di funzionamento reale si `e scelto di pubblicare il progetto su GitHub, servizio di hosting per progetti software, per renderlo (almeno nella sua forma primordiale) funzionate. I dettagli del funzionamento verranno esplicitati in una sezione apposita piu` avanti.
2 Dati
I dati utilizzati provengono da diversi dataset provenienti dalla nota piattaforma Kaggle. Per ogni argomento sono stati selezionati dei dataset separati e specifici. In linea generale i dataset sono delle review fatte sui vari argomenti di discussione, questa tipologia di testo risulta cruciale ai fini dell’analisi per la creazione di implementazioni per Vader. L’importanza `e data dal fatto che `e possibile identi- ficare la positivit`a e la negativit`a della sentiment dei commenti basandosi sul voto ad essi associato, cosi da poter attuare delle survey sensate. Procediamo ora alla rassegna delle propriet`a dei dati usati. La parte di interesse dei dati scaricati `e il testo. I testi verranno raggruppati sotto 4 argomenti (che vedremo a breve), gli argomenti sono ottenuti scaricando con riferimento dataset specifici. Per quanto riguarda il primo modello si utilizzeranno solamente i testi relativi di volta in volta ad un argomento diverso e le relative label ottenute dalle votazioni (verranno successivamente spiegate nel dettoaglio per ogni dataset). Invece il dataset per il secondo modello si compone quindi di una colonna ”testo” e una colonna terget ”argomento”, e vede al suo interno una merge di tutti i quattro dataset. L’obbiettivo di partenza nella ricerca dei dati era di avere a disposizione circa 40.000 righe per argomento. Di cui successivamente il 50% viene utilizzato per la creazione dei dizionari specializzati ed il restante viene usato per il modello di classificazione. Vediamo ora gli argomenti nel dettaglio.
Argomenti
1. Food 2. Electronics
Amazon Fine Food Reviews
Il dataset contiene review di prodotti alimen- tari, lasciate dai consumatori sul sito di Ama- zon, con un relativo ranking che spazia da 1 a 5. Per la creazione di label sono state considerate le review con punteggio 1 o 2 come ”Negative”, quelle con 4 o 5 come ”Positive”. Quelle con punteggio 3 sono state scartate poich ́e non di interesse per l’analisi, poich ́e considerato 3 un voto troppo volatile che rischia di raggruppare in una teorica categoria ”Neutral” recensioni positive e negative, andando di fatto ad inde- bolire l’analisi.
Amazon Reviews 2018 - Electronics
Il dataset contiene review di prodotti elettron- ici, lasciate dai consumatori sul sito di Ama- zon, con un relativo ranking che spazia da 1 a 5. Per la creazione di label sono state consid- erate le review con punteggio 1 o 2 come ”Neg- ative”, quelle con 4 o 5 come ”Positive”. Per la creazione di label sono state considerate le review con punteggio 1 o 2 come ”Negative”, quelle con 4 o 5 come ”Positive”. Le review con punteggio 3 sono state scartate per motivi analoghi ai dataset precedenti.
2

3. Disneyland 4. Finance
Disneyland Reviews
Il dataset contiene review dei tre famosi parchi di divertimento di Disneyland, ovvero quelli di Parigi, California e di Hong Kong. Le review sono state lasciate dai clienti sul sito di recen- sioni Trip Advisor, con un relativo ranking che spazia da punteggi di 1 a 5. Per la creazione di label sono state considerate le review con punteggio 1 o 2 come ”Negative”, quelle con 4 o 5 come ”Positive”. Le review con punteg- gio 3 sono state scartate per motivi analoghi ai dataset precedenti.
Financial Sentiment Analysis
Sentiment Analysis for Financial News Finance
Il dataset contiene review e tweet riguardanti argomenti finanziari, il dataset completo `e stato ottenuto unendo i tre dataset riportati sopra. Tutti e tre i dataset sono gi`a dotati di una la- bel che ne indica la positivit`a o la negativit`a.
Si `e cercato di selezionare argomenti il piu` possibile eterogenei. I dataset selezionati ovviamente non forniscono una visuale completa dell’argomento. Il lavoro svolto non vuole essere definitivo ma vuole essere un punto di partenza per poter sviluppare idee in senso di miglioramento e specializzazione di Vader.
3 Preprocessing
La pulizia dei testi gioca un ruolo fondamentale per i risultati dell’analisi, specialmente trattando testi provenienti da tweet, i quali spesso risultano sporcati da link, tag e hastag. Nel caso dei dataset selezionati, questo tipo di preprocessing era gia stato svolto, lasciando semplicemente il testo puro. Il preprocessing `e leggermente diverso per le due fasi del progetto, per questo motivo verranno spiegati i passaggi in modo separato. La pulizia attuata ugualmente per entrambe i modelli, ricopre la parte precedente all’avvio delle analisi in ”Python” e consiste nelle operazioni descritte di seguito. Ovvero: fare tokenization separando le parole con spazi, fare un lowercase andando ad eliminare tutto ci`o che non `e una parola uno spazio o un numero. Per ogni singola parola viene applicato lemmatization per ridurre le forme flesse di una parola alla loro forma canonica. Successivamente solamente per quanto riguarda il secondo modello, ovvero quello per la classificazione per argomento, sono state eliminate le stopwords, le quali non sono informative ai fini dell’analisi. Avendo finito questa fondamentale fase `e possibile ora procedere con l’esplicazione dei modelli usati e del loro funzionamento.
4 Parte 1: Specializzazione di Vader
La parte di progetto in questione ha lo scopo di identificare le parole ritenute piu` importanti per i vari argomenti al fine di modificarne il peso all’interno del dizionario di partenza, per creare dizionari plasmati appositamente per gli argomenti trattati. Si vuole identificare lo stato d’animo del creatore dei testi, in particolare il target `e ”Positive” e ”Negative” rispettivamente se il testo `e giudicato positivamente o negativamente dallo score, come si `e visto in fase di descrizione dei dati, al fine di valutare l’efficacia dei cambiamenti applicati ai dizionari. Come riportato precedentemente si `e presa una met`a dei dati per identificare le parole piu` frequenti e l’altra met`a (la quale viene anche usata per la parte relativa alla classificazione degli argomenti) per valutare il comportamento dei nuovi dizionari specializzati.
4.1 Identificazione parole
Al fine di identificare le parole piu` frequenti si `e usata una bag of words. La procedura si `e svolta usando count vectorizer per selezionare solamente le 2000 parole piu` importanti dei testi separati per argomento. Quindi `e stato costruito un dataset ad hoc contenente testi con relativi pesi (di frequenza normalizzata) delle parole scelte. Essendo state scelte solamente 2000 parole saranno presenti, in questa fase, testi con peso 0 dato che non contengono nessuna delle parole selezionate.
3

4.2 Descrizione modello e modello surrogato
Al fine di avere delle performance migliori e ridurre l’overfitting sui dati si `e scelto di adoperare una metodologia usante un modello principale per spiegare il target e un suo surrogato che fosse piu` leggibile e che si adattasse al meglio per assegnare dei pesi alle parole.
Per la scelta del modello, cos`ı detto, principale sono stati valutati due modelli, una Random Forest e un Naive Bayes. Il modello giudicato migliore `e stato scelto per i suoi parametri maggiori nel dataset con le performance peggiori, tuttavia i modelli sono paragonabili.
La Random Forest `e quindi il modello scelto, i cui parametri di tuning sono stati trovati attraverso una Grid Search di volta in volta rilanciata per ogni dataset. Per i dati di training si sono presi il 70% e il restante 30% `e stato usato come validation. Nel caso si fosse interessati ai parametri in particolare, si rimanda alla sezione LINK in fondo che a sua volta rimanda allo script originale. In generale il modello ha delle performance accettabili su tutti i dataset come osservabile da tabella (Table 1).
Accuracy Random Forest 0.82
0.87
0.82
0.79
Prima di usare il modello surrogato si `e rilanciato il modello principale su tutti i dati e sono state salvate le prediction. Successivamente si `e scelto di applicare un modello surrogato per spiegare il modello principale, da cui poi sono stati derivati i pesi. Il modello in questione `e un Logistic Model con i parametri di default. Per adattare questo modello si `e usato come target le prediction salvate precedentemente.
Per assegnare in fine i pesi alle parole sono stati usati i coefficienti ottenuti dal modello surrogato che secondo specifici valori sono stati riadattati al metodo di pesi congruenti con Vader.
4.3 Assegnazione pesi
Come appena esplicitato i coefficienti del modello surrogato sono stati usati come base per poter applicare dei pesi per il dizionario rule based. Sono state attuate diverse prove di metodologia per applicare i pesi al meglio, le strategie in questione comportano l’assegnazione di pesi da -4 a 4 a seconda dei valori dei coefficienti relativi alle parole.
Il primo metodo (metodo 1) consiste nel assegnare punteggi a fasce, come segue.
coefficiente ≤−2 ≤−1 ≤−0.5 ≥0.5 ≥1 ≥2 punteggio -4 -3.5 -2.5 2.5 3.5 4
Il secondo metodo (metodo 2) consiste solamente nell’assegnare i pesi estremi, secondo come espli- cato di seguito.
coefficiente ≤ −0.6 ≥ 0.6 punteggio -4 4
Infine il terzo metodo (metodo 3) `e un incrocio dei primi due, come visibile di seguito.
coefficiente ≤ −0.5 ≤ −1 ≥ 0.5 ≥ 1 punteggio -4 -3 3 4
Dopo queste prove per l’assegnazione di pesi si `e optato per selezionare solamente le parole con valori ”estremi” ovvero maggiori di 0.6 e minori di -0.6, alle quali si `e applicato un peso rispettivamente di 4 e -4. Si `e osservato che tra le tre alternative proposte il metodo 1 e il metodo 2 fossero preferibili
Argomenti Food Electronics Disneyland Finance
Accuracy Naive Bayes
0.85
0.85
0.86
 0.75
Table 1: Tabella che mostra i livelli di accuracy ottenuti dai modelli a confronto sui vari dataset
       4

al metodo 3. Non essendoci differenze significative tra i metodi fatta eccezione che per il dataset riguardante l’argomento Food, si `e scelto di usare il metodo 2. Si possono osservare dalla tabella (Table 2) i valori di adattamento.
Metodo 1 Metodo 2 Metodo 3
80.4% 86.9% 81.3%
82.3% 83.0% 82.9%
83.8% 83.3% 83.7%
63.9% 63.1% 63.5%
Food Electoinic Disneyland Finance
   Table 2: Tabella che confronta il livello adattamento dei vari metodi sui vari dataset
Con i pesi risultanti dall’operazione appena vista, sono stati creati i dizionari specializzati per ogni argomento, che verranno ora valutati per le loro performance rispetto ai dizionari di partenza.
4.4 Confronto con Vader
Da questo punto in avanti ci si riferisce ai dizionari specializzati come a Specialized Vader (S.V.). E` ora necessario valutare se effettivamente il passaggio da Vader a gli S.V. abbia portato a qualche sorta di miglioria per la valutazione del sentimento. Quello che ci si aspetta `e che, essendo gli S.V. plasmanti ad hoc sugli argomenti trattati, siano in grado di portare ad analisi piu` specifiche e quindi ad avere un accuratezza maggiore per identificare il sentimento dei testi. Nel caso contrario invece ci si interrogherebbe sulle cause di un mancato miglioramento, valutando altri metodi per l’assegnazione di pesi oppure valutando l’insuperabilit`a di Vader.
Per valutare l’accuratezza di Vader e degli S.V., `e stato preso il valore di compound risultante e si `e etichettato il testo come ”Positive”, nel caso quest’ultimo fosse maggiore di 0, e ”Negative” altrimenti. Successivamente si sono confrontate queste etichette basate sul compund con la loro controparte reale, ottenuta come spiegato in precedenza. Come ci si sarebbe aspettati, vedendo la tabella (Table 3) si osserva che per ogni argomento S.V. risulti piu` preciso di Vader di svariati punti in percentuale.
Argomenti Food Electronic Disneyland Finance
Vader
72.1% 75.5% 82.2% 49.7%
Specialized Vader
86.9% 83.0% 83.3% 63.1%
  Table 3: Tabella che confronta il livello di adattamento in percentuale tra Vader e Specialized Vader
Il risultato ottenuto mostra come lo scopo del progetto possa effettivamente portare ad un miglio- ramento sostanziale di Vader attraverso la sua specializzazione, portando ad analisi sempre piu` precise su argomenti sempre piu` capillari.
4.5 Word embedding e confronto con modello precedente
Si `e scelto di valutare se l’utilizzo di un word embedding potesse ulteriormente far crescere le per- formance degli S.V. rispetto alla loro forma classica. Sono state valutate due alternative chiamate rispettivamente Specialized Vader four e Specialized Vader one change. In generale quello che svolgono queste due modifiche `e, grazie al word embedding, la modifica dei pesi per le parole maggiormente simili a quelle modificate in precedenza. Si `e optato per l’utilizzo del modello non supervisionato con fastText piuttosto che word2vec poich ́e considerato piu` efficiente. S.V. four in particolare seleziona le parole con punteggio di similarit`a maggiore di 0.99, dalle parole cambiate per S.V., e assegna a queste parole un valore di 4 o -4 in base al valore positivo o negativo delle parole a cui sono state associate. Invece S.V. one change, seleziona le parole per cui cambiare il peso in maniera analoga a S.V. four, ma cambia i pesi sommando o sottraendo 1 rispetto al valore che queste parole hanno in Vader in base al valore positivo o negativo delle parole a cui sono state associate.
Come riportato dalla tabella (Table 4) si osservano le performance dei vari metodi di S.V., per scegliere la metodologia piu` appropriata per ogni metodo.
5

Argomenti Food Electronic Disneyland Finance
86.9%
83.0%
83.3%
63.1%
Specialized Vader
S.V. four
81.86% 83.08% 83.12% 70.15%
S.V. one change 81.86%
83.23%
83.12% 43.36%
  Table 4: Tabella che confronta il livello di adattamento tra Specialized Vader e le sue versioni che usano word embedding
Avendo valutato le performance di adattamento si `e scelto di non applicare word embedding agli argomenti Food e Disneyland, invece per quanto riguarda Electronic la scelta migliore ricade su S.V. one change ed infine per Finance si osserva un netto miglioramento in confronto agli altri due metodi per quanto riguarda S.V. four.
I dizionari specializzati sono ora completi e pienamente utilizzabili per analisi sui testi per i rela- tivi argomenti, come visto durante i passaggi che hanno portato al risultato, i dizionari specializzati produrranno analisi piu` accurate di quanto faceva Vader. Si vuole ora riportare l’attenzione, su come indipendentemente dalle scelte fatte, sui metodi di assegnazione pesi e sull’utilizzo del word embed- ding, i risultati dei dizionari specializzati comunque sorpassano quelli di Vader per praticamente tutte le combinazioni di scelte su tutti gli argomenti.
Come esempio pratico di come i dizionari specializzati hanno migliorato Vader si riporta una delle frasi dell’argomento Electronic.
”Faulty on arrival. The wire for one channel wasn’t ...”
La parola faulty (ovvero non funzionate) assume un connotato generalmente piu` negativo nel lin- guaggio naturale quando si parla di oggetti elettronici. Dato che l’argomento in questione comprende recensioni di oggetti elettronici vediamo come il peso di questa parola sia passato da -1.8 per Vader ad un -4 per Specialized Vader.
5 Parte 2: Classificazione argomenti
Come detto in precedenza il secondo modello si prefigge lo scopo di riuscire a classificare dei testi secondo gli argomenti di cui parlano. Il modello scelto ha quindi ovviamente la variabile target multi- classe, riferito agli argomenti sopra riportati. In questo paragrafo ne verranno descritte le principali caratteristiche. Del 50% del totale dei dati preso in precedenza, si `e optato per una proporzione di 70% e 30% rispettivamente per i dati di training e di test.
5.1 Descrizione modelli
Al fine di avere delle performance classificative ottimali si sono valutati due diversi modelli. I modelli in questione sono Naive Bayes e Decision Tree. Per il Naive Bayes si `e optato per un valore di alpha di 0.1. Per il Decision Tree si `e optato per il criterion di Gini, un albero con maxleafnodes senza limite e una maxdeap anche essa illimitata, cos`ı da lasciare il modello il piu` lasso possibile. Tutti i parametri sono stati tunati per selezionare quelli ottimali.
5.2 Modello vincente
La metrica di interesse principalmente osservata `e l’accuracy, ma comunque i modelli tendono ad avere alti valori anche per le altre metriche. Osservando le performance, il modello vincente `e risultato il Naive Bayes, con un livello di accuracy di 0.95 (rispetto ad un 0.88 per l’albero). Dunque la classificazione multitarget con il fine di individuare l’argomento di discussione sar`a appunto affidata al Naive Bayes con i parametri precedentemente selezionati.
E ́ tuttavia necessario precisare che questo modello risulti ottimale per questo tipo di classificazione di solamente quattro argomenti. Nel caso di sistemi di classificazione di argomenti di discussione piu` ampi con numeri di alternative di target estremamente maggiori, il modello ottimale verosimilmente sar`a un modello con una complessit`a maggiore, come ad esempio una rete neurale. Viene quindi ricordato che il modello viene creato, non tanto per la sua effettiva utilit`a, ma piuttosto per mostrare
6

la possibilit`a di sviluppo di un sistema coeso che identifichi l’argomento di discussione e rimandi ad uno specifico dizionario. Lo scopo `e quindi il poter ispirare alla creazione di dizionari specifici, per tutti gli argomenti di discussione, e creare un sistema che automaticamente riconosca l’argomento e reindirizzi al dizionario specializzato associato.
5.3 Explainability
L’explainability, come precedentemente precisato, `e stata affidata interamente a Lime. L’importanza di questa ultima fase non `e da sottovalutare, poich ́e per poter fare realmente affidamento su un modello di classificazione `e necessario conoscerne profondamente il funzionamento ed il metodo di scelta, cos`ı da poter applicare migliorie e poter guadagnare la fiducia dell’utente non esperto.
Campionando casualmente tra i diversi testi, si `e osservato come il modello classifichi sulla base di parole realmente significative e come al contrario non si basi su parole generali, le quali sarebbero applicabili a qualunque contesto. Viene sotto (Figure 1) riportato un testo riguardante l’argomento Finance, al fine di dare un idea generale della capacit`a esplicativa della classificazione.
Figure 1: Testo identificato in modo corretto come riguardate l’argomento Finance, vengono evidenziati i token che hanno portato il modello alla classificazione.
6 Funzionamento congiunto modelli
Il funzionamento congiunto dei modelli `e stato largamente introdotto nelle sezioni precedenti. Per riassumere, si riporta come le due parti di studio, ovvero la creazione degli Specialized Vader e la creazione di un modello che sia in grado di identificare l’argomento di discussione, siano pensate come parti distinte di un unico processo. Ovviamente, come gi`a precisato, lo studio fatto non ha lo scopo di essere in nessun modo definitivo, bens`ı vuole fungere come punto di partenza e ispirazione.
E` stata creata quindi una funzione che ricevendo un testo qualsiasi (ovviamente limitandoci ai nostri quattro argomenti) sia in grado di riconoscerne con precisione l’argomento e quindi affidare una sentiment analysis, che produca un punteggio di compund, al dizionario adeguato per l’argomento. Grazie a funzioni che lavorino come quella appena esplicitata `e possibile fornire un vero salto in avanti per l’accuratezza e la reliability di un sistema come Vader, che, per quanto affidabile e utile, necessita di un’evoluzione poich ́e rimane troppo generale, portando ad analisi poco affidabili per testi riguardanti argomenti specifici e che quindi hanno un linguaggio specifico.
Viene proposto ora un esempio della funzione sopra citata che ne riporta l’input e l’output, al fine di comprendere al meglio la potenzialita` del sistema ideato.
7 Github
!pip install Specialized Vader
8 Conclusioni
9 Link ai Notebook
Si riportano in questa sezione finale i link ai notebook python per lo sviluppo del progetto. 7
 
• Asegnazione Pesi
• Word Embedding
• Confornto con Vader • Classificazione