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
    
    # chiusura della connessione
    conn.close()

    return render_template('index.html', risultati1=risultati1, risultati2=risultati2 ,risultati3=risultati3, risultati4=risultati4, risultati5=risultati5, risultati6=risultati6 , risultati7=risultati7 , risultati8=risultati8 , risultati9=risultati9, risultati10=risultati10 , risultati11=risultati11 , risultati12=risultati12 , risultati13=risultati13 , risultati14=risultati14 , risultati15=risultati15 , risultati16=risultati16 , Delta1=Delta1, Delta2=Delta2, Delta3=Delta3 , Delta4=Delta4, Delta5=Delta5 , Delta6=Delta6 , Delta7=Delta7 , Delta8=Delta8 , Delta9=Delta9, Delta10=Delta10, Delta11=Delta11 , Delta12=Delta12 )
    
if __name__ == '__main__':
    app.run(debug=True)

   