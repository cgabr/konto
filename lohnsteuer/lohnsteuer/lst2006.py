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


class Lst2006:
    TAB1 = [0.0, 0.4, 0.384, 0.368, 0.352, 0.336, 0.32, 0.304, 0.288, 0.272, 0.256, 0.24, 0.224, 0.208, 0.192, 0.176, 0.16, 0.152, 0.144, 0.136, 0.128, 0.12, 0.112, 0.104, 0.096, 0.088, 0.08, 0.072, 0.064, 0.056, 0.048, 0.04, 0.032, 0.024, 0.016, 0.008, 0.0]
    """
    Tabelle fuer die Vomhundertsaetze des Versorgungsfreibetrags
    """

    TAB2 = [0, 3000, 2880, 2760, 2640, 2520, 2400, 2280, 2160, 2040, 1920, 1800, 1680, 1560, 1440, 1320, 1200, 1140, 1080, 1020, 960, 900, 840, 780, 720, 660, 600, 540, 480, 420, 360, 300, 240, 180, 120, 60, 0]
    """
    Tabelle fuer die Hoechstbetrage des Versorgungsfreibetrags
    """

    TAB3 = [0, 900, 864, 828, 792, 756, 720, 684, 648, 612, 576, 540, 504, 468, 432, 396, 360, 342, 324, 306, 288, 270, 252, 234, 216, 198, 180, 162, 144, 126, 108, 90, 72, 54, 36, 18, 0]
    """
    Tabelle fuer die Zuschlaege zum Versorgungsfreibetrag
    """

    TAB4 = [0.0, 0.4, 0.384, 0.368, 0.352, 0.336, 0.32, 0.304, 0.288, 0.272, 0.256, 0.24, 0.224, 0.208, 0.192, 0.176, 0.16, 0.152, 0.144, 0.136, 0.128, 0.12, 0.112, 0.104, 0.096, 0.088, 0.08, 0.072, 0.064, 0.056, 0.048, 0.04, 0.032, 0.024, 0.016, 0.008, 0.0]
    """
    Tabelle fuer die Vomhundertsaetze des Altersentlastungsbetrags
    """

    TAB5 = [0, 1900, 1824, 1748, 1672, 1596, 1520, 1444, 1368, 1292, 1216, 1140, 1064, 988, 912, 836, 760, 722, 684, 646, 608, 570, 532, 494, 456, 418, 380, 342, 304, 266, 228, 190, 152, 114, 76, 38, 0]
    """
    Tabelle fuer die Hoechstbetraege des Altersentlastungsbetrags
    """

    ZAHL0 = BigDecimal(0)
    """
    Zahlenkonstanten fuer im Plan oft genutzte BigDecimal Werte
    """

    ZAHL1 = BigDecimal(1)
    ZAHL2 = BigDecimal(2)
    ZAHL3 = BigDecimal(3)
    ZAHL4 = BigDecimal(4)
    ZAHL5 = BigDecimal(5)
    ZAHL6 = BigDecimal(6)
    ZAHL7 = BigDecimal(7)
    ZAHL8 = BigDecimal(8)
    ZAHL9 = BigDecimal(9)
    ZAHL10 = BigDecimal(10)
    ZAHL11 = BigDecimal(11)
    ZAHL12 = BigDecimal(12)
    ZAHL100 = BigDecimal(100)
    ZAHL360 = BigDecimal(360)

    def __init__(self, **kwargs):
        # input variables

        # Auf die Vollendung des 64. Lebensjahres folgende
        # Kalenderjahr (erforderlich, wenn ALTER1=1)
        self.AJAHR = 0
        if "AJAHR" in kwargs:
            self.setAjahr(kwargs["AJAHR"])

        # 1, wenn das 64. Lebensjahr zu Beginn des Kalenderjahres vollendet wurde, in dem
        # der Lohnzahlungszeitraum endet (§ 24 a EStG), sonst = 0
        self.ALTER1 = 0
        if "ALTER1" in kwargs:
            self.setAlter1(kwargs["ALTER1"])

        # In der Lohnsteuerkarte des Arbeitnehmers eingetragener Hinzurechnungsbetrag
        # fuer den Lohnzahlungszeitraum in Cents
        self.HINZUR = BigDecimal(0)
        if "HINZUR" in kwargs:
            self.setHinzur(kwargs["HINZUR"])

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
        # „sonstiger Bezuege“ (Feld SONSTB) oder bei Eingabe der „Verguetung
        # fuer mehrjaehrige Taetigkeit“ (Feld VMT).
        self.JRE4 = BigDecimal(0)
        if "JRE4" in kwargs:
            self.setJre4(kwargs["JRE4"])

        # In JRE4 enthaltene Versorgungsbezuege in Cents (ggf. 0)
        self.JVBEZ = BigDecimal(0)
        if "JVBEZ" in kwargs:
            self.setJvbez(kwargs["JVBEZ"])

        # 1 = der Arbeitnehmer ist im Lohnzahlungszeitraum in der gesetzlichen
        # Rentenversicherung versicherungsfrei und gehoert zu den in
        # § 10 c Abs. 3 EStG genannten Personen.
        # Bei anderen Arbeitnehmern ist „0“ einzusetzen.
        # Fuer die Zuordnung sind allein die dem Arbeitgeber ohnehin bekannten
        # Tatsachen ma&szlig;gebend; zusaetzliche Ermittlungen braucht
        # der Arbeitgeber nicht anzustellen.
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

        # In der Lohnsteuerkarte des Arbeitnehmers eingetragener Freibetrag
        # fuer den Lohnzahlungszeitraum in Cents
        self.WFUNDF = BigDecimal(0)
        if "WFUNDF" in kwargs:
            self.setWfundf(kwargs["WFUNDF"])

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

        # Altersentlastungsbetrag nach Alterseinkuenftegesetz in Cents
        self.ALTE = BigDecimal(0)

        # Arbeitnehmer-Pauschbetrag in EURO
        self.ANP = BigDecimal(0)

        # Auf den Lohnzahlungszeitraum entfallender Anteil von Jahreswerten
        # auf ganze Cents abgerundet
        self.ANTEIL1 = BigDecimal(0)

        # Auf den Lohnzahlungszeitraum entfallender Anteil von Jahreswerten
        # auf ganze Cents aufgerundet
        self.ANTEIL2 = BigDecimal(0)

        # Bemessungsgrundlage fuer Altersentlastungsbetrag in Cents
        self.BMG = BigDecimal(0)

        # Differenz zwischen ST1 und ST2 in EURO
        self.DIFF = BigDecimal(0)

        # Entlastungsbetrag fuer Alleinerziehende in EURO
        self.EFA = BigDecimal(0)

        # Versorgungsfreibetrag in Cents
        self.FVB = BigDecimal(0)

        # Zuschlag zum Versorgungsfreibetrag in EURO
        self.FVBZ = BigDecimal(0)

        # Massgeblich maximaler Versorgungsfreibetrag in Cents
        self.HFVB = BigDecimal(0)

        # Nummer der Tabellenwerte fuer Versorgungsparameter
        self.J = 0

        # Jahressteuer nach § 51a EStG, aus der Solidaritaetszuschlag und
        # Bemessungsgrundlage fuer die Kirchenlohnsteuer ermittelt werden in EURO
        self.JBMG = BigDecimal(0)

        # Jahreswert, dessen Anteil fuer einen Lohnzahlungszeitraum in
        # UPANTEIL errechnet werden soll in Cents
        self.JW = BigDecimal(0)

        # Nummer der Tabellenwerte fuer Parameter bei Altersentlastungsbetrag
        self.K = 0

        # Kennzeichen bei Verguetung fuer mehrjaehrige Taetigkeit
        # 0 = beim Vorwegabzug ist ZRE4VP zu beruecksichtigen
        # 1 = beim Vorwegabzug ist ZRE4VP1 zu beruecksichtigen
        self.KENNZ = 0

        # Summe der Freibetraege fuer Kinder in EURO
        self.KFB = BigDecimal(0)

        # Kennzahl fuer die Einkommensteuer-Tabellenart:
        # 1 = Grundtabelle
        # 2 = Splittingtabelle
        self.KZTAB = 0

        # Jahreslohnsteuer in EURO
        self.LSTJAHR = BigDecimal(0)

        # Zwischenfelder der Jahreslohnsteuer in Cents
        self.LST1 = BigDecimal(0)
        self.LST2 = BigDecimal(0)
        self.LST3 = BigDecimal(0)

        # Mindeststeuer fuer die Steuerklassen V und VI in EURO
        self.MIST = BigDecimal(0)

        # Arbeitslohn des Lohnzahlungszeitraums nach Abzug der Freibetraege
        # fuer Versorgungsbezuege, des Altersentlastungsbetrags und des
        # in der Lohnsteuerkarte eingetragenen Freibetrags und Hinzurechnung
        # eines Hinzurechnungsbetrags in Cents. Entspricht dem Arbeitslohn,
        # fuer den die Lohnsteuer im personellen Verfahren aus der
        # zum Lohnzahlungszeitraum gehoerenden Tabelle abgelesen wuerde
        self.RE4LZZ = BigDecimal(0)

        # Arbeitslohn des Lohnzahlungszeitraums nach Abzug der Freibetraege
        # fuer Versorgungsbezuege und des Altersentlastungsbetrags in
        # Cents zur Berechnung der Vorsorgepauschale
        self.RE4LZZV = BigDecimal(0)

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

        # Hoechstbetrag der Vorsorgepauschale nach § 10c Abs. 3 EStG in EURO
        self.VSPKURZ = BigDecimal(0)

        # Hoechstbetrag der Vorsorgepauschale nach § 10c Abs. 2 Nr. 2 EStG in EURO
        self.VSPMAX1 = BigDecimal(0)

        # Hoechstbetrag der Vorsorgepauschale nach § 10c Abs. 2 Nr. 3 EStG in EURO
        self.VSPMAX2 = BigDecimal(0)

        # Vorsorgepauschale nach § 10c Abs. 2 Satz 2 EStG vor der Hoechstbetragsberechnung
        # in EURO, C (2 Dezimalstellen)
        self.VSPO = BigDecimal(0)

        # Fuer den Abzug nach § 10c Abs. 2 Nrn. 2 und 3 EStG verbleibender
        # Rest von VSPO in EURO, C (2 Dezimalstellen)
        self.VSPREST = BigDecimal(0)

        # Hoechstbetrag der Vorsorgepauschale nach § 10c Abs. 2 Nr. 1 EStG
        # in EURO, C (2 Dezimalstellen)
        self.VSPVOR = BigDecimal(0)

        # Zu versteuerndes Einkommen gem. § 32a Abs. 1 und 2 EStG
        # (2 Dezimalstellen)
        self.X = BigDecimal(0)

        # gem. § 32a Abs. 1 EStG (6 Dezimalstellen)
        self.Y = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes RE4LZZ in EURO, C (2 Dezimalstellen)
        self.ZRE4 = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes RE4LZZV zur Berechnung
        # der Vorsorgepauschale in EURO, C (2 Dezimalstellen)
        self.ZRE4VP = BigDecimal(0)

        # Sicherungsfeld von ZRE4VP in EURO,C bei der Berechnung des Vorwegabzugs
        # fuer die Verguetung fuer mehrjaehrige Taetigkeit
        self.ZRE4VP1 = BigDecimal(0)

        # Feste Tabellenfreibetraege (ohne Vorsorgepauschale) in EURO
        self.ZTABFB = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes (VBEZ abzueglich FVB) in
        # EURO, C (2 Dezimalstellen)
        self.ZVBEZ = BigDecimal(0)

        # Zu versteuerndes Einkommen in EURO
        self.ZVE = BigDecimal(0)

        # Zwischenfelder zu X fuer die Berechnung der Steuer nach § 39b
        # Abs. 2 Satz 8 EStG in EURO.
        self.ZX = BigDecimal(0)
        self.ZZX = BigDecimal(0)
        self.HOCH = BigDecimal(0)
        self.VERGL = BigDecimal(0)


    def setAjahr(self, value):
        self.AJAHR = value

    def setAlter1(self, value):
        self.ALTER1 = value

    def setHinzur(self, value):
        self.HINZUR = BigDecimal(value)

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

    def setWfundf(self, value):
        self.WFUNDF = BigDecimal(value)

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
        PROGRAMMABLAUFPLAN 2006
        """
        self.MRE4LZZ()
        self.KENNZ = 0
        self.RE4ZZ = self.RE4.subtract(self.FVB).subtract(self.ALTE).subtract(self.WFUNDF).add(self.HINZUR)
        self.RE4ZZV = self.RE4.subtract(self.FVB).subtract(self.ALTE)
        self.MRE4()
        self.MZTABFB()
        self.MLSTJAHR()
        self.LSTJAHR = self.ST
        self.JW = self.LSTJAHR.multiply(Lst2006.ZAHL100)
        self.UPANTEIL()
        self.LSTLZZ = self.ANTEIL1
        if self.ZKF.compareTo(Lst2006.ZAHL0) == 1:
            self.ZTABFB = self.ZTABFB.add(self.KFB)
            self.MLSTJAHR()
            self.JBMG = self.ST
        else:
            self.JBMG = self.LSTJAHR
        self.MSOLZ()
        self.MSONST()
        self.MVMT()

    def MRE4LZZ(self):
        """
        Freibetraege fuer Versorgungsbezuege, Altersentlastungsbetrag (§39b Abs. 2 Satz 2 EStG)
        PAP Seite 10
        """
        if self.VBEZ.compareTo(Lst2006.ZAHL0) == 0:
            self.FVBZ = Lst2006.ZAHL0
            self.FVB = Lst2006.ZAHL0
        else:
            if self.VJAHR < 2006:
                self.J = 1
            else:
                if self.VJAHR < 2040:
                    self.J = self.VJAHR - 2004
                else:
                    self.J = 36
            if self.LZZ == 1:
                if self.STERBE.add(self.VKAPA).compareTo(Lst2006.ZAHL0) == 1:
                    self.VBEZB = self.VBEZM.multiply(BigDecimal.valueOf(self.ZMVB)).add(self.VBEZS)
                    self.HFVB = BigDecimal.valueOf(Lst2006.TAB2[self.J] * 100)
                    self.FVBZ = BigDecimal.valueOf(Lst2006.TAB3[self.J])
                else:
                    self.VBEZB = self.VBEZM.multiply(BigDecimal.valueOf(self.ZMVB)).add(self.VBEZS)
                    self.HFVB = BigDecimal.valueOf(Lst2006.TAB2[self.J] / 12 * self.ZMVB * 100)
                    self.FVBZ = BigDecimal.valueOf(Lst2006.TAB3[self.J] / 12 * self.ZMVB).setScale(0, BigDecimal.ROUND_UP)
            else:
                self.VBEZB = self.VBEZM.multiply(Lst2006.ZAHL12).add(self.VBEZS).setScale(2, BigDecimal.ROUND_DOWN)
                self.HFVB = BigDecimal.valueOf(Lst2006.TAB2[self.J] * 100)
                self.FVBZ = BigDecimal.valueOf(Lst2006.TAB3[self.J])
            self.FVB = self.VBEZB.multiply(BigDecimal.valueOf(Lst2006.TAB1[self.J])).setScale(0, BigDecimal.ROUND_UP)
            if self.FVB.compareTo(self.HFVB) == 1:
                self.FVB = self.HFVB
            self.JW = self.FVB
            self.UPANTEIL()
            self.FVB = self.ANTEIL2
        if self.ALTER1 == 0:
            self.ALTE = Lst2006.ZAHL0
        else:
            if self.AJAHR < 2006:
                self.K = 1
            else:
                if self.AJAHR < 2040:
                    self.K = self.AJAHR - 2004
                else:
                    self.K = 36
            self.BMG = self.RE4.subtract(self.VBEZ)
            self.ALTE = self.BMG.multiply(BigDecimal.valueOf(Lst2006.TAB4[self.K])).setScale(0, BigDecimal.ROUND_UP)
            self.JW = BigDecimal.valueOf(Lst2006.TAB5[self.K] * 100)
            self.UPANTEIL()
            if self.ALTE.compareTo(self.ANTEIL2) == 1:
                self.ALTE = self.ANTEIL2

    def MRE4(self):
        """
        Massgeblicher Arbeitslohn fuer die Jahreslohnsteuer
        PAP Seite 12
        """
        if self.LZZ == 1:
            self.ZRE4 = self.RE4ZZ.divide(Lst2006.ZAHL100, 2, BigDecimal.ROUND_DOWN)
            self.ZRE4VP = self.RE4ZZV.divide(Lst2006.ZAHL100, 2, BigDecimal.ROUND_DOWN)
            self.ZVBEZ = self.VBEZ.subtract(self.FVB).divide(Lst2006.ZAHL100, 2, BigDecimal.ROUND_DOWN)
        else:
            if self.LZZ == 2:
                self.ZRE4 = self.RE4ZZ.add(BigDecimal.valueOf(0.67)).multiply(BigDecimal.valueOf(0.12)).setScale(2, BigDecimal.ROUND_DOWN)
                self.ZRE4VP = self.RE4ZZV.add(BigDecimal.valueOf(0.67)).multiply(BigDecimal.valueOf(0.12)).setScale(2, BigDecimal.ROUND_DOWN)
                self.ZVBEZ = self.VBEZ.subtract(self.FVB).add(BigDecimal.valueOf(0.67)).multiply(BigDecimal.valueOf(0.12)).setScale(2, BigDecimal.ROUND_DOWN)
            else:
                if self.LZZ == 3:
                    self.ZRE4 = self.RE4ZZ.add(BigDecimal.valueOf(0.89)).multiply(BigDecimal.valueOf(3.6 / 7.0)).setScale(2, BigDecimal.ROUND_DOWN)
                    self.ZRE4VP = self.RE4ZZV.add(BigDecimal.valueOf(0.89)).multiply(BigDecimal.valueOf(3.6 / 7.0)).setScale(2, BigDecimal.ROUND_DOWN)
                    self.ZVBEZ = self.VBEZ.subtract(self.FVB).add(BigDecimal.valueOf(0.89)).multiply(BigDecimal.valueOf(3.6 / 7.0)).setScale(2, BigDecimal.ROUND_DOWN)
                else:
                    self.ZRE4 = self.RE4ZZ.add(BigDecimal.valueOf(0.56)).multiply(BigDecimal.valueOf(3.6)).setScale(2, BigDecimal.ROUND_DOWN)
                    self.ZRE4VP = self.RE4ZZV.add(BigDecimal.valueOf(0.56)).multiply(BigDecimal.valueOf(3.6)).setScale(2, BigDecimal.ROUND_DOWN)
                    self.ZVBEZ = self.VBEZ.subtract(self.FVB).add(BigDecimal.valueOf(0.56)).multiply(BigDecimal.valueOf(3.6)).setScale(2, BigDecimal.ROUND_DOWN)
        if self.ZRE4.compareTo(Lst2006.ZAHL0) == -1:
            self.ZRE4 = Lst2006.ZAHL0
        if self.ZVBEZ.compareTo(Lst2006.ZAHL0) == -1:
            self.ZVBEZ = Lst2006.ZAHL0

    def MZTABFB(self):
        """
        Ermittlung der festen Tabellenfreibetraege (ohne Vorsorgepauschale)
        PAP Seite 13
        """
        self.ANP = Lst2006.ZAHL0
        if self.ZVBEZ.compareTo(Lst2006.ZAHL0) == 1:
            if self.ZVBEZ.compareTo(self.FVBZ) == -1:
                self.FVBZ = self.ZVBEZ.setScale(0, BigDecimal.ROUND_DOWN)
        if self.STKL < 6:
            if self.ZVBEZ.compareTo(Lst2006.ZAHL0) == 1:
                if self.ZVBEZ.subtract(self.FVBZ).compareTo(BigDecimal.valueOf(102)) == -1:
                    self.ANP = self.ZVBEZ.subtract(self.FVBZ).setScale(0, BigDecimal.ROUND_DOWN)
                else:
                    self.ANP = BigDecimal.valueOf(102)
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
                        self.KFB = Lst2006.ZAHL0
        self.ZTABFB = self.EFA.add(self.ANP).add(self.SAP).add(self.FVBZ)

    def MLSTJAHR(self):
        """
        Ermittlung Jahreslohnsteuer
        PAP Seite 14
        """
        if self.STKL < 5:
            self.UPEVP()
        else:
            self.VSP = Lst2006.ZAHL0
        self.ZVE = self.ZRE4.subtract(self.ZTABFB).subtract(self.VSP).setScale(0, BigDecimal.ROUND_DOWN)
        if self.ZVE.compareTo(Lst2006.ZAHL1) == -1:
            self.ZVE = Lst2006.ZAHL0
            self.X = Lst2006.ZAHL0
        else:
            self.X = self.ZVE.divide(BigDecimal.valueOf(self.KZTAB), 0, BigDecimal.ROUND_DOWN)
        if self.STKL < 5:
            self.UPTAB05()
        else:
            self.MST5_6()

    def UPEVP(self):
        """
        Vorsorgepauschale (§39b Abs. 2 Satz 6 Nr 3 EStG)
        PAP Seite 15
        """
        if self.KRV == 1:
            self.VSP1 = Lst2006.ZAHL0
        else:
            if self.ZRE4VP.compareTo(BigDecimal.valueOf(63000)) == 1:
                self.ZRE4VP = BigDecimal.valueOf(63000)
            self.VSP1 = self.ZRE4VP.multiply(BigDecimal.valueOf(0.24)).setScale(2, BigDecimal.ROUND_DOWN)
            self.VSP1 = self.VSP1.multiply(BigDecimal.valueOf(0.0975)).setScale(2, BigDecimal.ROUND_DOWN)
        self.VSP2 = self.ZRE4VP.multiply(BigDecimal.valueOf(0.11))
        self.VHB = BigDecimal.valueOf(1500 * self.KZTAB)
        if self.VSP2.compareTo(self.VHB) == 1:
            self.VSP2 = self.VHB
        self.VSPN = self.VSP1.add(self.VSP2).setScale(0, BigDecimal.ROUND_UP)
        self.MVSP()
        if self.VSPN.compareTo(self.VSP) == 1:
            self.VSP = self.VSPN.setScale(2, BigDecimal.ROUND_DOWN)

    def MVSP(self):
        """
        Vorsorgepauschale (§39b Abs. 2 Satz 6 Nr 3 EStG) Vergleichsberechnung
        fuer Guenstigerpruefung
        PAP Seite 16
        """
        if self.KENNZ == 1:
            self.VSPO = self.ZRE4VP1.multiply(BigDecimal.valueOf(0.2))
        else:
            self.VSPO = self.ZRE4VP.multiply(BigDecimal.valueOf(0.2))
        self.VSPVOR = BigDecimal.valueOf(self.KZTAB * 3068)
        self.VSPMAX1 = BigDecimal.valueOf(self.KZTAB * 1334)
        self.VSPMAX2 = BigDecimal.valueOf(self.KZTAB * 667)
        self.VSPKURZ = BigDecimal.valueOf(self.KZTAB * 1134)
        if self.KRV == 1:
            if self.VSPO.compareTo(self.VSPKURZ) == 1:
                self.VSP = self.VSPKURZ
            else:
                self.VSP = self.VSPO.setScale(2, BigDecimal.ROUND_UP)
        else:
            self.UMVSP()

    def UMVSP(self):
        """
        Vorsorgepauschale
        PAP Seite 17
        """
        if self.KENNZ == 1:
            self.VSPVOR = self.VSPVOR.subtract(self.ZRE4VP1.multiply(BigDecimal.valueOf(0.16)))
        else:
            self.VSPVOR = self.VSPVOR.subtract(self.ZRE4VP.multiply(BigDecimal.valueOf(0.16)))
        if self.VSPVOR.compareTo(Lst2006.ZAHL0) == -1:
            self.VSPVOR = Lst2006.ZAHL0
        if self.VSPO.compareTo(self.VSPVOR) == 1:
            self.VSP = self.VSPVOR
            self.VSPREST = self.VSPO.subtract(self.VSPVOR)
            if self.VSPREST.compareTo(self.VSPMAX1) == 1:
                self.VSP = self.VSP.add(self.VSPMAX1)
                self.VSPREST = self.VSPREST.subtract(self.VSPMAX1).divide(Lst2006.ZAHL2, 2, BigDecimal.ROUND_UP)
                if self.VSPREST.compareTo(self.VSPMAX2) == 1:
                    self.VSP = self.VSP.add(self.VSPMAX2).setScale(0, BigDecimal.ROUND_UP)
                else:
                    self.VSP = self.VSP.add(self.VSPREST).setScale(0, BigDecimal.ROUND_UP)
            else:
                self.VSP = self.VSP.add(self.VSPREST).setScale(0, BigDecimal.ROUND_UP)
        else:
            self.VSP = self.VSPO.setScale(0, BigDecimal.ROUND_UP)

    def MST5_6(self):
        """
        Lohnsteuer fuer die Steuerklassen V und VI (§ 39b Abs. 2 Satz 8 EStG)
        PAP Seite 18
        """
        self.ZZX = self.X
        if self.ZZX.compareTo(BigDecimal.valueOf(25812)) == 1:
            self.ZX = BigDecimal.valueOf(25812)
            self.UP5_6()
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
        Lohnsteuer fuer die Steuerklassen V und VI (§ 39b Abs. 2 Satz 8 EStG)
        PAP Seite 18
        """
        self.X = self.ZX.multiply(BigDecimal.valueOf(1.25))
        self.UPTAB05()
        self.ST1 = self.ST
        self.X = self.ZX.multiply(BigDecimal.valueOf(0.75))
        self.UPTAB05()
        self.ST2 = self.ST
        self.DIFF = self.ST1.subtract(self.ST2).multiply(Lst2006.ZAHL2)
        self.MIST = self.ZX.multiply(BigDecimal.valueOf(0.15)).setScale(0, BigDecimal.ROUND_DOWN)
        if self.MIST.compareTo(self.DIFF) == 1:
            self.ST = self.MIST
        else:
            self.ST = self.DIFF

    def MSOLZ(self):
        """
        Solidaritaetszuschlag
        PAP Seite 19
        """
        self.SOLZFREI = BigDecimal.valueOf(972 * self.KZTAB)
        if self.JBMG.compareTo(self.SOLZFREI) == 1:
            self.SOLZJ = self.JBMG.multiply(BigDecimal.valueOf(5.5 / 100)).setScale(2, BigDecimal.ROUND_DOWN)
            self.SOLZMIN = self.JBMG.subtract(self.SOLZFREI).multiply(BigDecimal.valueOf(20.0 / 100.0))
            if self.SOLZMIN.compareTo(self.SOLZJ) == -1:
                self.SOLZJ = self.SOLZMIN
            self.JW = self.SOLZJ.multiply(Lst2006.ZAHL100).setScale(0, BigDecimal.ROUND_DOWN)
            self.UPANTEIL()
            self.SOLZLZZ = self.ANTEIL1
        else:
            self.SOLZLZZ = Lst2006.ZAHL0
        if self.R > 0:
            self.JW = self.JBMG.multiply(Lst2006.ZAHL100)
            self.UPANTEIL()
            self.BK = self.ANTEIL1
        else:
            self.BK = Lst2006.ZAHL0

    def UPANTEIL(self):
        """
        Anteil von Jahresbetraegen fuer einen LZZ (§ 39b Abs. 2 Satz 10 EStG)
        PAP Seite 20
        """
        if self.LZZ == 1:
            self.ANTEIL1 = self.JW
            self.ANTEIL2 = self.JW
        else:
            if self.LZZ == 2:
                self.ANTEIL1 = self.JW.divide(Lst2006.ZAHL12, 0, BigDecimal.ROUND_DOWN)
                self.ANTEIL2 = self.JW.divide(Lst2006.ZAHL12, 0, BigDecimal.ROUND_UP)
            else:
                if self.LZZ == 3:
                    self.ANTEIL1 = self.JW.multiply(Lst2006.ZAHL7).divide(Lst2006.ZAHL360, 0, BigDecimal.ROUND_DOWN)
                    self.ANTEIL2 = self.JW.multiply(Lst2006.ZAHL7).divide(Lst2006.ZAHL360, 0, BigDecimal.ROUND_UP)
                else:
                    self.ANTEIL1 = self.JW.divide(Lst2006.ZAHL360, 0, BigDecimal.ROUND_DOWN)
                    self.ANTEIL2 = self.JW.divide(Lst2006.ZAHL360, 0, BigDecimal.ROUND_UP)

    def MSONST(self):
        """
        Berechnung sonstiger Bezuege nach § 39b Abs. 3 Saetze 1 bis 7 EStG)
        PAP Seite 21
        """
        if self.SONSTB.compareTo(Lst2006.ZAHL0) == 1:
            self.LZZ = 1
            self.VBEZ = self.JVBEZ
            self.RE4 = self.JRE4
            self.MRE4LZZ()
            self.MRE4LZZ2()
            self.MLSTJAHR()
            self.LST1 = self.ST.multiply(Lst2006.ZAHL100)
            self.VBEZ = self.JVBEZ.add(self.VBS)
            self.RE4 = self.JRE4.add(self.SONSTB)
            self.VBEZS = self.VBEZS.add(self.STERBE)
            self.MRE4LZZ()
            self.MRE4LZZ2()
            self.MLSTJAHR()
            self.LST2 = self.ST.multiply(Lst2006.ZAHL100)
            self.STS = self.LST2.subtract(self.LST1)
            self.SOLZS = self.STS.multiply(BigDecimal.valueOf(5.5)).divide(Lst2006.ZAHL100, 0, BigDecimal.ROUND_DOWN)
            if self.R > 0:
                self.BKS = self.STS
            else:
                self.BKS = Lst2006.ZAHL0
        else:
            self.STS = Lst2006.ZAHL0
            self.SOLZS = Lst2006.ZAHL0
            self.BKS = Lst2006.ZAHL0

    def MRE4LZZ2(self):
        """
        Berechnung sonstiger Bezuege nach § 39b Abs. 3 Saetze 1 bis 7 EStG)
        PAP Seite 21
        """
        self.RE4ZZ = self.RE4.subtract(self.FVB).subtract(self.ALTE).subtract(self.JFREIB).add(self.JHINZU)
        self.RE4ZZV = self.RE4.subtract(self.FVB).subtract(self.ALTE)
        self.MRE4()
        self.MZTABFB()

    def MVMT(self):
        """
        Berechnung der Verguetung fuer mehrjaehrige Taetigkeit nach § 39b Abs. 3 Satz 9 EStG)
        PAP Seite 22
        """
        if self.VMT.add(self.VKAPA).compareTo(Lst2006.ZAHL0) == 1:
            self.LZZ = 1
            self.VBEZ = self.JVBEZ.add(self.VBS)
            self.RE4 = self.JRE4.add(self.SONSTB)
            self.MRE4LZZ()
            self.MRE4LZZ2()
            self.MLSTJAHR()
            self.LST1 = self.ST.multiply(Lst2006.ZAHL100)
            self.VMT = self.VMT.add(self.VKAPA)
            self.VBEZS = self.VBEZS.add(self.VKAPA)
            self.VBEZ = self.VBEZ.add(self.VKAPA)
            self.RE4 = self.JRE4.add(self.SONSTB).add(self.VMT)
            self.MRE4LZZ()
            self.MRE4LZZ2()
            self.KENNZ = 1
            self.ZRE4VP1 = self.ZRE4VP
            self.MLSTJAHR()
            self.LST3 = self.ST.multiply(Lst2006.ZAHL100)
            self.VBEZ = self.VBEZ.subtract(self.VKAPA)
            self.RE4 = self.JRE4.add(self.SONSTB)
            self.MRE4LZZ()
            if self.RE4.subtract(self.JFREIB).add(self.JHINZU).compareTo(Lst2006.ZAHL0) == -1:
                self.RE4 = self.RE4.subtract(self.JFREIB).add(self.JHINZU)
                self.JFREIB = Lst2006.ZAHL0
                self.JHINZU = Lst2006.ZAHL0
                self.RE4 = self.RE4.add(self.VMT).divide(Lst2006.ZAHL5, 0, BigDecimal.ROUND_DOWN)
                self.MRE4LZZ2()
                self.MLSTJAHR()
                self.LST2 = self.ST.multiply(Lst2006.ZAHL100)
                self.STV = self.LST2.multiply(Lst2006.ZAHL5)
            else:
                self.RE4 = self.RE4.add(self.VMT.divide(Lst2006.ZAHL5, 0, BigDecimal.ROUND_DOWN))
                self.MRE4LZZ2()
                self.MLSTJAHR()
                self.LST2 = self.ST.multiply(Lst2006.ZAHL100)
                self.STV = self.LST2.subtract(self.LST1).multiply(Lst2006.ZAHL5)
            self.LST3 = self.LST3.subtract(self.LST1)
            if self.LST3.compareTo(self.STV) == -1:
                self.STV = self.LST3
            self.SOLZV = self.STV.multiply(BigDecimal.valueOf(5.5)).divide(Lst2006.ZAHL100, 0, BigDecimal.ROUND_DOWN)
            if self.R > 0:
                self.BKV = self.STV
            else:
                self.BKV = Lst2006.ZAHL0
        else:
            self.STV = Lst2006.ZAHL0
            self.SOLZV = Lst2006.ZAHL0
            self.BKV = Lst2006.ZAHL0

    def UPTAB05(self):
        """
        Berechnung der Verguetung fuer mehrjaehrige Taetigkeit nach § 39b Abs. 3 Satz 9 EStG)
        PAP Seite 23
        """
        if self.X.compareTo(BigDecimal.valueOf(7665)) == -1:
            self.ST = Lst2006.ZAHL0
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
                    self.ST = self.X.multiply(BigDecimal.valueOf(0.42)).subtract(BigDecimal.valueOf(7914)).setScale(0, BigDecimal.ROUND_DOWN)
        self.ST = self.ST.multiply(BigDecimal.valueOf(self.KZTAB))
