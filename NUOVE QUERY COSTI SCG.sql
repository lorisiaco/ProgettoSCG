--BUDGET--
Create view CostoImpiegoRisorseBUDGET as
select i.NrArt,sum(i.Tempo*r.CostoBugetR)as CostiImpiego
from impiegoris i join risorsa r on (i.RisorsaC=r.RisorsaR and i.NrArea=r.AreaProdR )
where i.Tipologia like 'budget'
group by i.NrArt;

create view CostiConsumiBudget as
select NrArtC,sum(ImportoTot) as CostoConsumo
from consumo
where Tipol='Budget' and Tipol='BUDGET'
group by NrArtC;

create view CostiProdBudget as
select c.NrArtC,CostoConsumo+i.CostiImpiego as CostoTotaleProduzione
from CostiConsumiBudget c join CostoImpiegoRisorseBUDGET i  on(c.NrArtC=i.NrArt)
group by c.NrArtC;

create view CostiTotaliBudget as
select cp.NrArtC,CostoTotaleProduzione/vb.Qta as CostoTotaleUnitario
from CostiProdBudget cp join volumiarticolibudget vb on (cp.NrArtC=vb.NrArtV);

create view CostiTotaliperArticoloBudget as
select cp.NrArtC,cp.CostoTotaleUnitario*vb.Qta as CostoTotalePerArticolo,vb.qta
from CostiTotaliBudget cp join volumiarticolibudget vb on (cp.NrArtC=vb.NrArtV);

--CONSUNTIVO--

Create view CostoImpiegoRisorseConsuntivo as
select i.NrArt,sum(i.Tempo*r.CostoBugetR)as CostiImpiego
from impiegoris i join risorsa r on (i.RisorsaC=r.RisorsaR and i.NrArea=r.AreaProdR )
where i.Tipologia like 'Consuntivo'
group by i.NrArt;

create view CostiConsumiConsuntivo as
select NrArtC,sum(ImportoTot) as CostoConsumo
from consumo
where Tipol='Consuntivo' and Tipol='CONSUNTIVO'
group by NrArtC;

create view CostiProdConsuntivo as
select c.NrArtC,CostoConsumo+i.CostiImpiego as CostoTotaleProduzione
from CostiConsumiConsuntivo c join CostoImpiegoRisorseConsuntivo i  on(c.NrArtC=i.NrArt)
group by c.NrArtC;

create view CostiTotaliConsuntivo as
select cp.NrArtC,CostoTotaleProduzione/vb.Qta as CostoTotaleUnitario
from CostiProdConsuntivo cp join volumiarticoliConsuntivo vb on (cp.NrArtC=vb.NrArtV);

create view CostiTotaliperArticoloConsuntivo as
select cp.NrArtC,cp.CostoTotaleUnitario*vb.Qta as CostoTotalePerArticolo,vb.qta
from CostiTotaliConsuntivo cp join volumiarticoliConsuntivo vb on (cp.NrArtC=vb.NrArtV);

--CALCOLO COSTI MIX--

create view costimixstandardQueryBudget as
select c.NrArtC,sum(c.CostoTotaleUnitario*m.qta)as costimixstandard
from CostiTotaliBudget c join mixstandard m on c.NrArtC=m.NrArtV
group by c.NrArtC;

+
create view TotaleCostiMixStandard as
select sum(c.costimixstandard) as TotaleCostiMixStandard
from costimixstandardQueryBudget c;

create view costimixeffettivoQueryBudget as
select c.NrArtC,sum(c.CostoTotaleUnitario*m.qta)as costimixeffettivo
from CostiTotaliBudget c join mixeffettivo m on c.NrArtC=m.NrArtV
group by c.NrArtC;

+
create view TotaleCostiMixEffettivo as
select sum(c.costimixeffettivo) as TotaleCostiMixEffettivo
from costimixeffettivoQueryBudget c;

--Somma costi budget e consuntivo da aggiungere--
+
create view TotaleCostiBudgetDEFINITIVO as
select sum(CostoTotalePerArticolo) as TotaleCostiBudget
from CostiTotaliperArticoloBudget;

+
create view TotaleCostiConsuntivoDEFINITIVO as
select sum(CostoTotalePerArticolo) as TotaleCostiConsuntivo
from CostiTotaliperArticoloConsuntivo;

--------------------------------------------------------------------------------------------------
NUOVE:

create view CostiConsumiTotaliConsuntivo as
select cp.NrArtC,CostoConsumo/vb.Qta as CostoTotaleUnitario
from CostiConsumiConsuntivo cp join volumiarticoliConsuntivo vb on (cp.NrArtC=vb.NrArtV);

create view ConsumiTotaliPerArticoloConsuntivo as
select cp.NrArtC,cp.CostoTotaleUnitario*vb.Qta as CostoTotalePerArticolo,vb.qta
from CostiConsumiTotaliConsuntivo cp join volumiarticoliConsuntivo vb on (cp.NrArtC=vb.NrArtV);

create view CostiImpiegoTotaliConsuntivo as
select cp.NrArt,CostiImpiego/vb.Qta as CostoTotaleUnitario
from CostoImpiegoRisorseConsuntivo cp join volumiarticoliConsuntivo vb on (cp.NrArt=vb.NrArtV);

create view ImpiegoTotaliPerArticoloConsuntivo as
select cp.NrArt,cp.CostoTotaleUnitario*vb.Qta as CostoTotalePerArticolo,vb.qta
from CostiImpiegoTotaliConsuntivo cp join volumiarticoliConsuntivo vb on (cp.NrArt=vb.NrArtV);

create view TotaleImpiegoConsuntivoDEFINITIVO as
select sum(CostoTotalePerArticolo)
from ImpiegoTotaliPerArticoloConsuntivo;

create view CostiConsumiTotaliBudget as
select cp.NrArtC,CostoConsumo/vb.Qta as CostoTotaleUnitario
from CostiConsumiBudget cp join volumiarticoliBudget vb on (cp.NrArtC=vb.NrArtV);

create view ConsumiTotaliPerArticoloBudget as
select cp.NrArtC,cp.CostoTotaleUnitario*vb.Qta as CostoTotalePerArticolo,vb.qta
from CostiConsumiTotaliBudget cp join volumiarticoliBudget vb on (cp.NrArtC=vb.NrArtV);

create view TotaleConsumiBudgetDEFINITIVO as
select sum(CostoTotalePerArticolo)
from ConsumiTotaliPerArticoloBudget;

create view CostiImpiegoTotaliBudget as
select cp.NrArt,CostiImpiego/vb.Qta as CostoTotaleUnitario
from CostoImpiegoRisorseBudget cp join volumiarticoliBudget vb on (cp.NrArt=vb.NrArtV);

create view ImpiegoTotaliPerArticoloBudget as
select cp.NrArt,cp.CostoTotaleUnitario*vb.Qta as CostoTotalePerArticolo,vb.qta
from CostiImpiegoTotaliBudget cp join volumiarticoliBudget vb on (cp.NrArt=vb.NrArtV);

create view TotaleImpiegoBudgetDEFINITIVO as
select sum(CostoTotalePerArticolo)
from ImpiegoTotaliPerArticoloBudget;


create view ctbudget as
select c.`sum(CostoTotalePerArticolo)`+i.`sum(CostoTotalePerArticolo)` as costototalebudget
from TotaleImpiegoBudgetDEFINITIVO i,TotaleConsumiBudgetDEFINITIVO c,TotaleCostiBudgetDEFINITIVO d;

create view ctconsuntivo as
select c.`sum(CostoTotalePerArticolo)`+i.`sum(CostoTotalePerArticolo)` as costototaleconsuntivo
from TotaleImpiegoConsuntivoDEFINITIVO i,TotaleConsumiConsuntivoDEFINITIVO c,TotaleCostiConsuntivoDEFINITIVO d;


--DA CANCELLARE--
costimixstandardperarticolo
costimixeffettivoperarticolo
--RIMPIAZZARE CON--
