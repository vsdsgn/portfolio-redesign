document.documentElement.classList.add("js");
const revealObserver=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add("is-in")}),{threshold:.12});
document.querySelectorAll("[data-reveal],.project,.build-card,.ownership-line>div").forEach(el=>revealObserver.observe(el));
const answers={
"90":"Stephane works across four levels of ownership: growth experiments inside Kinopoisk, platform and team systems at EMCD, a marketplace as Jetable co-founder, and solo AI products like OutfitMe. The throughline is the same: find the constraint, make the decision explicit, ship, measure.",
"growth":"At Kinopoisk, Stephane worked on subscription growth through trial and onboarding experiments measured against conversion, ARPU and retention. One onboarding change produced +21% purchase conversion. The case keeps wins and losses in the same experiment story.",
"founder":"Jetable is the founder case: a hospitality booking marketplace with a guest app, staff app and web booking. The product is built around shared reservation logic, 15-minute slots, 90-minute table cycles and an acquisition loop that starts from venues themselves.",
"emcd":"At EMCD, Stephane is Head of Product Designers for the Mining BU. The design-system work starts from six co-existing lineages, audits what actually ships, treats production as the source of truth, and separates cleanup from redesign. The work is captured as 15 documented system decisions.",
"ai":"OutfitMe is the clearest solo-builder example: an AI-native wardrobe and outfit product where the core save action never waits on the model. Enhancement is asynchronous, failed cut-outs keep the original image, and taxonomy constrains AI output. Stephane also builds internal design tooling and synthetic-user workflows."
};
const overlay=document.querySelector(".ask-overlay");
const input=document.querySelector("#ask-input");
const answer=document.querySelector("#ask-answer");
function openAsk(){if(!overlay)return;overlay.hidden=false;overlay.setAttribute("aria-hidden","false");setTimeout(()=>input&&input.focus(),40)}
function closeAsk(){if(!overlay)return;overlay.hidden=true;overlay.setAttribute("aria-hidden","true")}
document.querySelectorAll("[data-open-ask]").forEach(b=>b.addEventListener("click",()=>{openAsk();const q=b.dataset.prefill;if(q){if(input)input.value=b.textContent.replace(/^→\s*/,"");answerQuestion(q)}}));
document.querySelectorAll("[data-close-ask]").forEach(b=>b.addEventListener("click",closeAsk));
if(overlay)overlay.addEventListener("click",e=>{if(e.target===overlay)closeAsk()});
document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==="k"){e.preventDefault();openAsk()}if(e.key==="Escape")closeAsk()});
function answerQuestion(q){
 const t=(q||"").toLowerCase();let key="90";
 if(/growth|kino|conversion|experiment/.test(t))key="growth";
 else if(/founder|jetable|marketplace|restaurant/.test(t))key="founder";
 else if(/emcd|system|lead|team/.test(t))key="emcd";
 else if(/ai|builder|outfit|solo|build/.test(t))key="ai";
 const titles={90:"The short version",growth:"Growth work",founder:"Founder work",emcd:"EMCD ownership",ai:"AI / builder work"};
 if(answer)answer.innerHTML="<strong>"+titles[key]+"</strong><br>"+answers[key];
}
document.querySelectorAll("[data-q]").forEach(b=>b.addEventListener("click",()=>{const k=b.dataset.q;if(input)input.value=b.textContent;answerQuestion(k)}));
if(input)input.addEventListener("keydown",e=>{if(e.key==="Enter")answerQuestion(input.value)});
