'use strict';

// All observations below are intentionally fictional. No remote resources are used.
const technologies = [
  {id:'jepa',name:'JEPA',category:'research',tag:'표현 학습',description:'픽셀 대신 의미 있는 표현을 예측하는 학습. 물리 세계의 이해로 연결될 수 있을까요?',change:'가려진 이미지 표현을 예측하는 설정을 영상의 시간적 변화로 확장한 예시입니다.',difference:'픽셀을 복원하는 생성 방식과 달리, 잠재 표현 사이의 예측에 초점을 둡니다.',papers:84,community:36,institutes:12,code:'예제 코드 공개',model:'일부 가중치 공개',uncertainty:'표현 예측의 개선이 실제 로봇 제어 성능으로 이어지는지는 별도 검증이 필요합니다.',published:'2026.09.21',observed:'2026.09.23',evidence:'Temporal Representations for Physical Interaction',finding:'고정된 실내 영상에서 잠재 표현 예측 오차가 줄어든 상황을 가정합니다. 로봇 제어 실험은 포함하지 않았습니다.',series:[18,23,21,32,39,45,58,61,72,84],discussion:[9,12,10,18,17,23,21,29,30,36],x:175,y:125},
  {id:'world',name:'World Models',category:'research',tag:'환경 모델',description:'행동의 결과를 미리 상상하는 모델. 계획과 제어 사이의 연결을 관찰합니다.',change:'관찰 영상만으로 다음 장면을 생성하던 설정에 행동 조건을 추가한 예시입니다.',difference:'즉시 행동을 출력하는 정책과 달리, 환경의 변화를 모델링하고 후보 행동을 비교합니다.',papers:112,community:64,institutes:18,code:'연구용 코드 공개',model:'제한적 공개',uncertainty:'긴 시간 범위에서 예측 오차가 누적되며, 실제 환경의 접촉과 마찰을 재현하기 어렵습니다.',published:'2026.09.28',observed:'2026.09.29',evidence:'Action-Conditioned Worlds for Tabletop Planning',finding:'테이블 위 단순 물체 이동 과제에서 짧은 계획 구간을 비교하는 예시입니다. 장기 계획으로 일반화할 수 없습니다.',series:[27,32,44,41,56,64,73,80,96,112],discussion:[15,19,21,28,26,37,44,46,58,64],x:395,y:100},
  {id:'vla',name:'VLA',category:'growth',tag:'시각 · 언어 · 행동',description:'보고, 지시를 이해하고, 행동하는 모델. 서로 다른 로봇으로의 확장이 관찰 지점입니다.',change:'하나의 로봇에 맞춘 학습에서 여러 형태의 로봇 데이터를 함께 활용하는 설정으로 바뀐 예시입니다.',difference:'언어 이해와 제어 정책을 분리하는 구성 대신, 시각·언어·행동을 연결해 학습합니다.',papers:96,community:81,institutes:15,code:'평가 코드 공개',model:'예제 가중치 공개',uncertainty:'데이터 구성과 로봇 형태가 달라지면 성능 비교가 어렵습니다. 새로운 작업의 성공은 보장되지 않습니다.',published:'2026.10.02',observed:'2026.10.03',evidence:'Cross-Embodiment Instruction Following',finding:'두 종류의 로봇 팔에서 정해진 지시 집합을 평가한 예시입니다. 학습에 없는 환경은 평가하지 않았습니다.',series:[11,19,25,38,42,57,62,74,83,96],discussion:[10,17,20,33,41,46,59,67,73,81],x:600,y:195},
  {id:'sim',name:'Sim-to-Real',category:'growth',tag:'전이 학습',description:'시뮬레이션의 경험을 실제 로봇으로. 환경 차이를 줄이는 방법을 살펴봅니다.',change:'일괄적인 무작위 환경 생성 대신, 실제 관찰에 따라 시뮬레이션 조건을 조정하는 예시입니다.',difference:'실제 환경 데이터만으로 정책을 학습하는 방식보다 시뮬레이션 경험을 적극 활용합니다.',papers:68,community:27,institutes:11,code:'시뮬레이션 코드 공개',model:'가중치 미공개',uncertainty:'센서 오차와 재질 차이, 하드웨어 지연의 영향은 여전히 남아 있습니다.',published:'2026.09.17',observed:'2026.09.19',evidence:'Adaptive Domain Randomization for Contact Tasks',finding:'단일 그리퍼의 물체 집기 과제에서 재질 변화에 따른 성공률을 비교하는 예시입니다.',series:[24,28,30,39,41,43,50,54,61,68],discussion:[8,10,9,13,17,16,20,21,24,27],x:410,y:345},
  {id:'diffusion',name:'Diffusion Policy',category:'community',tag:'행동 생성',description:'여러 가능한 움직임을 생성하는 정책. 재현 실험과 추론 지연 논의가 이어집니다.',change:'다단계 행동 생성의 반복 횟수를 줄이면서 제어 안정성을 유지하려는 설정입니다.',difference:'단일 행동을 직접 회귀하는 정책과 달리, 잡음 제거 과정을 통해 행동 시퀀스를 생성합니다.',papers:73,community:94,institutes:10,code:'재현 예제 공개',model:'실험 가중치 공개',uncertainty:'추론 속도와 행동 다양성 사이의 절충이 있습니다. 커뮤니티 논의량은 성능 지표가 아닙니다.',published:'2026.10.05',observed:'2026.10.06',evidence:'Few-Step Diffusion for Closed-Loop Manipulation',finding:'고정된 GPU와 제어 주기에서 행동 생성 지연을 비교하는 예시입니다. 다른 하드웨어에는 직접 적용할 수 없습니다.',series:[25,28,33,38,44,43,51,58,64,73],discussion:[14,23,32,28,49,53,68,72,86,94],x:175,y:310},
  {id:'tactile',name:'Tactile Learning',category:'new',tag:'촉각 학습',description:'시각으로 놓친 접촉의 순간. 촉각과 시각을 함께 배우는 접근이 새 후보로 포착됐습니다.',change:'촉각 센서 신호를 단독으로 처리하는 대신 영상 표현과 정렬하는 설정입니다.',difference:'영상 중심 정책에 접촉 압력과 미끄러짐 정보를 추가합니다.',papers:29,community:21,institutes:4,code:'일부 코드 공개',model:'가중치 미공개',uncertainty:'독립 기관이 4곳으로 표본이 작습니다. 센서별 차이가 커 재현성과 확산 여부를 확인해야 합니다.',published:'2026.10.09',observed:'2026.10.12',evidence:'Aligned Touch and Vision for Delicate Grasping',finding:'한 종류의 촉각 센서로 부드러운 물체를 집는 설정의 예시입니다. 센서 간 전이는 확인하지 않았습니다.',series:[3,4,7,6,10,12,14,19,22,29],discussion:[2,3,4,7,8,10,11,14,18,21],x:645,y:365},
  {id:'latent',name:'Latent Action Models',category:'new',tag:'행동 표현',description:'행동 라벨이 없는 영상에서 움직임의 구조를 학습합니다. 기존 접근과의 차이를 검토할 후보입니다.',change:'영상 사이의 변화를 잠재 행동으로 압축하고, 소량의 로봇 데이터와 연결하는 예시입니다.',difference:'명시적인 행동 라벨에 의존하는 모방 학습보다 라벨 없는 영상을 더 많이 활용합니다.',papers:18,community:15,institutes:3,code:'설계 예제 공개',model:'미공개',uncertainty:'잠재 행동이 실제 로봇 명령과 안정적으로 대응하는지 확인되지 않았습니다. 이름이 새롭다고 새 기술은 아닙니다.',published:'2026.10.11',observed:'2026.10.14',evidence:'Learning Action Tokens from Unlabeled Motion',finding:'제한된 카메라 시점에서 움직임을 압축하는 예시입니다. 실제 로봇 제어의 개선을 뜻하지 않습니다.',series:[2,3,3,5,7,8,10,12,15,18],discussion:[1,2,2,4,3,6,8,10,12,15],x:380,y:230},
  {id:'robot',name:'Robot Learning',category:'community',tag:'로봇 학습',description:'현실의 실패 사례와 재현 기록. 데이터 품질과 평가 기준에 대한 커뮤니티의 질문을 모았습니다.',change:'성공 사례 중심의 평가에서 실패 유형과 재현 조건을 함께 기록하는 설정입니다.',difference:'특정 알고리즘 한 개가 아닌, 로봇의 경험 기반 학습을 다루는 상위 연구 분야입니다.',papers:148,community:106,institutes:24,code:'공통 평가 예제 공개',model:'해당 없음 · 연구 분야',uncertainty:'서로 다른 과제와 로봇의 결과를 단순 합산해 성능이나 기술 우위를 판단할 수 없습니다.',published:'2026.09.14',observed:'2026.09.16',evidence:'Failure-Centered Evaluation of Learned Manipulation',finding:'실패 유형을 분류하는 평가 절차의 예시입니다. 모든 로봇이나 실제 산업 환경을 대표하지 않습니다.',series:[60,65,78,80,95,104,110,125,136,148],discussion:[35,41,48,57,59,71,78,86,99,106],x:790,y:105}
];
// Keep the 10 chart buckets consistent with the 30-day totals on the cards.
function distribute(total, weights) {
  const sum = weights.reduce((a,b)=>a+b,0);
  const values = weights.map(value=>Math.floor(value/sum*total));
  let remaining = total-values.reduce((a,b)=>a+b,0);
  for(let i=values.length-1;remaining>0;i=(i-1+values.length)%values.length,remaining--) values[i]++;
  return values;
}
technologies.forEach(t=>{t.series=distribute(t.papers,t.series);t.discussion=distribute(t.community,t.discussion);});
const groups = [
  {id:'research',title:'현재 연구 관심',subtitle:'논문 흐름에서 읽는 지금의 질문',number:'01'},
  {id:'new',title:'새 기술 후보',subtitle:'새롭게 포착 · 신규성은 검토 중',number:'02'},
  {id:'growth',title:'향후 성장 관찰 후보',subtitle:'확산 근거를 더 확인할 기술',number:'03'},
  {id:'community',title:'커뮤니티 논의',subtitle:'관심의 크기와 연구 성과는 별개',number:'04'}
];
const $ = selector => document.querySelector(selector);
const content = $('#content');
const dialog = $('#detail');
const storageKey = 'fieldnote-saved-v1';
let saved = new Set();
let storageAvailable = true;
try { const value = JSON.parse(localStorage.getItem(storageKey) || '[]'); if (Array.isArray(value)) saved = new Set(value.filter(id => technologies.some(t => t.id === id))); } catch { storageAvailable = false; }
let tab = 'summary', filter = 'all', query = '', selected = null, previousFocus = null;
const graph = {zoom:1, x:0, y:0, tech:true, company:true, correlation:false};
function announce(message) { $('#announcement').textContent = message; }
function updateCount() { $('#saved-count').textContent = saved.size; }
function toggleSave(id) {
  saved.has(id) ? saved.delete(id) : saved.add(id);
  try { localStorage.setItem(storageKey, JSON.stringify([...saved])); } catch { storageAvailable = false; }
  updateCount();
  const focusedSave = !dialog.open && document.activeElement?.dataset?.save === id;
  if (tab !== 'graph') render();
  if (focusedSave) {
    const target=document.querySelector(`[data-save="${id}"]`) || document.querySelector(`[data-tab="${tab}"]`);
    target.focus();
  }
  if (selected) updateDetailSave();
  announce(`${technologies.find(t=>t.id===id).name} ${saved.has(id)?'관심 목록에 저장했습니다.':'관심 목록에서 해제했습니다.'}${storageAvailable?'':' 이 브라우저에서는 영구 저장이 제한되어 현재 화면에서만 유지됩니다.'}`);
}
function points(values,width=100,height=30,pad=2) { const max=Math.max(...values,1); return values.map((v,i)=>`${pad+i*(width-pad*2)/(values.length-1)},${height-pad-v/max*(height-pad*2)}`).join(' '); }
function card(t,index) {
  return `<article class="card"><div class="card-header"><span class="tag">${t.tag}</span><span class="card-index">FIELD / ${String(index+1).padStart(2,'0')}</span></div><h3 class="card-title"><button class="card-open" data-open="${t.id}" aria-label="${t.name} 상세 보기">${t.name} <span aria-hidden="true" class="muted">↗</span></button></h3><p class="card-description">${t.description}</p><div class="card-bottom"><div class="metric"><strong>${t.papers}</strong> 논문 <span class="muted">/ 30일</span><br><span>독립 기관 ${t.institutes}곳${t.institutes<5?' · 표본 적음':''}</span></div><svg class="sparkline" viewBox="0 0 100 30" aria-label="${t.name} 예시 논문 추이" role="img"><polyline points="${points(t.series)}" fill="none" stroke="#177b70" stroke-width="1.8"/></svg><button class="save-small" data-save="${t.id}" aria-label="${t.name} 관심 ${saved.has(t.id)?'해제':'저장'}" aria-pressed="${saved.has(t.id)}">${saved.has(t.id)?'★':'☆'}</button></div><div class="card-meta">커뮤니티 ${t.community}개 원문 · 포착 ${t.observed}</div></article>`;
}
function matches(t) { return (filter==='all'||t.category===filter)&&`${t.name} ${t.tag} ${t.description}`.toLocaleLowerCase().includes(query.toLocaleLowerCase()); }
function render() {
  updateCount();
  if(tab==='graph') { renderGraph(); return; }
  const list = technologies.filter(t=>matches(t)&&(tab!=='saved'||saved.has(t.id)));
  if(!list.length) {
    content.innerHTML=`<section class="empty"><p class="eyebrow">A LITTLE ROOM FOR DISCOVERY</p><h2>${tab==='saved'&&saved.size===0?'관심 기술을 모아보세요.':'일치하는 기술이 없습니다.'}</h2><p>${tab==='saved'&&saved.size===0?'기술 카드의 ☆ 또는 상세 화면의 관심 저장을 눌러보세요.':'검색어를 바꾸거나 분류 필터를 전체로 설정해보세요.'}</p><button id="clear-search">${tab==='saved'&&saved.size===0?'오늘의 레이더 보기':'검색 · 필터 초기화'}</button></section>`;
    return;
  }
  content.innerHTML = (tab==='saved'?`<p class="saved-intro">관심 기술 ${saved.size}개${storageAvailable?' · 이 브라우저에 저장됩니다.':' · 브라우저 저장이 제한되어 현재 화면에서만 유지됩니다.'}</p>`:'') + groups.map(group=>{
    const items=list.filter(t=>t.category===group.id);
    return items.length?`<section class="section"><div class="section-heading"><h2><span class="section-number">${group.number}</span>${group.title}</h2><span class="section-subtitle">${group.subtitle}</span></div><div class="grid">${items.map(t=>card(t,technologies.indexOf(t))).join('')}</div></section>`:'';
  }).join('') + (tab==='summary'?'<p class="summary-note">관찰 포인트 &nbsp; 촉각과 행동 표현에서 작은 신호가 보입니다. 독립 기관 수와 재현 조건을 먼저 확인해보세요.</p>':'');
}
function setTab(next) {
  tab=next;
  document.querySelectorAll('[data-tab]').forEach(b=>{b.classList.toggle('active',b.dataset.tab===tab); if(b.dataset.tab===tab)b.setAttribute('aria-current','page');else b.removeAttribute('aria-current');});
  $('#page-title').textContent=tab==='graph'?'기술은 서로 연결됩니다.':tab==='saved'?'계속 지켜볼 질문들.':'다음 움직임의 단서.';
  $('#page-description').textContent=tab==='graph'?'연구 접근의 관계를 따라가며 각 기술의 위치를 살펴보세요.':tab==='saved'?'다시 살펴보고 싶은 기술을 나만의 관측 목록에 모았습니다.':'Physical AI의 연구 흐름부터 새롭게 등장한 질문까지, 한눈에 살펴보세요.';
  render();
}
function trend(t) {
  const max=Math.ceil(Math.max(...t.series,...t.discussion)/20)*20;
  const line=values=>values.map((v,i)=>`${45+i*430/(values.length-1)},${175-v/max*145}`).join(' ');
  return `<div class="chart-legend"><span>━━ 논문 수</span><span>┄┄ 커뮤니티 원문 수</span></div><svg class="chart" viewBox="0 0 510 210" role="img" aria-label="최근 30일을 10개 구간으로 나눈 논문 및 커뮤니티 원문 수 추이. 30일 합계 논문 ${t.papers}건, 커뮤니티 ${t.community}건. 두 지표는 별도 집계입니다.">${[0,.5,1].map(r=>`<line x1="45" y1="${175-r*145}" x2="475" y2="${175-r*145}" stroke="#e4eae4"/><text x="32" y="${179-r*145}" text-anchor="end" fill="#6f7d82" font-size="10">${max*r}</text>`).join('')}<polyline points="${line(t.series)}" fill="none" stroke="#177b70" stroke-width="2.5"/><polyline points="${line(t.discussion)}" fill="none" stroke="#a3764d" stroke-width="2" stroke-dasharray="5 4"/><text x="45" y="199" font-size="10" fill="#6f7d82">09.19</text><text x="475" y="199" text-anchor="end" font-size="10" fill="#6f7d82">10.18</text></svg><p class="chart-label"><span>최근 30일 · 10개 구간별 건수</span><span>예시 데이터 · 합산 점수 없음</span></p>`;
}
function openDetail(id) {
  const t=technologies.find(t=>t.id===id); if(!t)return;
  selected=id;previousFocus=document.activeElement;
  $('#detail-body').innerHTML=`<p class="tag" style="margin-top:24px">${t.tag}</p><h2 id="detail-title">${t.name}</h2><p class="detail-lead">${t.description}</p><button id="detail-save" class="detail-save" data-save="${t.id}"></button><div class="facts"><div class="fact"><span>독립 연구 기관</span>${t.institutes}곳${t.institutes<5?' · 표본 적음':''}</div><div class="fact"><span>관찰 분류</span>${groups.find(g=>g.id===t.category).title}</div><div class="fact"><span>공개일 · 예시</span>${t.published}</div><div class="fact"><span>최초 포착일 · 예시</span>${t.observed}</div></div><section class="detail-section"><h3>무엇이 새로 달라졌나요?</h3><p>${t.change}</p><h3>이전 접근과의 차이</h3><p>${t.difference}</p></section><section class="detail-section"><h3>연구 관심 추이</h3>${trend(t)}<p>논문과 커뮤니티 원문은 별도로 집계합니다. 커뮤니티 논의량은 연구 성과나 기술 성공 가능성을 뜻하지 않습니다.</p></section><section class="detail-section"><h3>대표 근거</h3><article class="evidence"><span class="tag">예시 논문 · 가상 연구</span><h3 style="margin-top:10px">${t.evidence}</h3><p>${t.finding}</p><p>실제 출처가 없는 설명용 요약입니다.</p></article></section><section class="detail-section"><h3>코드 · 모델 상태</h3><div class="facts"><div class="fact"><span>코드</span>${t.code}</div><div class="fact"><span>모델</span>${t.model}</div></div><p>공개 상태 역시 예시입니다. 다운로드할 실제 코드나 모델은 연결하지 않았습니다.</p></section><section class="detail-section"><h3>아직 확인할 것</h3><div class="uncertainty">${t.uncertainty}</div></section><details class="disclosure"><summary>기업 · 주가 보조 정보 <span class="muted">(더미)</span></summary><p>아래 가상 기업은 화면 탐색용 연결입니다. 기술 보유나 상용화의 근거가 아닙니다.</p><div class="stock-row"><span>Orion Robotics · 가상 기업</span><strong>$128.40 <span class="muted">+1.2%</span></strong></div><div class="stock-row"><span>Atlas Compute · 가상 기업</span><strong>$84.60 <span class="muted">−0.7%</span></strong></div><p>예시 종가 · 2026.10.16 · USD · 실제 거래소 없음. 수익률 예측이 아닙니다.</p></details>`;
  updateDetailSave();
  if(!dialog.open)dialog.showModal();
  dialog.scrollTop=0;$('#close-detail').focus();
}
function updateDetailSave(){const button=$('#detail-save');if(!button)return;button.textContent=saved.has(selected)?'★ 관심 저장됨':'☆ 관심 저장';button.setAttribute('aria-pressed',String(saved.has(selected)));}
function closeDetail(){dialog.close();}
dialog.addEventListener('close',()=>{selected=null;if(previousFocus?.isConnected)previousFocus.focus();else document.querySelector(`[data-tab="${tab}"]`).focus();});
$('#close-detail').addEventListener('click',closeDetail);
dialog.addEventListener('click',event=>{if(event.target===dialog){const rect=dialog.getBoundingClientRect();if(event.clientX<rect.left||event.clientX>rect.right)closeDetail();}});
document.addEventListener('click',event=>{
  const save=event.target.closest('[data-save]');if(save){toggleSave(save.dataset.save);return;}
  const open=event.target.closest('[data-open]');if(open){openDetail(open.dataset.open);return;}
  const nav=event.target.closest('[data-tab]');if(nav){setTab(nav.dataset.tab);return;}
  const choice=event.target.closest('[data-filter]');if(choice){filter=choice.dataset.filter;updateFilters();render();return;}
  if(event.target.closest('#clear-search')){query='';filter='all';$('#search').value='';updateFilters();if(tab==='saved'&&!saved.size)setTab('summary');else render();}
});
function updateFilters(){document.querySelectorAll('[data-filter]').forEach(b=>{b.classList.toggle('active',b.dataset.filter===filter);b.setAttribute('aria-pressed',String(b.dataset.filter===filter));});}
$('#search').addEventListener('input',event=>{query=event.target.value.trim();render();});

const relations=[['jepa','world','similar_to'],['world','vla','uses'],['vla','robot','is_a'],['sim','world','uses'],['diffusion','vla','combines_with'],['tactile','vla','combines_with'],['latent','jepa','similar_to'],['latent','vla','uses'],['sim','robot','is_a']];
const companies=[{id:'orion',name:'Orion Robotics',x:800,y:300,tech:'vla'},{id:'atlas',name:'Atlas Compute',x:100,y:430,tech:'world'}];
function renderGraph(){
  content.innerHTML=`<div class="graph-header"><p>노드를 눌러 상세 보기 · 드래그로 이동 · 휠로 확대/축소</p><div class="graph-controls"><button id="zoom-out" aria-label="그래프 축소">−</button><output id="zoom-value" aria-live="polite"></output><button id="zoom-in" aria-label="그래프 확대">+</button><button id="zoom-reset">초기화</button></div></div><div class="layer-controls"><label><input id="layer-tech" type="checkbox" ${graph.tech?'checked':''}> 기술</label><label><input id="layer-company" type="checkbox" ${graph.company?'checked':''}> 기업</label><label><input id="layer-correlation" type="checkbox" ${graph.correlation?'checked':''}> 주가 상관</label></div><div class="graph-shell"><svg id="graph" class="graph-svg" viewBox="0 0 930 500" aria-label="기술 관계도. Tab으로 노드를 선택하고 Enter로 상세를 확인하세요." role="group"><g id="graph-scene"></g></svg></div><div class="graph-legend"><span>○ 기술</span><span>□ 가상 기업 · 120% 이상에서 표시</span><span><i class="legend-line"></i>기술 관계</span><span><i class="legend-line dashed"></i>기업 간 수익률 상관</span></div><p class="graph-note">is_a: 하위 분야 · uses: 활용 · combines_with: 결합 · similar_to: 유사 접근. 관계 방향은 화살표 기준이며 모두 예시입니다.</p><p id="graph-context" class="graph-note"></p>`;
  $('#zoom-in').onclick=()=>zoomBy(1.2);$('#zoom-out').onclick=()=>zoomBy(1/1.2);$('#zoom-reset').onclick=()=>{graph.zoom=1;graph.x=0;graph.y=0;drawGraph();};
  ['tech','company','correlation'].forEach(layer=>{$(`#layer-${layer}`).onchange=event=>{graph[layer]=event.target.checked;drawGraph();};});
  const svg=$('#graph');
  svg.addEventListener('wheel',event=>{event.preventDefault();zoomBy(event.deltaY<0?1.1:1/1.1);},{passive:false});
  let drag=null,moved=false;
  svg.addEventListener('pointerdown',event=>{if(event.button!==0||event.target.closest('[data-node]'))return;drag={x:event.clientX,y:event.clientY,px:graph.x,py:graph.y};moved=false;svg.setPointerCapture(event.pointerId);svg.classList.add('dragging');});
  svg.addEventListener('pointermove',event=>{if(!drag)return;const scale=930/svg.getBoundingClientRect().width;const dx=(event.clientX-drag.x)*scale,dy=(event.clientY-drag.y)*scale;moved=Math.abs(dx)+Math.abs(dy)>4;graph.x=drag.px+dx;graph.y=drag.py+dy;transformGraph();});
  const stop=()=>{drag=null;svg.classList.remove('dragging');};svg.addEventListener('pointerup',stop);svg.addEventListener('pointercancel',stop);
  svg.addEventListener('click',event=>{const node=event.target.closest('[data-node]');if(node&&!moved)openGraphNode(node.dataset.node);moved=false;});
  svg.addEventListener('keydown',event=>{const node=event.target.closest('[data-node]');if(node&&(event.key==='Enter'||event.key===' ')){event.preventDefault();openGraphNode(node.dataset.node);}});
  drawGraph();
}
function openGraphNode(id){const company=companies.find(c=>c.id===id);openDetail(company?company.tech:id);}
function zoomBy(factor){graph.zoom=Math.max(.6,Math.min(2.5,Math.round(graph.zoom*factor*100)/100));drawGraph();}
function transformGraph(){const scene=$('#graph-scene');if(scene)scene.setAttribute('transform',`translate(${465+graph.x} ${250+graph.y}) scale(${graph.zoom}) translate(-465 -250)`);}
function drawGraph(){
  const scene=$('#graph-scene');if(!scene)return;
  const visible=graph.tech?technologies.filter(matches):[];
  const ids=new Set(visible.map(t=>t.id));
  const showCompanies=graph.company&&graph.zoom>=1.2;
  const companyList=showCompanies?companies.filter(c=>(filter==='all'&&!query)||ids.has(c.tech)):[];
  const companyIds=new Set(companyList.map(c=>c.id));
  scene.innerHTML=`<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#a6bdb2"/></marker></defs>`+relations.filter(([a,b])=>ids.has(a)&&ids.has(b)).map(([a,b,label])=>{const p=technologies.find(t=>t.id===a),q=technologies.find(t=>t.id===b),d=Math.hypot(q.x-p.x,q.y-p.y),r=40;return `<line class="edge" x1="${p.x+(q.x-p.x)*r/d}" y1="${p.y+(q.y-p.y)*r/d}" x2="${q.x-(q.x-p.x)*r/d}" y2="${q.y-(q.y-p.y)*r/d}" marker-end="url(#arrow)"/><text class="edge-label" text-anchor="middle" x="${(p.x+q.x)/2}" y="${(p.y+q.y)/2-5}">${label}</text>`;}).join('')+companyList.map(c=>{const t=technologies.find(t=>t.id===c.tech);return ids.has(t.id)?`<line class="edge" x1="${c.x}" y1="${c.y}" x2="${t.x}" y2="${t.y}"/><text class="edge-label" x="${(c.x+t.x)/2}" y="${(c.y+t.y)/2}">연구 연결 예시</text>`:'';}).join('')+(graph.correlation&&companyIds.size===2?'<line class="correlation" x1="800" y1="300" x2="100" y2="430"/><text class="edge-label" x="450" y="380">r = 0.42 · 더미</text>':'')+visible.map(t=>`<g class="graph-node" data-node="${t.id}" tabindex="0" role="button" aria-label="${t.name} 상세 보기" transform="translate(${t.x} ${t.y})"><circle r="${t.id==='world'?42:32}"/><text text-anchor="middle" y="${t.id==='world'?61:51}">${t.name}</text><circle r="4" style="fill:#177b70;stroke:none"/></g>`).join('')+companyList.map(c=>`<g class="graph-node company" data-node="${c.id}" tabindex="0" role="button" aria-label="${c.name} 가상 기업, 연결 기술 상세 보기" transform="translate(${c.x} ${c.y})"><rect x="-55" y="-17" width="110" height="34" rx="3"/><text text-anchor="middle" y="4">${c.name}</text></g>`).join('')+(!visible.length&&!companyList.length?'<text x="465" y="230" text-anchor="middle" fill="#6f7d82" font-size="15">표시할 노드가 없습니다. 검색·필터 또는 레이어를 조정하세요.</text>':'');
  $('#zoom-value').textContent=`${Math.round(graph.zoom*100)}%`;
  $('#graph-context').textContent=graph.correlation?'상관은 가상 기업의 최근 120거래일 조정 종가 일간 수익률을 가정한 더미 값(r = 0.42)입니다. 기술 관계·인과관계·미래 수익률과 별개입니다. 두 기업이 표시될 때 점선이 나타납니다.':'기업은 120% 이상 확대하면 표시됩니다. 기업 노드는 연결 기술의 상세를 엽니다. 주가 상관 레이어는 기술 관계와 별도입니다.';
  transformGraph();
}
render();
