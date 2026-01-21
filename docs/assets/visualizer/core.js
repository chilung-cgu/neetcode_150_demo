class AlgorithmVisualizer {
  constructor(config) {
    this.steps = [];
    this.currStep = 0;
    this.isPlaying = false;
    this.autoPlayInterval = null;
    this.playSpeed = 1500; // 預設速度 1.5 秒
    this.config = Object.assign(
      {
        codeLines: [],
        onStepChange: () => {},
        parentId: "viz-container",
      },
      config,
    );

    this.initUI();
  }

  initUI() {
    // UI binding can be done here or in the HTML
    // For now, we assume controls are present in the HTML structure
    this.prevBtn = document.getElementById("prevBtn");
    this.nextBtn = document.getElementById("nextBtn");
    this.stepDisplay = document.getElementById("currentStep");
    this.totalStepsDisplay = document.getElementById("totalSteps");
    this.codeDisplay = document.getElementById("codeDisplay");
    this.explanationDisplay = document.getElementById("explanation");
    this.chartContainer = document.getElementById("chartContainer");

    if (this.prevBtn) this.prevBtn.onclick = () => this.prev();
    if (this.nextBtn) this.nextBtn.onclick = () => this.next();

    // Keyboard support
    document.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight" || e.key === " ") {
        e.preventDefault();
        this.next();
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        this.prev();
      }
    });

    this.renderCode();
  }

  setSteps(newSteps) {
    this.steps = newSteps;
    this.currStep = 0;
    if (this.totalStepsDisplay) {
      this.totalStepsDisplay.textContent = Math.max(0, this.steps.length - 1);
    }
    this.update();
  }

  next() {
    if (this.currStep < this.steps.length - 1) {
      this.currStep++;
      this.update();
    }
  }

  prev() {
    if (this.currStep > 0) {
      this.currStep--;
      this.update();
    }
  }

  update() {
    const step = this.steps[this.currStep];
    if (!step) return;

    // 1. Controls
    if (this.prevBtn) this.prevBtn.disabled = this.currStep === 0;
    if (this.nextBtn)
      this.nextBtn.disabled = this.currStep === this.steps.length - 1;
    if (this.stepDisplay) this.stepDisplay.textContent = this.currStep;

    // 2. Explanation
    if (this.explanationDisplay) {
      let html = `<h3>${step.explanation?.title || ""}</h3>`;
      html += `<p>${step.explanation?.text || ""}</p>`;
      if (step.explanation?.formula) {
        html += `<div style="background:rgba(255,255,255,0.05); padding:8px; border-radius:6px; margin-top:8px; font-family:monospace;">${step.explanation.formula}</div>`;
      }
      this.explanationDisplay.innerHTML = html;
    }

    // 3. Code Highlight
    this.highlightCode(step.highlightLines || []);

    // 4. Custom Callback (Mainly for Chart)
    if (this.config.onStepChange) {
      this.config.onStepChange(step, this.config.data);
    }
  }

  renderCode() {
    if (!this.codeDisplay) return;
    this.codeDisplay.innerHTML = this.config.codeLines
      .map((lineObj) => {
        return `<div class="code-line" id="code-${lineObj.id}">${lineObj.line}</div>`;
      })
      .join("");
  }

  highlightCode(lineIds) {
    if (!this.codeDisplay) return;
    // Reset all
    const lines = this.codeDisplay.getElementsByClassName("code-line");
    Array.from(lines).forEach((el) => el.classList.remove("active"));

    // Active
    lineIds.forEach((id) => {
      const el = document.getElementById(`code-${id}`);
      if (el) el.classList.add("active");
    });
  }

  // --- Auto Play Controls ---
  toggleAutoPlay() {
    if (this.isPlaying) {
      this.stopAutoPlay();
    } else {
      this.startAutoPlay();
    }
  }

  startAutoPlay() {
    if (this.isPlaying) return;
    this.isPlaying = true;
    this.updatePlayButton();
    
    this.autoPlayInterval = setInterval(() => {
      if (this.currStep < this.steps.length - 1) {
        this.next();
      } else {
        this.stopAutoPlay();
      }
    }, this.playSpeed);
  }

  stopAutoPlay() {
    this.isPlaying = false;
    if (this.autoPlayInterval) {
      clearInterval(this.autoPlayInterval);
      this.autoPlayInterval = null;
    }
    this.updatePlayButton();
  }

  setSpeed(speedMs) {
    this.playSpeed = speedMs;
    // 如果正在播放，重新啟動以應用新速度
    if (this.isPlaying) {
      this.stopAutoPlay();
      this.startAutoPlay();
    }
    this.updateSpeedDisplay();
  }

  updatePlayButton() {
    const playBtn = document.getElementById("playBtn");
    if (playBtn) {
      playBtn.innerHTML = this.isPlaying ? "⏸ 暫停" : "▶ 自動播放";
      playBtn.classList.toggle("playing", this.isPlaying);
    }
  }

  updateSpeedDisplay() {
    const speedDisplay = document.getElementById("speedDisplay");
    if (speedDisplay) {
      const speedLabel = this.playSpeed <= 500 ? "2x" : this.playSpeed <= 1000 ? "1.5x" : this.playSpeed <= 1500 ? "1x" : "0.5x";
      speedDisplay.textContent = speedLabel;
    }
  }

  // --- Helper for Charts ---
  static renderBars(container, heights, states = [], config = {}) {
    container.innerHTML = "";
    const maxH = Math.max(...heights, 1);
    const containerHeight = config.height || 260; // leave room for index

    heights.forEach((h, i) => {
      const barWrapper = document.createElement("div");
      barWrapper.className = "bar";
      barWrapper.style.width = `${100 / heights.length}%`;

      const fillHeight = (h / maxH) * containerHeight;
      const stateClass = states[i] || ""; // 'current', 'in-stack', etc.

      barWrapper.innerHTML = `
                <div class="bar-fill ${stateClass}" style="height: ${fillHeight}px;">${h}</div>
                <div class="bar-index">${i}</div>
            `;
      container.appendChild(barWrapper);
    });
  }

  // --- Theme Toggle ---
  static initThemeToggle() {
    // 檢測 MkDocs 主題或使用者偏好
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const savedTheme = localStorage.getItem('viz-theme');
    
    if (savedTheme === 'light' || (!savedTheme && !prefersDark)) {
      document.body.classList.add('light-theme');
    }
    
    // 監聽 MkDocs 主題切換
    const observer = new MutationObserver(() => {
      const mkdocsSlate = document.documentElement.getAttribute('data-md-color-scheme') === 'slate';
      if (mkdocsSlate) {
        document.body.classList.remove('light-theme');
      } else {
        document.body.classList.add('light-theme');
      }
    });
    
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['data-md-color-scheme'] });
  }

  static toggleTheme() {
    document.body.classList.toggle('light-theme');
    const isLight = document.body.classList.contains('light-theme');
    localStorage.setItem('viz-theme', isLight ? 'light' : 'dark');
  }
}

// 自動初始化主題
if (typeof window !== 'undefined') {
  AlgorithmVisualizer.initThemeToggle();
}
