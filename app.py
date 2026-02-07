import streamlit as st

page_bg = """
    <style>
    .stApp {
    background-color: #333333;
    font-family: "Countier New", monospace;
    }
    h1 {
    color: #ff2800;
    text-decoration: underline;
    font-family : "Courier New" , monospace;
    font-style: bold;
    }
    span, label {
    color: white,
    font-family: "Countier New", monospace;
    }
    blockquote, p.quote {
    font-family: "Countier New", monospace;
    font-style: italic;
    color: #fcc00;
    }
    div.stButton > button {
    backgroud-color:#333333;
    colour: white;
    border-radius: 10px;
    border: 1px solid #ff2800;
    }
    div[data-baseweb="slider"] > div > div {
    background: #ff2800 !important;
    }
    div[data-baseweb="slider"] > div > div > div {
    background: #ff2800 !important;
    }
    div[data-testid="stProgressBar"] > div > div {
    background-color: #ff2800 !important;
    }
    </style>
    """
if "index" not in st.session_state:
    st.session_state["index"] = 0

if st.session_state["index"] == 0:
    st.title("Wie würdest du Italien erobern?")
    st.write("Die Republik ist jung und es wurde beschlossen die Gebiete der römischen Republik auszuweiten...")

    if st.button("Start", key="start_1"):
        st.session_state["index"] += 1 #1

elif st.session_state["index"] == 1:
    st.header("Wer willst du sein?")

    col1, col2, col3,col4 = st.columns(4)

    with col1:
        if st.button("Konsul", key="konsul_1"):
           st.session_state["index"] += 1 #2

    with col2:
        if st.button("Prätur", key="praetor_1"):
           st.session_state["index"] += 2 #3

    with col3:
        if st.button("Ädilen", key="aedilen_1"):
           st.session_state["index"] += 3 #4

    with col4:
        if st.button("Quästor", key="quaestor_1"):
           st.session_state["index"] += 4 #5

# Konsul

elif st.session_state["index"] == 2:
    st.header("Ok, was sind deine Aufgaben?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_1000"):
            st.session_state["index"] += 1498

    with col2:
        if st.button("B", key = "b_1000"):
            st.session_state["index"] += 1498

    with col3:
        if st.button("C", key = "c_1000"):
            st.session_state["index"] += 998

    st.write("A) Ich bin eines der mächtigsten Ämter und bin der alleinige Leiter des Senats, der Volksversammlung, des Militärs, der Rechtsprechung und der Wirtschaft.")
    st.write("B) Ich bin eines der mächtigsten Ämter und bin Verantwortlich für den Senat, die Volksversammlung, das Militärs, die Rechtssprechung, die Wirtschaft und  in Notlage der Alleinherrscher über Rom.")
    st.write("C) Ich bin zuständig für den Senat, die Volksversammlung, das Militär, die Rechtssprechung und die Wirtschaft.")

elif st.session_state["index"] == 1000:
    st.header("Wie kommst du ins Amt?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_1100"):
            st.session_state["index"] += 600

    with col2:
        if st.button("B", key = "b_1100"):
            st.session_state["index"] += 600

    with col3:
        if st.button("C", key = "c_1100"):
            st.session_state["index"] += 100

    st.write("A) Ich bekomme das Amt, wenn ich in die Familie geboren werde, die dieses Amt übernimmt.")
    st.write("B) In der Republik kann ich nach dem Prinzip der Anuallität jährlich gewählt werden und das schon seit Beginn der römischen Republik kann jeder Konsul werden.")
    st.write("C) Ich kann ins Amt durch jährliche Wahlen (Annualität) aus dem Volk, aka. männliche Patrizier, Ritter und Plebejer. Chancen auf das Amt hatten allerdings nur männliche Patrizier.")

elif st.session_state["index"] == 1500:
    st.write("Das ist falsch. Der Konsul ist nach dem Prinzip der Kollegialität immer zu zweit im Amt. Er ist verantwortlich für den Senat, die Volksversammllung, die Rechtsprechung, das Militär und die Wirtschaft. Er wird zudem nicht zum Diktator in Notzeitung.")

    if st.button("OK", key = "ok_1500"):
        st.session_state["index"] -= 500

elif st.session_state["index"] == 1600:
    st.write("Konsul konnten nur männliche Patrizier werden und das ganze passiert jährlich (Annualität) innerhalb der Volksversammlung, wo das Stimmengewicht basierend auf dem Eigentum des Bürgers vergeben wurde.")

    if st.button("OK", key = "ok_1600"):
        st.session_state["index"] -= 500


elif st.session_state["index"] == 1100: 
    st.write("Die aktuelle Situation ist unsicher. Du bist als einer der Konsuln verantwortlich dafür einen Krieg mit Stämmen in Mittelitalien zu starten.")

    if st.button("OK", key = "ok_3"):
        st.session_state["index"] -= 1094 #6

elif st.session_state["index"] == 6:
    st.header("Wie verhälst du dich?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_3"):
            st.session_state["index"] += 4 #10

    with col2:
        if st.button("B", key = "b_3"):
            st.session_state["index"] += 8 #14

    with col3:
        if st.button("C", key = "c_3"):
            st.session_state["index"] += 12 #18

    st.write("A) Wir müssen Aufrüsten und ich muss den Quästor auf meine Seite kriegen. Wir müssen ein Gesetz beschließen um die Steuern zu erhöhen.")
    st.write("B) Ich möchte meinen Fokus auf die Inzinierung des Krieges legen. Ich werde mit dem Ädilen Spiele planen. Am besten auch schon eine Statur um mich als erfolgreichen Feldherren zu inszinieren.")
    st.write("C) Ich versuche direkt mit den Stämmen die ich angreife in Kontakt zu kommen und ihnen die Vorteile der römischen Zivilisation zu erklären.")

elif st.session_state["index"] == 10:
    st.write("Ok, der Quästor ist auf deiner Seite und ihr habt schon ein Gesetz besprochen, um die Steuern zu senken. Aber die Bevölkerung empört sich mehrheitlich über die Steuererhöhung.")

    if st.button("OK", key = "ok_5"):
        st.session_state["index"] += 24 #34

elif st.session_state["index"] == 34:
    st.header("Wie reagierst du?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_5"):
            st.session_state["index"] += 10000-34

    with col2:
        if st.button("B", key = "b_5"):
            st.session_state["index"] += 10000-34

    with col3:
        if st.button("C", key = "c_5"):
            st.session_state["index"] += 10000-34

    st.write("A) Ich entschuldige mich bei der Bevölkerung und versuche das Gesetz zu verhindern. Wegen den Standeskämpfen möchte ich nicht noch für mehr aufruhe sorgen.")
    st.write("B) Ich bleibe hard und versuche der Bevölkerung in einem öffendlichen Ansprache Angst vor dem gemeinsamen Kriegsfeind zu machen. Ein gemeinsamer Feind hilft Rom zusammenzuhalten.")
    st.write("C) Ich versuche die Aufruhe zu ignorieren, der nächste 'Skandal' ist bestimmt nicht lang entfernt. Die Bevölkerung wird von dem Gesetz schon schnell vergessen.")

elif st.session_state["index"] == 38:
    st.write("Deine Entschuldigung wird als Schwäche interpretiert. Und der andere Konsul nimmt dies als Anlass seine eigene Beliebteit zu steigern, indem er seinen starken Charakter insziniert. Die Steuereinnahmen bleiben unverändert und die Armee ist unterfinanziert.")

    if st.button("OK", key = "ok_5"):
        st.session_state["index"] += 1 #39

elif st.session_state["index"] == 39:
    
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_5"):
            st.session_state["index"] += 10000-39

    with col2:
        if st.button("B", key = "b_5"):
            st.session_state["index"] += 10000-39

    with col3:
        if st.button("C", key = "c_5"):
            st.session_state["index"] += 10000-39

    st.header("Wie gehst du damit um?")
    st.write("A) Ich fokusiere mich in der Öffendlichkeit auf die Willensstärke meine Legionäre und rufe den Kriegsgott Mars dazu auf unseren tapferen Kriegern bezustehen")
    st.write("B) Ich bleibe bei meinem Standpunkt und spreche die Probleme des Volkes und unserer Krieger anzusprechen. In den Standeskämpfen kann mir das eventuell auch Vorteile verschaffen.")
    st.write("C) Ich trete zurück, da ich mit der Verantwortung nicht mehr umgehen kann.")

elif st.session_state["index"] == 42:
    st.write("Deine Angstrhetorik hat nur teilweise funktioniert. Die Stimmung ist angespannd zwischen Hass bezüglich der Regierung und Angst vor dem Feind. Das stärkt die radikale Opposition der Plebejer und die neuen Steuererhöhungen werden nicht von allen akzeptiert.")

    if st.button("OK", key = "ok_6"):
        st.session_state["index"] += 3

elif st.session_state["index"] == 45:

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_6"):
            st.session_state["index"] += 10000-45

    with col2:
        if st.button("B", key = "b_6"):
            st.session_state["index"] += 10000-45

    with col3:
        if st.button("C", key = "c_6"):
            st.session_state["index"] += 10000-45

    st.header("Wie gehst du mit der Situation um?")
    st.write("A) Ich zeige mich offen zu Gesprächen mit den Plebejern und hoffe, dass sie das Problem vergessen. Sollte das nicht der Fall sein dann zeige ich mich offen für Kompromisse.")
    st.write("B) Ich verstärke die militäreische Präsenz in Rom und bereite mich auf eine mögliche gewaltsame Unterdrückung vor, falls die Plebejer tatsächlich ausziehen sollten.")
    st.write("C) Ich versuche den Fokus der Regierung und die Investition unserer Resourcen auf die Armee zu zentrisieren. So haben wir bessere Chancen mit einem Sieg die innenpolitische Krise zu überschatten.")

elif st.session_state["index"] == 46:
    st.write("Die verhoften Skandale sind eingetroffen, aber vielen Pleberjern bleibt dein Handeln besonders im Kopf, da sie die neue höhere Steuer im alltäglichen Leben belastent.")

    if st.button("OK", key = "ok_7"):
        st.session_state["index"] += 10 #56

elif st.session_state["index"] == 56:

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_7"):
            st.session_state["index"] += 10000-56

    with col2:
        if st.button("B", key = "b_7"):
            st.session_state["index"] += 10000-56

    with col3:
        if st.button("C", key = "c_7"):
            st.session_state["index"] += 10000-56

    st.header("Wie reagierst du auf diese Situation?")
    st.write("A) Ich emphatisiere öffendlich mit der Situation der Plebejer und verbreite Hoffnung indem ich erkläre, dass das Steuergeld uns hilft mehr Gebiete zu erobern, von desen Reichtum wir uns bedienen werde. So haben sie eine Aussicht auf ein Ende der Situation.")
    st.write("B) Ich bitte den Ädilen, große Siele zu organisieren. So lenken wir die Bevölkerung von innenpolitischen Konflikten abzulenken.")
    st.write("C) Ich warne vor innenpolitischen Konflikten, die uns in unseren Kämpfen schwächen könnten und rufe auf unsere tapferen Legionäre mehr zu unterstützen.")

# Prätur

elif st.session_state["index"] == 3:
    st.header("Was ist deine Aufgabe?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_2000"):
            st.session_state["index"] += 1997 #2000

    with col2:
        if st.button("B", key = "b_2000"):
            st.session_state["index"] += 2497 #2500

    with col3:
        if st.button("C", key = "c_2000"):
            st.session_state["index"] += 2497 #2500

    st.write("A) Als Prätor bin ich für Justiz zuständig.")
    st.write("B) Ich verantworte das Bauwesen, Templen und die Spiele.")
    st.write("C) Ich regele das Finanzwesen.")

elif st.session_state["index"] == 2000:
    st.header("Wie kannst du ins Amt kommen?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_2100"):
            st.session_state["index"] += 600 #2600

    with col1:
        if st.button("B", key = "b_2100"):
            st.session_state["index"] += 100 #2100

    with col3:
        if st.button("C", key = "c_2100"):
            st.session_state["index"] += 600 #2600

    st.write("A) Ich werde in das Amt gebohren, also wird es innerhalb einer Adelsfamilie weitergegeben.")
    st.write("B) Ich werde einmal jährlich in einer Volksversammlung gewählt.")
    st.write("C) Ich werde einmal alle 5 Jahre von der Volksversammlung gewählt.")

elif st.session_state["index"] == 2500:
    st.header("Das war falsch.")
    st.write("Als Prätur bis du für die Justiz also die Rechtssprechung verantwortlich.")

    if st.button("OK", key = "ok_2500"):
        st.session_state["index"] -= 500 #2000

elif st.session_state["index"] == 2600:
    st.header("Als Prätur wirst du jährlich gewählt (Annualität), also kannst du das Amt auch nicht erben.")

    if st.button("OK", key = "ok_2600"):
        st.session_state["index"] -= 500 #2100


elif st.session_state["index"] == 2100:
    st.write("Du als der Prätur bist verantwortich für die Rechtsprechung. Und wärend der Aufrüsung in Röm und Bedruhungslage von vielen Stämmen, müssen Resource gespart werden.")

    if st.button("OK", key = "ok_4"):
        st.session_state["index"] += 4 #7

    if st.session_state["index"] == 7:

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("A", key = "a_4"):
                st.session_state["index"] += 4 #11

        with col2:
            if st.button("B", key = "b_4"):
                st.session_state["index"] += 8 #15

        with col3:
            if st.button("C", key = "c_4"):
                st.session_state["index"] += 12 #19

    st.header("Wie verhälst du dich?")
    st.write("A) Ich werde veranlassen mein Zuständigkeitsgebiet effizienter zu machen und unterstütze einen Volksentscheid der Plebejer, das veranlasst sie nicht zu stark zu kontrollieren. So mache ich mich unter ihnen beliebt und auch bei den Konsuln, da die Rechtsprechung weniger Steuereinnahmen verwenden muss.")
    st.write("B) Für die Rechtsprechung sind aktuell nicht so viele Kapazitäten, aber wir müssen als Römer in Ordnung leben. Ich werde dies in meinen nächsten Reden hervorheben, um die Patrizier daran zu erinnern mein Zuständigkeitsgebiet zu respektieren und doch mit mehr Geld zu fördern.")
    st.write("C) Ich muss mit der Kürzung umgehen, also streiche ich alles was ich mir nicht mehr erlauben kann. Um mich bei den Patriziern beliebt zu machen, propagiere ich Angst vor den neuen Staatsbürgern aus den eroberten Gebieten, damit weniger Fokus auf das Handeln der aktuellen Regierung fällt.")

elif st.session_state["index"] == 11:

    st.write("Deine Effizienzmaßnahmen und die Unterstüzung der Plebejer machen dich bei dem volk beliebter. Allerdings fühlen sich viele Patrizier in ihrer Position betroht, da sie den Plebejern nicht mehr Zugeständnisse geben wollte.")

    if st.button("OK", key = "ok_8"):
        st.session_state["index"] += 100 #111

elif st.session_state["index"] == 111:

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_8"):
            st.session_state["index"] += 10000-111

    with col2:
        if st.button("B", key = "b_8"):
            st.session_state["index"] += 10000-111

    with col3:
        if st.button("C", key = "c_8"):
            st.session_state["index"] += 10000-111

    st.header("Wie reagierst du?")
    st.write("A) Ich setze mich mehr für die Plebejer ein und besonders auch für die Legionäre. Dabei fokusiere ich mich darauf, dass die Plebejer zentral für die Gesellschaft sind. Denn ich kann ja ohnehin nur für ein Jahr Konsul sein.")
    st.write("B) Ich versuche die Patrizier zu beschwichtigen, indem ich in einigen symbolischen Fällen härter gegen Plejern urteile. So zeige ich, dass ich mich 'neutral' verhalte und nicht den Plebjern besonders vollwollend gegenüber stehe.")
    st.write("C) Ich ich fokusiere mich darauf, dass die niedrigeren Steuern den Patriziern mit ihrem höheren Einkommen mehr zugute kommen.")

elif st.session_state["index"] == 15:
    st.write("Die Patrizier respektieren deine Prinzipientreue und die schlechtere Finanzierung sorgt für weniger Prozesse. Offiziell gehen also die dokumentierten Straftaten runter. Aber die Situation im Volk wird langsam in mitleidenschaft gezogen, da besonders dijenigen ohne finanzielle Perspektiven häufiger Lebensmittel stehlen, da sie kam noch befürchten müssen dafür bestraft zu werden.")

    if st.button("OK", key = "ok_9"):
        st.session_state["index"] += 50 #65

elif st.session_state["index"] == 65:

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_9"):
            st.session_state["index"] += 10000-65

    with col2:
        if st.button("B", key = "b_9"):
            st.session_state["index"] += 10000-65

    with col3:
        if st.button("C", key = "c_9"):
            st.session_state["index"] += 10000-65

    st.header("Wie gehst du damit um?")
    st.write("A) Ich führe vereinfachte Gerichtsverfahren ein, um trotz weniger Ressourven mehr Fälle bearbeiten zu können. Ein schnelle Justiz ist besser als eine Perfekte.")
    st.write("B) Ich verlange hohe Gebühren für den Kläger, so bekommt die Justiz mehr Geld ohne das Steuergelder dafür verwendet werden.")
    st.write("C) Ich beauftrage lokale Richter eigenständig Lösungen zu finden. Wenn ich die Verantwortung abgebe, dann kann ich mich um andere Punkte fokusieren.")

elif st.session_state["index"] == 19:

    st.write("Die Angstpropaganda gegen neue Staatsbürger führt zu ethnischen Spannungen in Rom. Einige Bürger fordern jetzt die Stoppung der Eroberung, um neue Bürger fernzuhalten.")

    if st.button("OK", key = "ok_10"):
        st.session_state["index"] += 49 # 68

elif st.session_state["index"] == 68:

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_10"):
            st.session_state["index"] += 10000-68

    with col2:
        if st.button("B", key = "b_10"):
            st.session_state["index"] += 10000-68

    with col3:
        if st.button("C", key = "c_10"):
            st.session_state["index"] += 10000-68

    st.header("Wie gehst du mit dieser Situation um?")
    st.write("A) Ich verwende die Situation, um die Wichtigkeit der Justiz hervorzuheben und fordere die Konsuln auf mehr Steuergelder in die Justiz zu investieren. Viele Plebejer und Patrizier ständen in der aktuellen Situation hinter dieser Forderung.")
    st.write("B) Entschuldige dich für die Rhetorik, die innenpolitisch für mehr Beunruhigungen geführt hat. Und beschwichtige die Bevölkerung dadurch zu planen, mehr Geld für die Justiz zu fordern, wenn sich die Situation auf den Schlachtfeldern beruhigt.")
    st.write("C) Schlage vor die neuen Bürger möglichst schnell in die Gesellschaft zu integrieren, um ihnen Perspektiven in der römischen Gesellschaft zu geben.")

#Ädile

elif st.session_state["index"] == 4:
    st.header("Was ist deine Aufgabe als Ädile?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_3000"):
            st.session_state["index"] += 2996 #3000

    with col2:
        if st.button("B", key = "b_3000"):
            st.session_state["index"] += 3496 #3500

    with col3:
        if st.button("C", key = "c_3000"):
            st.session_state["index"] += 3496 #3500

    st.write("A) Ich bin verantwortlich für das Bauwesen, die Thermen und die Spiele.")
    st.write("B) Ich bin zuständig für das Finanzwesen.")
    st.write("C) Ich bin verantwortlich für die Justiz.")

elif st.session_state["index"] == 3000:
    st.header("Wie kommst du ins Amt?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_3100"):
            st.session_state["index"] += 600 #3600

    with col2:
        if st.button("B", key = "b_3100"):
            st.session_state["index"] += 100 #3100

    with col3:
        if st.button("C", key = "c_3100"):
            st.session_state["index"] += 600 #3600

    st.write("A) Ich werde in mein Amt geboren, also werde ich Ädile, wenn ich der älteste Sohn bin und mein Vater das Amt nicht mehr ausüben kann.")
    st.write("B) Ich kann mich alle 5 Jahre wählen lassen und kann mich für jede Wahl nochmal wählen lassen.")
    st.write("C) Ich kann einmal pro Jahr gewählt werden und muss zwei Jahre warten noch meinem Jahr um mich wieder zur Wahl aufzustellen.")

elif st.session_state["index"] == 3500:
    st.header("Das war falsch.")
    st.write("Die Aufgabe des Ädile ist es das Bauwesen, die Thermen und die Spile zu leiten beziehungsweise zu verantworten.")
    if st.button("OK", key = "ok_3500"):
        st.session_state["index"] -= 500

elif st.session_state["index"] == 3600:
    st.header("Das ist falsch.")
    st.write("Ein Ädile wird einmal pro Jahr gewählt (Anualität und man kann sich erst zwei Jahre nach der letzen Wahl wirder zur Wahl aufstellen.")
    if st.button("OK", key = "ok_3600"):
        st.session_state["index"] -= 500



elif st.session_state["index"] == 3100:
    st.write("Du bist der Ädiler und damit verantwortlich für das Bauwesen, die Tempel und Spiele. In der aktuell angespannten Situation hast du die Möglichkeit besonders die Bevölkerung aufzuheitern. Wobei dir durch die Kriege aktuell weniger Geld zu verfügung steht.")

    if st.button("OK", key = "ok_13"):
        st.session_state["index"] += 200 #204

elif st.session_state["index"] == 204:
    st.header("Wie gehst du mit der Situation um?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_13"):
            st.session_state["index"] += 4 #208

    with col2:
        if st.button("B", key = "b_13"):
            st.session_state["index"] += 8 #212

    with col3:
        if st.button("C", key = "c_13"):
            st.session_state["index"] += 12 #216

    st.write("A) Ich fokusiere mich auf Spiele und organisiere so viele wie möglich. So lenke ich die Bevölkerung ab.")
    st.write("B) Durch die Kriege sind viele Gebäude zerstört. Ich sollte all mein Geld darauf konzentrieren. Denn die zerstärten Gebäude wirken wie Wunden den man im Alltag ständig begegnet, auch für die neuen Bürger.")
    st.write("C) Ich sollte mich auf den Glauben der Römer fokusieren und besonders viel Geld in die Tempel investieren. Der Glaube gibt der Römern Kraft, besonder der Kriegsgott Mars zu Zeiten des Krieges.")

elif st.session_state["index"] == 208:
    st.write("Deine Strategie läuft gut. Die Römer können in den Spielen den belastenden Alltag verdrengen. Aber das Bauwesen leidet und mehr und mehr Römer bemerken die Sparmassnahmen im Alltag. Besonders Brandvorbeugung wäre hilfreich.")

    if st.button("OK", key = "ok_14"):
        st.session_state["index"] += 3 #211

elif st.session_state["index"] == 211:
    st.header("Wie reagierst du?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_14"):
            st.session_state["index"] += 10000-211

    with col2:
        if st.button("B", key = "b_14"):
            st.session_state["index"] += 10000-211

    with col3: 
        if st.button("C", key = "c_14"):
            st.session_state["index"] += 10000-211

    st.write("A) Ich stoße ein Gesetz an, die im Bauwesen Brandschutzstandards vorschreiben. Dafür holle ich das lokale Personal der Feuerwehr in den Senat, um zu erklären, was gebraucht wird. Das kostet mich wenig und die Verantwortung für das Einhalten wird von einer anderen Behörde kontroliert.")
    st.write("B) Ich werde mich nicht zu sehr auf das Problem zu fokusieren. Neue Vorschriften bedeuten höhere Kosten für andere Behörden und die Besitzer von Wohnhäuser könnten damit relativieren ihre Preise weiter zu erhöhen. Das würde besonders die Plebejer verärgern.")
    st.write("C) Ich könnte auf Freiwilligkeit setzen. Mit öffendlichen Aufrufen könnte ich den Feuerwehrmännern eine Bühne geben und die Hausbezitzer dazu auffordern Brandschutz umzusetzen. So sieht es aus als ob sich die Regierung kömmert, ohne das die Hausbesitzer dazu gezwungen werden.")

elif st.session_state["index"] == 212:
    st.write("Okay, dein Plan findet Zustimmung, aber es gibt einen Haken: die Bauprojekte dauern lange und viele Sklaven die ansonsten im Bauwesen tätig wären, sind aktuell im Krieg.")

    if st.button("OK", key = "ok_15"):
        st.session_state["index"] += 5 #217

elif st.session_state["index"] == 217:
    st.header("Wie gehst du damit um?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_15"):
            st.session_state["index"] += 10000-217

    with col2:
        if st.button("B", key = "b_15"):
            st.session_state["index"] += 10000-217

    with col3:
        if st.button("C", key = "c_15"):
            st.session_state["index"] += 10000-217

    st.write("A) Ich bleibe auf meinem Kurs. Langfristige Ergebnisse sind gegenüber kurzfristigen zu priorisieren.")
    st.write("B) Ich fokusiere mich doch auch auf die Spiele, um die angespannte Innenpolitische Situation etwas zu regulieren.")
    st.write("C) Ich versuche die Konsuln speziefisch davon zu überzeugen dem Bauwesen mehr Kapazietäten zuzugestehen, um die Römer im Alltag nicht an mögliche Schwächen des Staates zu erinnern.")

elif st.session_state["index"] == 216:
    st.write("Deine Strategie zeigt Wirkung. Und da so viele Römer angehörige im Krieg haben, finden sie Sicherheit in dem Glaube. Aber diese Strategie hat ihre Limitierung, da nicht jeder in Rom den Glauben so priorisiert und Rom...")


#Quästur

elif st.session_state["index"] == 5:
    st.write("Als Verantwortlicher für Steuereinnahmen fällt dir auf, dass sich dieses Jahr fast 10% der Plebejer aus Protest weigerte Steuern zu zahlen. Die Armee benötigt diese aber dringend.")

    if st.button("OK", key= "ok_1"):
        st.session_state.index += 4 #9
        st.write("Wie gehst du vor?")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("A", key = "a_1"):
                st.session_state.index += 4 #13

        with col2:
            if st.button("B", key = "b_1"):
                st.session_state.index += 8 #17

        with col3:
            if st.button("C", key = "c_1"):
                st.session_state.index += 12 #21
 

        st.write("A) Schicke sofort eine Gruppe Steuereintreiber um hard durchzugreifen.")
        st.write("B) Schicke eine Delegation von Senatoren, um mit den Protestieren zu verhandeln.")
        st.write("C) Erhöhe die Steuern generell und starte ein öffendliche Kampange gegen die Protestieren, um sie als Feinde darzustellen und die Bevölkerung gegen sie aufzuhetzen.")
       
elif st.session_state["index"] == 13:
    st.write("Die Präsenz der Steuereintreiber hat mehr Plebejer gegen die Regierung aufgehätzt und auch die beiden Konsuln haben sich öffendlich gegen dich ausgesprochen.")
    
    if st.button("OK", key= "ok_2"):
        st.session_state.index += 3 #16
        st.header("Wie handelst du?")

        col1, col2, col3 = st.columns(3)

        with col1:
           if st.button("A", key = "a_2"):
               st.session_state.index += 10000-13

        with col2:
           if st.button("B", key = "b_2"):
               st.session_state.index += 10000-13

        with col3:
           if st.button("C", key = "c_2"):
               st.session_state.index += 10000-13

 

        st.write("A) Ich versuche mich für ein Gesetz einzusetzen, welches Steuersenkungen umsetzten möchte und entschuldige mich für mein vorgehen")
        st.write("B) Ich erkläre der Öffendlichkeit meinen Standpunkt und betone die Wichtigkeit der Steuereinnahmen für die Armee in unserem aktuellen Krieg gegen umlegende Stämme.")
        st.write("C) Ich rede mit dem befreundeten Ädile, damit er eine Spiel organisiert, die Angst vor unseren Feinden im Krieg. Mit dem Ziel die Protestierenden durch Angst zur Konformität zu zwingen.")

elif st.session_state["index"] == 17:
    st.write("Der Dialog mit den Bürgern hat die Situation beruhigt. Aber im Senat sind viele Senatoren nicht bereit den Plebejern Zugeständnisse zu geben.")

    if st.button("OK", key = "ok_11"):
        st.session_state["index"] += 90 #107

elif st.session_state["index"] == 107:

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_11"):
            st.session_state["index"] += 10000-107

    with col2:
        if st.button("B", key = "b_11"):
            st.session_state["index"] += 10000-107

    with col3:
        if st.button("C", key = "c_11"):
            st.session_state["index"] += 10000-107

    st.header("Wie gehst du damit um?")
    st.write("A) Ich versuche zu kommunizieren, dass die Steuereinnahmen essenziell sind, für den Staat und auch unseren Erfolg auf dem Schlachtfeld. Also sollten wir schnell Verhandeln, um uns auf andere Aspekte fokusieren zu können.")
    st.write("B) Ich schlage vor, die Steuern zu senken, wenn neue Gebiete erobert wurden und wir die Kriegsbeute in die Staatskasse einzahlen. Dann bleiben alle fokusiert auf unsere Kriege und es bietet Hoffnung auf bessere Zeiten.")
    st.write("C) Ich spreche an, dass wohlhabende Patrizier mehr Steuern zahlen könnten, um die Plebejer zu besämptigen. Wenn sie nicht bereit sind ihnen Zugeständnisse zuzugestehen.")

elif st.session_state["index"] == 21:
    st.write("Der Anteil der Personen, die gegen die Steuererhöhungen sind ist viel höher als gedacht. Auch Patrizier schließen sich den Protesten an. Steht ein Bürgerkrieg bevor? Zum Glück ist dein Magistratum nicht so bedeutend und du die Proteste sind mehr gegen die Konsuln gerichtet.")
    if st.button("OK", key = "ok_12"):
        st.session_state["index"] += 100 #121

elif st.session_state["index"] == 121:

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("A", key = "a_12"):
            st.session_state["index"] += 10000-121 

    with col2:
        if st.button("B",key = "b_12"):
            st.session_state["index"] += 10000-121

    with col3:
        if st.button("C", key = "c_12"):
            st.session_state["index"] += 10000-121

    st.header("Wie reagierst du?")
    st.write("A) Ich lehne mich zurück und zeige mich als den Konsuln unterlegen. So schiebe ich die öffendliche Aufmerksamkeit negativ auf die Konsuln.")
    st.write("B) Ich setze mich proaktiv für die Protestierenden ein und mein Amt wird schreicken bis die Steuer verkleinert wurde. Die Konsequenzen brauchen mich als reichen Patrizier im Zuständigkeit für das Steuereintreiben erstmal nicht interessieren. Und hoffendlich gewinne ich Sympathien bei den Plebejer und Patrizier für meine Solidarität mit ihnen.")
    st.write("C) Ich gehe in den Dialog mit dem Senat und versuche in der Regierung eine Lösung zu finden. Denn ich möchte mich bei ihnen als loyal präsentieren.")

elif st.session_state["index"] == 10000:
    st.header("Danke fürs mitmachen (-:")



       

        







    

