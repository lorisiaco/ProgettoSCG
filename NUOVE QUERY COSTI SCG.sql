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
select c.NrArtC,sum(c.CostoTotalePerArticolo*m.mix) as costimixstandard
from CostiTotaliperArticoloBudget c join mixvolumibudget m on c.NrArtC=m.NrArtV
group by c.NrArtC;

create view TotaleCostiMixStandard as
select (sum(c.costimixstandard)/vb.VolumeTotaleVenditeBudget)*vc.VolumeTotaleVenditeConsuntivo
from costimixstandardQueryBudget c,voltotalevenditebudget vb,voltotalevenditeconsuntivo vc;

create view costimixeffettivoQueryBudget as
select c.NrArtC,sum(c.CostoTotalePerArticolo*m.mix) as costimixstandard
from CostiTotaliperArticoloBudget c join mixvolumiconsuntivo m on c.NrArtC=m.NrArtV
group by c.NrArtC;

create view TotaleCostiMixeffettivo as
select (sum(c.costimixstandard)/vb.VolumeTotaleVenditeBudget)*vc.VolumeTotaleVenditeConsuntivo
from costimixstandardQueryBudget c,voltotalevenditebudget vb,voltotalevenditeconsuntivo vc




--DA CANCELLARE--
costimixstandardperarticolo
costimixeffettivoperarticolo
--RIMPIAZZARE CON--
