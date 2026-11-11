(function(){
  "use strict";
  var eur = new Intl.NumberFormat("de-AT",{style:"currency",currency:"EUR"});
  function num(id){var v=parseFloat(String(document.getElementById(id).value).replace(",","."));return isFinite(v)&&v>0?v:0;}
  function bind(form,fn){var f=document.getElementById(form);if(!f)return;f.addEventListener("input",fn);fn();}
  // Sätze 2026 (Quellen siehe Seite, abgerufen 11.11.2026)
  var KU_GRENZE=55000, KU_TOL=60500;
  var KM={pkw:0.50,moto:0.25,rad:0.25}, KM_MIT=0.15;
  var TAG=30, STD=2.5, NACHT=17;

  bind("ku",function(){
    var vj=num("ku_vj"), b=num("ku_bisher"), n=num("ku_neu"), s=b+n, o=document.getElementById("ku_out"), t, c="";
    if(vj>KU_GRENZE){t="Vorjahresumsatz "+eur.format(vj)+" liegt über 55.000 € – heuer gilt die Kleinunternehmerbefreiung nicht.";c="bad";}
    else if(s<=KU_GRENZE){t="Gesamt heuer: "+eur.format(s)+". Unter der Grenze von 55.000 € – Befreiung bleibt. Noch frei bis zur Grenze: "+eur.format(KU_GRENZE-s)+".";}
    else if(s<=KU_TOL){t="Gesamt heuer: "+eur.format(s)+" ("+((s/KU_GRENZE-1)*100).toFixed(1).replace(".",",")+" % über 55.000 €). Innerhalb der 10-%-Toleranz: Rechnungen bis Jahresende noch ohne USt, im Folgejahr keine Befreiung mehr. Noch frei bis 60.500 €: "+eur.format(KU_TOL-s)+".";c="warn";}
    else{t="Gesamt heuer: "+eur.format(s)+" – über 60.500 €. Ab dem Umsatz, mit dem die Grenze überschritten wird, ist Umsatzsteuer zu verrechnen.";c="bad";}
    o.textContent=t;o.className=c;
  });

  bind("km",function(){
    var typ=document.getElementById("km_typ").value, km=num("km_km"), mit=typ==="pkw"?Math.floor(num("km_mit")):0, o=document.getElementById("km_out");
    var basis=km*KM[typ], zus=km*mit*KM_MIT, t=eur.format(basis)+" Kilometergeld ("+km.toLocaleString("de-AT")+" km × "+eur.format(KM[typ])+")";
    if(mit>0)t+=" + "+eur.format(zus)+" Mitfahrende ("+mit+" × "+km.toLocaleString("de-AT")+" km × 0,15 €)";
    t+=" = "+eur.format(basis+zus)+".";
    var lim=typ==="rad"?3000:30000; if(km>lim)t+=" Achtung: mehr als "+lim.toLocaleString("de-AT")+" km – Jahresgrenze beachten.";
    o.textContent=t;o.className=km>lim?"warn":"";
  });

  function teil(h){ if(h<=3)return 0; return Math.min(TAG,Math.ceil(h)*STD); }
  bind("di",function(){
    var h=num("di_h"), n=Math.floor(num("di_n")), o=document.getElementById("di_out");
    var tage=Math.floor(h/24), rest=h-tage*24, tg=tage*TAG+teil(rest), ng=n*NACHT;
    var t="Tagesgeld: "+eur.format(tg); if(tage>0)t+=" ("+tage+" × 30 € + Rest "+rest.toLocaleString("de-AT")+" h = "+eur.format(teil(rest))+")";
    if(n>0)t+=" · Nächtigungsgeld: "+n+" × 17 € = "+eur.format(ng);
    t+=" · Gesamt: "+eur.format(tg+ng)+".";
    o.textContent=t;o.className="";
  });
})();
