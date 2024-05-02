import pandas as pd
import sqlite3
def CreazioneDB():
    # connessione al database
    conn = sqlite3.connect('Database.db')
    # lettura del file CSV
    TabellaClienti=pd.read_csv('Clienti.csv',index_col=False, delimiter = ',')
    Cli=TabellaClienti[["Nr.","Fatt. cumulative","Valuta"]]
    Cli=Cli.rename(columns={'Nr.': 'CodCli','Fatt. cumulative':'FattureCum'})
    TabellaTdC=pd.read_csv('Tassi di cambio.csv',index_col=False, delimiter = ',')
    TabellaTdC=TabellaTdC.rename(columns={'Codice valuta': 'CodVal','Anno':'Tipo','Tasso di cambio medio':'Tasso'})
    TabellaVendite=pd.read_csv('Vendite1.csv',index_col=False, delimiter = ';')
    Ven=TabellaVendite[["Nr. movimento","budget/cons","Nr articolo","Nr. origine","Quantità","Importo vendita in valuta locale (TOTALE VENDITA)"]]
    Ven=Ven.rename(columns={'Nr. movimento': 'NrMov','budget/cons':'Tipologia','Nr articolo':'NrArtV','Nr. origine': 'NrOrig','Quantità':'Qta','Importo vendita in valuta locale (TOTALE VENDITA)':'ImportV'})
    TabellaConsumi=pd.read_csv('Consumi.csv',index_col=False, delimiter = ';')
    Cons=TabellaConsumi[["Nr. movimento","Budget/cons","Codice MP","Nr articolo","Nr. documento","Quantità MP impiegata","Importo costo (TOTALE)"]]
    Cons=Cons.rename(columns={'Nr. movimento': 'NrMovim','Budget/cons':'Tipol','Codice MP':'CodiceMP','Nr articolo': 'NrArtC','Nr. documento':'NrDoc','Quantità MP impiegata':'QuantitàMP','Importo costo (TOTALE)':'ImportoTot'})
    TabellaCostRis=pd.read_csv('CostoRisorse.csv',index_col=False, delimiter = ';')
    TabellaCostRis=TabellaCostRis.rename(columns={'IDRis': 'IDRis','Risorsa':'RisorsaR','Area di produzione': 'AreaProdR','Costo orario Budget(€/h)':'CostoBudgetR','Costo orario Cons (€/h)':'CostoConsR'})
    Imp=pd.read_csv('Impiego.csv',index_col=False, delimiter = ';')
    Imp=Imp.rename(columns={'IDImp': 'IDImp','nr articolo':'NrArt','budget/consuntivo':'Tipologia','Nr. Ordine di produzione': 'NrOrdine','Descrizione':'Descrizione','Nr. Area di produzione':'NrArea','Risorsa':'RisorsaC','Tempo risorsa':'Tempo','Quantità di output':'Quantitá'})
    # scrittura dei dati del DataFrame in una tabella SQLite facendo cosi tolgo il ciclo for ed ottimizzo il caricamento e la creazione del database ad un tempo quasi istante
    Cli.to_sql('Cliente', conn, if_exists='replace')
    TabellaTdC.to_sql('Valuta', conn, if_exists='replace')
    Ven.to_sql('Vendita', conn, if_exists='replace')
    Cons.to_sql('Consumo', conn, if_exists='replace')
    TabellaCostRis.to_sql('Risorsa', conn, if_exists='replace')
    Imp.to_sql('ImpiegoRis', conn, if_exists='replace')
    # chiusura della connessione
    conn.close()


#Funzione per creare le viste nel database e poterci lavorare  
def CreaViste():
    #Connessione al database
    conn = sqlite3.connect("Database.db")
    #Creazione tabella Clienti ed inserimento dati
    cursor = conn.cursor()
    #Creazione
    cursor.execute('DROP VIEW IF EXISTS venditeBudget;')
    cursor.execute('DROP VIEW IF EXISTS venditeBudgetinVALUTALOCALE;')
    cursor.execute('DROP VIEW IF EXISTS ImportiVenditePerArticoloBudget;')
    cursor.execute('DROP VIEW IF EXISTS TotaleVenditeBudget;')
    cursor.execute('DROP VIEW IF EXISTS VolumiArticoliBudget;')
    cursor.execute('DROP VIEW IF EXISTS mixVolumibudget;')
    cursor.execute('DROP VIEW IF EXISTS venditeConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS venditeConsuntivoinVALUTALOCALE;')
    cursor.execute('DROP VIEW IF EXISTS ImportiVenditePerArticoloConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS TotaleVenditeConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS VolumiArticoliConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS mixVolumiConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS VolTotaleVenditeConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS VolTotaleVenditeBudget;')
    cursor.execute('DROP VIEW IF EXISTS mixstandard;')
    cursor.execute('DROP VIEW IF EXISTS volTotaleMixStandard;')
    cursor.execute('DROP VIEW IF EXISTS mixeffettivo;')
    cursor.execute('DROP VIEW IF EXISTS volTotaleMixconsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS Prezzomedioperarticolobudget;')
    cursor.execute('DROP VIEW IF EXISTS Prezzomedioperarticoloconsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS totaleconsumibudget;')
    cursor.execute('DROP VIEW IF EXISTS CostiVariabiliEQTAbudget;')
    cursor.execute('DROP VIEW IF EXISTS CostiVariabiliperArticoloImpiegoBudget;')
    cursor.execute('DROP VIEW IF EXISTS CostiVariabiliperArticoloBudget;')
    cursor.execute('DROP VIEW IF EXISTS quantitaperArticoloBudget;')
    cursor.execute('DROP VIEW IF EXISTS totaleCostiVariabilibudget;')
    cursor.execute('DROP VIEW IF EXISTS totalecostiBudget;')
    cursor.execute('DROP VIEW IF EXISTS totaleconsumiconsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS CostiVariabiliEQTAConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS CostiVariabiliperArticoloConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS quantitaperArticoloConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS totaleCostiVariabiliconsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS totalecostiConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS quantitàOutputBudget;')
    cursor.execute('DROP VIEW IF EXISTS costounitarioBudget;')
    cursor.execute('DROP VIEW IF EXISTS costoPerArticoloBudget;')
    cursor.execute('DROP VIEW IF EXISTS quantitàOutputConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS costounitarioConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS costoPerArticoloConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS mixstandardVendite;')
    cursor.execute('DROP VIEW IF EXISTS mixeffettivovendite;')
    cursor.execute('DROP VIEW IF EXISTS ricavimixstandard;')
    cursor.execute('DROP VIEW IF EXISTS ricavimixeffettivo;')
    cursor.execute('DROP VIEW IF EXISTS costimixstandardperarticolo;')
    cursor.execute('DROP VIEW IF EXISTS costitotalimixstandard;')
    cursor.execute('DROP VIEW IF EXISTS molmixstandard;')
    cursor.execute('DROP VIEW IF EXISTS costimixeffettivoperarticolo;')
    cursor.execute('DROP VIEW IF EXISTS costitotalimixeffettivo;')
    cursor.execute('DROP VIEW IF EXISTS molbudget;')
    cursor.execute('DROP VIEW IF EXISTS molconsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS molmixstandard;')
    cursor.execute('DROP VIEW IF EXISTS molmixeffettivo;')
    #PARTE NUOVA/QUERY NUOVE PER MODIFICA
    cursor.execute('DROP VIEW IF EXISTS CostoImpiegoRisorseBUDGET;')
    cursor.execute('DROP VIEW IF EXISTS CostiConsumiBudget;')
    cursor.execute('DROP VIEW IF EXISTS CostiProdBudget;')
    cursor.execute('DROP VIEW IF EXISTS CostiTotaliBudget;')
    cursor.execute('DROP VIEW IF EXISTS CostiTotaliperArticoloBudget;')
    cursor.execute('DROP VIEW IF EXISTS TotaleCostiBudgetDEFINITIVO')
    cursor.execute('DROP VIEW IF EXISTS TotaleCostiConsuntivoDEFINITIVO;')
    
    cursor.execute('DROP VIEW IF EXISTS CostoImpiegoRisorseCONSUNTIVO;')
    cursor.execute('DROP VIEW IF EXISTS CostiConsumiConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS CostiProdConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS CostiTotaliConsuntivo;')
    cursor.execute('DROP VIEW IF EXISTS CostiTotaliperArticoloConsuntivo;')

    cursor.execute('DROP VIEW IF EXISTS costimixstandardQueryBudget;')
    cursor.execute('DROP VIEW IF EXISTS TotaleCostiMixStandard;')
    cursor.execute('DROP VIEW IF EXISTS costimixeffettivoQueryBudget;')
    cursor.execute('DROP VIEW IF EXISTS TotaleCostiMixEffettivo;')

    cursor.execute('DROP VIEW IF EXISTS venditeBudgetinVALUTALOCALECONSUNTIVO;')
    cursor.execute('DROP VIEW IF EXISTS ImportiVenditePerArticoloBudgetVALUTACONSUNTIVO;')

    cursor.execute('DROP VIEW IF EXISTS TotaleVenditeBudgetVALUTACONSUNTIVO;')

    cursor.execute('DROP VIEW IF EXISTS TassiBudget;')
    cursor.execute('DROP VIEW IF EXISTS TassiConsuntivo;')

    cursor.execute('DROP VIEW IF EXISTS ScostamentoTassiDiCambio ;')

    cursor.execute('DROP VIEW IF EXISTS ScostamentoCostoOrarioAreaProd ;')

    cursor.execute('DROP VIEW IF EXISTS costomedioMPperCodiceMPBudget ;')
    cursor.execute('DROP VIEW IF EXISTS costomedioMPperCodiceMPConsuntivo ;')
    cursor.execute('DROP VIEW IF EXISTS ScostamentoMateriePrime ;')

    cursor.execute("CREATE VIEW venditeBudget as select * from vendita where Tipologia='BUDGET' or Tipologia='Budget' and ImportV>0;")
    cursor.execute("CREATE VIEW venditeBudgetinVALUTALOCALE as select vb.NrMov,vb.Tipologia,vb.NrArtV,vb.NrOrig,vb.Qta,vb.ImportV/v.Tasso as RealImportV,v.CodVal from venditebudget vb join cliente c on vb.NrOrig=c.CodCLi join valuta v on c.Valuta=v.CodVal where v.Tipo='Budget' or v.Tipo='BUDGET';" )
    cursor.execute("Create view ImportiVenditePerArticoloBudget AS select vbvl.NrArtV,sum(RealImportV) as ImportoTotArticolo,sum(vbvl.Qta) as Qta from venditebudgetinvalutalocale vbvl group by vbvl.NrArtV; ")
    cursor.execute("Create view TotaleVenditeBudget as select sum(ImportoTotArticolo) as TotaleVenditeBudget from ImportiVenditePerArticoloBudget;")
    cursor.execute("create view VolumiArticoliBudget as select NrArtV,sum(Qta) as Qta from vendita where Tipologia='Budget' or tipologia='BUDGET' group by NrArtV order by NrArtV desc; ") #7224
    cursor.execute("Create View mixVolumibudget as select NrArtV ,(Qta*0.013842746) as mix from volumiarticolibudget group by NrArtV; ")    #0.013842746=100/volumibudget(7224)
    cursor.execute("CREATE VIEW venditeConsuntivo as select * from vendita where Tipologia='CONSUNTIVO' or Tipologia='Consuntivo'  and ImportV>0; ")
    cursor.execute("CREATE VIEW venditeConsuntivoinVALUTALOCALE as select vc.NrMov,vc.Tipologia,vc.NrArtV,vc.NrOrig,vc.Qta,vc.ImportV/v.Tasso as RealImportV,v.CodVal from venditeConsuntivo vc join cliente c on vc.NrOrig=c.CodCLi join valuta v on c.Valuta=v.CodVal where v.Tipo='CONSUNTIVO';" )
    cursor.execute("Create view ImportiVenditePerArticoloConsuntivo AS select vcvl.NrArtV,sum(RealImportV) as ImportoTotArticolo,sum(vcvl.Qta) as Qta from venditeConsuntivoinvalutalocale vcvl group by vcvl.NrArtV;")
    cursor.execute("Create view TotaleVenditeConsuntivo as select sum(ImportoTotArticolo) as TotaleVenditeConsuntivo from ImportiVenditePerArticoloConsuntivo;")
    cursor.execute("create view VolumiArticoliConsuntivo as select NrArtV,sum(Qta) as Qta from vendita where Tipologia='Consuntivo' or Tipologia='CONSUNTIVO' group by NrArtV order by NrArtV desc; ") #9329
    cursor.execute("Create View mixVolumiConsuntivo as select NrArtV ,(Qta*0.010719262) as mix from volumiarticoliConsuntivo group by NrArtV; ") #0.010719262=100/volumiconsuntivo(9329)
    cursor.execute("Create view VolTotaleVenditeConsuntivo as select sum(Qta) as VolumeTotaleVenditeConsuntivo from volumiarticoliConsuntivo;")
    cursor.execute("Create view VolTotaleVenditeBudget as select sum(Qta) as VolumeTotaleVenditeBudget from volumiarticoliBudget;")
    cursor.execute("create view mixstandard as select NrArtV,(mix*vtvc.VolumeTotaleVenditeconsuntivo)/100 as qta from mixvolumibudget mvb,VolTotaleVenditeconsuntivo vtvc;")
    cursor.execute("create view volTotaleMixStandard as select sum(qta) as qta from mixstandard;")
    cursor.execute("create view mixeffettivo as select NrArtV,(mvc.mix*vtvc.VolumeTotaleVenditeconsuntivo)/100 as qta from mixvolumiconsuntivo mvc,VolTotaleVenditeconsuntivo vtvc;")
    cursor.execute("create view volTotaleMixconsuntivo as select sum(qta) as qta from mixeffettivo; ")
    cursor.execute("create view Prezzomedioperarticolobudget as select NrArtV,ImportoTotArticolo/Qta as prezzomedio from importivenditeperarticolobudget;")
    cursor.execute("create view Prezzomedioperarticoloconsuntivo as select NrArtV,ImportoTotArticolo/Qta as prezzomedio from importivenditeperarticoloconsuntivo;")
    cursor.execute("create view totaleconsumibudget as SELECT sum(ImportoTot) AS 'TotaleCostoMP' FROM Consumo WHERE Tipol = 'BUDGET' or Tipol='Budget';")
    cursor.execute("create view CostiVariabiliEQTAbudget as select i.NrArt,i.NrOrdine,max(i.Quantitá)as quantitàOutput,sum(i.Tempo*r.CostoBudgetR)as CostiVariabili from impiegoris i join risorsa r on (i.RisorsaC=r.RisorsaR and i.NrArea=r.AreaProdR ) where i.Tipologia ='Budget' or i.Tipologia='BUDGET' group by i.NrArt,i.NrOrdine;")
    cursor.execute("create view CostiVariabiliperArticoloImpiegoBudget as select NrArt,sum(CostiVariabili) as CostiVariabiliperArticolo from CostiVariabiliEQTAbudget group by NrArt;")
    cursor.execute("create view CostiVariabiliperArticoloBudget as select NrArtV,sum(CostiVariabiliperArticolo) from costivariabiliperarticoloImpiegobudget join venditebudgetinvalutalocale on NrArt=NrArtV group by NrArtV;")
    cursor.execute("create view quantitaperArticoloBudget as select NrArt,sum(quantitàOutput) as QtaOutputperArticolo from CostiVariabiliEQTAbudget group by NrArt;")
    cursor.execute("create view totaleCostiVariabilibudget as select sum(CostiVariabili) as 'Totale_costi_variabili' from costivariabilieqtabudget;")
    cursor.execute("create view totalecostiBudget as select TotaleCostoMP+sum(t.'Totale_costi_variabili') as 'TOTALE_COSTI_A_BUDGET' from totaleconsumibudget,totalecostivariabilibudget t;")
    cursor.execute("create view totaleconsumiconsuntivo as SELECT SUM(ImportoTot) AS 'TotaleCostoMP' FROM Consumo WHERE Tipol = 'CONSUNTIVO' or Tipol='Consuntivo';")
    cursor.execute("create view CostiVariabiliEQTAConsuntivo as select i.NrArt,i.NrOrdine,max(i.Quantitá)as quantitàOutput,sum(i.Tempo*r.CostoConsR)as CostiVariabili from impiegoris i join risorsa r on (i.RisorsaC=r.RisorsaR and i.NrArea=r.AreaProdR ) where i.Tipologia='Consuntivo' or i.Tipologia='CONSUNTIVO' group by i.NrArt,i.NrOrdine;")
    cursor.execute("create view CostiVariabiliperArticoloConsuntivo as select NrArt,sum(CostiVariabili) as CostiVariabiliperArticolo from CostiVariabiliEQTAConsuntivo group by NrArt;")
    cursor.execute("create view quantitaperArticoloConsuntivo as select NrArt,sum(quantitàOutput) as QtaOutputperArticolo from CostiVariabiliEQTAConsuntivo group by NrArt;")
    cursor.execute("create view totaleCostiVariabiliconsuntivo as select sum(CostiVariabili) as 'Totale_costi_variabili' from costivariabilieqtaConsuntivo;")
    cursor.execute("create view totalecostiConsuntivo as select TotaleCostoMP+sum(t.'Totale_costi_variabili')  as 'TOTALE_COSTI_A_CONSUNTIVO' from totaleconsumiConsuntivo,totaleCostiVariabiliconsuntivo t;")
    cursor.execute("create view quantitàOutputBudget as select sum(quantitàOutput) as quantitàOutputBudget from costivariabilieqtabudget;")
    cursor.execute("create view costounitarioBudget as select `TOTALE_COSTI_A_BUDGET`/quantitàOutputBudget as costoUnitario from quantitàOutputBudget,totalecostibudget;")
    cursor.execute("create view costoPerArticoloBudget as select NrArt,costoUnitario*quantitàOutput as costoPerArticolo from costoUnitarioBudget,costivariabilieqtabudget;")
    cursor.execute("create view quantitàOutputConsuntivo as select sum(quantitàOutput) as quantitàOutputConsuntivo from costivariabilieqtaConsuntivo;")
    cursor.execute("create view costounitarioConsuntivo as select `TOTALE_COSTI_A_CONSUNTIVO`/quantitàOutputConsuntivo as costoUnitario from quantitàOutputConsuntivo,totalecosticonsuntivo;")
    cursor.execute("create view costoPerArticoloConsuntivo as select NrArt,costoUnitario*quantitàOutput as costoPerArticolo from costounitarioConsuntivo,costivariabilieqtaConsuntivo;")
    cursor.execute("create view mixstandardVendite as select m.NrArtV,(p.prezzomedio*m.qta) as venditemix from mixstandard m join prezzomedioperarticolobudget p on m.NrArtV=p.NrArtV;")
    cursor.execute("create view mixeffettivovendite as select m.NrArtV,(p.prezzomedio*m.qta) as venditemix from mixeffettivo m join prezzomedioperarticoloconsuntivo p on m.NrArtV=p.NrArtV;")
    cursor.execute("create view ricavimixstandard as select sum(venditemix) as 'Ricavo' from mixstandardvendite;")
    cursor.execute("create view ricavimixeffettivo as select sum(venditemix) as 'Ricavo' from mixeffettivovendite;")
    cursor.execute("create view costimixstandardperarticolo as select c.NrArt,sum((c.costoPerArticolo*m.mix)) as costimixstandard from costoperarticolobudget c join mixvolumibudget m on c.NrArt=m.NrArtV group by c.NrArt;")
    cursor.execute("create view costitotalimixstandard as select sum(costimixstandard) as costitotalimixstandard from costimixstandardperarticolo;")
    cursor.execute("create view costimixeffettivoperarticolo as select c.NrArt,sum((c.costoPerArticolo*m.mix)) as costimixeffettivo from costoperarticolobudget c join mixvolumiconsuntivo m on c.NrArt=m.NrArtV group by c.NrArt;")
    cursor.execute("create view costitotalimixeffettivo as select sum(costimixeffettivo) as costitotalimixeffettivo from costimixeffettivoperarticolo;")

    #PARTE NUOVA/QUERY NUOVE PER MODIFICA
    #NUOVI COSTI
    #--BUDGET--
    cursor.execute("Create view CostoImpiegoRisorseBUDGET as select i.NrArt,sum(i.Tempo*r.CostoBudgetR)as CostiImpiego from impiegoris i join risorsa r on (i.RisorsaC=r.RisorsaR and i.NrArea=r.AreaProdR ) where i.Tipologia like 'budget' group by i.NrArt;")
    cursor.execute("create view CostiConsumiBudget as select NrArtC,sum(ImportoTot) as CostoConsumo from consumo where Tipol='Budget' or Tipol='BUDGET' group by NrArtC;")
    cursor.execute("create view CostiProdBudget as select c.NrArtC,CostoConsumo+i.CostiImpiego as CostoTotaleProduzione from CostiConsumiBudget c join CostoImpiegoRisorseBUDGET i  on(c.NrArtC=i.NrArt) group by c.NrArtC;")
    cursor.execute("create view CostiTotaliBudget as select cp.NrArtC,CostoTotaleProduzione/vb.Qta as CostoTotaleUnitario from CostiProdBudget cp join volumiarticolibudget vb on (cp.NrArtC=vb.NrArtV);")
    cursor.execute("create view CostiTotaliperArticoloBudget as select cp.NrArtC,cp.CostoTotaleUnitario*vb.Qta as CostoTotalePerArticolo,vb.qta from CostiTotaliBudget cp join volumiarticolibudget vb on (cp.NrArtC=vb.NrArtV);")
    #--CONSUNTIVO--
    cursor.execute("Create view CostoImpiegoRisorseConsuntivo as select i.NrArt,sum(i.Tempo*r.CostoConsR)as CostiImpiego from impiegoris i join risorsa r on (i.RisorsaC=r.RisorsaR and i.NrArea=r.AreaProdR ) where i.Tipologia like 'Consuntivo' group by i.NrArt;")
    cursor.execute("create view CostiConsumiConsuntivo as select NrArtC,sum(ImportoTot) as CostoConsumo from consumo where Tipol='Consuntivo' or Tipol='CONSUNTIVO' group by NrArtC;")
    cursor.execute("create view CostiProdConsuntivo as select c.NrArtC,CostoConsumo+i.CostiImpiego as CostoTotaleProduzione from CostiConsumiConsuntivo c join CostoImpiegoRisorseConsuntivo i  on(c.NrArtC=i.NrArt) group by c.NrArtC;")
    cursor.execute("create view CostiTotaliConsuntivo as select cp.NrArtC,CostoTotaleProduzione/vb.Qta as CostoTotaleUnitario from CostiProdConsuntivo cp join volumiarticoliConsuntivo vb on (cp.NrArtC=vb.NrArtV);")
    cursor.execute("create view CostiTotaliperArticoloConsuntivo as select cp.NrArtC,cp.CostoTotaleUnitario*vb.Qta as CostoTotalePerArticolo,vb.qta from CostiTotaliConsuntivo cp join volumiarticoliConsuntivo vb on (cp.NrArtC=vb.NrArtV);")
    #--CALCOLO COSTI MIX--
    cursor.execute("create view costimixstandardQueryBudget as select c.NrArtC,sum(c.CostoTotaleUnitario*m.qta)as costimixstandard from CostiTotaliBudget c join mixstandard m on c.NrArtC=m.NrArtV group by c.NrArtC;")
    cursor.execute("create view TotaleCostiMixStandard as select sum(c.costimixstandard) as TotaleCostiMixStandard from costimixstandardQueryBudget c;")
    cursor.execute("create view costimixeffettivoQueryBudget as select c.NrArtC,sum(c.CostoTotaleUnitario*m.qta)as costimixeffettivo from CostiTotaliBudget c join mixeffettivo m on c.NrArtC=m.NrArtV group by c.NrArtC;")
    cursor.execute("create view TotaleCostiMixEffettivo as select sum(c.costimixeffettivo) as TotaleCostiMixEffettivo from costimixeffettivoQueryBudget c;")

    cursor.execute("CREATE VIEW venditeBudgetinVALUTALOCALECONSUNTIVO as select vb.NrMov,vb.Tipologia,vb.NrArtV,vb.NrOrig,vb.Qta,vb.ImportV/v.Tasso as RealImportV,v.CodVal from venditebudget vb join cliente c on vb.NrOrig=c.CodCLi join valuta v on c.Valuta=v.CodVal where v.Tipo = 'consuntivo' OR v.Tipo = 'CONSUNTIVO';")
    cursor.execute("Create view ImportiVenditePerArticoloBudgetVALUTACONSUNTIVO AS select vbvl.NrArtV,sum(RealImportV) as ImportoTotArticolo,sum(vbvl.Qta) as Qta from venditeBudgetinVALUTALOCALECONSUNTIVO vbvl group by vbvl.NrArtV;")

    cursor.execute("Create view TotaleVenditeBudgetVALUTACONSUNTIVO as select sum(ImportoTotArticolo) as TotaleVenditeBudgetValutaConsuntivo from ImportiVenditePerArticoloBudgetVALUTACONSUNTIVO;")

    cursor.execute('create view TassiBudget as select CodVal,Tasso from valuta where Tipo="Budget" or Tipo="BUDGET";')
    cursor.execute('create view TassiConsuntivo as select CodVal,Tasso from valuta where Tipo="Consuntivo" or Tipo="CONSUNTIVO";')

    cursor.execute('create view ScostamentoTassiDiCambio as select b.Tasso as "TassoBudget", c.Tasso-b.Tasso as "Scostamento",c.Tasso as "TassoConsuntivo" from TassiBudget b,TassiConsuntivo c where b.CodVal=c.CodVal;')

    cursor.execute('create view ScostamentoCostoOrarioAreaProd as select AreaProdR,RisorsaR,CostoBudgetR,(CostoConsR-CostoBudgetR) as Scostamento,CostoConsR from risorsa;')

    cursor.execute('create view costomedioMPperCodiceMPBudget as select CodiceMP as CodiceMP, avg(ImportoTot/QuantitàMP) as costomedioMP from consumo where Tipol="Budget" or Tipol="BUDGET" group by CodiceMP;')
    cursor.execute('create view costomedioMPperCodiceMPConsuntivo as select CodiceMP as CodiceMP, avg(ImportoTot/QuantitàMP) as costomedioMP from consumo where Tipol="Consuntivo" or Tipol="CONSUNTIVO" group by CodiceMP;')
    cursor.execute('create view ScostamentoMateriePrime as select b.CodiceMP,b.costomedioMP as costomedioMPbudget,c.costomedioMP-b.costomedioMP as scostamento,c.costomedioMP as costomedioMPconsuntivo from costomedioMPperCodiceMPBudget b join costomedioMPperCodiceMPConsuntivo c on(b.CodiceMP=c.CodiceMP) group by b.CodiceMP')
   
    cursor.execute('create view TotaleCostiBudgetDEFINITIVO as select sum(CostoTotalePerArticolo) as TotaleCostiBudget from CostiTotaliperArticoloBudget;')
    cursor.execute('create view TotaleCostiConsuntivoDEFINITIVO as select sum(CostoTotalePerArticolo) as TotaleCostiConsuntivo from CostiTotaliperArticoloConsuntivo;')

    #--MOL--
    cursor.execute("create VIEW molbudget AS SELECT v.TotaleVenditeBudget - c.TotaleCostiBudget AS `MOL_BUDGET` FROM (TotaleCostiBudgetDEFINITIVO c JOIN totalevenditebudget v);")
    cursor.execute("create view molconsuntivo AS SELECT (v.TotaleVenditeConsuntivo - c.TotaleCostiConsuntivo) AS `MOL_CONSUNTIVO` FROM (TotaleCostiConsuntivoDEFINITIVO c JOIN totalevenditeconsuntivo v)    ; ")
    cursor.execute("create view molmixstandard as select Ricavo-TotaleCostiMixStandard as `MOL_mix_standard` from ricavimixstandard,TotaleCostiMixStandard;")
    cursor.execute("create view molmixeffettivo as select Ricavo-TotaleCostiMixEffettivo as `MOL_mix_effettivo` from ricavimixeffettivo,TotaleCostiMixEffettivo;")

    print("View created!")
    conn.close()
    
 

def Risultati():
    # Apre la connessione al database e esegue la query
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()
    #COSTI
        # Query 1
        #ROUND per arrotondare a 2 cifre decimali
    cur.execute('SELECT ROUND(TOTALE_COSTI_A_BUDGET,2) FROM totalecostiBudget ')
    risultati1 = cur.fetchall()
        # Query 2
    cur.execute('SELECT ROUND(TOTALE_COSTI_A_CONSUNTIVO,2) FROM totalecostiConsuntivo')
    risultati2 = cur.fetchall()
    #RICAVI
        # Query 3
    cur.execute('SELECT ROUND(TotaleVenditeBudget,2) FROM totalevenditebudget')
    risultati3 = cur.fetchall()
        # Query 4
    cur.execute('SELECT ROUND(TotaleVenditeConsuntivo,2) FROM totalevenditeconsuntivo')
    risultati4 = cur.fetchall()
    #MIX STANDARD
    # Query 5
    cur.execute('SELECT ROUND(sum(venditemix),2) from  mixstandardvendite')
    risultati5 = cur.fetchall()
    # Query 6
    cur.execute('SELECT ROUND(sum(costitotalimixstandard),2) from  costitotalimixstandard')
    risultati6 = cur.fetchall()
    # Query 7
    cur.execute('SELECT ROUND(sum(MOL_mix_standard),2) from  molmixstandard')
    risultati7 = cur.fetchall()
    #MIX EFFETTIVO
    # Query 8
    cur.execute('SELECT ROUND(sum(venditemix),2) from  mixeffettivovendite')
    risultati8 = cur.fetchall()
    # Query 9
    cur.execute('SELECT ROUND(sum(costitotalimixeffettivo),2) from  costitotalimixeffettivo')
    risultati9 = cur.fetchall()
    # Query 10
    cur.execute('SELECT ROUND(sum(MOL_mix_effettivo),2) from  molmixeffettivo')
    risultati10 = cur.fetchall()
    #MOL
    #Query 11
    cur.execute("SELECT ROUND(sum(MOL_BUDGET),2) from molbudget")
    risultati11=cur.fetchall()
    #Query 12
    cur.execute("SELECT ROUND(sum(MOL_Consuntivo),2) from molconsuntivo")
    risultati12=cur.fetchall()
    #Quantitá
    #Query 13
    cur.execute("SELECT ROUND(sum(Qta),0) FROM VolumiArticoliBudget ")
    risultati13=cur.fetchall()
    #Query 14
    cur.execute("SELECT ROUND(sum(Qta),0) FROM VolumiArticoliConsuntivo ")
    risultati14=cur.fetchall()
    #Query 15
    cur.execute("SELECT ROUND(sum(qta),0) FROM volTotaleMixStandard ")
    risultati15=cur.fetchall()
    #Query 16
    cur.execute("SELECT ROUND(sum(qta),0) FROM volTotaleMixconsuntivo ")
    risultati16=cur.fetchall()
    #DELTA
    #Delta1
    cur.execute("SELECT ROUND(sum(venditemix),2)-(SELECT ROUND(TotaleVenditeBudget,2) FROM totalevenditebudget) from  mixstandardvendite ")
    Delta1=cur.fetchall()
    #Delta2
    cur.execute("SELECT ROUND(sum(venditemix),2)-(SELECT ROUND(sum(venditemix),2) from  mixstandardvendite) from  mixeffettivovendite")
    Delta2=cur.fetchall()
    #Delta3
    cur.execute("SELECT ROUND(TotaleVenditeConsuntivo,2)-(SELECT ROUND(sum(venditemix),2) from  mixeffettivovendite) FROM totalevenditeconsuntivo")
    Delta3=cur.fetchall()
    #Delta4
    cur.execute(" SELECT ROUND(sum(costitotalimixstandard),2) -(SELECT ROUND(TOTALE_COSTI_A_BUDGET,2) FROM totalecostiBudget ) from  costitotalimixstandard")
    Delta4=cur.fetchall()  
    #Delta5
    cur.execute("SELECT ROUND(sum(costitotalimixeffettivo),2)-(SELECT ROUND(sum(costitotalimixstandard),2) from  costitotalimixstandard) from  costitotalimixeffettivo")
    Delta5=cur.fetchall()
    #Delta6
    cur.execute("SELECT ROUND(TOTALE_COSTI_A_CONSUNTIVO,2) -(SELECT ROUND(sum(costitotalimixeffettivo),2) from  costitotalimixeffettivo)FROM totalecostiConsuntivo")
    Delta6=cur.fetchall()
    #Delta7
    cur.execute("SELECT ROUND(sum(MOL_mix_standard),2) -(SELECT ROUND(sum(MOL_BUDGET),2) from molbudget)from  molmixstandard")
    Delta7=cur.fetchall()
    #Delta8
    cur.execute("SELECT ROUND(sum(MOL_mix_effettivo),2)-(SELECT ROUND(sum(MOL_mix_standard),2) from  molmixstandard) from  molmixeffettivo")
    Delta8=cur.fetchall()
    #Delta9
    cur.execute("SELECT ROUND(sum(MOL_Consuntivo),2) -(SELECT ROUND(sum(MOL_mix_effettivo),2) from  molmixeffettivo)from molconsuntivo")
    Delta9=cur.fetchall()
    #Delta10
    cur.execute("SELECT ROUND(sum(qta),0)-(SELECT ROUND(sum(Qta),0) FROM VolumiArticoliBudget) FROM volTotaleMixStandard")
    Delta10=cur.fetchall()
    #Delta11
    cur.execute("SELECT ROUND(sum(qta),0)-(SELECT ROUND(sum(qta),0) FROM volTotaleMixStandard) FROM volTotaleMixconsuntivo ")
    Delta11=cur.fetchall()
    #Delta12
    cur.execute("SELECT ROUND(sum(Qta),0) -(SELECT ROUND(sum(qta),0) FROM volTotaleMixconsuntivo )FROM VolumiArticoliConsuntivo")
    Delta12=cur.fetchall()
