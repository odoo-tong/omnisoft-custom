/** @odoo-module **/

import { Service } from "./Components/Service";

const { Component, tags } = owl
const { useState } = owl.hooks

export class Counter extends Component {
    static template = tags.xml/* xml */`
      <button t-on-click.prevent="() => state.value = state.value + props.increment">
        Click Me! [<t t-esc="state.value"/>]
      </button>`;

    state = useState({ value: 0 });
  }

export class App extends Component {
    setup() {
    }
}

App.template = "DemoApp"
App.components = { Counter, Service }
