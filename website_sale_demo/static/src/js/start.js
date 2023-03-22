/** @odoo-module **/

import { _lt } from '@web/core/l10n/translation';
import { loadBundleTemplates } from '@web/core/assets';
import { makeEnv } from '@web/env';
import { startServices } from './env';

const { whenReady } = owl.utils;

export async function startWebClient(Webclient, widget){
    const env = makeEnv();
    env.qweb.translateFn = _lt;
    const [, templates] = await Promise.all([
        startServices(env),
        loadBundleTemplates("website_sale_demo.assets_qweb"),
    ])
    env.qweb.addTemplates(templates)
    env.widget = widget
    await whenReady()
    await owl.mount(Webclient, { env, target: widget.el });
}
