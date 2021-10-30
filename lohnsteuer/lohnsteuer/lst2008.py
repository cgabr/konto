# coding: utf-8

import decimal

class BigDecimal(decimal.Decimal):
    """ Compatibility class for decimal.Decimal """

    ROUND_DOWN = decimal.ROUND_DOWN
    ROUND_UP = decimal.ROUND_UP

    @classmethod
    def _mk_exp(cls, prec):
        return cls('0.' + '0' * prec)

    def divide(self, other, scale=None, rounding=None):
        if not scale and not rounding:
            return BigDecimal(self / other)
        if type(scale) is not int:
            raise ValueError("Expected integer value for scale")
        exp = BigDecimal._mk_exp(scale)
        return BigDecimal((self / other).quantize(exp, rounding=rounding))

    @classmethod
    def valueOf(cls, value):
        return cls(value)

    def multiply(self, other):
        return BigDecimal(self * other)

    def setScale(self, scale, rounding=ROUND_DOWN):
        exp = BigDecimal._mk_exp(scale)
        return BigDecimal(self.quantize(exp, rounding=rounding))

    def add(self, other):
        return BigDecimal(self + other)

    def subtract(self, other):
        return BigDecimal(self - other)

    def longValue(self):
        return int(self)

    def compareTo(self, other):
        return BigDecimal(self.compare(other))

BigDecimal.ZERO = BigDecimal(0)
BigDecimal.ONE = BigDecimal(1)
BigDecimal.TEN = BigDecimal(10)


class Lst2008:
    TAB1 = [BigDecimal.valueOf(0.0), BigDecimal.valueOf(0.4), BigDecimal.valueOf(0.384), BigDecimal.valueOf(0.368), BigDecimal.valueOf(0.352), BigDecimal.valueOf(0.336), BigDecimal.valueOf(0.32), BigDecimal.valueOf(0.304), BigDecimal.valueOf(0.288), BigDecimal.valueOf(0.272), BigDecimal.valueOf(0.256), BigDecimal.valueOf(0.24), BigDecimal.valueOf(0.224), BigDecimal.valueOf(0.208), BigDecimal.valueOf(0.192), BigDecimal.valueOf(0.176), BigDecimal.valueOf(0.16), BigDecimal.valueOf(0.152), BigDecimal.valueOf(0.144), BigDecimal.valueOf(0.136), BigDecimal.valueOf(0.128), BigDecimal.valueOf(0.12), BigDecimal.valueOf(0.112), BigDecimal.valueOf(0.104), BigDecimal.valueOf(0.096), BigDecimal.valueOf(0.088), BigDecimal.valueOf(0.08), BigDecimal.valueOf(0.072), BigDecimal.valueOf(0.064), BigDecimal.valueOf(0.056), BigDecimal.valueOf(0.048), BigDecimal.valueOf(0.04), BigDecimal.valueOf(0.032), BigDecimal.valueOf(0.024), BigDecimal.valueOf(0.016), BigDecimal.valueOf(0.008), BigDecimal.valueOf(0.0)]
    """
    Tabelle fuer die Vomhundertsaetze des Versorgungsfreibetrags
    """

    TAB2 = [BigDecimal.valueOf(0), BigDecimal.valueOf(3000), BigDecimal.valueOf(2880), BigDecimal.valueOf(2760), BigDecimal.valueOf(2640), BigDecimal.valueOf(2520), BigDecimal.valueOf(2400), BigDecimal.valueOf(2280), BigDecimal.valueOf(2160), BigDecimal.valueOf(2040), BigDecimal.valueOf(1920), BigDecimal.valueOf(1800), BigDecimal.valueOf(1680), BigDecimal.valueOf(1560), BigDecimal.valueOf(1440), BigDecimal.valueOf(1320), BigDecimal.valueOf(1200), BigDecimal.valueOf(1140), BigDecimal.valueOf(1080), BigDecimal.valueOf(1020), BigDecimal.valueOf(960), BigDecimal.valueOf(900), BigDecimal.valueOf(840), BigDecimal.valueOf(780), BigDecimal.valueOf(720), BigDecimal.valueOf(660), BigDecimal.valueOf(600), BigDecimal.valueOf(540), BigDecimal.valueOf(480), BigDecimal.valueOf(420), BigDecimal.valueOf(360), BigDecimal.valueOf(300), BigDecimal.valueOf(240), BigDecimal.valueOf(180), BigDecimal.valueOf(120), BigDecimal.valueOf(60), BigDecimal.valueOf(0)]
    """
    Tabelle fuer die Hoechstbetrage des Versorgungsfreibetrags
    """

    TAB3 = [BigDecimal.valueOf(0), BigDecimal.valueOf(900), BigDecimal.valueOf(864), BigDecimal.valueOf(828), BigDecimal.valueOf(792), BigDecimal.valueOf(756), BigDecimal.valueOf(720), BigDecimal.valueOf(684), BigDecimal.valueOf(648), BigDecimal.valueOf(612), BigDecimal.valueOf(576), BigDecimal.valueOf(540), BigDecimal.valueOf(504), BigDecimal.valueOf(468), BigDecimal.valueOf(432), BigDecimal.valueOf(396), BigDecimal.valueOf(360), BigDecimal.valueOf(342), BigDecimal.valueOf(324), BigDecimal.valueOf(306), BigDecimal.valueOf(288), BigDecimal.valueOf(270), BigDecimal.valueOf(252), BigDecimal.valueOf(234), BigDecimal.valueOf(216), BigDecimal.valueOf(198), BigDecimal.valueOf(180), BigDecimal.valueOf(162), BigDecimal.valueOf(144), BigDecimal.valueOf(126), BigDecimal.valueOf(108), BigDecimal.valueOf(90), BigDecimal.valueOf(72), BigDecimal.valueOf(54), BigDecimal.valueOf(36), BigDecimal.valueOf(18), BigDecimal.valueOf(0)]
    """
    Tabelle fuer die Zuschlaege zum Versorgungsfreibetrag
    """

    TAB4 = [BigDecimal.valueOf(0.0), BigDecimal.valueOf(0.4), BigDecimal.valueOf(0.384), BigDecimal.valueOf(0.368), BigDecimal.valueOf(0.352), BigDecimal.valueOf(0.336), BigDecimal.valueOf(0.32), BigDecimal.valueOf(0.304), BigDecimal.valueOf(0.288), BigDecimal.valueOf(0.272), BigDecimal.valueOf(0.256), BigDecimal.valueOf(0.24), BigDecimal.valueOf(0.224), BigDecimal.valueOf(0.208), BigDecimal.valueOf(0.192), BigDecimal.valueOf(0.176), BigDecimal.valueOf(0.16), BigDecimal.valueOf(0.152), BigDecimal.valueOf(0.144), BigDecimal.valueOf(0.136), BigDecimal.valueOf(0.128), BigDecimal.valueOf(0.12), BigDecimal.valueOf(0.112), BigDecimal.valueOf(0.104), BigDecimal.valueOf(0.096), BigDecimal.valueOf(0.088), BigDecimal.valueOf(0.08), BigDecimal.valueOf(0.072), BigDecimal.valueOf(0.064), BigDecimal.valueOf(0.056), BigDecimal.valueOf(0.048), BigDecimal.valueOf(0.04), BigDecimal.valueOf(0.032), BigDecimal.valueOf(0.024), BigDecimal.valueOf(0.016), BigDecimal.valueOf(0.008), BigDecimal.valueOf(0.0)]
    """
    Tabelle fuer die Vomhundertsaetze des Altersentlastungsbetrags
    """

    TAB5 = [BigDecimal.valueOf(0), BigDecimal.valueOf(1900), BigDecimal.valueOf(1824), BigDecimal.valueOf(1748), BigDecimal.valueOf(1672), BigDecimal.valueOf(1596), BigDecimal.valueOf(1520), BigDecimal.valueOf(1444), BigDecimal.valueOf(1368), BigDecimal.valueOf(1292), BigDecimal.valueOf(1216), BigDecimal.valueOf(1140), BigDecimal.valueOf(1064), BigDecimal.valueOf(988), BigDecimal.valueOf(912), BigDecimal.valueOf(836), BigDecimal.valueOf(760), BigDecimal.valueOf(722), BigDecimal.valueOf(684), BigDecimal.valueOf(646), BigDecimal.valueOf(608), BigDecimal.valueOf(570), BigDecimal.valueOf(532), BigDecimal.valueOf(494), BigDecimal.valueOf(456), BigDecimal.valueOf(418), BigDecimal.valueOf(380), BigDecimal.valueOf(342), BigDecimal.valueOf(304), BigDecimal.valueOf(266), BigDecimal.valueOf(228), BigDecimal.valueOf(190), BigDecimal.valueOf(152), BigDecimal.valueOf(114), BigDecimal.valueOf(76), BigDecimal.valueOf(38), BigDecimal.valueOf(0)]
    """
    Tabelle fuer die Hoechstbetraege des Altersentlastungsbetrags
    """

    ZAHL1 = BigDecimal.ONE
    """
    Zahlenkonstanten fuer im Plan oft genutzte BigDecimal Werte
    """

    ZAHL2 = BigDecimal(2)
    ZAHL3 = BigDecimal(3)
    ZAHL4 = BigDecimal(4)
    ZAHL5 = BigDecimal(5)
    ZAHL6 = BigDecimal(6)
    ZAHL7 = BigDecimal(7)
    ZAHL8 = BigDecimal(8)
    ZAHL9 = BigDecimal(9)
    ZAHL10 = BigDecimal.TEN
    ZAHL11 = BigDecimal(11)
    ZAHL12 = BigDecimal(12)
    ZAHL100 = BigDecimal(100)
    ZAHL360 = BigDecimal(360)
    ZAHL700 = BigDecimal(700)

    def __init__(self, **kwargs):
        # input variables

        # Auf die Vollendung des 64. Lebensjahres folgende
        # Kalenderjahr (erforderlich, wenn ALTER1=1)
        self.AJAHR = 0
        if "AJAHR" in kwargs:
            self.setAjahr(kwargs["AJAHR"])

        # 1, wenn das 64. Lebensjahr zu Beginn des Kalenderjahres vollendet wurde, in dem
        # der Lohnzahlungszeitraum endet (Â§ 24 a EStG), sonst = 0
        self.ALTER1 = 0
        if "ALTER1" in kwargs:
            self.setAlter1(kwargs["ALTER1"])

        # Jahresfreibetrag nach Ma&szlig;gabe der Eintragungen auf der
        # Lohnsteuerkarte in Cents (ggf. 0)
        self.JFREIB = BigDecimal(0)
        if "JFREIB" in kwargs:
            self.setJfreib(kwargs["JFREIB"])

        # Jahreshinzurechnungsbetrag in Cents (ggf. 0)
        self.JHINZU = BigDecimal(0)
        if "JHINZU" in kwargs:
            self.setJhinzu(kwargs["JHINZU"])

        # Voraussichtlicher Jahresarbeitslohn ohne sonstige Bezuege und
        # ohne Verguetung fuer mehrjaehrige Taetigkeit in Cents (ggf. 0)
        # Anmerkung: Die Eingabe dieses Feldes ist erforderlich bei Eingabe
        # â€žsonstiger Bezuegeâ€œ (Feld SONSTB) oder bei Eingabe der â€žVerguetung
        # fuer mehrjaehrige Taetigkeitâ€œ (Feld VMT).
        self.JRE4 = BigDecimal(0)
        if "JRE4" in kwargs:
            self.setJre4(kwargs["JRE4"])

        # In JRE4 enthaltene Versorgungsbezuege in Cents (ggf. 0)
        self.JVBEZ = BigDecimal(0)
        if "JVBEZ" in kwargs:
            self.setJvbez(kwargs["JVBEZ"])

        # 2 = fÃ¼r den Arbeitnehmer wird die gekÃ¼rzte Vorsorgepauschale nach dem Recht 2008 angesetzt
        # (Â§ 10c Abs. 3 EStG n.F.), jedoch bei der GÃ¼nstigerprÃ¼fung die ungekÃ¼rzte Vorsorgepauschale
        # nach dem Recht bis 2004 berÃ¼cksichtigt (Â§ 10c Abs. 2 EStG a.F.); Ã„nderung durch das JStG 2008.
        # 1 = fÃ¼r den Arbeitnehmer wird die gekÃ¼rzte Vorsorgepauschale angewandt (Â§ 10c Abs. 3 EStG),
        # soweit nicht Arbeitnehmer der Fallgruppe 2.
        # 0 = andere Arbeitnehmer.
        # FÃ¼r die Zuordnung sind allein die dem Arbeitgeber ohnehin bekannten Tatsachen maÃŸgebend;
        # zusÃ¤tzliche Ermittlungen braucht der Arbeitgeber nicht anzustellen.
        self.KRV = 0
        if "KRV" in kwargs:
            self.setKrv(kwargs["KRV"])

        # Lohnzahlungszeitraum:
        # 1 = Jahr
        # 2 = Monat
        # 3 = Woche
        # 4 = Tag
        self.LZZ = 0
        if "LZZ" in kwargs:
            self.setLzz(kwargs["LZZ"])

        # In der Lohnsteuerkarte des Arbeitnehmers eingetragener Freibetrag fÃ¼r
        # den Lohnzahlungszeitraum in Cent
        self.LZZFREIB = BigDecimal(0)
        if "LZZFREIB" in kwargs:
            self.setLzzfreib(kwargs["LZZFREIB"])

        # In der Lohnsteuerkarte des Arbeitnehmers eingetragener Hinzurechnungsbetrag
        # fÃ¼r den Lohnzahlungszeitraum in Cent
        self.LZZHINZU = BigDecimal(0)
        if "LZZHINZU" in kwargs:
            self.setLzzhinzu(kwargs["LZZHINZU"])

        # Religionsgemeinschaft des Arbeitnehmers lt. Lohnsteuerkarte (bei
        # keiner Religionszugehoerigkeit = 0)
        self.R = 0
        if "R" in kwargs:
            self.setR(kwargs["R"])

        # Steuerpflichtiger Arbeitslohn vor Beruecksichtigung der Freibetraege
        # fuer Versorgungsbezuege, des Altersentlastungsbetrags und des auf
        # der Lohnsteuerkarte fuer den Lohnzahlungszeitraum eingetragenen
        # Freibetrags in Cents.
        self.RE4 = BigDecimal(0)
        if "RE4" in kwargs:
            self.setRe4(kwargs["RE4"])

        # Sonstige Bezuege (ohne Verguetung aus mehrjaehriger Taetigkeit) einschliesslich
        # Sterbegeld bei Versorgungsbezuegen sowie Kapitalauszahlungen/Abfindungen,
        # soweit es sich nicht um Bezuege fuer mehrere Jahre handelt in Cents (ggf. 0)
        self.SONSTB = BigDecimal(0)
        if "SONSTB" in kwargs:
            self.setSonstb(kwargs["SONSTB"])

        # Sterbegeld bei Versorgungsbezuegen sowie Kapitalauszahlungen/Abfindungen,
        # soweit es sich nicht um Bezuege fuer mehrere Jahre handelt
        # (in SONSTB enthalten) in Cents
        self.STERBE = BigDecimal(0)
        if "STERBE" in kwargs:
            self.setSterbe(kwargs["STERBE"])

        # Steuerklasse:
        # 1 = I
        # 2 = II
        # 3 = III
        # 4 = IV
        # 5 = V
        # 6 = VI
        self.STKL = 0
        if "STKL" in kwargs:
            self.setStkl(kwargs["STKL"])

        # In RE4 enthaltene Versorgungsbezuege in Cents (ggf. 0)
        self.VBEZ = BigDecimal(0)
        if "VBEZ" in kwargs:
            self.setVbez(kwargs["VBEZ"])

        # Vorsorgungsbezug im Januar 2005 bzw. fuer den ersten vollen Monat
        # in Cents
        self.VBEZM = BigDecimal(0)
        if "VBEZM" in kwargs:
            self.setVbezm(kwargs["VBEZM"])

        # Voraussichtliche Sonderzahlungen im Kalenderjahr des Versorgungsbeginns
        # bei Versorgungsempfaengern ohne Sterbegeld, Kapitalauszahlungen/Abfindungen
        # bei Versorgungsbezuegen in Cents
        self.VBEZS = BigDecimal(0)
        if "VBEZS" in kwargs:
            self.setVbezs(kwargs["VBEZS"])

        # In SONSTB enthaltene Versorgungsbezuege einschliesslich Sterbegeld
        # in Cents (ggf. 0)
        self.VBS = BigDecimal(0)
        if "VBS" in kwargs:
            self.setVbs(kwargs["VBS"])

        # Jahr, in dem der Versorgungsbezug erstmalig gewaehrt wurde; werden
        # mehrere Versorgungsbezuege gezahlt, so gilt der aelteste erstmalige Bezug
        self.VJAHR = 0
        if "VJAHR" in kwargs:
            self.setVjahr(kwargs["VJAHR"])

        # Kapitalauszahlungen/Abfindungen bei Versorgungsbezuegen fuer mehrere Jahre in Cents (ggf. 0)
        self.VKAPA = BigDecimal(0)
        if "VKAPA" in kwargs:
            self.setVkapa(kwargs["VKAPA"])

        # Verguetung fuer mehrjaehrige Taetigkeit ohne Kapitalauszahlungen/Abfindungen bei
        # Versorgungsbezuegen in Cents (ggf. 0)
        self.VMT = BigDecimal(0)
        if "VMT" in kwargs:
            self.setVmt(kwargs["VMT"])

        # Zahl der Freibetraege fuer Kinder (eine Dezimalstelle, nur bei Steuerklassen
        # I, II, III und IV)
        self.ZKF = BigDecimal(0)
        if "ZKF" in kwargs:
            self.setZkf(kwargs["ZKF"])

        # Zahl der Monate, fuer die Versorgungsbezuege gezahlt werden (nur
        # erforderlich bei Jahresberechnung (LZZ = 1)
        self.ZMVB = 0
        if "ZMVB" in kwargs:
            self.setZmvb(kwargs["ZMVB"])

        # output variables

        # Bemessungsgrundlage fuer die Kirchenlohnsteuer in Cents
        self.BK = BigDecimal(0)

        # Bemessungsgrundlage der sonstigen Einkuenfte (ohne Verguetung
        # fuer mehrjaehrige Taetigkeit) fuer die Kirchenlohnsteuer in Cents
        self.BKS = BigDecimal(0)
        self.BKV = BigDecimal(0)

        # Fuer den Lohnzahlungszeitraum einzubehaltende Lohnsteuer in Cents
        self.LSTLZZ = BigDecimal(0)

        # Fuer den Lohnzahlungszeitraum einzubehaltender Solidaritaetszuschlag
        # in Cents
        self.SOLZLZZ = BigDecimal(0)

        # Solidaritaetszuschlag fuer sonstige Bezuege (ohne Verguetung fuer mehrjaehrige
        # Taetigkeit) in Cents
        self.SOLZS = BigDecimal(0)

        # Solidaritaetszuschlag fuer die Verguetung fuer mehrjaehrige Taetigkeit in
        # Cents
        self.SOLZV = BigDecimal(0)

        # Lohnsteuer fuer sonstige Einkuenfte (ohne Verguetung fuer mehrjaehrige
        # Taetigkeit) in Cents
        self.STS = BigDecimal(0)

        # Lohnsteuer fuer Verguetung fuer mehrjaehrige Taetigkeit in Cents
        self.STV = BigDecimal(0)

        # internal variables

        # Altersentlastungsbetrag nach AlterseinkÃ¼nftegesetz in â‚¬,
        # Cent (2 Dezimalstellen)
        self.ALTE = BigDecimal(0)

        # Arbeitnehmer-Pauschbetrag in EURO
        self.ANP = BigDecimal(0)

        # Auf den Lohnzahlungszeitraum entfallender Anteil von Jahreswerten
        # auf ganze Cents abgerundet
        self.ANTEIL1 = BigDecimal(0)

        # Auf den Lohnzahlungszeitraum entfallender Anteil von Jahreswerten
        # auf ganze Cents aufgerundet
        self.ANTEIL2 = BigDecimal(0)

        # Bemessungsgrundlage fÃ¼r Altersentlastungsbetrag in â‚¬, Cent
        # (2 Dezimalstellen)
        self.BMG = BigDecimal(0)

        # Differenz zwischen ST1 und ST2 in EURO
        self.DIFF = BigDecimal(0)

        # Entlastungsbetrag fuer Alleinerziehende in EURO
        self.EFA = BigDecimal(0)

        # Versorgungsfreibetrag in â‚¬, Cent (2 Dezimalstellen)
        self.FVB = BigDecimal(0)

        # Versorgungsfreibetrag in â‚¬, Cent (2 Dezimalstellen) fÃ¼r die Berechnung
        # der Lohnsteuer fÃ¼r den sonstigen Bezug
        self.FVBSO = BigDecimal(0)

        # Zuschlag zum Versorgungsfreibetrag in EURO
        self.FVBZ = BigDecimal(0)

        # Zuschlag zum Versorgungsfreibetrag in EURO fuer die Berechnung
        # der Lohnsteuer beim sonstigen Bezug
        self.FVBZSO = BigDecimal(0)

        # Sicherungsfeld fÃ¼r den Zuschlag zum Versorgungsfreibetrag in â‚¬ fÃ¼r
        # die Berechnung der Lohnsteuer fÃ¼r die VergÃ¼tung fÃ¼r mehrjÃ¤hrige
        # TÃ¤tigkeit
        self.FVBZOSO = BigDecimal(0)

        # Maximaler Altersentlastungsbetrag in â‚¬
        self.HBALTE = BigDecimal(0)

        # MaÃŸgeblicher maximaler Versorgungsfreibetrag in â‚¬
        self.HFVB = BigDecimal(0)

        # MaÃŸgeblicher maximaler Zuschlag zum Versorgungsfreibetrag in â‚¬,Cent
        # (2 Dezimalstellen)
        self.HFVBZ = BigDecimal(0)

        # MaÃŸgeblicher maximaler Zuschlag zum Versorgungsfreibetrag in â‚¬, Cent
        # (2 Dezimalstellen) fÃ¼r die Berechnung der Lohnsteuer fÃ¼r den
        # sonstigen Bezug
        self.HFVBZSO = BigDecimal(0)

        # Nummer der Tabellenwerte fuer Versorgungsparameter
        self.J = 0

        # Jahressteuer nach Â§ 51a EStG, aus der Solidaritaetszuschlag und
        # Bemessungsgrundlage fuer die Kirchenlohnsteuer ermittelt werden in EURO
        self.JBMG = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechneter LZZFREIB in â‚¬, Cent
        # (2 Dezimalstellen)
        self.JLFREIB = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnete LZZHINZU in â‚¬, Cent
        # (2 Dezimalstellen)
        self.JLHINZU = BigDecimal(0)

        # Jahreswert, dessen Anteil fuer einen Lohnzahlungszeitraum in
        # UPANTEIL errechnet werden soll in Cents
        self.JW = BigDecimal(0)

        # Nummer der Tabellenwerte fuer Parameter bei Altersentlastungsbetrag
        self.K = 0

        # Merker fÃ¼r Berechnung Lohnsteuer fÃ¼r mehrjÃ¤hrige TÃ¤tigkeit.
        # 0 = normale Steuerberechnung
        # 1 = Steuerberechnung fÃ¼r mehrjÃ¤hrige TÃ¤tigkeit
        # 2 = Steuerberechnung fÃ¼r mehrjÃ¤hrige TÃ¤tigkeit Sonderfall nach Â§ 34 Abs. 1 Satz 3 EStG
        self.KENNVMT = 0

        # Summe der Freibetraege fuer Kinder in EURO
        self.KFB = BigDecimal(0)

        # Kennzahl fuer die Einkommensteuer-Tabellenart:
        # 1 = Grundtabelle
        # 2 = Splittingtabelle
        self.KZTAB = 0

        # Jahreslohnsteuer in EURO
        self.LSTJAHR = BigDecimal(0)

        # Zwischenfelder der Jahreslohnsteuer in Cent
        self.LST1 = BigDecimal(0)
        self.LST2 = BigDecimal(0)
        self.LST3 = BigDecimal(0)
        self.LSTOSO = BigDecimal(0)
        self.LSTSO = BigDecimal(0)

        # Mindeststeuer fuer die Steuerklassen V und VI in EURO
        self.MIST = BigDecimal(0)

        # Rechenwert in Gleitkommadarstellung
        self.RW = BigDecimal(0)

        # Sonderausgaben-Pauschbetrag in EURO
        self.SAP = BigDecimal(0)

        # Freigrenze fuer den Solidaritaetszuschlag in EURO
        self.SOLZFREI = BigDecimal(0)

        # Solidaritaetszuschlag auf die Jahreslohnsteuer in EURO, C (2 Dezimalstellen)
        self.SOLZJ = BigDecimal(0)

        # Zwischenwert fuer den Solidaritaetszuschlag auf die Jahreslohnsteuer
        # in EURO, C (2 Dezimalstellen)
        self.SOLZMIN = BigDecimal(0)

        # Tarifliche Einkommensteuer in EURO
        self.ST = BigDecimal(0)

        # Tarifliche Einkommensteuer auf das 1,25-fache ZX in EURO
        self.ST1 = BigDecimal(0)

        # Tarifliche Einkommensteuer auf das 0,75-fache ZX in EURO
        self.ST2 = BigDecimal(0)

        # Bemessungsgrundlage fuer den Versorgungsfreibetrag in Cents
        self.VBEZB = BigDecimal(0)

        # Bemessungsgrundlage fÃ¼r den Versorgungsfreibetrag in Cent fÃ¼r
        # den sonstigen Bezug
        self.VBEZBSO = BigDecimal(0)

        # Hoechstbetrag der Vorsorgepauschale nach Alterseinkuenftegesetz in EURO, C
        self.VHB = BigDecimal(0)

        # Vorsorgepauschale in EURO, C (2 Dezimalstellen)
        self.VSP = BigDecimal(0)

        # Vorsorgepauschale nach Alterseinkuenftegesetz in EURO, C
        self.VSPN = BigDecimal(0)

        # Zwischenwert 1 bei der Berechnung der Vorsorgepauschale nach
        # dem Alterseinkuenftegesetz in EURO, C (2 Dezimalstellen)
        self.VSP1 = BigDecimal(0)

        # Zwischenwert 2 bei der Berechnung der Vorsorgepauschale nach
        # dem Alterseinkuenftegesetz in EURO, C (2 Dezimalstellen)
        self.VSP2 = BigDecimal(0)

        # Hoechstbetrag der Vorsorgepauschale nach Â§ 10c Abs. 3 EStG in EURO
        self.VSPKURZ = BigDecimal(0)

        # Hoechstbetrag der Vorsorgepauschale nach Â§ 10c Abs. 2 Nr. 2 EStG in EURO
        self.VSPMAX1 = BigDecimal(0)

        # Hoechstbetrag der Vorsorgepauschale nach Â§ 10c Abs. 2 Nr. 3 EStG in EURO
        self.VSPMAX2 = BigDecimal(0)

        # Vorsorgepauschale nach Â§ 10c Abs. 2 Satz 2 EStG vor der Hoechstbetragsberechnung
        # in EURO, C (2 Dezimalstellen)
        self.VSPO = BigDecimal(0)

        # Fuer den Abzug nach Â§ 10c Abs. 2 Nrn. 2 und 3 EStG verbleibender
        # Rest von VSPO in EURO, C (2 Dezimalstellen)
        self.VSPREST = BigDecimal(0)

        # Hoechstbetrag der Vorsorgepauschale nach Â§ 10c Abs. 2 Nr. 1 EStG
        # in EURO, C (2 Dezimalstellen)
        self.VSPVOR = BigDecimal(0)

        # Zu versteuerndes Einkommen gem. Â§ 32a Abs. 1 und 2 EStG â‚¬, C
        # (2 Dezimalstellen)
        self.X = BigDecimal(0)

        # gem. Â§ 32a Abs. 1 EStG (6 Dezimalstellen)
        self.Y = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes RE4 in â‚¬, C (2 Dezimalstellen)
        # nach Abzug der FreibetrÃ¤ge nach Â§ 39 b Abs. 2 Satz 3 und 4.
        self.ZRE4 = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes RE4 in â‚¬, C (2 Dezimalstellen)
        self.ZRE4J = BigDecimal(0)

        # Sicherungsfeld von ZRE4 bei der Berechnung der Lohnsteuer fÃ¼r
        # die VergÃ¼tung fÃ¼r mehrjÃ¤hrige TÃ¤tigkeit in â‚¬, C (2 Dezimalstellen)
        self.ZRE4OSO = BigDecimal(0)

        # 1/5 des mehrjÃ¤hriger Bezugs abzÃ¼glich der auf diesen Lohnbestandteil
        # entfallenden festen TabellenfreibetrÃ¤ge in â‚¬, C (2 Dezimalstellen)
        self.ZRE4VMT = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes RE4 in â‚¬, C (2 Dezimalstellen)
        # nach Abzug des Versorgungsfreibetrags und des Alterentlastungsbetrags
        # zur Berechnung der Vorsorgepauschale in â‚¬, Cent (2 Dezimalstellen)
        self.ZRE4VP = BigDecimal(0)

        # Feste TabellenfreibetrÃ¤ge (ohne Vorsorgepauschale) in â‚¬, Cent
        # (2 Dezimalstellen)
        self.ZTABFB = BigDecimal(0)

        # Sicherungsfeld von ZTABFB bei der Berechnung fÃ¼r die VergÃ¼tung
        # fÃ¼r mehrjÃ¤hrige TÃ¤tigkeit in â‚¬, Cent (2 Dezimalstellen)
        self.ZTABFBOSO = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes (VBEZ abzueglich FVB) in
        # EURO, C (2 Dezimalstellen)
        self.ZVBEZ = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes VBEZ in â‚¬, C (2 Dezimalstellen)
        self.ZVBEZJ = BigDecimal(0)

        # Zu versteuerndes Einkommen in â‚¬, C (2 Dezimalstellen)
        self.ZVE = BigDecimal(0)

        # Zwischenfelder zu X fuer die Berechnung der Steuer nach Â§ 39b
        # Abs. 2 Satz 8 EStG in EURO.
        self.ZX = BigDecimal(0)
        self.ZZX = BigDecimal(0)
        self.HOCH = BigDecimal(0)
        self.VERGL = BigDecimal(0)


    def setAjahr(self, value):
        self.AJAHR = value

    def setAlter1(self, value):
        self.ALTER1 = value

    def setJfreib(self, value):
        self.JFREIB = BigDecimal(value)

    def setJhinzu(self, value):
        self.JHINZU = BigDecimal(value)

    def setJre4(self, value):
        self.JRE4 = BigDecimal(value)

    def setJvbez(self, value):
        self.JVBEZ = BigDecimal(value)

    def setKrv(self, value):
        self.KRV = value

    def setLzz(self, value):
        self.LZZ = value

    def setLzzfreib(self, value):
        self.LZZFREIB = BigDecimal(value)

    def setLzzhinzu(self, value):
        self.LZZHINZU = BigDecimal(value)

    def setR(self, value):
        self.R = value

    def setRe4(self, value):
        self.RE4 = BigDecimal(value)

    def setSonstb(self, value):
        self.SONSTB = BigDecimal(value)

    def setSterbe(self, value):
        self.STERBE = BigDecimal(value)

    def setStkl(self, value):
        self.STKL = value

    def setVbez(self, value):
        self.VBEZ = BigDecimal(value)

    def setVbezm(self, value):
        self.VBEZM = BigDecimal(value)

    def setVbezs(self, value):
        self.VBEZS = BigDecimal(value)

    def setVbs(self, value):
        self.VBS = BigDecimal(value)

    def setVjahr(self, value):
        self.VJAHR = value

    def setVkapa(self, value):
        self.VKAPA = BigDecimal(value)

    def setVmt(self, value):
        self.VMT = BigDecimal(value)

    def setZkf(self, value):
        self.ZKF = BigDecimal(value)

    def setZmvb(self, value):
        self.ZMVB = value

    def getBk(self):
        return self.BK

    def getBks(self):
        return self.BKS

    def getBkv(self):
        return self.BKV

    def getLstlzz(self):
        return self.LSTLZZ

    def getSolzlzz(self):
        return self.SOLZLZZ

    def getSolzs(self):
        return self.SOLZS

    def getSolzv(self):
        return self.SOLZV

    def getSts(self):
        return self.STS

    def getStv(self):
        return self.STV

    def MAIN(self):
        """
        PROGRAMMABLAUFPLAN 2008, PAP Seite 10
        """
        self.MRE4JL()
        self.MRE4()
        self.MRE4ABZ()
        self.MZTABFB()
        self.KENNVMT = 0
        self.MLSTJAHR()
        self.LSTJAHR = self.ST
        self.JW = self.LSTJAHR.multiply(Lst2008.ZAHL100)
        self.UPANTEIL()
        self.LSTLZZ = self.ANTEIL1
        if self.ZKF.compareTo(BigDecimal.ZERO) == 1:
            self.ZTABFB = self.ZTABFB.add(self.KFB).setScale(2, BigDecimal.ROUND_DOWN)
            self.MLSTJAHR()
            self.JBMG = self.ST
        else:
            self.JBMG = self.LSTJAHR
        self.MSOLZ()
        self.MSONST()
        self.MVMT()

    def MRE4JL(self):
        """
        Ermittlung des Jahresarbeitslohns und der FreibetrÃ¤ge Â§ 39 b Abs. 2 Satz 2 EStG, PAP Seite 11
        """
        if self.LZZ == 1:
            self.ZRE4J = self.RE4.divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
            self.ZVBEZJ = self.VBEZ.divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
            self.JLFREIB = self.LZZFREIB.divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
            self.JLHINZU = self.LZZHINZU.divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
        else:
            if self.LZZ == 2:
                self.ZRE4J = self.RE4.multiply(Lst2008.ZAHL12).divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                self.ZVBEZJ = self.VBEZ.multiply(Lst2008.ZAHL12).divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                self.JLFREIB = self.LZZFREIB.multiply(Lst2008.ZAHL12).divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                self.JLHINZU = self.LZZHINZU.multiply(Lst2008.ZAHL12).divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
            else:
                if self.LZZ == 3:
                    self.ZRE4J = self.RE4.multiply(Lst2008.ZAHL360).divide(Lst2008.ZAHL700, 2, BigDecimal.ROUND_DOWN)
                    self.ZVBEZJ = self.VBEZ.multiply(Lst2008.ZAHL360).divide(Lst2008.ZAHL700, 2, BigDecimal.ROUND_DOWN)
                    self.JLFREIB = self.LZZFREIB.multiply(Lst2008.ZAHL360).divide(Lst2008.ZAHL700, 2, BigDecimal.ROUND_DOWN)
                    self.JLHINZU = self.LZZHINZU.multiply(Lst2008.ZAHL360).divide(Lst2008.ZAHL700, 2, BigDecimal.ROUND_DOWN)
                else:
                    self.ZRE4J = self.RE4.multiply(Lst2008.ZAHL360).divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                    self.ZVBEZJ = self.VBEZ.multiply(Lst2008.ZAHL360).divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                    self.JLFREIB = self.LZZFREIB.multiply(Lst2008.ZAHL360).divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                    self.JLHINZU = self.LZZHINZU.multiply(Lst2008.ZAHL360).divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)

    def MRE4(self):
        """
        FreibetrÃ¤ge fÃ¼r VersorgungsbezÃ¼ge, Altersentlastungsbetrag (Â§ 39b Abs. 2 Satz 3 EStG), PAP Seite 12
        """
        if self.ZVBEZJ.compareTo(BigDecimal.ZERO) == 0:
            self.FVBZ = BigDecimal.ZERO
            self.FVB = BigDecimal.ZERO
            self.FVBZSO = BigDecimal.ZERO
            self.FVBSO = BigDecimal.ZERO
        else:
            if self.VJAHR < 2006:
                self.J = 1
            else:
                if self.VJAHR < 2040:
                    self.J = self.VJAHR - 2004
                else:
                    self.J = 36
            if self.LZZ == 1:
                self.VBEZB = self.VBEZM.multiply(BigDecimal.valueOf(self.ZMVB)).add(self.VBEZS)
                self.HFVB = Lst2008.TAB2[self.J].divide(Lst2008.ZAHL12).multiply(BigDecimal.valueOf(self.ZMVB))
                self.FVBZ = Lst2008.TAB3[self.J].divide(Lst2008.ZAHL12).multiply(BigDecimal.valueOf(self.ZMVB)).setScale(0, BigDecimal.ROUND_UP)
            else:
                self.VBEZB = self.VBEZM.multiply(Lst2008.ZAHL12).add(self.VBEZS).setScale(2, BigDecimal.ROUND_DOWN)
                self.HFVB = Lst2008.TAB2[self.J]
                self.FVBZ = Lst2008.TAB3[self.J]
            self.FVB = self.VBEZB.multiply(Lst2008.TAB1[self.J]).divide(Lst2008.ZAHL100).setScale(2, BigDecimal.ROUND_UP)
            if self.FVB.compareTo(self.HFVB) == 1:
                self.FVB = self.HFVB
            self.VBEZBSO = self.STERBE.add(self.VKAPA)
            self.FVBSO = self.FVB.add(self.VBEZBSO.multiply(Lst2008.TAB1[self.J]).divide(Lst2008.ZAHL100)).setScale(2, BigDecimal.ROUND_UP)
            if self.FVBSO.compareTo(Lst2008.TAB2[self.J]) == 1:
                self.FVBSO = Lst2008.TAB2[self.J]
            self.HFVBZSO = self.VBEZB.add(self.VBEZBSO).divide(Lst2008.ZAHL100).subtract(self.FVBSO).setScale(2, BigDecimal.ROUND_DOWN)
            if Lst2008.TAB3[3].compareTo(self.HFVBZSO) == 1:
                self.FVBZSO = self.HFVBZSO.setScale(0, BigDecimal.ROUND_UP)
            else:
                self.FVBZSO = Lst2008.TAB3[self.J]
            self.HFVBZ = self.VBEZB.divide(Lst2008.ZAHL100).subtract(self.FVB).setScale(2, BigDecimal.ROUND_DOWN)
            if self.FVBZ.compareTo(self.HFVBZ) == 1:
                self.FVBZ = self.HFVBZ.setScale(0, BigDecimal.ROUND_UP)
        self.MRE4ALTE()

    def MRE4ALTE(self):
        """
        Altersentlastungsbetrag (Â§ 39b Abs. 2 Satz 3 EStG), PAP Seite 13
        """
        if self.ALTER1 == 0:
            self.ALTE = BigDecimal.ZERO
        else:
            if self.AJAHR < 2006:
                self.K = 1
            else:
                if self.AJAHR < 2040:
                    self.K = self.AJAHR - 2004
                else:
                    self.K = 36
            self.BMG = self.ZRE4J.subtract(self.ZVBEZJ)
            self.ALTE = self.BMG.multiply(Lst2008.TAB4[self.K]).setScale(2, BigDecimal.ROUND_UP)
            self.HBALTE = Lst2008.TAB5[self.K]
            if self.ALTE.compareTo(self.HBALTE) == 1:
                self.ALTE = self.HBALTE

    def MRE4ABZ(self):
        """
        Ermittlung des Jahresarbeitslohns nach Abzug der FreibetrÃ¤ge nach Â§ 39 b Abs. 2 Satz 3 und 4 EStG, PAP Seite 15
        """
        self.ZRE4 = self.ZRE4J.subtract(self.FVB).subtract(self.ALTE).subtract(self.JLFREIB).add(self.JLHINZU).setScale(2, BigDecimal.ROUND_DOWN)
        if self.ZRE4.compareTo(BigDecimal.ZERO) == -1:
            self.ZRE4 = BigDecimal.ZERO
        self.ZRE4VP = self.ZRE4J.subtract(self.FVB).subtract(self.ALTE).setScale(2, BigDecimal.ROUND_DOWN)
        if self.ZRE4VP.compareTo(BigDecimal.ZERO) == -1:
            self.ZRE4VP = BigDecimal.ZERO
        self.ZVBEZ = self.ZVBEZJ.subtract(self.FVB).setScale(2, BigDecimal.ROUND_DOWN)
        if self.ZVBEZ.compareTo(BigDecimal.ZERO) == -1:
            self.ZVBEZ = BigDecimal.ZERO

    def MZTABFB(self):
        """
        Ermittlung der festen TabellenfreibetrÃ¤ge (ohne Vorsorgepauschale), PAP Seite 16
        """
        self.ANP = BigDecimal.ZERO
        if self.ZVBEZ.compareTo(BigDecimal.ZERO) >= 0:
            if self.ZVBEZ.compareTo(self.FVBZ) == -1:
                self.FVBZ = self.ZVBEZ.setScale(0, BigDecimal.ROUND_DOWN)
        if self.STKL < 6:
            if self.ZVBEZ.compareTo(BigDecimal.ZERO) == 1:
                if self.ZVBEZ.subtract(self.FVBZ).compareTo(BigDecimal.valueOf(102)) == -1:
                    self.ANP = self.ZVBEZ.subtract(self.FVBZ).setScale(0, BigDecimal.ROUND_DOWN)
                else:
                    self.ANP = BigDecimal.valueOf(102)
        else:
            self.FVBZ = BigDecimal.valueOf(0)
            self.FVBZSO = BigDecimal.valueOf(0)
        if self.STKL < 6:
            if self.ZRE4.compareTo(self.ZVBEZ) == 1:
                if self.ZRE4.subtract(self.ZVBEZ).compareTo(BigDecimal.valueOf(920)) == -1:
                    self.ANP = self.ANP.add(self.ZRE4).subtract(self.ZVBEZ).setScale(0, BigDecimal.ROUND_DOWN)
                else:
                    self.ANP = self.ANP.add(BigDecimal.valueOf(920))
        self.KZTAB = 1
        if self.STKL == 1:
            self.SAP = BigDecimal.valueOf(36)
            self.KFB = self.ZKF.multiply(BigDecimal.valueOf(5808)).setScale(0, BigDecimal.ROUND_DOWN)
        else:
            if self.STKL == 2:
                self.EFA = BigDecimal.valueOf(1308)
                self.SAP = BigDecimal.valueOf(36)
                self.KFB = self.ZKF.multiply(BigDecimal.valueOf(5808)).setScale(0, BigDecimal.ROUND_DOWN)
            else:
                if self.STKL == 3:
                    self.KZTAB = 2
                    self.SAP = BigDecimal.valueOf(72)
                    self.KFB = self.ZKF.multiply(BigDecimal.valueOf(5808)).setScale(0, BigDecimal.ROUND_DOWN)
                else:
                    if self.STKL == 4:
                        self.SAP = BigDecimal.valueOf(36)
                        self.KFB = self.ZKF.multiply(BigDecimal.valueOf(2904)).setScale(0, BigDecimal.ROUND_DOWN)
                    else:
                        self.KFB = BigDecimal.ZERO
        self.ZTABFB = self.EFA.add(self.ANP).add(self.SAP).add(self.FVBZ).setScale(2, BigDecimal.ROUND_DOWN)

    def MLSTJAHR(self):
        """
        Ermittlung Jahreslohnsteuer, PAP Seite 17
        """
        if self.STKL < 5:
            self.UPEVP()
        else:
            self.VSP = BigDecimal.ZERO
        if self.KENNVMT == 0:
            self.ZVE = self.ZRE4.subtract(self.ZTABFB).subtract(self.VSP).setScale(2, BigDecimal.ROUND_DOWN)
        else:
            if self.KENNVMT == 1:
                self.ZVE = self.ZRE4OSO.subtract(self.ZTABFBOSO).add(self.ZRE4VMT).subtract(self.VSP).setScale(2, BigDecimal.ROUND_DOWN)
            else:
                self.ZVE = self.ZRE4.subtract(self.ZTABFB).divide(Lst2008.ZAHL5).subtract(self.VSP).setScale(2, BigDecimal.ROUND_DOWN)
        if self.ZVE.compareTo(Lst2008.ZAHL1) == -1:
            self.ZVE = BigDecimal.ZERO
            self.X = BigDecimal.ZERO
        else:
            self.X = self.ZVE.divide(BigDecimal.valueOf(self.KZTAB), 0, BigDecimal.ROUND_DOWN)
        if self.STKL < 5:
            self.UPTAB07()
        else:
            self.MST5_6()

    def UPEVP(self):
        """
        Vorsorgepauschale (Â§ 39b Abs. 2 Satz 6 Nr 3 EStG) nach AlterseinkÃ¼nftegesetz, PAP Seite 18
        """
        if self.KRV > 0:
            self.VSP1 = BigDecimal.ZERO
        else:
            if self.ZRE4VP.compareTo(BigDecimal.valueOf(63600)) == 1:
                self.ZRE4VP = BigDecimal.valueOf(63600)
            self.VSP1 = self.ZRE4VP.multiply(BigDecimal.valueOf(0.32)).setScale(2, BigDecimal.ROUND_DOWN)
            self.VSP1 = self.VSP1.multiply(BigDecimal.valueOf(0.0995)).setScale(2, BigDecimal.ROUND_DOWN)
        self.VSP2 = self.ZRE4VP.multiply(BigDecimal.valueOf(0.11)).setScale(2, BigDecimal.ROUND_DOWN)
        self.VHB = BigDecimal.valueOf(self.KZTAB).multiply(BigDecimal.valueOf(1500)).setScale(2, BigDecimal.ROUND_DOWN)
        if self.VSP2.compareTo(self.VHB) == 1:
            self.VSP2 = self.VHB
        self.VSPN = self.VSP1.add(self.VSP2).setScale(0, BigDecimal.ROUND_UP)
        self.MVSP()
        if self.VSPN.compareTo(self.VSP) == 1:
            self.VSP = self.VSPN.setScale(2, BigDecimal.ROUND_DOWN)

    def MVSP(self):
        """
        Vorsorgepauschale (Â§39b Abs. 2 Satz 6 Nr 3 EStG) Vergleichsberechnung fuer Guenstigerpruefung, PAP Seite 19
        """
        self.VSPO = self.ZRE4VP.multiply(BigDecimal.valueOf(0.2)).setScale(2, BigDecimal.ROUND_DOWN)
        self.VSPVOR = BigDecimal.valueOf(self.KZTAB).multiply(BigDecimal.valueOf(3068)).setScale(2, BigDecimal.ROUND_DOWN)
        self.VSPMAX1 = BigDecimal.valueOf(self.KZTAB).multiply(BigDecimal.valueOf(1334))
        self.VSPMAX2 = BigDecimal.valueOf(self.KZTAB).multiply(BigDecimal.valueOf(667))
        self.VSPKURZ = BigDecimal.valueOf(self.KZTAB).multiply(BigDecimal.valueOf(1134))
        if self.KRV == 1:
            if self.VSPO.compareTo(self.VSPKURZ) == 1:
                self.VSP = self.VSPKURZ
            else:
                self.VSP = self.VSPO.setScale(0, BigDecimal.ROUND_DOWN)
        else:
            self.UMVSP()

    def UMVSP(self):
        """
        Vorsorgepauschale, PAP Seite 20
        """
        self.VSPVOR = self.VSPVOR.subtract(self.ZRE4VP.multiply(BigDecimal.valueOf(0.16))).setScale(2, BigDecimal.ROUND_DOWN)
        if self.VSPVOR.compareTo(BigDecimal.ZERO) == -1:
            self.VSPVOR = BigDecimal.ZERO
        if self.VSPO.compareTo(self.VSPVOR) == 1:
            self.VSP = self.VSPVOR
            self.VSPREST = self.VSPO.subtract(self.VSPVOR)
            if self.VSPREST.compareTo(self.VSPMAX1) == 1:
                self.VSP = self.VSP.add(self.VSPMAX1)
                self.VSPREST = self.VSPREST.subtract(self.VSPMAX1).divide(Lst2008.ZAHL2, 2, BigDecimal.ROUND_UP)
                if self.VSPREST.compareTo(self.VSPMAX2) == 1:
                    self.VSP = self.VSP.add(self.VSPMAX2).setScale(0, BigDecimal.ROUND_DOWN)
                else:
                    self.VSP = self.VSP.add(self.VSPREST).setScale(0, BigDecimal.ROUND_DOWN)
            else:
                self.VSP = self.VSP.add(self.VSPREST).setScale(0, BigDecimal.ROUND_DOWN)
        else:
            self.VSP = self.VSPO.setScale(0, BigDecimal.ROUND_DOWN)

    def MST5_6(self):
        """
        Lohnsteuer fuer die Steuerklassen V und VI (Â§ 39b Abs. 2 Satz 8 EStG), PAP Seite 21
        """
        self.ZZX = self.X
        if self.ZZX.compareTo(BigDecimal.valueOf(25812)) == 1:
            self.ZX = BigDecimal.valueOf(25812)
            self.UP5_6()
            if self.ZZX.compareTo(BigDecimal.valueOf(200000)) == 1:
                self.ST = self.ST.add(BigDecimal.valueOf(73158.96)).setScale(0, BigDecimal.ROUND_DOWN)
                self.ST = self.ST.add(self.ZZX.subtract(BigDecimal.valueOf(200000)).multiply(BigDecimal.valueOf(0.45))).setScale(0, BigDecimal.ROUND_DOWN)
            else:
                self.ST = self.ST.add(self.ZZX.subtract(BigDecimal.valueOf(25812)).multiply(BigDecimal.valueOf(0.42))).setScale(0, BigDecimal.ROUND_DOWN)
        else:
            self.ZX = self.ZZX
            self.UP5_6()
            if self.ZZX.compareTo(BigDecimal.valueOf(9144)) == 1:
                self.VERGL = self.ST
                self.ZX = BigDecimal.valueOf(9144)
                self.UP5_6()
                self.HOCH = self.ST.add(self.ZZX.subtract(BigDecimal.valueOf(9144)).multiply(BigDecimal.valueOf(0.42))).setScale(0, BigDecimal.ROUND_DOWN)
                if self.HOCH.compareTo(self.VERGL) == -1:
                    self.ST = self.HOCH
                else:
                    self.ST = self.VERGL

    def UP5_6(self):
        """
        Lohnsteuer fuer die Steuerklassen V und VI (Â§ 39b Abs. 2 Satz 8 EStG), PAP Seite 21
        """
        self.X = self.ZX.multiply(BigDecimal.valueOf(1.25)).setScale(2, BigDecimal.ROUND_DOWN)
        self.UPTAB07()
        self.ST1 = self.ST
        self.X = self.ZX.multiply(BigDecimal.valueOf(0.75)).setScale(2, BigDecimal.ROUND_DOWN)
        self.UPTAB07()
        self.ST2 = self.ST
        self.DIFF = self.ST1.subtract(self.ST2).multiply(Lst2008.ZAHL2)
        self.MIST = self.ZX.multiply(BigDecimal.valueOf(0.15)).setScale(0, BigDecimal.ROUND_DOWN)
        if self.MIST.compareTo(self.DIFF) == 1:
            self.ST = self.MIST
        else:
            self.ST = self.DIFF

    def MSOLZ(self):
        """
        Solidaritaetszuschlag, PAP Seite 22
        """
        self.SOLZFREI = BigDecimal.valueOf(972 * self.KZTAB)
        if self.JBMG.compareTo(self.SOLZFREI) == 1:
            self.SOLZJ = self.JBMG.multiply(BigDecimal.valueOf(5.5)).divide(Lst2008.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
            self.SOLZMIN = self.JBMG.subtract(self.SOLZFREI).multiply(BigDecimal.valueOf(20)).divide(Lst2008.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
            if self.SOLZMIN.compareTo(self.SOLZJ) == -1:
                self.SOLZJ = self.SOLZMIN
            self.JW = self.SOLZJ.multiply(Lst2008.ZAHL100).setScale(0, BigDecimal.ROUND_DOWN)
            self.UPANTEIL()
            self.SOLZLZZ = self.ANTEIL1
        else:
            self.SOLZLZZ = BigDecimal.ZERO
        if self.R > 0:
            self.JW = self.JBMG.multiply(Lst2008.ZAHL100)
            self.UPANTEIL()
            self.BK = self.ANTEIL1
        else:
            self.BK = BigDecimal.ZERO

    def UPANTEIL(self):
        """
        Anteil von Jahresbetraegen fuer einen LZZ (Â§ 39b Abs. 2 Satz 10 EStG), PAP Seite 23
        """
        if self.LZZ == 1:
            self.ANTEIL1 = self.JW
            self.ANTEIL2 = self.JW
        else:
            if self.LZZ == 2:
                self.ANTEIL1 = self.JW.divide(Lst2008.ZAHL12, 0, BigDecimal.ROUND_DOWN)
                self.ANTEIL2 = self.JW.divide(Lst2008.ZAHL12, 0, BigDecimal.ROUND_UP)
            else:
                if self.LZZ == 3:
                    self.ANTEIL1 = self.JW.multiply(Lst2008.ZAHL7).divide(Lst2008.ZAHL360, 0, BigDecimal.ROUND_DOWN)
                    self.ANTEIL2 = self.JW.multiply(Lst2008.ZAHL7).divide(Lst2008.ZAHL360, 0, BigDecimal.ROUND_UP)
                else:
                    self.ANTEIL1 = self.JW.divide(Lst2008.ZAHL360, 0, BigDecimal.ROUND_DOWN)
                    self.ANTEIL2 = self.JW.divide(Lst2008.ZAHL360, 0, BigDecimal.ROUND_UP)

    def MSONST(self):
        """
        Berechnung sonstiger Bezuege nach Â§ 39b Abs. 3 Saetze 1 bis 7 EStG), PAP Seite 24
        """
        self.LZZ = 1
        if self.ZMVB == 0:
            self.ZMVB = 12
        if self.SONSTB.compareTo(BigDecimal.ZERO) == 0:
            self.LSTSO = BigDecimal.ZERO
            self.STS = BigDecimal.ZERO
            self.SOLZS = BigDecimal.ZERO
            self.BKS = BigDecimal.ZERO
        else:
            self.MOSONST()
            self.ZRE4J = self.JRE4.add(self.SONSTB).divide(Lst2008.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
            self.ZVBEZJ = self.JVBEZ.add(self.VBS).divide(Lst2008.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
            self.MRE4SONST()
            self.MLSTJAHR()
            self.LSTSO = self.ST.multiply(Lst2008.ZAHL100)
            self.STS = self.LSTSO.subtract(self.LSTOSO)
            if self.STS.compareTo(BigDecimal.ZERO) == -1:
                self.STS = BigDecimal.ZERO
            self.SOLZS = self.STS.multiply(BigDecimal.valueOf(5.5)).divide(Lst2008.ZAHL100, 0, BigDecimal.ROUND_DOWN)
            if self.R > 0:
                self.BKS = self.STS
            else:
                self.BKS = BigDecimal.ZERO

    def MVMT(self):
        """
        Berechnung der Verguetung fuer mehrjaehrige Taetigkeit nach Â§ 39b Abs. 3 Satz 9 EStG), PAP Seite 25
        """
        if self.VKAPA.compareTo(BigDecimal.ZERO) == -1:
            self.VKAPA = BigDecimal.ZERO
        if self.VMT.add(self.VKAPA).compareTo(BigDecimal.ZERO) == 1:
            if self.LSTSO.compareTo(BigDecimal.ZERO) == 0:
                self.MOSONST()
                self.LST1 = self.LSTOSO
            else:
                self.LST1 = self.LSTSO
            self.ZRE4OSO = self.ZRE4
            self.ZTABFBOSO = self.ZTABFB
            self.FVBZOSO = self.FVBZ
            self.ZRE4J = self.JRE4.add(self.SONSTB).add(self.VMT).add(self.VKAPA).divide(Lst2008.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
            self.ZVBEZJ = self.JVBEZ.add(self.VBS).add(self.VKAPA).divide(Lst2008.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
            self.MRE4SONST()
            self.MLSTJAHR()
            self.LST3 = self.ST.multiply(Lst2008.ZAHL100)
            self.ZTABFB = self.ZTABFB.subtract(self.FVBZ).add(self.FVBZOSO).setScale(2, BigDecimal.ROUND_DOWN)
            self.KENNVMT = 1
            if self.JRE4.add(self.SONSTB).subtract(self.JFREIB).add(self.JHINZU).compareTo(BigDecimal.ZERO) == -1:
                self.KENNVMT = 2
                self.MLSTJAHR()
                self.LST2 = self.ST.multiply(Lst2008.ZAHL100)
                self.STV = self.LST2.multiply(Lst2008.ZAHL5)
            else:
                self.ZRE4VMT = self.VMT.divide(Lst2008.ZAHL100).add(self.VKAPA.divide(Lst2008.ZAHL100)).subtract(self.ZTABFB).add(self.ZTABFBOSO).divide(Lst2008.ZAHL5).setScale(2, BigDecimal.ROUND_DOWN)
                self.MLSTJAHR()
                self.LST2 = self.ST.multiply(Lst2008.ZAHL100)
                self.STV = self.LST2.subtract(self.LST1).multiply(Lst2008.ZAHL5)
            self.LST3 = self.LST3.subtract(self.LST1)
            if self.LST3.compareTo(self.STV) == -1:
                self.STV = self.LST3
            if self.STV.compareTo(BigDecimal.ZERO) == -1:
                self.STV = BigDecimal.ZERO
            self.SOLZV = self.STV.multiply(BigDecimal.valueOf(5.5)).divide(Lst2008.ZAHL100, 0, BigDecimal.ROUND_DOWN)
            if self.R > 0:
                self.BKV = self.STV
            else:
                self.BKV = BigDecimal.ZERO
        else:
            self.STV = BigDecimal.ZERO
            self.SOLZV = BigDecimal.ZERO
            self.BKV = BigDecimal.ZERO

    def MOSONST(self):
        """
        Sonderberechnung ohne sonstige BezÃ¼ge fÃ¼r Berechnung bei sonstigen BezÃ¼gen oder VergÃ¼tung fÃ¼r mehrjÃ¤hrige TÃ¤tigkeit, PAP Seite 26
        """
        self.ZRE4J = self.JRE4.divide(Lst2008.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
        self.ZVBEZJ = self.JVBEZ.divide(Lst2008.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
        self.JLFREIB = self.JFREIB.divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
        self.JLHINZU = self.JHINZU.divide(Lst2008.ZAHL100, 2, BigDecimal.ROUND_DOWN)
        self.MRE4()
        self.MRE4ABZ()
        self.MZTABFB()
        self.MLSTJAHR()
        self.LSTOSO = self.ST.multiply(Lst2008.ZAHL100)

    def MRE4SONST(self):
        """
        Sonderberechnung mit sonstige BezÃ¼ge fÃ¼r Berechnung bei sonstigen BezÃ¼gen oder VergÃ¼tung fÃ¼r mehrjÃ¤hrige TÃ¤tigkeit, PAP Seite 26
        """
        self.MRE4()
        self.FVB = self.FVBSO
        self.MRE4ABZ()
        self.FVBZ = self.FVBZSO
        self.MZTABFB()

    def UPTAB07(self):
        """
        Tarifliche Einkommensteuer Â§32a EStG, PAP Seite 27
        """
        if self.X.compareTo(BigDecimal.valueOf(7665)) == -1:
            self.ST = BigDecimal.ZERO
        else:
            if self.X.compareTo(BigDecimal.valueOf(12740)) == -1:
                self.Y = self.X.subtract(BigDecimal.valueOf(7664)).divide(BigDecimal.valueOf(10000), 6, BigDecimal.ROUND_DOWN)
                self.RW = self.Y.multiply(BigDecimal.valueOf(883.74))
                self.RW = self.RW.add(BigDecimal.valueOf(1500))
                self.ST = self.RW.multiply(self.Y).setScale(0, BigDecimal.ROUND_DOWN)
            else:
                if self.X.compareTo(BigDecimal.valueOf(52152)) == -1:
                    self.Y = self.X.subtract(BigDecimal.valueOf(12739)).divide(BigDecimal.valueOf(10000), 6, BigDecimal.ROUND_DOWN)
                    self.RW = self.Y.multiply(BigDecimal.valueOf(228.74))
                    self.RW = self.RW.add(BigDecimal.valueOf(2397))
                    self.RW = self.RW.multiply(self.Y)
                    self.ST = self.RW.add(BigDecimal.valueOf(989)).setScale(0, BigDecimal.ROUND_DOWN)
                else:
                    if self.X.compareTo(BigDecimal.valueOf(250001)) == -1:
                        self.ST = self.X.multiply(BigDecimal.valueOf(0.42)).subtract(BigDecimal.valueOf(7914)).setScale(0, BigDecimal.ROUND_DOWN)
                    else:
                        self.ST = self.X.multiply(BigDecimal.valueOf(0.45)).subtract(BigDecimal.valueOf(15414)).setScale(0, BigDecimal.ROUND_DOWN)
        self.ST = self.ST.multiply(BigDecimal.valueOf(self.KZTAB))
