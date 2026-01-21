/**
 * NeetCode 150 進度追蹤器
 * 使用 localStorage 儲存用戶完成的題目
 */

(function() {
  'use strict';

  const STORAGE_KEY = 'neetcode_progress';

  // 載入進度
  function loadProgress() {
    try {
      const data = localStorage.getItem(STORAGE_KEY);
      return data ? JSON.parse(data) : {};
    } catch (e) {
      console.error('無法載入進度:', e);
      return {};
    }
  }

  // 儲存進度
  function saveProgress(progress) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
    } catch (e) {
      console.error('無法儲存進度:', e);
    }
  }

  // 取得當前頁面的題目 ID
  function getCurrentProblemId() {
    const path = window.location.pathname;
    const match = path.match(/(\d+_[^/]+)\/(\d+_[^/]+?)(?:\.html)?$/);
    if (match) {
      return `${match[1]}/${match[2]}`;
    }
    return null;
  }

  // 創建完成按鈕
  function createCompletionButton() {
    const problemId = getCurrentProblemId();
    if (!problemId) return;

    const progress = loadProgress();
    const isCompleted = progress[problemId] === true;

    const button = document.createElement('button');
    button.id = 'completion-toggle';
    button.className = 'completion-btn' + (isCompleted ? ' completed' : '');
    button.innerHTML = isCompleted ? '✅ 已完成' : '☐ 標記完成';
    button.title = '點擊標記此題為已完成';
    
    button.onclick = function() {
      const progress = loadProgress();
      const newState = !progress[problemId];
      progress[problemId] = newState;
      saveProgress(progress);
      
      button.className = 'completion-btn' + (newState ? ' completed' : '');
      button.innerHTML = newState ? '✅ 已完成' : '☐ 標記完成';
      
      updateProgressStats();
    };

    // 插入到標題後面
    const h1 = document.querySelector('article h1');
    if (h1) {
      h1.parentNode.insertBefore(button, h1.nextSibling);
    }
  }

  // 更新進度統計
  function updateProgressStats() {
    const progress = loadProgress();
    const completed = Object.values(progress).filter(v => v === true).length;
    const total = 150;
    
    // 更新首頁進度 (如果在首頁)
    const progressElement = document.getElementById('user-progress');
    if (progressElement) {
      progressElement.innerHTML = `<strong>📊 你的進度: ${completed}/${total}</strong> (${(completed/total*100).toFixed(1)}%)`;
    }
  }

  // 初始化
  function init() {
    // 等待 DOM 載入完成
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
      return;
    }

    createCompletionButton();
    updateProgressStats();
  }

  init();
})();
