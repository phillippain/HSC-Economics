def make(B):
    c, cd = "#8a3fb0", "#6a2a8a"
    ed = B.ed
    text = (
    "<h3>What labour market policies do</h3>"
    "<p><b>Labour market policies</b> are the rules and programs that shape how workers and employers are matched, how wages and conditions are set, and how skilled the workforce is. They are a form of <b>microeconomic (supply-side) policy</b>. Their objectives are lower unemployment, higher participation, higher productivity and fair pay, without pushing up inflation. They work on the labour market itself, rather than on aggregate demand.</p>"
    "<h3>Wage setting and industrial relations</h3>"
    "<p>Australia moved from centralised wage fixing to <b>enterprise bargaining</b> in the 1990s, so that pay could reflect productivity at the firm level. The <b>Fair Work Act 2009</b> now sets the framework: a safety net of National Employment Standards, modern awards for each industry, and bargaining for enterprise agreements, all overseen by the <b>Fair Work Commission</b>. Recent changes include the 2022 Secure Jobs, Better Pay reforms, which widened multi-employer bargaining, and the Building Cooperative Workplaces Act 2026, which took effect on 7 July 2026 and eases the workload of the Commission.</p>"
    "<h3>Minimum wages</h3>"
    "<p>Each year the Fair Work Commission reviews minimum wages. On 2 June 2026 it lifted modern award minimum rates by 4.75 per cent and the national minimum wage by about 6 per cent, to $26.44 an hour ($1,004.90 a week), from 1 July 2026. This is the first time the weekly rate has passed $1,000. About 2.8 million employees, roughly 21 per cent of the workforce, are paid at an award minimum rate. Supporters say minimum wages protect low-paid workers and support demand. Critics say a wage floor above the market wage can reduce the number of jobs for low-skilled workers, particularly young people (Figure 3).</p>"
    "<h3>Education, training and skills</h3>"
    "<p>Skills policy tackles <b>structural unemployment</b> by improving the match between workers and jobs. Free TAFE is now permanent under the Free TAFE Act 2025, with a $1.5 billion agreement with the states for more than 500,000 places. Apprenticeship incentives and national skills priorities aim to fill shortages in areas such as construction, care and clean energy. Higher skills raise labour productivity and so shift the LRAS curve to the right.</p>"
    "<h3>Employment services and participation</h3>"
    "<p><b>Workforce Australia</b> is the government employment service that helps job seekers train, find work and meet mutual obligation requirements. Income support such as JobSeeker acts as a safety net, but must be designed so that it does not weaken the incentive to look for work. Other measures lift participation, such as childcare subsidies, which make it easier for parents to work, and skilled migration, which adds workers where there are shortages.</p>"
    "<h3>The labour market now</h3>"
    "<p>Unemployment rose to 4.7 per cent in September 2026, the highest in almost five years, although the trend rate was 4.6 per cent. The RBA says a rate between 4.5 and 5 per cent is needed to ease inflation pressure, so policy is balancing two aims: keeping people in work, and keeping wage growth consistent with the inflation target.</p>"
    "<h3>Evaluating labour market policies</h3>"
    "<ul><li><b>Strengths:</b> they lift productivity and participation, reduce structural unemployment, protect low-paid workers and can make wages respond to firm performance.</li>"
    "<li><b>Limitations:</b> skills programs take years to pay off and may train people for the wrong jobs. Higher minimum wages may cost some jobs and raise business costs. Flexible bargaining can widen pay differences, and rules can add compliance costs.</li>"
    "<li><b>Policy mix:</b> they do not fix a cyclical downturn, so they work alongside fiscal and monetary policy.</li></ul>"
    "<p><b>Use it in an exam:</b> pick one tool, say which type of unemployment or productivity problem it targets, show the effect on the labour market or LRAS, then weigh the long-run gain against costs and time lags.</p>"
    "<p>Sources: <a href=\"https://www.claytonutz.com/insights/2026/june/annual-wage-review-2026-the-immediate-compliance-impacts-and-beyond\">Clayton Utz, Annual Wage Review 2026</a>; <a href=\"https://www.abs.gov.au/media-centre/media-releases/unemployment-rate-47-september\">ABS, Unemployment rate at 4.7% in September</a>; <a href=\"https://www.fairwork.gov.au/newsroom/news/building-cooperative-workplaces-reforms\">Fair Work Ombudsman, Building Cooperative Workplaces reforms</a>; <a href=\"https://www.dewr.gov.au/el/newsroom/data-dashboard\">DEWR data dashboard</a>; <a href=\"https://www.newcastleherald.com.au/story/9356375/unemployment-rate-climbs-to-near-five-year-high/\">Newcastle Herald (AAP), RBA comments</a>.</p>"
    )
    tiles = ('<div class="k"><div><b>4.7%</b><i>Unemployment rate</i><u>September 2026</u></div><div><b>66.8%</b><i>Participation rate</i><u>September 2026</u></div>'
             '<div><b>$26.44</b><i>National minimum wage</i><u>Per hour from 1 July 2026</u></div><div><b>4.75%</b><i>Award wage rise</i><u>2026 Annual Wage Review</u></div></div>')
    floor = ed.price_floor(ed.TOPIC[4], good="labour", ylabel="Wage")
    figs = [
      B.fig(1, "Key numbers", tiles),
      B.fig(2, "Labour market policy tools", B.table(["Tool", "Aim", "Example"], [["Wage setting", "Pay linked to productivity", "Enterprise bargaining"], ["Minimum wages", "Protect low paid", "$26.44 an hour"], ["Skills and training", "Cut structural unemployment", "Free TAFE"], ["Employment services", "Match workers to jobs", "Workforce Australia"], ["Participation", "Larger labour force", "Childcare subsidies"], ["Migration", "Fill skill shortages", "Skilled visas"]])),
      B.fig(3, "A minimum wage above the market wage", floor.svg(), "A wage floor set above the equilibrium wage raises pay for those who keep jobs but leaves a surplus of labour, which is unemployment. Not to scale."),
      B.fig(4, "Chain: how skills policy lifts output", B.chain(["More training and better job matching", "Structural unemployment falls", "Labour productivity rises", "LRAS shifts right", "Higher output and real wages"])),
      B.fig(5, "Evaluating labour market policy", B.table(["Strength", "Limitation"], [["Raises productivity and participation", "Skills programs are slow"], ["Protects low-paid workers", "Wage floors may cost jobs"], ["Cuts structural unemployment", "Compliance and pay-gap costs"]])),
      B.tools([("glance", "Latest labour market data"), ("macro", "Draw AD/AS and LRAS shifts"), ("policy", "Test the policy mix"), ("chain", "Build cause-and-effect chains"),
               ("qf", "Past HSC questions on labour policy"), ("mcq", "Section I questions with explanations"), ("ef", "Find evidence on the labour market"), ("map", "See how topics connect")]),
    ]
    B.build("labour-market-policies", c, cd, text, figs, "")
