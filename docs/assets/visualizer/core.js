class AlgorithmVisualizer {
  constructor(config) {
    this.steps = [];
    this.currStep = 0;
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
}
