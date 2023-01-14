

--VISTE PER FARE COMPARAZIONE RICAVI USANDO I TASSI DI CAMBIO MEDI A CONSUNTIVO--


CREATE VIEW venditeBudgetinVALUTALOCALECONSUNTIVO as
select vb.NrMov,vb.Tipologia,vb.NrArtV,vb.NrOrig,vb.Qta,vb.ImportV/v.Tasso as RealImportV,v.CodVal
from venditebudget vb join cliente c on vb.NrOrig=c.CodCLi join valuta v on c.Valuta=v.CodVal
where v.Tipo = 'consuntivo' OR v.Tipo = 'CONSUNTIVO';

Create view ImportiVenditePerArticoloBudgetVALUTACONSUNTIVO AS
select vbvl.NrArtV,sum(RealImportV) as ImportoTotArticolo,sum(vbvl.Qta) as Qta
from venditeBudgetinVALUTALOCALECONSUNTIVO vbvl
group by vbvl.NrArtV;


--questa è quella da stampare:--

Create view TotaleVenditeBudgetVALUTACONSUNTIVO as
select sum(ImportoTotArticolo) as TotaleVenditeBudget
from ImportiVenditePerArticoloBudget;



--Sotto la tabella di questi scostamenti fare la seguente tabella di scostamenti Tassi di Cambio:

create view TassiBudget as
select CodVal,Tasso
from valuta
where Tipo='Budget' or Tipo='BUDGET';

create view TassiConsuntivo as
select CodVal,Tasso
from valuta
where Tipo='Consuntivo' or Tipo='CONSUNTIVO';

-- questa è quella da stampare--
create view ScostamentoTassiDiCambio as
select b.Tasso as 'TassoBudget',c.Tasso-b.Tasso as 'Scostamento',c.Tasso as 'TassoConsuntivo'
from TassiBudget b,TassiConsuntivo c
where b.CodVal=c.CodVal


-- //////////////////////////////////////////////////////////////////////////////////////--

-- PER pagina scostamenti costi per AREAPRODUZIONE--


 create view CostiPerAreaProdBudget as
select i.NrArea,i.RisorsaC,r.CostoBugetR,sum(i.Tempo*r.CostoBugetR)as CostiImpiego
from impiegoris i join risorsa r on (i.RisorsaC=r.RisorsaR and i.NrArea=r.AreaProdR )
where (i.Tipologia = 'budget' or i.Tipologia='BUDGET') and i.Quantitá>=0
group by i.NrArea,i.RisorsaC
ORDER BY sum(i.Tempo) DESC;

 create view CostiPerAreaProdConsuntivo as
select i.NrArea,i.RisorsaC,r.CostoConsR,sum(i.Tempo*r.CostoConsR)as CostiImpiego
from impiegoris i join risorsa r on (i.RisorsaC=r.RisorsaR and i.NrArea=r.AreaProdR )
where (i.Tipologia = 'consuntivo' or i.Tipologia='CONSUNTIVO') and i.Quantitá>=0
group by i.NrArea,i.RisorsaC
ORDER BY sum(i.Tempo) DESC

--------------------------------------------------------------------------------------------------

--aggiungi queste query--

create view costomedioMPperCodiceMPBudget as
select CodiceMP as CodiceMP, avg(ImportoTot/QuantitàMP) as costomedioMP
from consumo
where Tipol='Budget' or Tipol='BUDGET'
group by CodiceMP;

create view costomedioMPperCodiceMPConsuntivo as
select CodiceMP as CodiceMP, avg(ImportoTot/QuantitàMP) as costomedioMP
from consumo
where Tipol='Consuntivo' or Tipol='CONSUNTIVO'
group by CodiceMP;

--e stampa questa --
create view ScostamentoMateriePrime as
select b.CodiceMP,b.costomedioMP as costomedioMPbudget,c.costomedioMP-b.costomedioMP as scostamento,c.costomedioMP as costomedioMPconsuntivo
from costomedioMPperCodiceMPBudget b join costomedioMPperCodiceMPConsuntivo c on(b.CodiceMP=c.CodiceMP)
group by b.CodiceMP

--------------------------------------------------

create view ScostamentiPerArticolo as
select vb.NrArtV as NrArticolo,vc.Qta-vb.Qta as ScostamentoQuantità ,vc.ImportoTotArticolo-vb.ImportoTotArticolo as ScostamentoRicavo,cc.CostoTotalePerArticolo-cb.CostoTotalePerArticolo as  ScostamentoCosti, (vc.ImportoTotArticolo-vb.ImportoTotArticolo) - (cc.CostoTotalePerArticolo-cb.CostoTotalePerArticolo)  as ScostamentoMol
from (importivenditeperarticolobudget vb join importivenditeperarticoloconsuntivo vc on(vb.NrArtV=vc.NrArtV) 
		join CostiTotaliperArticoloBudget cb on (cb.NrArtC=vb.NrArtV) join CostiTotaliperArticoloConsuntivo cc on (cc.NrArtC=vb.NrArtV))
        

