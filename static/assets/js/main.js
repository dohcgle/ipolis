miscPolyfillsForIE();

class Collapse {
  constructor(container, options = {}) {
    let defaults = {
      accordion: false,
      initClass: 'collapse-init',
      activeClass: 'panel-active',
      heightClass: 'collapse-reading-height'
    };


    this.settings = Object.assign({}, defaults, options);

    this._container = container;
    this._panels = container.querySelectorAll("details");

    this.events = {
      openingPanel: new CustomEvent('openingPanel'),
      openedPanel: new CustomEvent('openedPanel'),
      closingPanel: new CustomEvent('closingPanel'),
      closedPanel: new CustomEvent('closedPanel')
    };

  }

  _setPanelHeight(panel) {
    let contents = panel.querySelector("summary + *");

    contents.style.height = contents.scrollHeight + "px";
  }

  _removePanelHeight(panel) {
    let contents = panel.querySelector("summary + *");

    contents.style.height = null;
  }

  //=== Open panel
  open(panel) {
    panel.dispatchEvent(this.events.openingPanel);

    panel.open = true;
  }

  _afterOpen(panel) {
    this._setPanelHeight(panel);
    panel.classList.add(this.settings.activeClass);
  }

  _endOpen(panel) {
    panel.dispatchEvent(this.events.openedPanel);

    this._removePanelHeight(panel);
  }

  close(panel) {
    panel.dispatchEvent(this.events.closingPanel);
    this._afterClose(panel);
  }

  _afterClose(panel) {
    this._setPanelHeight(panel);

    setTimeout(() => {
      panel.classList.remove(this.settings.activeClass);
      this._removePanelHeight(panel);
    }, 100);
  }

  _endClose(panel) {
    panel.dispatchEvent(this.events.closedPanel);

    panel.open = false;
  }

  toggle(panel) {
    panel.open ? this.close(panel) : this.open(panel);
  }

  openSinglePanel(panel) {
    this._panels.forEach(element => {
      if (panel == element && !panel.open) {
        this.open(element);
      } else {
        this.close(element);
      }
    });
  }

  openAll() {
    this._panels.forEach(element => {
      this.open(element);
    });
  }

  closeAll() {
    this._panels.forEach(element => {
      this.close(element);
    });
  }

  _attachEvents() {
    this._panels.forEach(panel => {
      let toggler = panel.querySelector("summary");
      let contents = panel.querySelector("summary + *");

      panel.addEventListener("toggle", e => {
        let isReadingHeight = panel.classList.contains(this.settings.heightClass);

        if (panel.open && !isReadingHeight) {
          this._afterOpen(panel);
        }
      });

      toggler.addEventListener("click", e => {
        if (this.settings.accordion) {
          this.openSinglePanel(panel);
          e.preventDefault();
        }

        else if (panel.open) {
          this.close(panel);
          e.preventDefault();
        }

      });

      let propToWatch = '';

      contents.addEventListener("transitionend", e => {
        if (e.target !== contents) {
          return;
        }

        if (!propToWatch) propToWatch = e.propertyName;

        if (e.propertyName == propToWatch) {
          let wasOpened = panel.classList.contains(this.settings.activeClass);
          wasOpened ? this._endOpen(panel) : this._endClose(panel);
        }
      });
    });
  }

  init() {
    this._attachEvents();

    if (this.settings.accordion) {
      this.openSinglePanel(this._panels[0]);
    }

    this._container.classList.add(this.settings.initClass);

    return this;
  }
}


let makeMePretty = document.querySelector(".collapse");
let accordion = new Collapse(makeMePretty, { accordion: true }).init();

document.querySelector("#accordion-toggle").
  addEventListener("change", function () {
    this.checked ?
      accordion.settings.accordion = false :
      accordion.settings.accordion = true;
  });

function miscPolyfillsForIE() {
  if (window.NodeList && !NodeList.prototype.forEach) {
    NodeList.prototype.forEach = Array.prototype.forEach;
  }

  "function" != typeof Object.assign && Object.defineProperty(Object, "assign", { value: function (e, t) { "use strict"; if (null == e) throw new TypeError("Cannot convert undefined or null to object"); for (var n = Object(e), r = 1; r < arguments.length; r++) { var o = arguments[r]; if (null != o) for (var c in o) Object.prototype.hasOwnProperty.call(o, c) && (n[c] = o[c]); } return n; }, writable: !0, configurable: !0 });

  !function () { if ("function" == typeof window.CustomEvent) return !1; function t(t, e) { e = e || { bubbles: !1, cancelable: !1, detail: void 0 }; var n = document.createEvent("CustomEvent"); return n.initCustomEvent(t, e.bubbles, e.cancelable, e.detail), n; } t.prototype = window.Event.prototype, window.CustomEvent = t; }();
}