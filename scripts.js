script.js
const API_BASE = 'http://127.0.0.1:5000';

async function getFormData(){
  return {
    name: document.getElementById('name').value,
    age: document.getElementById('age').value,
    gender: document.getElementById('gender').value,
    weight: document.getElementById('weight').value,
    height: document.getElementById('height').value,
    activity_level: document.getElementById('activity_level').value,
    medical_history: document.getElementById('medical_history').value,
    goal: document.getElementById('goal').value
  }
}

async function showRecommendation(){
  const data = await getFormData();
  const res = await fetch(API_BASE + '/api/recommend', {
    method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data)
  });
  const json = await res.json();
  renderResult(json);
}

function renderResult(data){
  const el = document.getElementById('result');
  el.innerHTML = '';
  const header = document.createElement('h3'); header.textContent = 'Recommendation'; el.appendChild(header);

  const info = document.createElement('div'); info.className='result-section';
  info.innerHTML = `<strong>BMI:</strong> ${data.bmi} <br/><strong>Risk:</strong> ${data.risk}`;
  el.appendChild(info);

  const workout = document.createElement('div'); workout.className='result-section'; workout.innerHTML = `<strong>Workout:</strong> ${data.workout}`; el.appendChild(workout);

  const diet = document.createElement('div'); diet.className='result-section';
  diet.innerHTML = '<strong>Diet:</strong><br/>' + Object.entries(data.diet).map(([k,v])=>`<div><b>${k}:</b> ${v}</div>`).join('');
  el.appendChild(diet);

  const timeframe = document.createElement('div'); timeframe.className='result-section'; timeframe.innerHTML = `<strong>Timeframe:</strong> ${data.timeframe}`; el.appendChild(timeframe);

  const plan = document.createElement('div'); plan.className='result-section';
  plan.innerHTML = `<strong>Daily plan (Week 1 sample):</strong><br/><pre class='pre'>${JSON.stringify(data.daily_plan['Week 1'], null, 2)}</pre>`;
  el.appendChild(plan);
}

async function downloadPdf(){
  const data = await getFormData();
  const res = await fetch(API_BASE + '/api/report', {
    method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(data)
  });
  const blob = await res.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a'); a.href = url; a.download = 'Health_Fitness_Report.pdf'; document.body.appendChild(a); a.click(); a.remove();
}

document.getElementById('getRec').addEventListener('click', showRecommendation);
document.getElementById('downloadPdf').addEventListener('click', downloadPdf);