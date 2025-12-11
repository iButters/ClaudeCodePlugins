/**
 * Base class for all UI-Kit Web Components
 * Provides common functionality and patterns
 */
export class BaseComponent extends HTMLElement {
  /**
   * Observed attributes - override in subclass
   * @returns {string[]}
   */
  static get observedAttributes() {
    return [];
  }

  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this._initialized = false;
  }

  /**
   * Called when element is added to DOM
   */
  connectedCallback() {
    if (!this._initialized) {
      this._initialized = true;
      this.render();
    }
  }

  /**
   * Called when observed attribute changes
   */
  attributeChangedCallback(name, oldValue, newValue) {
    if (oldValue !== newValue && this._initialized) {
      this.render();
    }
  }

  /**
   * Get attribute with default value
   * @param {string} name - Attribute name
   * @param {string} defaultValue - Default value if not set
   * @returns {string}
   */
  attr(name, defaultValue = '') {
    return this.getAttribute(name) ?? defaultValue;
  }

  /**
   * Check if boolean attribute is present
   * @param {string} name - Attribute name
   * @returns {boolean}
   */
  hasAttr(name) {
    return this.hasAttribute(name);
  }

  /**
   * Get base styles that should be included in all components
   * @returns {string}
   */
  getBaseStyles() {
    return `
      :host {
        display: inline-block;
        box-sizing: border-box;
      }

      :host([hidden]) {
        display: none !important;
      }

      *,
      *::before,
      *::after {
        box-sizing: inherit;
      }
    `;
  }

  /**
   * Get tokens link - components inherit CSS custom properties from document
   * Shadow DOM inherits custom properties automatically
   * @returns {string}
   */
  getTokensStyle() {
    return `
      /* CSS Custom Properties are inherited from :root through Shadow DOM */
      /* No explicit link needed - tokens.css must be loaded in the document */
    `;
  }

  /**
   * Render method - override in subclass
   * Should set this.shadowRoot.innerHTML
   */
  render() {
    throw new Error('render() must be implemented by subclass');
  }

  /**
   * Emit a custom event
   * @param {string} eventName - Name of the event
   * @param {*} detail - Event detail data
   */
  emit(eventName, detail = null) {
    this.dispatchEvent(new CustomEvent(eventName, {
      bubbles: true,
      composed: true, // Cross shadow DOM boundary
      detail
    }));
  }
}

/**
 * Helper to define a component with automatic registration
 * @param {string} tagName - Custom element tag name (e.g., 'ui-button')
 * @param {typeof BaseComponent} componentClass - Component class
 */
export function defineComponent(tagName, componentClass) {
  if (!customElements.get(tagName)) {
    customElements.define(tagName, componentClass);
  }
}

/**
 * Template literal tag for HTML with syntax highlighting support
 * @param {TemplateStringsArray} strings
 * @param  {...any} values
 * @returns {string}
 */
export function html(strings, ...values) {
  return strings.reduce((result, string, i) => {
    const value = values[i] ?? '';
    return result + string + value;
  }, '');
}

/**
 * Template literal tag for CSS with syntax highlighting support
 * @param {TemplateStringsArray} strings
 * @param  {...any} values
 * @returns {string}
 */
export function css(strings, ...values) {
  return strings.reduce((result, string, i) => {
    const value = values[i] ?? '';
    return result + string + value;
  }, '');
}
