from flask import Flask, render_template
import sqlite3
import Prova

app = Flask(__name__)

@app.route('/')
def table():
    Prova.CreazioneDB()
    Prova.CreaViste()
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()
    cur.execute('SELECT ROUND(TOTALE_COSTI_A_BUDGET,2) FROM totalecostiBudget ')
    risultat1 = cur.fetchall()
    risultati1 = list(map(float, [x[0] for x in risultat1]))
        # Query 2
    cur.execute('SELECT ROUND(TOTALE_COSTI_A_CONSUNTIVO,2) FROM totalecostiConsuntivo')
    risultat2 = cur.fetchall()
    risultati2 = list(map(float, [x[0] for x in risultat2]))
    #RICAVI
        # Query 3
    cur.execute('SELECT ROUND(TotaleVenditeBudget,2) FROM totalevenditebudget')
    risultat3 = cur.fetchall()
    risultati3 = list(map(float, [x[0] for x in risultat3]))
        # Query 4
    cur.execute('SELECT ROUND(TotaleVenditeConsuntivo,2) FROM totalevenditeconsuntivo')
    risultat4 = cur.fetchall()
    risultati4 = list(map(float, [x[0] for x in risultat4]))
    #MIX STANDARD
    # Query 5
    cur.execute('SELECT ROUND(sum(venditemix),2) from  mixstandardvendite')
    risultat5 = cur.fetchall()
    risultati5 = list(map(float, [x[0] for x in risultat5]))
    # Query 6
    cur.execute('SELECT ROUND(sum(costitotalimixstandard),2) from  costitotalimixstandard')
    risultat6 = cur.fetchall()
    risultati6 = list(map(float, [x[0] for x in risultat6]))
    # Query 7
    cur.execute('SELECT ROUND(sum(MOL_mix_standard),2) from  molmixstandard')
    risultat7 = cur.fetchall()
    risultati7 = list(map(float, [x[0] for x in risultat7]))
    #MIX EFFETTIVO
    # Query 8
    cur.execute('SELECT ROUND(sum(venditemix),2) from  mixeffettivovendite')
    risultat8 = cur.fetchall()
    risultati8 = list(map(float, [x[0] for x in risultat8]))
    # Query 9
    cur.execute('SELECT ROUND(sum(costitotalimixeffettivo),2) from  costitotalimixeffettivo')
    risultat9 = cur.fetchall()
    risultati9 = list(map(float, [x[0] for x in risultat9]))
    # Query 10
    cur.execute('SELECT ROUND(sum(MOL_mix_effettivo),2) from  molmixeffettivo')
    risultat10 = cur.fetchall()
    risultati10 = list(map(float, [x[0] for x in risultat10]))
    #MOL
    #Query 11
    cur.execute("SELECT ROUND(sum(MOL_BUDGET),2) from molbudget")
    risultat11 = cur.fetchall()
    risultati11 = list(map(float, [x[0] for x in risultat11]))
    #Query 12
    cur.execute("SELECT ROUND(sum(MOL_Consuntivo),2) from molconsuntivo")
    risultat12 = cur.fetchall()
    risultati12 = list(map(float, [x[0] for x in risultat12]))
    #Quantitá
    #Query 13
    cur.execute("SELECT ROUND(sum(Qta),0) FROM VolumiArticoliBudget ")
    risultat13 = cur.fetchall()
    risultati13 = list(map(int, [x[0] for x in risultat13]))
    #Query 14
    cur.execute("SELECT ROUND(sum(Qta),0) FROM VolumiArticoliConsuntivo ")
    risultat14 = cur.fetchall()
    risultati14 = list(map(int, [x[0] for x in risultat14]))
    #Query 15
    cur.execute("SELECT ROUND(sum(qta),0) FROM volTotaleMixStandard ")
    risultat15 = cur.fetchall()
    risultati15 = list(map(int, [x[0] for x in risultat15]))
    #Query 16
    cur.execute("SELECT ROUND(sum(qta),0) FROM volTotaleMixconsuntivo ")
    risultat16 = cur.fetchall()
    risultati16 = list(map(int, [x[0] for x in risultat16]))
    #DELTA
    #Delta1
    cur.execute("SELECT ROUND(sum(venditemix),2)-(SELECT ROUND(TotaleVenditeBudget,2) FROM totalevenditebudget) from  mixstandardvendite ")
    Delt1=cur.fetchall()
    Delta1 = [round(x[0], 2) for x in Delt1]
    #Delta2
    cur.execute("SELECT ROUND(sum(venditemix),2)-(SELECT ROUND(sum(venditemix),2) from  mixstandardvendite) from  mixeffettivovendite")
    Delt2=cur.fetchall()
    Delta2 = [round(x[0], 2) for x in Delt2]
    #Delta3
    cur.execute("SELECT ROUND(TotaleVenditeConsuntivo,2)-(SELECT ROUND(sum(venditemix),2) from  mixeffettivovendite) FROM totalevenditeconsuntivo")
    Delt3=cur.fetchall()
    Delta3 = [round(x[0], 2) for x in Delt3]
    #Delta4
    cur.execute(" SELECT ROUND(sum(costitotalimixstandard),2) -(SELECT ROUND(TOTALE_COSTI_A_BUDGET,2) FROM totalecostiBudget ) from  costitotalimixstandard")
    Delt4=cur.fetchall()
    Delta4 = [round(x[0], 2) for x in Delt4]
    #Delta5
    cur.execute("SELECT ROUND(sum(costitotalimixeffettivo),2)-(SELECT ROUND(sum(costitotalimixstandard),2) from  costitotalimixstandard) from  costitotalimixeffettivo")
    Delt5=cur.fetchall()
    Delta5 = [round(x[0], 2) for x in Delt5]
    #Delta6
    cur.execute("SELECT ROUND(TOTALE_COSTI_A_CONSUNTIVO,2) -(SELECT ROUND(sum(costitotalimixeffettivo),2) from  costitotalimixeffettivo)FROM totalecostiConsuntivo")
    Delt6=cur.fetchall()
    Delta6 = [round(x[0], 2) for x in Delt6]
    #Delta7
    cur.execute("SELECT ROUND(sum(MOL_mix_standard),2) -(SELECT ROUND(sum(MOL_BUDGET),2) from molbudget)from  molmixstandard")
    Delt7=cur.fetchall()
    Delta7 = [round(x[0], 2) for x in Delt7]
    #Delta8
    cur.execute("SELECT ROUND(sum(MOL_mix_effettivo),2)-(SELECT ROUND(sum(MOL_mix_standard),2) from  molmixstandard) from  molmixeffettivo")
    Delt8=cur.fetchall()
    Delta8 = [round(x[0], 2) for x in Delt8]
    #Delta9
    cur.execute("SELECT ROUND(sum(MOL_Consuntivo),2) -(SELECT ROUND(sum(MOL_mix_effettivo),2) from  molmixeffettivo)from molconsuntivo")
    Delt9=cur.fetchall()
    Delta9 = [round(x[0], 2) for x in Delt9]
    #Delta10
    cur.execute("SELECT ROUND(sum(qta),0)-(SELECT ROUND(sum(Qta),0) FROM VolumiArticoliBudget) FROM volTotaleMixStandard")
    Delt10=cur.fetchall()
    Delta10 = [int(x[0]) for x in Delt10]
    #Delta11
    cur.execute("SELECT ROUND(sum(qta),0)-(SELECT ROUND(sum(qta),0) FROM volTotaleMixStandard) FROM volTotaleMixconsuntivo ")
    Delt11=cur.fetchall()
    Delta11 = [int(x[0]) for x in Delt11]
    #Delta12
    cur.execute("SELECT ROUND(sum(Qta),0) -(SELECT ROUND(sum(qta),0) FROM volTotaleMixconsuntivo )FROM VolumiArticoliConsuntivo")
    Delt12=cur.fetchall()
    Delta12 = [int(x[0]) for x in Delt12]
    # chiusura della connessione
    conn.close()

    return render_template('home.html', risultati1=risultati1, risultati2=risultati2 ,risultati3=risultati3, risultati4=risultati4, risultati5=risultati5, risultati6=risultati6 , risultati7=risultati7 , risultati8=risultati8 , risultati9=risultati9, risultati10=risultati10 , risultati11=risultati11 , risultati12=risultati12 , risultati13=risultati13 , risultati14=risultati14 , risultati15=risultati15 , risultati16=risultati16 , Delta1=Delta1, Delta2=Delta2, Delta3=Delta3 , Delta4=Delta4, Delta5=Delta5 , Delta6=Delta6 , Delta7=Delta7 , Delta8=Delta8 , Delta9=Delta9, Delta10=Delta10, Delta11=Delta11 , Delta12=Delta12)

@app.route('/TotaleVenditeBudget')
def VALUTACONSUNTIVO():
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM TotaleVenditeBudgetVALUTACONSUNTIVO ')
    rs = cur.fetchall()
    return render_template('TotaleVenditeBudget.html', rs=rs)

@app.route('/ScostamentoTassiDiCambio')
def ScostamentoTassiDiCambio():
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM ScostamentoTassiDiCambio ')
    rs1 = cur.fetchall()
    return render_template('ScostamentoTassiDiCambio.html', rs1=rs1)

@app.route('/ScostamentoCostoOrarioAreaProduzione')
def ScostamentoCostoOrarioAreaProduzione():
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM ScostamentoCostoOrarioAreaProd  ')
    rs2 = cur.fetchall()
    return render_template('ScostamentoCostoOrarioAreaProduzione.html', rs2=rs2)


if __name__ == '__main__':
    app.run(debug=True)

   