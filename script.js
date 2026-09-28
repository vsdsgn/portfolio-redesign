document.documentElement.classList.add("js");
const cases={
"kinopoisk-growth":{
slug:"kinopoisk-growth",cls:"kino",no:"01",name:"Kinopoisk Growth",
title:"Subscription experiments, published with their losses.",
stand:"Growth work around trial, onboarding, conversion, ARPU and retention — tested as hypotheses, including the ones that lost.",
metric:"+21%",metricLabel:"onboarding purchase conversion",
role:"Product / growth design inside Kinopoisk.",
situation:"The job was not to decorate a subscription screen. It was to change conversion without making the viewing product worse, and to treat every experiment as evidence rather than a story about success.",
decisions:[
["Explain the trial instead of hiding it.","A thermometer-like timeline showed what happens between starting a trial and being charged."],
["Tie the pattern to the offer.","When no trial came back, the interface fell back to benefits instead of showing a broken timeline."],
["Publish losses too.","The experiment ledger keeps losing and neutral results alongside wins."]
]},
emcd:{
slug:"emcd",cls:"emcd",no:"02",name:"EMCD",
title:"One contract for six design systems.",
stand:"A mining business with six drifting design-system lineages needed one practical migration plan without smuggling redesign into cleanup.",
metric:"15",metricLabel:"documented design-system decisions",
role:"Head of Product Designers · Mining BU.",
situation:"The audit showed the company did not have one design system in practice. It had a family of systems, forks and product-specific interpretations.",
decisions:[
["Production is the source of truth.","Internal forks can contain ideas, but the real product validates the contract."],
["Separate cleanup from redesign.","Naming, aliases and parity move first. Visual evolution is a separate opt-in track."],
["Design the migration, not just the library.","The output is a plan products can actually adopt, not a prettier Figma file."]
]},
jetable:{
slug:"jetable",cls:"jetable",no:"03",name:"Jetable",
title:"A booking marketplace, from a note to launch.",
stand:"Guest app, staff app and web booking — built as one marketplace instead of SaaS for venues.",
metric:"6",metricLabel:"venues booking live",
role:"Co-founder · product, design and business model.",
situation:"Booking a table still mostly means calling. The product had to make demand useful for guests while giving venues a workable operating surface.",
decisions:[
["Build an ecosystem, not venue SaaS.","Guest demand is the asset. The business model follows bookings that originate in the product."],
["List non-partners honestly.","An empty map loses guests. Non-partners stay visible with a clear cannot-book state."],
["Put acquisition on the table.","QR codes on tables and doors connect offline traffic to measurable venue-level acquisition."]
]},
outfitme:{
slug:"outfitme",cls:"outfitme",no:"04",name:"OutfitMe",
title:"The AI is an enhancement, never a gate.",
stand:"A solo AI-native wardrobe and outfit builder, from photo ingestion to taxonomy and try-on flows.",
metric:"2 days",metricLabel:"plan to shipped feature, solo",
role:"Solo product, design and build.",
situation:"The product had to feel immediate even when AI services were slow or imperfect. The system therefore treats enrichment as optional after the core save action.",
decisions:[
["Save first, enhance later.","An item lands in the wardrobe immediately; background removal and tagging happen afterwards."],
["Degrade, do not fail.","If enhancement fails, the original photo remains useful."],
["Constrain the model.","A deliberate taxonomy turns AI output into product data instead of free-form guesses."]
]}
};
const order=["kinopoisk-growth","emcd","jetable","outfitme"];
function motif(slug){
 if(slug==="kinopoisk-growth") return '<svg viewBox="0 0 320 460" fill="none"><rect x="140" y="20" width="40" height="380" rx="20" fill="currentColor" opacity=".22"/><rect x="150" y="210" width="20" height="190" rx="10" fill="currentColor" opacity=".5"/><circle cx="160" cy="400" r="34" fill="currentColor" opacity=".5"/><path d="M50 80h70M50 150h70M50 220h70M200 120h70M200 190h70M200 260h70" stroke="currentColor" stroke-width="3" opacity=".45"/></svg>';
 if(slug==="emcd") return '<svg viewBox="0 0 360 360" fill="none"><g stroke="currentColor" stroke-width="3" opacity=".5"><path d="M45 45L180 180 315 45M45 180h270M45 315l135-135 135 135"/></g><g fill="currentColor"><rect x="25" y="25" width="40" height="40"/><rect x="295" y="25" width="40" height="40"/><rect x="25" y="160" width="40" height="40"/><rect x="295" y="160" width="40" height="40"/><rect x="25" y="295" width="40" height="40"/><rect x="295" y="295" width="40" height="40"/><circle cx="180" cy="180" r="38"/></g></svg>';
 if(slug==="jetable") return '<svg viewBox="0 0 360 420" fill="none"><rect x="20" y="70" width="170" height="250" stroke="currentColor" stroke-width="4"/><rect x="95" y="110" width="170" height="250" stroke="currentColor" stroke-width="4"/><rect x="170" y="40" width="170" height="250" stroke="currentColor" stroke-width="4"/><path d="M260 145c0 42-48 65-48 108 0-43-48-66-48-108a48 48 0 1 1 96 0z" fill="currentColor"/></svg>';
 return '<svg viewBox="0 0 320 360" fill="currentColor">'+Array.from({length:42},(_,i)=>{const x=(i%6)*48+8,y=Math.floor(i/6)*48+8,o=i===20?1:.22;return '<rect x="'+x+'" y="'+y+'" width="38" height="38" opacity="'+o+'"/>';}).join("")+'</svg>';
}
function chapter(c){
 return '<section class="case-chapter '+c.cls+' reveal" id="'+c.slug+'"><div class="motif">'+motif(c.slug)+'</div><div class="case-copy"><div class="case-no">'+c.no+' · '+c.name+'</div><h2 class="case-title">'+c.title+'</h2><p class="case-stand">'+c.stand+'</p><div class="case-grid"><div class="decisions">'+c.decisions.slice(0,3).map(d=>'<div class="decision"><b>'+d[0]+'</b><span>'+d[1]+'</span></div>').join("")+'</div><div><div class="metric">'+c.metric+'</div><div class="metric-label">'+c.metricLabel+'</div></div></div><a class="chapter-link" href="/work/'+c.slug+'">Open case ↗</a></div></section>';
}
function renderHome(){
 const main=document.querySelector("#main");
 main.innerHTML=
 '<section class="hero"><div><div class="eyebrow">Stephane Vasadze · Product / Design / Growth</div></div><h1>Growth experiments. Design systems. Marketplaces. AI products.</h1><div><p class="hero-sub">I move from ambiguity to shipped systems.</p><nav class="index-strip" aria-label="Case studies">'+order.map(s=>{const c=cases[s];return '<a href="#'+s+'"><span class="case-no">'+c.no+'</span><br>'+c.name+'</a>';}).join("")+'</nav></div></section>'+
 order.map(s=>chapter(cases[s])).join("")+
 '<section class="close reveal"><div class="section-label">Stephane Vasadze</div><h2>Four cases. One operator.</h2><p>Growth, systems, marketplaces and AI products — the context changes, the operating principle does not: find the constraint, make the smallest useful move, ship what survives contact with reality.</p><div class="meta">Product · Design · Growth</div></section>';
}
function evidence(slug){
 return '<div class="evidence">'+motif(slug)+'<div class="evidence-caption">System diagram · abstracted from case logic</div></div>';
}
function renderCase(slug){
 const c=cases[slug],i=order.indexOf(slug),next=cases[order[(i+1)%order.length]];
 document.querySelector("#main").innerHTML=
 '<header class="case-hero '+c.cls+'"><div class="motif">'+motif(slug)+'</div><div class="case-copy"><div class="case-no">'+c.no+' · '+c.name+'</div><h1>'+c.title+'</h1><p>'+c.stand+'</p><div class="metric">'+c.metric+'</div><div class="metric-label" style="text-align:left">'+c.metricLabel+'</div></div></header>'+
 '<div class="case-main"><section class="case-section reveal"><div class="section-label">Situation</div><h2>What had to change</h2><p>'+c.situation+'</p></section>'+
 '<section class="case-section reveal"><div class="section-label">Role / Scope</div><h2>Ownership</h2><p>'+c.role+'</p></section>'+
 '<section class="case-section reveal"><div class="section-label">Decisions</div><h2>The calls that shaped it</h2><div class="case-decisions">'+c.decisions.map((d,n)=>'<article><div class="case-no">'+String(n+1).padStart(2,"0")+'</div><h3>'+d[0]+'</h3><p>'+d[1]+'</p></article>').join("")+'</div></section>'+
 '<section class="case-section reveal"><div class="section-label">Evidence</div><h2>The system behind the screen</h2>'+evidence(slug)+'</section>'+
 '<section class="case-section reveal"><div class="section-label">Outcome</div><div class="metric" style="text-align:left">'+c.metric+'</div><div class="metric-label" style="text-align:left">'+c.metricLabel+'</div></section></div>'+
 '<a class="next-case '+next.cls+'" href="/work/'+next.slug+'"><span>Next case</span><strong>'+next.name+'</strong></a>';
}
if(document.body.dataset.page==="home") renderHome(); else renderCase(document.body.dataset.case);
const io=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add("is-in")}),{threshold:.12});
document.querySelectorAll(".reveal").forEach(el=>io.observe(el));
